#!/usr/bin/env python3
"""Portuguese-audience versions of the "Bom dia" posts for Patio Language School.
IG carousel (3 slides, 1080x1350) + FB square (1080x1080).
Same design/photos as build_bomdia.py; copy in European Portuguese (informal 'tu').
NOTE: have Sofia proofread before posting, per the usual PT review workflow.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = r"C:/Users/Claire/Patio Language School/assets/img/Patio-Language-School-Logo-White.png"

GOLD = "#D8B778"
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

# ---------- SLIDE 1 : HOOK (cliffs) ----------
s1 = f"""
<div class="num">01 / 03</div>
<div class="wrap">
  <div class="eyebrow">Come&ccedil;a o dia em portugu&ecirc;s</div>
  <div class="h1" style="font-size:196px">Bom dia<span class="terra">.</span></div>
  <div class="body" style="font-size:42px;margin-top:26px;letter-spacing:.5px">
    A primeira palavra de cada dia.
  </div>
</div>
<div class="swipe">Arrasta &rarr;</div>
"""

# ---------- SLIDE 2 : TEACH (sunrise) ----------
s2 = f"""
<div class="num">02 / 03</div>
<div class="wrap">
  <div class="eyebrow">Ao ritmo do sol</div>
  <div class="h1" style="font-size:96px">Sauda&ccedil;&otilde;es que<br>seguem o sol.</div>
  <div class="body" style="font-size:39px;line-height:1.5;margin-top:34px">
    <b class="gold">Bom dia</b> &nbsp;at&eacute; ao meio&#8209;dia<br>
    <b class="gold">Boa tarde</b> &nbsp;durante a tarde<br>
    <b class="gold">Boa noite</b> &nbsp;quando a luz se vai
  </div>
  <div class="body" style="font-size:33px;margin-top:34px;opacity:.9;font-weight:400">
    Pequenos detalhes que fazem toda a diferen&ccedil;a.
  </div>
</div>
"""

# ---------- SLIDE 3 : CTA (meia praia) ----------
s3 = f"""
<div class="num">03 / 03</div>
<div class="wrap">
  <div class="eyebrow">Turma de outono &middot; inscri&ccedil;&otilde;es abertas</div>
  <div class="h1" style="font-size:98px">Come&ccedil;a com<br><span class="gold">bom dia.</span></div>
  <div class="body" style="font-size:35px;line-height:1.5;margin-top:30px;font-weight:400">
    Aulas de portugu&ecirc;s europeu, em pequenos grupos ou individuais,
    aqui em Lagos. Iniciantes s&atilde;o sempre bem&#8209;vindos.
  </div>
  <div class="pill" style="font-size:41px;padding:26px 44px;margin-top:44px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

# ---------- FB SQUARE (sunrise) ----------
fb = f"""
<div class="wrap" style="bottom:80px">
  <div class="eyebrow">Come&ccedil;a o dia em portugu&ecirc;s</div>
  <div class="h1" style="font-size:150px">Bom dia<span class="terra">.</span></div>
  <div class="body" style="font-size:38px;margin-top:22px;letter-spacing:.5px">
    A primeira palavra de cada dia.
  </div>
  <div class="body" style="font-size:33px;margin-top:26px;font-weight:400;opacity:.92">
    Turma de outono com inscri&ccedil;&otilde;es abertas. Iniciantes bem&#8209;vindos.
  </div>
  <div class="pill" style="font-size:37px;padding:22px 40px;margin-top:38px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

JOBS = [
    ("bomdia-pt-1-hook-ig-1080x1350",   1080, 1350, s1, "cliffs", "center 55%"),
    ("bomdia-pt-2-teach-ig-1080x1350",  1080, 1350, s2, "sun",    "center 42%"),
    ("bomdia-pt-3-cta-ig-1080x1350",    1080, 1350, s3, "meia",   "center 40%"),
    ("bomdia-pt-fb-1080x1080",          1080, 1080, fb, "sun",    "center 55%"),
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
