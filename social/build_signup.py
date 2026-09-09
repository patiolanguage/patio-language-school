#!/usr/bin/env python3
"""Fall-term sign-up hero for Patio Language School.
Angle: small friendly groups, easy parking, cafes nearby, all levels.
IG story 1080x1920 + IG portrait 1080x1350 + FB square 1080x1080. Photo = lagos-dona-ana.jpg.
Renders HTML via headless Chrome. Fonts: DM Serif Display + Barlow. No dashes.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = r"C:/Users/Claire/Patio Language School/assets/img"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(ASSETS, "Patio-Language-School-Logo-White.png")
PHOTO = os.path.join(ASSETS, "lagos-dona-ana.jpg")

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
PHOTO_B64 = b64(PHOTO)

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay():
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.42) 0%,rgba(43,31,24,.04) 18%,"
            f"rgba(43,31,24,.10) 40%,rgba(43,31,24,.70) 68%,rgba(43,31,24,.97) 100%),"
            f"url(data:image/jpeg;base64,{PHOTO_B64})")

def page(w, h, body, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay()};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:60px;left:72px;width:250px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.6))}}
    .wrap{{position:absolute;left:72px;right:72px;bottom:70px}}
    .eyebrow{{font-weight:700;font-size:34px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:22px;text-shadow:0 2px 14px rgba(0,0,0,.7)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:.98;
      text-shadow:0 3px 24px rgba(0,0,0,.6)}}
    .perks{{font-weight:700;text-shadow:0 3px 16px rgba(0,0,0,.98);color:{CREAM}}}
    .dot{{color:{GOLD};font-weight:700}}
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
  <div class="h1" style="font-size:100px">Learn Portuguese,<br><span class="gold">the Patio way.</span></div>
  <div class="perks" style="font-size:45px;line-height:1.45;margin-top:26px">
    Small, friendly groups <span class="dot">&middot;</span> Easy parking<br>
    Great cafes next door <span class="dot">&middot;</span> All levels welcome
  </div>
  <div class="pill" style="font-size:40px;padding:25px 44px;margin-top:36px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

# FB square body (tighter)
fb = f"""
<div class="wrap" style="bottom:60px">
  <div class="eyebrow">Fall term &middot; now enrolling</div>
  <div class="h1" style="font-size:80px">Learn Portuguese,<br><span class="gold">the Patio way.</span></div>
  <div class="perks" style="font-size:41px;line-height:1.45;margin-top:20px">
    Small, friendly groups <span class="dot">&middot;</span> Easy parking<br>
    Great cafes next door <span class="dot">&middot;</span> All levels welcome
  </div>
  <div class="pill" style="font-size:35px;padding:21px 40px;margin-top:28px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

# IG story body
story = f"""
<div class="wrap" style="bottom:150px">
  <div class="eyebrow">Fall term &middot; now enrolling</div>
  <div class="h1" style="font-size:104px">Learn Portuguese,<br><span class="gold">the Patio way.</span></div>
  <div class="perks" style="font-size:49px;line-height:1.45;margin-top:26px">
    Small, friendly groups <span class="dot">&middot;</span> Easy parking<br>
    Great cafes next door <span class="dot">&middot;</span> All levels welcome
  </div>
  <div class="pill" style="font-size:40px;padding:25px 44px;margin-top:36px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

JOBS = [
    ("patio-signup-story-1080x1920", 1080, 1920, story, "center 44%"),
    ("patio-signup-ig-1080x1350", 1080, 1350, ig, "center 44%"),
    ("patio-signup-fb-1080x1080", 1080, 1080, fb, "center 48%"),
]
for name, w, h, body, pos in JOBS:
    html = page(w, h, body, pos)
    hp = os.path.join(HERE, name + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    os.remove(hp)
    print("built", out)
print("done")
