#!/usr/bin/env python3
"""'Find your path to Portuguese' hero for Patio Language School (EN + PT).
Logo top-right, text block top-left over open sky, CTA pill at end of the path.
Photo = Claire's Lagos promenade (assets/img/lagos-promenade.jpg).
Formats: IG story 1080x1920, IG post 1080x1350, FB square 1080x1080.
Fonts: DM Serif Display + Barlow. No dashes.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = r"C:/Users/Claire/Patio Language School/assets/img"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(ASSETS, "Patio-Language-School-Logo-White.png")
PHOTO = os.path.join(ASSETS, "lagos-promenade.jpg")

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
            f"rgba(20,28,46,.56) 0%,rgba(20,28,46,.40) 22%,rgba(20,28,46,.20) 40%,"
            f"rgba(43,31,24,.04) 54%,rgba(43,31,24,.00) 66%,"
            f"rgba(43,31,24,.34) 82%,rgba(43,31,24,.88) 100%),"
            f"url(data:image/jpeg;base64,{PHOTO_B64})")

def page(w, h, body, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay()};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:56px;right:72px;width:230px;
      filter:drop-shadow(0 2px 16px rgba(0,0,0,.7))}}
    .top{{position:absolute;left:72px;right:72px;}}
    .eyebrow{{font-weight:700;font-size:34px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:22px;text-shadow:0 2px 14px rgba(0,0,0,.7)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:1.0;
      text-shadow:0 3px 26px rgba(0,0,0,.7)}}
    .sub{{font-weight:700;text-shadow:0 3px 18px rgba(0,0,0,1);color:{CREAM};margin-top:26px}}
    .gold{{color:{GOLD}}}
    .pill{{position:absolute;left:72px;display:inline-flex;align-items:center;gap:14px;
      background:{TERRA};color:{CREAM};font-weight:700;border-radius:999px;
      box-shadow:0 8px 30px rgba(0,0,0,.45)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

# --- copy sets ---
EN = dict(
    eyebrow="Now enrolling &middot; Lagos",
    h1='Find your <span class="gold">path</span><br>to Portuguese.',
    sub='Small, friendly groups.<br>Beginner to Advanced Levels.',
)
PT = dict(
    eyebrow="Inscrições abertas &middot; Lagos",
    h1='Encontra o teu <span class="gold">caminho</span><br>para o português.',
    sub='Grupos pequenos e acolhedores.<br>Do iniciante ao avançado.',
)
PILL = 'patiolanguage.pt &nbsp;&rarr;'

def body(top, h1size, subsize, T, pill_bottom, pill_fs, pill_pad):
    return f"""
<div class="top" style="top:{top}px">
  <div class="eyebrow">{T['eyebrow']}</div>
  <div class="h1" style="font-size:{h1size}px">{T['h1']}</div>
  <div class="sub" style="font-size:{subsize}px;line-height:1.35">{T['sub']}</div>
</div>
<div class="pill" style="bottom:{pill_bottom}px;font-size:{pill_fs}px;padding:{pill_pad}">
  {PILL}
</div>
"""

# name, w, h, top, h1_en, h1_pt, sub, pill_bottom, pill_fs, pill_pad, pos
FORMATS = [
    ("story", 1080, 1920, 210, 98, 82, 46, 150, 40, "25px 46px", "center 50%"),
    ("ig",    1080, 1350, 140, 84, 72, 42,  80, 38, "23px 42px", "center 28%"),
    ("fb",    1080, 1080, 120, 72, 62, 38,  70, 36, "22px 40px", "center 34%"),
]

JOBS = []
for fmt, w, h, top, h1en, h1pt, sub, pb, pfs, ppad, pos in FORMATS:
    JOBS.append((f"patio-path-{fmt}-{w}x{h}", w, h,
                 body(top, h1en, sub, EN, pb, pfs, ppad), pos))
    JOBS.append((f"patio-path-pt-{fmt}-{w}x{h}", w, h,
                 body(top, h1pt, sub, PT, pb, pfs, ppad), pos))

for name, w, h, bd, pos in JOBS:
    html = page(w, h, bd, pos)
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
