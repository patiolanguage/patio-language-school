#!/usr/bin/env python3
"""Build the "Bom dia" mini-lesson posts for Patio Language School.
IG carousel (3 slides, 1080x1350) + FB square (1080x1080).
Anchor: "Bom dia" as the first teachable phrase, using Claire's own Lagos photos:
  sunrise (hook) / pretty cliffs (teach) / view to meia praia (CTA).
Renders HTML via headless Chrome. Fonts: DM Serif Display + Barlow (Google Fonts).
"""
import base64, subprocess, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = r"C:/Users/Claire/Patio Language School/assets/img/Patio-Language-School-Logo-White.png"

# brand palette
GOLD = "#D8B778"      # praia gold, lifted for contrast on photos
GOLD_DEEP = "#C19D5F"
TERRA = "#B8593A"
CREAM = "#FBF6EE"

def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMGS = {k: b64(os.path.join(SCRATCH, k + ".jpg")) for k in ("sun", "cliffs", "meia")}

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay(img):
    """Dark scrim: top for logo, heavy bottom for text, photo visible in middle."""
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.60) 0%,rgba(43,31,24,.12) 22%,"
            f"rgba(43,31,24,.10) 46%,rgba(43,31,24,.55) 72%,rgba(43,31,24,.93) 100%),"
            f"url(data:image/jpeg;base64,{IMGS[img]})")

def page(w, h, body, img, obj_pos="center"):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay(img)};
      background-size:cover;background-position:{obj_pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:64px;left:72px;width:250px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.55))}}
    .wrap{{position:absolute;left:72px;right:72px;bottom:70px}}
    .eyebrow{{font-weight:600;font-size:25px;letter-spacing:5px;
      text-transform:uppercase;color:{GOLD};margin-bottom:22px;
      text-shadow:0 2px 12px rgba(0,0,0,.5)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:.96;
      text-shadow:0 3px 24px rgba(0,0,0,.55)}}
    .body{{font-weight:500;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .gold{{color:{GOLD}}}
    .terra{{color:{TERRA}}}
    .pill{{display:inline-flex;align-items:center;gap:14px;
      background:{TERRA};color:{CREAM};font-weight:700;
      border-radius:999px;box-shadow:0 8px 30px rgba(0,0,0,.35)}}
    .swipe{{position:absolute;right:72px;bottom:74px;font-weight:700;
      font-size:30px;letter-spacing:1px;color:{CREAM};
      text-shadow:0 2px 12px rgba(0,0,0,.6);opacity:.95}}
    .num{{position:absolute;top:70px;right:78px;font-weight:700;font-size:26px;
      letter-spacing:3px;color:{CREAM};opacity:.85;
      text-shadow:0 2px 10px rgba(0,0,0,.6)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

# ---------- SLIDE 1 : HOOK (sunrise) ----------
s1 = f"""
<div class="num">01 / 03</div>
<div class="wrap">
  <div class="eyebrow">Your first word of Portuguese</div>
  <div class="h1" style="font-size:196px">Bom dia<span class="terra">.</span></div>
  <div class="body" style="font-size:44px;margin-top:26px;letter-spacing:1px">
    <span class="gold" style="font-weight:600">bong DEE&#8209;ah</span>
    &nbsp;&middot;&nbsp; &ldquo;Good morning&rdquo;
  </div>
</div>
<div class="swipe">Swipe &rarr;</div>
"""

# ---------- SLIDE 2 : TEACH (cliffs) ----------
s2 = f"""
<div class="num">02 / 03</div>
<div class="wrap">
  <div class="eyebrow">How the locals use it</div>
  <div class="h1" style="font-size:104px">Greetings that<br>follow the sun.</div>
  <div class="body" style="font-size:39px;line-height:1.5;margin-top:34px">
    <b class="gold">Bom dia</b> &nbsp;until midday<br>
    <b class="gold">Boa tarde</b> &nbsp;through the afternoon<br>
    <b class="gold">Boa noite</b> &nbsp;once the light goes
  </div>
  <div class="body" style="font-size:33px;margin-top:34px;opacity:.9;font-weight:400">
    Get the timing right and Lagos feels a little more like home.
  </div>
</div>
"""

# ---------- SLIDE 3 : CTA (meia praia) ----------
s3 = f"""
<div class="num">03 / 03</div>
<div class="wrap">
  <div class="eyebrow">Fall term &middot; now enrolling</div>
  <div class="h1" style="font-size:98px">Start with<br><span class="gold">bom dia.</span></div>
  <div class="body" style="font-size:35px;line-height:1.5;margin-top:30px;font-weight:400">
    Small&#8209;group &amp; private classes in European Portuguese,
    here in Lagos. Beginners always welcome.
  </div>
  <div class="pill" style="font-size:41px;padding:26px 44px;margin-top:44px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

# ---------- FB SQUARE (sunrise) ----------
fb = f"""
<div class="wrap" style="bottom:80px">
  <div class="eyebrow">Your first word of Portuguese</div>
  <div class="h1" style="font-size:150px">Bom dia<span class="terra">.</span></div>
  <div class="body" style="font-size:38px;margin-top:22px;letter-spacing:1px">
    <span class="gold" style="font-weight:600">bong DEE&#8209;ah</span>
    &nbsp;&middot;&nbsp; &ldquo;Good morning&rdquo;
  </div>
  <div class="body" style="font-size:33px;margin-top:26px;font-weight:400;opacity:.92">
    Fall term now enrolling. Beginners always welcome.
  </div>
  <div class="pill" style="font-size:37px;padding:22px 40px;margin-top:38px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

JOBS = [
    ("bomdia-1-hook-ig-1080x1350",   1080, 1350, s1, "cliffs", "center 55%"),
    ("bomdia-2-teach-ig-1080x1350",  1080, 1350, s2, "sun",    "center 42%"),
    ("bomdia-3-cta-ig-1080x1350",    1080, 1350, s3, "meia",   "center 40%"),
    ("bomdia-fb-1080x1080",          1080, 1080, fb, "sun",    "center 55%"),
]

for name, w, h, body, img, pos in JOBS:
    html = page(w, h, body, img, pos)
    hp = os.path.join(SCRATCH, name + ".html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")],
        check=True, capture_output=True)
    print("built", out)
print("done")
