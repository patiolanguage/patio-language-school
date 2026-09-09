#!/usr/bin/env python3
"""Bright, happy testimonial post (Karin Liiv) for Patio Language School.
Photo = class-conversation.jpg (Sofia laughing) brightened; LIGHT overlay top,
strong scrim only at the bottom for the quote. EN + PT, IG post / story / FB square.
No dashes; "Patio" no accent.
"""
import base64, subprocess, os
from PIL import Image, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/7f4cb33e-62e6-44e9-815e-f978ea8d0de9/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-White.png")

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

# brighten + a touch more colour for a happy feel
_im = Image.open(os.path.join(IMGDIR, "class-conversation.jpg")).convert("RGB")
_im = ImageEnhance.Brightness(_im).enhance(1.08)
_im = ImageEnhance.Color(_im).enhance(1.08)
_bright = os.path.join(SCRATCH, "sofia-bright.jpg")
_im.save(_bright, quality=92)

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMG_B64 = b64(_bright)

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay():
    # light up top (keeps it bright), strong scrim only in the lower third for the quote
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.24) 0%,rgba(43,31,24,.04) 26%,rgba(43,31,24,.02) 44%,"
            f"rgba(43,31,24,.34) 58%,rgba(43,31,24,.82) 76%,rgba(43,31,24,.97) 100%),"
            f"url(data:image/jpeg;base64,{IMG_B64})")

def page(w, h, body, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay()};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:60px;left:72px;width:240px;
      filter:drop-shadow(0 2px 16px rgba(0,0,0,.9))}}
    .wrap{{position:absolute;left:72px;right:72px;}}
    .eyebrow{{font-weight:700;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};text-shadow:0 2px 12px rgba(0,0,0,.7)}}
    .qmark{{font-family:'DM Serif Display',serif;color:{GOLD};line-height:.6;
      text-shadow:0 2px 14px rgba(0,0,0,.6)}}
    .quote{{font-family:'DM Serif Display',serif;line-height:1.28;
      text-shadow:0 3px 22px rgba(0,0,0,.85)}}
    .who{{font-weight:700;color:{GOLD};text-shadow:0 2px 12px rgba(0,0,0,.8)}}
    .foot{{font-weight:500;text-shadow:0 2px 12px rgba(0,0,0,.85)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

TXT = {
 "en": {
  "eyebrow": "What students say",
  "quote": ("Sofia knows exactly when to push my edge (and when to ease up!). "
            "I can&rsquo;t remember a single class where we didn&rsquo;t laugh. "
            "She makes learning a whole new language fun. Who could ask for more?"),
  "who": "Karin Liiv",
  "foot": "Learning Portuguese at Patio &nbsp;&middot;&nbsp; patiolanguage.pt",
 },
 "pt": {
  "eyebrow": "O que dizem os alunos",
  "quote": ("A Sofia sabe exatamente quando me desafiar (e quando aliviar!). "
            "N&atilde;o me lembro de uma &uacute;nica aula em que n&atilde;o nos tenhamos rido. "
            "Ela torna divertido aprender uma l&iacute;ngua nova. Quem podia pedir mais?"),
  "who": "Karin Liiv",
  "foot": "A aprender portugu&ecirc;s no Patio &nbsp;&middot;&nbsp; patiolanguage.pt",
 },
}

def body(fmt, t):
    if fmt == "ig":
        bottom, ey, qm, qz, wz, fz = 78, 26, 120, 45, 35, 28
    elif fmt == "story":
        bottom, ey, qm, qz, wz, fz = 250, 28, 140, 52, 40, 31
    else:  # fb
        bottom, ey, qm, qz, wz, fz = 62, 23, 104, 39, 30, 25
    return f"""
    <div class="wrap" style="bottom:{bottom}px">
      <div class="eyebrow" style="font-size:{ey}px;margin-bottom:8px">{t['eyebrow']}</div>
      <div class="qmark" style="font-size:{qm}px;margin-bottom:-4px">&ldquo;</div>
      <div class="quote" style="font-size:{qz}px">{t['quote']}</div>
      <div class="who" style="font-size:{wz}px;margin-top:26px">{t['who']}</div>
      <div class="foot" style="font-size:{fz}px;margin-top:6px">{t['foot']}</div>
    </div>"""

def render(name, w, h, fmt, pos, top=None, lang="en"):
    html = page(w, h, body(fmt, TXT[lang]), pos)
    if top is not None:
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

for lang in ("en", "pt"):
    sfx = "" if lang == "en" else "-pt"
    render(f"patio-testimonial-karin{sfx}-ig-1080x1350", 1080, 1350, "ig", "center 30%", lang=lang)
    render(f"patio-testimonial-karin{sfx}-fb-1080x1080", 1080, 1080, "fb", "center 30%", lang=lang)
    render(f"patio-testimonial-karin{sfx}-story-1080x1920", 1080, 1920, "story", "center 30%", top=130, lang=lang)
print("done")
