#!/usr/bin/env python3
"""Photo-free testimonial card (Karin Liiv) for Patio Language School.
Neutral cream background, colour logo, gold quote mark, chocolate serif quote.
EN + PT, IG post 1080x1350, IG story 1080x1920, FB square 1080x1080.
No dashes; "Patio" no accent.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-Color.png")

CREAM = "#FBF6EE"; CHOC = "#2B1F18"; GOLD = "#C19D5F"; TERRA = "#B8593A"; TEAL = "#617C7B"; GALAO = "#726651"

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def page(w, h, logo_w, logo_top, box_top, qm, qz, wz, fz, t):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;background:{CREAM};
      font-family:'Barlow',sans-serif;color:{CHOC};overflow:hidden}}
    .logo{{position:absolute;top:{logo_top}px;left:50%;transform:translateX(-50%);
      width:{logo_w}px}}
    .box{{position:absolute;top:{box_top}px;left:88px;right:88px;text-align:center}}
    .eyebrow{{font-weight:700;letter-spacing:6px;text-transform:uppercase;
      color:{GOLD};font-size:{fz+2}px;margin-bottom:14px}}
    .qmark{{font-family:'DM Serif Display',serif;color:{GOLD};line-height:.5;
      font-size:{qm}px;height:{int(qm*0.42)}px}}
    .quote{{font-family:'DM Serif Display',serif;line-height:1.28;font-size:{qz}px;color:{TEAL}}}
    .rule{{width:70px;height:4px;background:{TERRA};border-radius:3px;margin:34px auto 26px}}
    .who{{font-weight:700;color:{TERRA};font-size:{wz}px;letter-spacing:.5px}}
    .foot{{font-weight:600;color:{GALAO};font-size:{fz}px;margin-top:8px}}
    .dots{{position:absolute;bottom:{logo_top}px;left:50%;transform:translateX(-50%);
      display:flex;gap:14px}}
    .dots span{{width:16px;height:16px;border-radius:4px}}
    """
    body = f"""
    <div class="box">
      <div class="eyebrow">{t['eyebrow']}</div>
      <div class="qmark">&ldquo;</div>
      <div class="quote">{t['quote']}</div>
      <div class="rule"></div>
      <div class="who">{t['who']}</div>
      <div class="foot">{t['foot']}</div>
    </div>
    <div class="dots">
      <span style="background:{TERRA}"></span>
      <span style="background:{GOLD}"></span>
      <span style="background:{TEAL}"></span>
    </div>
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

# name, w, h, logo_w, logo_top, box_top, qmark, quote, who, foot
FORMATS = [
    ("ig",    1080, 1350, 300, 120, 430, 165, 58, 42, 29),
    ("story", 1080, 1920, 320, 250, 660, 180, 63, 44, 31),
    ("fb",    1080, 1080, 260,  84, 320, 150, 51, 38, 27),
]

for lang in ("en", "pt"):
    sfx = "" if lang == "en" else "-pt"
    for fmt, w, h, lw, lt, bt, qm, qz, wz, fz in FORMATS:
        html = page(w, h, lw, lt, bt, qm, qz, wz, fz, TXT[lang])
        name = f"patio-testimonial-plain{sfx}-{fmt}-{w}x{h}"
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
