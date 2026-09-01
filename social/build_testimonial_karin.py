#!/usr/bin/env python3
"""Testimonial post (Karin Liiv) for Patio Language School.
IG portrait 1080x1350 + IG story 1080x1920 + FB square 1080x1080.
Photo: class-conversation.jpg (Sofia laughing with a student) - matches the
'we laugh every class' quote. No em dashes (brand rule).
"""
import base64, subprocess, os
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-White.png")

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

# exif-correct the group photo (stored rotated) -> upright portrait
_src = r"C:/Users/Claire/Documents/Patio Language/Patio Pix/group foto.jpeg"
_grp = os.path.join(SCRATCH, "group-foto.jpg")
_im = ImageOps.exif_transpose(Image.open(_src)).convert("RGB")
_im = ImageEnhance.Brightness(_im).enhance(0.98)   # keep it moodier (shadow hides faces)
_im = ImageEnhance.Contrast(_im).enhance(1.02)

# Privacy: soft-blur the three STUDENTS' faces (keep Sofia, the founder, sharp).
# Boxes in source px (image is 3024x4032 upright). Feathered ellipse for a natural edge.
def blur_face(im, box, feather=55):
    x0, y0, x1, y1 = box
    w = x1 - x0
    crop = im.crop(box)
    crop = crop.filter(ImageFilter.GaussianBlur(radius=max(9, w // 20)))  # gentle, less obvious
    mask = Image.new("L", (w, y1 - y0), 0)
    ImageDraw.Draw(mask).ellipse([feather, feather, w - feather, (y1 - y0) - feather], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(feather))
    im.paste(crop, box, mask)

for _box in [
    (2070, 1400, 2520, 1900),   # green-top woman (right)
    (540, 1620, 1000, 2110),    # blonde in floral (left, foreground)
    (320, 1330, 720, 1800),     # woman behind her (back-left)
]:
    blur_face(_im, _box)

_im.save(_grp, quality=90)

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMG_B64 = b64(_grp)

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay():
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.52) 0%,rgba(43,31,24,.34) 16%,"
            f"rgba(43,31,24,.50) 38%,rgba(43,31,24,.88) 60%,rgba(43,31,24,.98) 100%),"
            f"url(data:image/jpeg;base64,{IMG_B64})")

def page(w, h, body, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay()};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:60px;left:72px;width:240px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.6))}}
    .wrap{{position:absolute;left:72px;right:72px;}}
    .eyebrow{{font-weight:600;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .qmark{{font-family:'DM Serif Display',serif;color:{GOLD};line-height:.6;
      text-shadow:0 2px 14px rgba(0,0,0,.5)}}
    .quote{{font-family:'DM Serif Display',serif;line-height:1.28;
      text-shadow:0 3px 20px rgba(0,0,0,.7)}}
    .who{{font-weight:700;color:{GOLD};text-shadow:0 2px 12px rgba(0,0,0,.7)}}
    .foot{{font-weight:400;text-shadow:0 2px 12px rgba(0,0,0,.75)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

# Pull-quotes (em dashes removed: "-- and when to ease up! --" -> parentheses)
TXT = {
 "en": {
  "eyebrow": "What students say",
  "quote": ("Sofia knows exactly when to push my edge (and when to ease up!) as I "
            "learn Portuguese. I can&rsquo;t remember one single class where we did "
            "not laugh. She makes learning a brand-new language fun."),
  "who": "Karin Liiv",
  "foot": "Learning Portuguese at Patio &nbsp;&middot;&nbsp; patiolanguage.pt",
 },
 "pt": {
  "eyebrow": "O que dizem os alunos",
  "quote": ("A Sofia sabe exatamente quando me desafiar (e quando aliviar!) &agrave; "
            "medida que aprendo portugu&ecirc;s. N&atilde;o me lembro de uma &uacute;nica "
            "aula em que n&atilde;o nos tenhamos rido. Ela torna divertido aprender "
            "uma l&iacute;ngua nova."),
  "who": "Karin Liiv",
  "foot": "A aprender portugu&ecirc;s no P&aacute;tio &nbsp;&middot;&nbsp; patiolanguage.pt",
 },
}

def body(fmt, t):
    if fmt == "ig":
        bottom, ey, qm, qz, wz, fz = 76, 24, 120, 47, 35, 28
    elif fmt == "story":
        bottom, ey, qm, qz, wz, fz = 280, 26, 140, 56, 41, 31
    else:  # fb
        bottom, ey, qm, qz, wz, fz = 60, 22, 100, 39, 30, 25
    return f"""
    <div class="wrap" style="bottom:{bottom}px">
      <div class="eyebrow" style="font-size:{ey}px;margin-bottom:6px">{t['eyebrow']}</div>
      <div class="qmark" style="font-size:{qm}px;margin-bottom:-6px">&ldquo;</div>
      <div class="quote" style="font-size:{qz}px">{t['quote']}</div>
      <div class="who" style="font-size:{wz}px;margin-top:28px">{t['who']}</div>
      <div class="foot" style="font-size:{fz}px;margin-top:6px">
        {t['foot']}
      </div>
    </div>"""

def render(name, w, h, fmt, pos, top=None, lang="en"):
    html = page(w, h, body(fmt, TXT[lang]), pos)
    if top is not None:  # story: drop logo lower into safe zone
        html = html.replace("top:60px;left:72px", f"top:{top}px;left:80px")
    hp = os.path.join(HERE, "_tmp_" + name + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    os.remove(hp)
    print("built", out)

render("patio-testimonial-karin-ig-1080x1350", 1080, 1350, "ig", "center 34%")
render("patio-testimonial-karin-fb-1080x1080", 1080, 1080, "fb", "center 32%")
render("patio-testimonial-karin-ig-story-1080x1920", 1080, 1920, "story", "center 32%", top=130)
# Portuguese FB version
render("patio-testimonial-karin-pt-fb-1080x1080", 1080, 1080, "fb", "center 32%", lang="pt")
print("done")
