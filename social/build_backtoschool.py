#!/usr/bin/env python3
"""'Back to school' Fall-term post for Patio Language School (EN + PT).
Adult back-to-school angle. Photo = class-conversation.jpg (teacher + student, grammar book).
Bottom-anchored text over a strong scrim; logo top-left.
Formats: IG story 1080x1920, IG post 1080x1350, FB square 1080x1080.
Fonts: DM Serif Display + Barlow. No dashes.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = r"C:/Users/Claire/Patio Language School/assets/img"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(ASSETS, "Patio-Language-School-Logo-White.png")
PHOTO = os.path.join(ASSETS, "space-classroom.jpg")

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
            f"rgba(43,31,24,.58) 0%,rgba(43,31,24,.14) 20%,rgba(43,31,24,.06) 42%,"
            f"rgba(43,31,24,.60) 68%,rgba(43,31,24,.97) 100%),"
            f"url(data:image/jpeg;base64,{PHOTO_B64})")

def page(w, h, body, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay()};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:58px;left:72px;width:240px;
      filter:drop-shadow(0 2px 16px rgba(0,0,0,.85))}}
    .wrap{{position:absolute;left:72px;right:72px;}}
    .eyebrow{{font-weight:700;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:20px;text-shadow:0 2px 14px rgba(0,0,0,.7)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:1.0;
      text-shadow:0 3px 26px rgba(0,0,0,.75)}}
    .sub{{font-weight:700;text-shadow:0 3px 18px rgba(0,0,0,1);color:{CREAM};margin-top:24px}}
    .gold{{color:{GOLD}}}
    .pill{{display:inline-flex;align-items:center;gap:14px;
      background:{TERRA};color:{CREAM};font-weight:700;border-radius:999px;
      box-shadow:0 8px 30px rgba(0,0,0,.45)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

EN = dict(
    eyebrow="Back to school &middot; Lagos",
    h1='The kids are<br>going back.<br><span class="gold">Your turn now.</span>',
    sub='Portuguese classes start 21 September.<br>Every level welcome.',
)
PT = dict(
    eyebrow="Aulas de outono &middot; Lagos",
    h1='Os miúdos vão voltar.<br><span class="gold">Agora é a tua vez.</span>',
    sub='Aulas de português a partir de 21 de setembro.<br>Todos os níveis.',
)
PILL = 'patiolanguage.pt &nbsp;&rarr;'

def body(bottom, eyb, h1size, subsize, T, pill_fs, pill_pad):
    return f"""
<div class="wrap" style="bottom:{bottom}px">
  <div class="eyebrow" style="font-size:{eyb}px">{T['eyebrow']}</div>
  <div class="h1" style="font-size:{h1size}px">{T['h1']}</div>
  <div class="sub" style="font-size:{subsize}px;line-height:1.35">{T['sub']}</div>
  <div class="pill" style="font-size:{pill_fs}px;padding:{pill_pad};margin-top:36px">{PILL}</div>
</div>
"""

# name, w, h, bottom, eyebrow, h1_en, h1_pt, sub, pill_fs, pill_pad, pos
FORMATS = [
    ("story", 1080, 1920, 150, 32, 88, 78, 40, 40, "25px 46px", "center 45%"),
    ("ig",    1080, 1350,  95, 30, 80, 70, 36, 38, "23px 42px", "center 48%"),
    ("fb",    1080, 1080,  70, 28, 72, 62, 33, 36, "22px 40px", "center 48%"),
]

JOBS = []
for fmt, w, h, bt, eyb, h1en, h1pt, sub, pfs, ppad, pos in FORMATS:
    JOBS.append((f"patio-b2s-{fmt}-{w}x{h}", w, h,
                 body(bt, eyb, h1en, sub, EN, pfs, ppad), pos))
    JOBS.append((f"patio-b2s-pt-{fmt}-{w}x{h}", w, h,
                 body(bt, eyb, h1pt, sub, PT, pfs, ppad), pos))

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
