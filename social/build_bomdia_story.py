#!/usr/bin/env python3
"""IG Story versions (1080x1920) of the three "Bom dia" carousel slides.
EN + PT. Same photos/brand as build_bomdia.py, re-laid-out for 9:16 with
story safe zones (logo below top UI, text above the bottom bar).
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = r"C:/Users/Claire/Patio Language School/assets/img/Patio-Language-School-Logo-White.png"

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"
W, H = 1080, 1920

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMGS = {k: b64(os.path.join(SCRATCH, k + ".jpg")) for k in ("sun", "cliffs", "meia")}

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay(img):
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.55) 0%,rgba(43,31,24,.08) 17%,"
            f"rgba(43,31,24,.05) 40%,rgba(43,31,24,.50) 64%,rgba(43,31,24,.95) 100%),"
            f"url(data:image/jpeg;base64,{IMGS[img]})")

def page(body, img, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{W}px;height:{H}px;overflow:hidden}}
    .card{{position:relative;width:{W}px;height:{H}px;
      background-image:{overlay(img)};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:130px;left:80px;width:260px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.55))}}
    .wrap{{position:absolute;left:80px;right:80px;bottom:270px}}
    .eyebrow{{font-weight:600;font-size:27px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:24px;text-shadow:0 2px 12px rgba(0,0,0,.5)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:.96;
      text-shadow:0 3px 24px rgba(0,0,0,.55)}}
    .body{{font-weight:500;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .gold{{color:{GOLD}}} .terra{{color:{TERRA}}}
    .pill{{display:inline-flex;align-items:center;gap:14px;background:{TERRA};color:{CREAM};
      font-weight:700;border-radius:999px;box-shadow:0 8px 30px rgba(0,0,0,.35)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

STR = {
 "en": {
  "eb1": "Your first word of Portuguese",
  "sub1": '<span class="gold" style="font-weight:600">bong DEE&#8209;ah</span> &nbsp;&middot;&nbsp; &ldquo;Good morning&rdquo;',
  "eb2": "How the locals use it",
  "h2": "Greetings that<br>follow the sun.",
  "items": [("Bom dia","until midday"),("Boa tarde","through the afternoon"),("Boa noite","once the light goes")],
  "close2": "Get the timing right and Lagos feels a little more like home.",
  "eb3": "Fall term &middot; now enrolling",
  "h3a": "Start with", "h3b": "bom dia.",
  "body3": "Small&#8209;group &amp; private classes in European Portuguese, here in Lagos. Beginners always welcome.",
 },
 "pt": {
  "eb1": "Come&ccedil;a o dia em portugu&ecirc;s",
  "sub1": "A primeira palavra de cada dia.",
  "eb2": "Ao ritmo do sol",
  "h2": "Sauda&ccedil;&otilde;es que<br>seguem o sol.",
  "items": [("Bom dia","at&eacute; ao meio&#8209;dia"),("Boa tarde","durante a tarde"),("Boa noite","quando a luz se vai")],
  "close2": "Pequenos detalhes que fazem toda a diferen&ccedil;a.",
  "eb3": "Turma de outono &middot; inscri&ccedil;&otilde;es abertas",
  "h3a": "Come&ccedil;a com", "h3b": "bom dia.",
  "body3": "Aulas de portugu&ecirc;s europeu, em pequenos grupos ou individuais, aqui em Lagos. Iniciantes s&atilde;o sempre bem&#8209;vindos.",
 },
}

def bodies(t):
    s1 = f"""<div class="wrap">
      <div class="eyebrow">{t['eb1']}</div>
      <div class="h1" style="font-size:210px">Bom dia<span class="terra">.</span></div>
      <div class="body" style="font-size:44px;margin-top:30px;letter-spacing:.5px">{t['sub1']}</div>
    </div>"""
    rows = "".join(
      f'<div style="margin-bottom:8px"><b class="gold">{a}</b> &nbsp;{b}</div>' for a,b in t['items'])
    s2 = f"""<div class="wrap">
      <div class="eyebrow">{t['eb2']}</div>
      <div class="h1" style="font-size:112px">{t['h2']}</div>
      <div class="body" style="font-size:44px;line-height:1.5;margin-top:40px">{rows}</div>
      <div class="body" style="font-size:36px;margin-top:38px;opacity:.9;font-weight:400">{t['close2']}</div>
    </div>"""
    s3 = f"""<div class="wrap">
      <div class="eyebrow">{t['eb3']}</div>
      <div class="h1" style="font-size:110px">{t['h3a']}<br><span class="gold">{t['h3b']}</span></div>
      <div class="body" style="font-size:39px;line-height:1.5;margin-top:34px;font-weight:400">{t['body3']}</div>
      <div class="pill" style="font-size:44px;padding:28px 48px;margin-top:48px">patiolanguage.pt &nbsp;&rarr;</div>
    </div>"""
    return [s1, s2, s3]

SLIDES = [  # (imgkey, object-position tuned for 9:16 crop)
    ("cliffs", "58% 58%"),
    ("sun",    "72% 42%"),
    ("meia",   "center 48%"),
]

for lang, t in STR.items():
    tag = "" if lang == "en" else "-pt"
    b = bodies(t)
    names = ["1-hook", "2-teach", "3-cta"]
    for i, (nm, (img, pos)) in enumerate(zip(names, SLIDES)):
        html = page(b[i], img, pos)
        hp = os.path.join(SCRATCH, f"bomdia{tag}-{nm}-story.html")
        with open(hp, "w", encoding="utf-8") as f: f.write(html)
        out = os.path.join(HERE, f"bomdia{tag}-{nm}-ig-story-1080x1920.png")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--window-size={W},{H}",
            "--virtual-time-budget=5000", f"--screenshot={out}",
            "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
        print("built", out)
print("done")
