#!/usr/bin/env python3
"""Short 'register now' invite hero for Patio Language School.
Pairs with patio-fall-2026-schedule.png as slide 2 / second image.
IG portrait 1080x1350 + FB square 1080x1080, founders photo (Claire & Sofia).
Renders HTML via headless Chrome. Fonts: DM Serif Display + Barlow.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = r"C:/Users/Claire/Patio Language School/assets/img/Patio-Language-School-Logo-White.png"

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMGS = {k: b64(os.path.join(SCRATCH, k + ".jpg")) for k in ("founders", "office", "classroom")}

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay(img):
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.48) 0%,rgba(43,31,24,.06) 20%,"
            f"rgba(43,31,24,.10) 42%,rgba(43,31,24,.66) 70%,rgba(43,31,24,.96) 100%),"
            f"url(data:image/jpeg;base64,{IMGS[img]})")

def page(w, h, body, img, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay(img)};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:60px;left:72px;width:250px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.6))}}
    .wrap{{position:absolute;left:72px;right:72px;bottom:70px}}
    .eyebrow{{font-weight:600;font-size:26px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:22px;text-shadow:0 2px 12px rgba(0,0,0,.55)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:.98;
      text-shadow:0 3px 24px rgba(0,0,0,.6)}}
    .body{{font-weight:500;text-shadow:0 2px 12px rgba(0,0,0,.7)}}
    .gold{{color:{GOLD}}} .terra{{color:{TERRA}}}
    .pill{{display:inline-flex;align-items:center;gap:14px;background:{TERRA};color:{CREAM};
      font-weight:700;border-radius:999px;box-shadow:0 8px 30px rgba(0,0,0,.4)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

# IG portrait body
ig = f"""
<div class="wrap">
  <div class="eyebrow">Fall term &middot; now enrolling</div>
  <div class="h1" style="font-size:104px">Learn Portuguese,<br><span class="gold">the Patio way.</span></div>
  <div class="body" style="font-size:35px;line-height:1.5;margin-top:28px;font-weight:400">
    Small groups, real conversation and cultural workshops,
    here in Lagos. All levels welcome.
  </div>
  <div class="pill" style="font-size:40px;padding:25px 44px;margin-top:40px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

# FB square body (a touch tighter)
fb = f"""
<div class="wrap" style="bottom:64px">
  <div class="eyebrow">Fall term &middot; now enrolling</div>
  <div class="h1" style="font-size:84px">Learn Portuguese,<br><span class="gold">the Patio way.</span></div>
  <div class="body" style="font-size:31px;line-height:1.45;margin-top:22px;font-weight:400">
    Small groups, real conversation &amp; cultural workshops in Lagos. All levels welcome.
  </div>
  <div class="pill" style="font-size:35px;padding:21px 40px;margin-top:32px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

JOBS = [
    ("patio-invite-ig-1080x1350", 1080, 1350, ig, "founders", "center 26%"),
    ("patio-invite-fb-1080x1080", 1080, 1080, fb, "founders", "center 22%"),
]
for name, w, h, body, img, pos in JOBS:
    html = page(w, h, body, img, pos)
    hp = os.path.join(SCRATCH, name + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    print("built", out)
print("done")
