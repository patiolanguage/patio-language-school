#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bright, welcoming event creative for the Happy Hour + workshops: Story + Post.

Warm cream/peach/gold palette, inviting tone. Happy Hour is the hero, with the
two workshops below. Brand: DM Serif Display + Barlow. No em/en dashes.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
SPACE = b64(os.path.join(IMG, "ai-room-photo.jpg")) if os.path.exists(os.path.join(IMG, "ai-room-photo.jpg")) else ""
def b64jpg(path):
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
SPACE = b64jpg(os.path.join(IMG, "ai-room-photo.jpg"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

URL = "patiolanguage.pt/ai"
# bright, warm welcoming background
BG = "background:radial-gradient(130% 95% at 50% 8%,#FFF9F0 0%,#FDEBDC 48%,#F7D9BE 100%);"

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def render(fname, html, w, h):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--default-background-color=00000000",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)


def build(kind, w, h):
    if kind == "story":
        pad, logo, eb, h1, cheers, nm, dt, pricep, rn, rm, rp, foot, cardpad, gap, ctaf, hookf = \
            "140px 92px 160px", 186, 40, 114, 84, 54, 54, 50, 46, 34, 52, 42, "40px 46px", 36, 60, 58
    else:  # ig post 1080x1350
        pad, logo, eb, h1, cheers, nm, dt, pricep, rn, rm, rp, foot, cardpad, gap, ctaf, hookf = \
            "36px 82px 32px", 146, 32, 80, 60, 46, 45, 40, 38, 29, 44, 36, "28px 38px", 18, 48, 48
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;{BG}
  color:#2B1F18;display:flex;flex-direction:column;align-items:center;text-align:center;padding:{pad};}}
.c > .spacebg{{position:absolute;inset:-12px;z-index:0;background-image:url('{SPACE}');background-size:180% auto;
  background-position:center 78%;filter:blur(3px) brightness(.82) sepia(.28) saturate(1.25);}}
.c > .wash{{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(255,247,237,.74) 0%,rgba(253,238,225,.56) 34%,rgba(250,225,203,.44) 60%,rgba(244,205,176,.6) 100%);}}
.c > *{{position:relative;z-index:2;}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;z-index:3;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:{logo}px;object-fit:contain;}}
.eyebrow{{color:#A84A2C;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:{eb}px;margin-top:8px;text-shadow:0 1px 10px rgba(255,249,242,1),0 1px 3px rgba(255,249,242,1);}}
.cheers{{font-size:{cheers}px;line-height:1;margin-top:10px;}}
h1{{font-family:'DM Serif Display',serif;font-size:{h1}px;line-height:1.0;margin-top:8px;
  text-shadow:0 2px 12px rgba(255,249,242,1),0 1px 4px rgba(255,249,242,1),0 0 30px rgba(255,249,242,.9);}}
.hook{{display:inline-block;background:rgba(255,250,244,.9);color:#B8593A;font-weight:700;
  font-size:{hookf}px;margin-top:18px;padding:{int(hookf*0.34)}px {int(hookf*0.7)}px;
  border-radius:999px;box-shadow:0 10px 26px rgba(43,31,24,.16);}}
.card{{width:100%;background:#fff;border-radius:28px;padding:{cardpad};margin-top:{gap}px;
  box-shadow:0 16px 40px rgba(43,31,24,.14);border-top:12px solid #C19D5F;}}
.card .nm{{font-family:'DM Serif Display',serif;font-size:{nm}px;color:#2B1F18;line-height:1.02;}}
.card .dt{{color:#2B1F18;font-weight:700;font-size:{dt}px;margin-top:14px;}}
.pill{{display:inline-block;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:{pricep}px;
  border-radius:999px;padding:18px 40px;margin-top:22px;}}
.pill b{{color:#F4E7CF;}}
.rows{{width:100%;display:flex;flex-direction:column;gap:14px;margin-top:{gap}px;}}
.row{{background:#fff;border-radius:18px;padding:20px 28px;display:flex;align-items:center;
  justify-content:space-between;gap:16px;box-shadow:0 8px 22px rgba(43,31,24,.08);border-left:10px solid #B8593A;text-align:left;}}
.row:nth-child(2){{border-left-color:#617C7B;}}
.row .l .rn{{font-family:'DM Serif Display',serif;font-size:{rn}px;color:#2B1F18;line-height:1;}}
.row .l .rm{{color:#6a5f52;font-weight:700;font-size:{rm}px;margin-top:4px;}}
.row .rp{{font-family:'DM Serif Display',serif;font-size:{rp}px;color:#B8593A;flex:none;}}
.row:nth-child(2) .rp{{color:#617C7B;}}
.foot{{margin-top:auto;padding-top:{gap}px;display:flex;flex-direction:column;align-items:center;}}
.cta{{background:linear-gradient(135deg,#C4674B,#B8593A);color:#FBF6EE;font-weight:700;
  font-size:{ctaf}px;border-radius:999px;padding:{int(ctaf*0.5)}px {int(ctaf*1.2)}px;
  box-shadow:0 14px 34px rgba(184,89,58,.4);letter-spacing:.01em;}}
.foot .u{{color:#2B1F18;font-weight:700;font-size:{foot}px;margin-top:16px;}}
.foot .w{{color:#7a4a33;font-weight:600;font-size:{foot-4}px;margin-top:6px;}}
"""
    body = f"""<div class="c">
<div class="spacebg"></div><div class="wash"></div>
<div class="bar"></div>
<img class="logo" src="{LOGO_COLOR}">
<div class="eyebrow">You're invited</div>
<div class="cheers">&#129346;</div>
<h1>AI Happy Hour &amp; Workshop</h1>
<div class="hook">Want to use AI smarter?</div>
<div class="card">
  <div class="nm">AI Made Practical Workshop</div>
  <div class="dt">Wed 7 Oct &middot; 17h00 to 19h30</div>
  <div class="pill"><b>&euro;20</b> &middot; includes a drink</div>
</div>
<div class="rows">
  <div class="row"><div class="l"><div class="rn">AI for Business</div>
    <div class="rm">Wed from 14 Oct</div></div><div class="rp">&euro;249</div></div>
  <div class="row"><div class="l"><div class="rn">AI Made Simple</div>
    <div class="rm">Fri from 16 Oct</div></div><div class="rp">&euro;149</div></div>
</div>
<div class="foot">
  <div class="cta">Register today</div>
  <div class="u">{URL}</div>
  <div class="w">All welcome &middot; Lagos</div>
</div>
</div>"""
    render(f"event-{kind}-{w}x{h}.html", page(css, body), w, h)


if __name__ == "__main__":
    build("story", 1080, 1920)
    build("post", 1080, 1350)
    print("done")
