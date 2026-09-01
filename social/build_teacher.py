#!/usr/bin/env python3
"""'Meet your teacher' post — Sofia Nabais, Director of Studies.
Bio distilled from patiolanguage.pt founders section.
2-slide IG carousel (1080x1350) + FB square (1080x1080).
Photos: class-conversation.jpg (hero), class-standing.jpg (bio slide).
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-White.png")

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMGS = {k: b64(os.path.join(IMGDIR, k + ".jpg")) for k in ("class-conversation", "class-standing")}

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay(img):
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.42) 0%,rgba(43,31,24,.05) 20%,"
            f"rgba(43,31,24,.14) 40%,rgba(43,31,24,.68) 68%,rgba(43,31,24,.96) 100%),"
            f"url(data:image/jpeg;base64,{IMGS[img]})")

def page(w, h, body, img, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay(img)};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:60px;left:72px;width:240px;
      filter:drop-shadow(0 2px 16px rgba(0,0,0,.7))}}
    .wrap{{position:absolute;left:72px;right:72px;bottom:70px}}
    .eyebrow{{font-weight:600;font-size:26px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:20px;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .h1{{font-family:'DM Serif Display',serif;line-height:1.0;
      text-shadow:0 3px 24px rgba(0,0,0,.65)}}
    .role{{font-weight:600;font-size:33px;color:{GOLD};margin-top:16px;
      text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .body{{font-weight:500;text-shadow:0 2px 14px rgba(0,0,0,.8)}}
    .gold{{color:{GOLD}}} .terra{{color:{TERRA}}}
    .pill{{display:inline-flex;align-items:center;gap:14px;background:{TERRA};color:{CREAM};
      font-weight:700;border-radius:999px;box-shadow:0 8px 30px rgba(0,0,0,.4)}}
    .swipe{{position:absolute;right:72px;bottom:74px;font-weight:700;font-size:30px;
      letter-spacing:1px;color:{CREAM};text-shadow:0 2px 12px rgba(0,0,0,.7)}}
    .num{{position:absolute;top:66px;right:78px;font-weight:700;font-size:26px;letter-spacing:3px;
      color:{CREAM};opacity:.85;text-shadow:0 2px 10px rgba(0,0,0,.7)}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

# Slide 1 — hero
s1 = f"""
<div class="num">01 / 02</div>
<div class="wrap">
  <div class="eyebrow">Meet your teacher</div>
  <div class="h1" style="font-size:104px">Sofia Nabais</div>
  <div class="role">Co&#8209;Founder &amp; Director of Studies</div>
  <div class="body" style="font-size:34px;line-height:1.5;margin-top:26px;font-weight:400">
    She has learned a language in a new country herself, so she teaches
    from experience, not just a textbook.
  </div>
</div>
<div class="swipe">Swipe &rarr;</div>
"""

# Slide 2 — bio + CTA
s2 = f"""
<div class="num">02 / 02</div>
<div class="wrap">
  <div class="eyebrow">A little about Sofia</div>
  <div class="h1" style="font-size:78px">She&rsquo;s been the<br><span class="gold">new person too.</span></div>
  <div class="body" style="font-size:34px;line-height:1.5;margin-top:26px;font-weight:400">
    She knows what it takes to learn the language of a new home, and
    now teaches European Portuguese in Lagos, at every level.
  </div>
  <div class="pill" style="font-size:38px;padding:23px 42px;margin-top:36px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

# FB square — hero + CTA
fb = f"""
<div class="wrap" style="bottom:60px">
  <div class="eyebrow">Meet your teacher</div>
  <div class="h1" style="font-size:82px">Sofia Nabais</div>
  <div class="role" style="font-size:30px">Co&#8209;Founder &amp; Director of Studies</div>
  <div class="body" style="font-size:30px;line-height:1.45;margin-top:20px;font-weight:400">
    She has learned a language in a new country herself, so she teaches from
    experience, not just a textbook.
  </div>
  <div class="pill" style="font-size:33px;padding:20px 38px;margin-top:30px">
    patiolanguage.pt &nbsp;&rarr;
  </div>
</div>
"""

JOBS = [
    ("patio-teacher-1-ig-1080x1350", 1080, 1350, s1, "class-standing",     "center 24%"),
    ("patio-teacher-2-ig-1080x1350", 1080, 1350, s2, "class-conversation", "center 32%"),
    ("patio-teacher-fb-1080x1080",   1080, 1080, fb, "class-standing",     "center 22%"),
]
for name, w, h, body, img, pos in JOBS:
    html = page(w, h, body, img, pos)
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
