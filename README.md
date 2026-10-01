# Patio Language School — website

The website for [patiolanguage.pt](https://patiolanguage.pt), a language school and
cultural community in Lagos, Portugal.

## What this is

A hand-coded **static site**: plain HTML + one CSS file, with a small amount of
vanilla JavaScript. **No framework, no build step, no backend** — the files are
served as-is.

- No `package.json`, no React/Vue/Next/Vite/Tailwind, no bundler.
- To make changes: edit the HTML/CSS and redeploy (see below). Nothing to install or compile.

## Structure

```
index.html            Main one-page site (English) with anchor sections
about.html            (redirect/stub)
classes.html          (redirect/stub)
contact.html          (redirect/stub)
pt/index.html         European Portuguese version
ai/index.html         Practical AI courses landing page + register-interest form (English)
css/style.css         Single stylesheet (cache-busted via ?v=NN in the HTML)
assets/img/           Images, icons, logos
_redirects            Cloudflare Pages redirects (short links)
functions/            Cloudflare Pages Functions (server code), NOT static, stays at repo root
  api/ai-interest.js  POST endpoint: validates + saves AI registrations to Supabase
migrations/           Versioned SQL for the Supabase database
social/               Marketing assets + Python generators (not part of the site)
merch/                Merch catalogue (HTML + PDF)
forms/                Google Apps Script for the registration form
```

The AI landing page is otherwise the same static stack as the rest of the site.
The only server-side piece is the single Pages Function below.

## Tech / integrations

- **Fonts:** Google Fonts (Anton for headings, Barlow for body).
- **Bilingual:** English at `/`, European Portuguese at `/pt/`, linked with `hreflang` tags.
- **Contact form:** [Formspree](https://formspree.io) (submissions go to patiolanguage@gmail.com). No server code.
- **Newsletter:** [MailerLite](https://mailerlite.com) embedded form + universal script. The same
  form is embedded twice (hero + footer), so a small inline script de-duplicates the element ids.
- **Class registration:** an external Google Form. Short links `/inscrever` (PT) and `/register` (EN)
  redirect to it via `_redirects`.

## Hosting & deploy

- Hosted on **Cloudflare Pages**; custom domain **patiolanguage.pt** on Cloudflare DNS.
- Deploys are done with the **Wrangler** CLI from a clean `dist/` folder:

  ```bash
  # build a clean dist/ (copy the html + css/ + assets/img/ + pt/ + ai/ + _redirects), then:
  npx wrangler pages deploy dist --project-name=patio-language-school --branch=main --commit-dirty=true
  ```

- **Run the deploy from the repository root.** Wrangler uploads `dist/` as the static
  site and separately compiles the `functions/` directory it finds in the working
  directory. Keep `functions/` at the repo root (outside `dist/`) so the server code is
  never published as static files.
- `dist/`, `.wrangler/`, `.dev.vars`, and a few scratch files are git-ignored.

## Practical AI courses (`/ai/`) + register-interest form

The AI landing page collects registrations of interest through a small server flow:

```
ai/index.html (form)  ->  POST /api/ai-interest (Cloudflare Pages Function)  ->  Supabase
```

Only the server endpoint talks to Supabase, using the **service-role** key. The database
has Row-Level Security **on with no policies**, so the public/anon key cannot read or write.

### 1. Database setup (Supabase)

Run the migration once against your Supabase project. Either paste
`migrations/0001_ai_course_interest.sql` into **SQL Editor → New query → Run**, or with the
Supabase CLI (`supabase db push` on a linked project). It creates the `ai_course_interest`
table (`id, email, course_interest, preferred_slot, created_at`), enforces the allowed
course/slot values and a unique email with CHECK constraints, and enables RLS.

### 2. Environment variables / secrets (Cloudflare Pages → Settings → Variables and Secrets)

| Name | Type | Required | Notes |
|------|------|----------|-------|
| `SUPABASE_URL` | Variable | yes | e.g. `https://xxxx.supabase.co` |
| `SUPABASE_SERVICE_ROLE_KEY` | **Secret** | yes | service-role key; bypasses RLS. Never put in the browser or Git. |
| `TURNSTILE_SECRET` | **Secret** | recommended | Cloudflare Turnstile secret key (server-side verification). |

Never commit any of these. Locally they live in `.dev.vars` (git-ignored; see
`.dev.vars.example`).

### 3. Spam protection (Cloudflare Turnstile)

1. Create a Turnstile widget in the Cloudflare dashboard; you get a **site key** (public)
   and a **secret key** (private).
2. Put the site key in `ai/index.html`, in the `TURNSTILE_SITE_KEY` constant near the bottom.
3. Put the secret in the `TURNSTILE_SECRET` env secret (above).

When `TURNSTILE_SECRET` is set, the server **requires** a valid token. Left unset (e.g. local
dev) the check is skipped. Optional extra: bind a KV namespace named `RATE_LIMIT_KV` to the
Pages project for best-effort per-IP rate limiting (the IP is hashed, never stored raw).

### 4. Local development

```bash
cp .dev.vars.example .dev.vars     # then fill in the values
# build dist/ (include ai/), then serve dist as assets + compile ./functions:
npx wrangler pages dev dist
```

Open the printed URL and go to `/ai/`. Turnstile can be left off locally, or use Cloudflare's
always-passes test keys (noted in `.dev.vars.example`).

### Privacy

The form stores only the email, chosen course and preferred slot. Emails are used **only** to
follow up about these AI courses; registrants are **not** added to the MailerLite newsletter.
The server never logs email addresses or request bodies.

## Source control

GitHub: [patiolanguage/patio-language-school](https://github.com/patiolanguage/patio-language-school)

## Notes

- Bump the CSS cache-buster (`?v=NN` on the `style.css` link in each HTML file) when you change `css/style.css`.
- CDN edge cache can serve old pages for a while after deploy; purge in the Cloudflare dashboard if needed.
