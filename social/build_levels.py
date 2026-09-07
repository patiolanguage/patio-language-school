#!/usr/bin/env python3
"""'All levels' sign-up post: entices beginners AND people who already speak
some Portuguese and want to improve. IG 1080x1350 + FB 1080x1080 + story 1080x1920.
Photo: the welcoming space (better office pic), exif-corrected. No em dashes.
"""
import base64, subprocess, os
from PIL import Image, ImageOps, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-White.png")

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

_src = r"C:/Users/Claire/Documents/Patio Language/Patio Pix/better office pic.jpeg"
_img = os.path.join(SCRATCH, "office-levels.jpg")
_im = ImageOps.exif_transpose(Image.open(_src)).convert("RGB")
_im = ImageEnhance.Brightness(_im).enhance(1.05)
_im.save(_img, quality=90)

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()
LOGO_B64 = b64(LOGO); IMG_B64 = b64(_img)

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay():
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.48) 0%,rgba(43,31,24,.10) 20%,"
            f"rgba(43,31,24,.16) 42%,rgba(43,31,24,.70) 68%,rgba(43,31,24,.96) 100%),"
            f"url(data:image/jpeg;base64,{IMG_B64})")

def page(w, h, body, pos, logotop=60):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay()};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:{logotop}px;left:72px;width:240px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.6))}}
    .wrap{{position:absolute;left:72px;right:72px;}}
    .eyebrow{{font-weight:600;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:1.0;
      text-shadow:0 3px 24px rgba(0,0,0,.6)}}
    .body{{font-weight:500;text-shadow:0 2px 14px rgba(0,0,0,.75)}}
    .gold{{color:{GOLD}}}
    .pill{{display:inline-flex;align-items:center;gap:14px;background:{TERRA};color:{CREAM};
      font-weight:700;border-radius:999px;box-shadow:0 8px 30px rgba(0,0,0,.4)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

def body(fmt):
    if fmt == "ig":
        bt, eb, h1, bd, pl, ph = 74, 26, 92, 34, 40, "26px 44px"
    elif fmt == "story":
        bt, eb, h1, bd, pl, ph = 280, 28, 110, 40, 44, "28px 48px"
    else:  # fb
        bt, eb, h1, bd, pl, ph = 60, 23, 74, 30, 34, "20px 38px"
    return f"""
    <div class="wrap" style="bottom:{bt}px">
      <div class="eyebrow" style="font-size:{eb}px;margin-bottom:20px">Fall term &middot; now enrolling</div>
      <div class="h1" style="font-size:{h1}px">From your first word<br><span class="gold">to real conversation.</span></div>
      <div class="body" style="font-size:{bd}px;line-height:1.5;margin-top:26px;font-weight:400">
        Total beginner or already speak some Portuguese and want to improve,
        there&rsquo;s a class at your level. Small groups from A1 to B1+, plus
        conversation and cultural workshops, here in Lagos.
      </div>
      <div class="pill" style="font-size:{pl}px;padding:{ph};margin-top:36px">patiolanguage.pt &nbsp;&rarr;</div>
    </div>"""

JOBS = [
    ("patio-levels-ig-1080x1350", 1080, 1350, "ig", "center 40%", 60),
    ("patio-levels-fb-1080x1080", 1080, 1080, "fb", "center 38%", 60),
    ("patio-levels-ig-story-1080x1920", 1080, 1920, "story", "center 42%", 130),
]
for name, w, h, fmt, pos, lt in JOBS:
    html = page(w, h, body(fmt), pos, lt)
    hp = os.path.join(HERE, "_tmp_" + name + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    os.remove(hp)
    print("built", out)
print("done")
