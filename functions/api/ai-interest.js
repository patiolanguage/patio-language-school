/**
 * POST /api/ai-interest
 *
 * Same-origin endpoint for the Practical AI "register interest" form.
 * Flow:  HTML form  ->  this Cloudflare Pages Function  ->  Supabase (REST).
 *
 * Environment (set as Cloudflare Pages secrets / vars, never in Git):
 *   SUPABASE_URL              e.g. https://xxxx.supabase.co         (required)
 *   SUPABASE_SERVICE_ROLE_KEY the service_role key (bypasses RLS)   (required, secret)
 *   TURNSTILE_SECRET          Cloudflare Turnstile secret key       (recommended, secret)
 * Optional binding:
 *   RATE_LIMIT_KV             a KV namespace for per-IP rate limiting
 *
 * Privacy: we never log email addresses or request bodies. Errors log a code only.
 */

const COURSES = new Set(["ai_made_simple", "ai_for_business", "either"]);
const SLOTS = new Set(["wed_afternoon", "wed_evening", "fri_afternoon", "fri_evening"]);

const MAX_BYTES = 2048;        // reject oversized request bodies
const MAX_EMAIL = 254;         // RFC 5321 practical maximum
const RATE_LIMIT = 8;          // max submissions ...
const RATE_WINDOW = 600;       // ... per this many seconds, per IP

const json = (status, body) =>
  new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "referrer-policy": "no-referrer",
    },
  });

// A single neutral acknowledgement. Returned identically whether the row was
// newly inserted or already existed, so repeat submissions reveal nothing and
// cannot inflate or overwrite demand.
const ok = () => json(200, { ok: true, message: "Thanks, your interest is registered." });

// Normalize an email for storage and de-duplication: trim + lower-case.
function normalizeEmail(raw) {
  return String(raw).trim().toLowerCase();
}

// Pragmatic email check (server-side; the browser also validates).
function validEmail(email) {
  if (email.length < 3 || email.length > MAX_EMAIL) return false;
  // one @, non-empty local part, a dotted domain, no spaces
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

async function verifyTurnstile(secret, token, ip) {
  if (!token) return false;
  const form = new FormData();
  form.append("secret", secret);
  form.append("response", token);
  if (ip) form.append("remoteip", ip);
  try {
    const res = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      body: form,
    });
    const data = await res.json();
    return data.success === true;
  } catch (_) {
    return false;
  }
}

// Best-effort per-IP rate limiting. Only active when a RATE_LIMIT_KV namespace
// is bound; otherwise Turnstile is the primary defence. The IP is hashed so no
// raw address is persisted.
async function rateLimited(env, ip) {
  if (!env.RATE_LIMIT_KV || !ip) return false;
  try {
    const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(ip));
    const hex = [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, "0")).join("");
    const key = `rl:${hex}`;
    const current = parseInt((await env.RATE_LIMIT_KV.get(key)) || "0", 10);
    if (current >= RATE_LIMIT) return true;
    await env.RATE_LIMIT_KV.put(key, String(current + 1), { expirationTtl: RATE_WINDOW });
    return false;
  } catch (_) {
    return false; // never block a legitimate user because the limiter errored
  }
}

async function handlePost({ request, env }) {
  // Config guard: fail loudly server-side, neutrally client-side.
  if (!env.SUPABASE_URL || !env.SUPABASE_SERVICE_ROLE_KEY) {
    console.error("ai-interest: missing Supabase configuration");
    return json(503, { ok: false, message: "Registration is temporarily unavailable. Please email us." });
  }

  // Size guard via Content-Length (bodies are tiny JSON).
  const len = parseInt(request.headers.get("content-length") || "0", 10);
  if (len > MAX_BYTES) return json(413, { ok: false, message: "Request too large." });

  // Parse body defensively and cap actual bytes read.
  let payload;
  try {
    const text = await request.text();
    if (text.length > MAX_BYTES) return json(413, { ok: false, message: "Request too large." });
    payload = JSON.parse(text);
  } catch (_) {
    return json(400, { ok: false, message: "Invalid request." });
  }
  if (!payload || typeof payload !== "object") {
    return json(400, { ok: false, message: "Invalid request." });
  }

  const ip = request.headers.get("cf-connecting-ip") || "";

  // Rate limit (best-effort).
  if (await rateLimited(env, ip)) {
    return json(429, { ok: false, message: "Too many attempts. Please try again later." });
  }

  // Spam protection. Required whenever a secret is configured; skipped only in
  // unconfigured (local/dev) environments. See README.
  if (env.TURNSTILE_SECRET) {
    const passed = await verifyTurnstile(env.TURNSTILE_SECRET, payload.turnstileToken, ip);
    if (!passed) {
      return json(403, { ok: false, message: "Spam check failed. Please try again." });
    }
  }

  // Validate fields.
  const email = normalizeEmail(payload.email || "");
  const course_interest = String(payload.course_interest || "");
  const preferred_slot = String(payload.preferred_slot || "");

  if (!validEmail(email)) {
    return json(422, { ok: false, field: "email", message: "Please enter a valid email address." });
  }
  if (!COURSES.has(course_interest)) {
    return json(422, { ok: false, field: "course_interest", message: "Please choose a course." });
  }
  if (!SLOTS.has(preferred_slot)) {
    return json(422, { ok: false, field: "preferred_slot", message: "Please choose a preferred time." });
  }

  // Insert into Supabase. on_conflict=email + resolution=ignore-duplicates means
  // a repeat email is a no-op (the existing preference is preserved), and the
  // response is a neutral 201 either way, no information leak about who exists.
  let res;
  try {
    res = await fetch(
      `${env.SUPABASE_URL}/rest/v1/ai_course_interest?on_conflict=email`,
      {
        method: "POST",
        headers: {
          apikey: env.SUPABASE_SERVICE_ROLE_KEY,
          authorization: `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}`,
          "content-type": "application/json",
          prefer: "resolution=ignore-duplicates,return=minimal",
        },
        body: JSON.stringify({ email, course_interest, preferred_slot }),
      }
    );
  } catch (_) {
    console.error("ai-interest: supabase request failed");
    return json(502, { ok: false, message: "We couldn't save that just now. Please try again." });
  }

  // 201 = inserted, 200 = ignored duplicate. Both are success for the user.
  if (res.status === 201 || res.status === 200) return ok();

  // Never log the response body (could echo submitted data); log status only.
  console.error("ai-interest: supabase insert status", res.status);
  return json(502, { ok: false, message: "We couldn't save that just now. Please try again." });
}

// Single entry point so method dispatch is explicit: only POST is accepted;
// every other method gets a clear 405 (rather than falling through to static
// assets).
export async function onRequest(context) {
  if (context.request.method !== "POST") {
    return json(405, { ok: false, message: "Method not allowed." });
  }
  return handlePost(context);
}
