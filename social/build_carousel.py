#!/usr/bin/env python3
"""3-slide register-now carousel (+ FB square hero) for Patio Language School.
Carousel: slide1 = founders invite, slide2 = the space (classroom),
slide3 = patio-fall-2026-schedule.png (existing graphic, reused as-is).
EN + PT. Renders slides 1 & 2 (IG 1080x1350) and FB squares (1080x1080).
PT copy is non-native: have Sofia proofread before posting.
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
    .swipe{{position:absolute;right:72px;bottom:74px;font-weight:700;font-size:30px;
      letter-spacing:1px;color:{CREAM};text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .num{{position:absolute;top:66px;right:78px;font-weight:700;font-size:26px;letter-spacing:3px;
      color:{CREAM};opacity:.85;text-shadow:0 2px 10px rgba(0,0,0,.6)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

T = {
 "en": {
  "s1_eb":"Fall term &middot; now enrolling","s1_sz":104,"s1_h":"Learn Portuguese,<br><span class='gold'>the Patio way.</span>",
  "s1_b":"Small groups, real conversation and cultural workshops, here in Lagos. All levels welcome.",
  "swipe":"Swipe &rarr;",
  "s2_eb":"A place to belong","s2_sz":92,"s2_h":"A calm space to<br>learn and connect.",
  "s2_b":"Small classes around one table, good coffee, and a community that feels like home.",
  "fb_sz":84,"fb_b":"Small groups, real conversation &amp; cultural workshops in Lagos. All levels welcome.",
 },
 "pt": {
  "s1_eb":"Inscri&ccedil;&otilde;es abertas &middot; outono","s1_sz":98,"s1_h":"O teu portugu&ecirc;s<br><span class='gold'>come&ccedil;a aqui.</span>",
  "s1_b":"Turmas pequenas, conversa&ccedil;&atilde;o e oficinas culturais, aqui em Lagos. Todos os n&iacute;veis s&atilde;o bem&#8209;vindos.",
  "swipe":"Arrasta &rarr;",
  "s2_eb":"Um lugar para pertencer","s2_sz":86,"s2_h":"Um espa&ccedil;o para<br>aprender e conviver.",
  "s2_b":"Turmas pequenas &agrave; volta de uma mesa, um bom caf&eacute; e uma comunidade que se sente como casa.",
  "fb_sz":82,"fb_b":"Turmas pequenas, conversa&ccedil;&atilde;o e oficinas culturais em Lagos. Todos os n&iacute;veis s&atilde;o bem&#8209;vindos.",
 },
}

def s1_body(t, num=True):
    n = f'<div class="num">01 / 03</div>' if num else ''
    return f"""{n}<div class="wrap">
      <div class="eyebrow">{t['s1_eb']}</div>
      <div class="h1" style="font-size:{t['s1_sz']}px">{t['s1_h']}</div>
      <div class="body" style="font-size:35px;line-height:1.5;margin-top:28px;font-weight:400">{t['s1_b']}</div>
    </div><div class="swipe">{t['swipe']}</div>"""

def s2_body(t):
    return f"""<div class="num">02 / 03</div><div class="wrap">
      <div class="eyebrow">{t['s2_eb']}</div>
      <div class="h1" style="font-size:{t['s2_sz']}px">{t['s2_h']}</div>
      <div class="body" style="font-size:35px;line-height:1.5;margin-top:28px;font-weight:400">{t['s2_b']}</div>
    </div>"""

def fb_body(t):
    return f"""<div class="wrap" style="bottom:64px">
      <div class="eyebrow">{t['s1_eb']}</div>
      <div class="h1" style="font-size:{t['fb_sz']}px">{t['s1_h']}</div>
      <div class="body" style="font-size:31px;line-height:1.45;margin-top:22px;font-weight:400">{t['fb_b']}</div>
      <div class="pill" style="font-size:35px;padding:21px 40px;margin-top:32px">patiolanguage.pt &nbsp;&rarr;</div>
    </div>"""

def render(name, w, h, body, img, pos):
    html = page(w, h, body, img, pos)
    hp = os.path.join(SCRATCH, name + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    print("built", out)

for lang, t in T.items():
    tag = "" if lang == "en" else "-pt"
    render(f"patio-carousel{tag}-1-invite-ig-1080x1350", 1080, 1350, s1_body(t), "founders", "center 26%")
    render(f"patio-carousel{tag}-2-space-ig-1080x1350",  1080, 1350, s2_body(t), "classroom", "center 42%")
    render(f"patio-invite{tag}-fb-1080x1080",            1080, 1080, fb_body(t), "founders", "center 22%")
print("done")
