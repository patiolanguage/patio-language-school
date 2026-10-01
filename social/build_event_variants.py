#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Two background options for the event story, side by side.
A: full-bleed people photo (brighter).  B: clean bright brand bg + photo accent card.
"""
import base64, os, subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H = 1080, 1920

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
PEOPLE = b64(os.path.join(IMG, "ai-workshop-photo.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display&display=swap" rel="stylesheet">')
URL = "patiolanguage.pt/ai"

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def render(fname, html, w=W, h=H):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--default-background-color=00000000",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return os.path.join(SOCIAL, png)

ROWS = """
<div class="rows">
  <div class="row"><div class="l"><div class="rn">AI for Business</div>
    <div class="rm">Wed from 14 Oct</div></div><div class="rp b">&euro;249</div></div>
  <div class="row s"><div class="l"><div class="rn">AI Made Simple</div>
    <div class="rm">Fri from 16 Oct</div></div><div class="rp t">&euro;149</div></div>
</div>"""

def variant_A():
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{W}px;height:{H}px;}}
.c{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Barlow',sans-serif;
  display:flex;flex-direction:column;align-items:center;text-align:center;padding:140px 90px 150px;}}
.c>.bg{{position:absolute;inset:-10px;z-index:0;background-image:url('{PEOPLE}');background-size:cover;
  background-position:center 36%;}}
.c>.wash{{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(255,247,237,.8) 0%,rgba(253,236,223,.46) 30%,rgba(43,31,24,.26) 68%,rgba(43,31,24,.5) 100%);}}
.c>*{{position:relative;z-index:2;}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;z-index:3;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:176px;object-fit:contain;}}
.eyebrow{{color:#A84A2C;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:38px;margin-top:8px;text-shadow:0 1px 10px rgba(255,249,242,1);}}
h1{{font-family:'DM Serif Display',serif;font-size:112px;line-height:1;margin-top:8px;color:#2B1F18;
  text-shadow:0 2px 12px rgba(255,249,242,1),0 0 30px rgba(255,249,242,.9);}}
.hook{{display:inline-block;background:rgba(255,250,244,.92);color:#B8593A;font-weight:700;font-size:56px;
  margin-top:18px;padding:19px 40px;border-radius:999px;box-shadow:0 10px 26px rgba(43,31,24,.18);}}
.card{{width:100%;background:#fff;border-radius:28px;padding:38px 44px;margin-top:38px;
  box-shadow:0 16px 40px rgba(43,31,24,.2);border-top:12px solid #C19D5F;}}
.card .nm{{font-family:'DM Serif Display',serif;font-size:54px;color:#2B1F18;}}
.card .dt{{color:#2B1F18;font-weight:700;font-size:52px;margin-top:12px;}}
.pill{{display:inline-block;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:48px;border-radius:999px;padding:16px 38px;margin-top:20px;}}
.pill b{{color:#F4E7CF;}}
.rows{{width:100%;display:flex;flex-direction:column;gap:14px;margin-top:36px;}}
.row{{background:#fff;border-radius:18px;padding:20px 28px;display:flex;align-items:center;justify-content:space-between;
  box-shadow:0 8px 22px rgba(43,31,24,.14);border-left:10px solid #B8593A;text-align:left;}}
.row.s{{border-left-color:#617C7B;}}
.rn{{font-family:'DM Serif Display',serif;font-size:46px;color:#2B1F18;}}
.rm{{color:#6a5f52;font-weight:700;font-size:34px;margin-top:4px;}}
.rp{{font-family:'DM Serif Display',serif;font-size:52px;}}.rp.b{{color:#B8593A;}}.rp.t{{color:#617C7B;}}
.foot{{margin-top:auto;padding-top:34px;display:flex;flex-direction:column;align-items:center;}}
.cta{{background:linear-gradient(135deg,#C4674B,#B8593A);color:#FBF6EE;font-weight:700;font-size:58px;
  border-radius:999px;padding:30px 70px;box-shadow:0 14px 34px rgba(184,89,58,.5);}}
.u{{color:#FBF6EE;font-weight:700;font-size:42px;margin-top:16px;text-shadow:0 1px 8px rgba(0,0,0,.4);}}
.w{{color:#FBE9DA;font-weight:600;font-size:36px;margin-top:6px;text-shadow:0 1px 8px rgba(0,0,0,.4);}}
"""
    body = f"""<div class="c"><div class="bg"></div><div class="wash"></div><div class="bar"></div>
<img class="logo" src="{LOGO}">
<div class="eyebrow">You're invited</div>
<h1>AI Happy Hour &amp; Workshop</h1>
<div class="hook">Want to use AI smarter?</div>
<div class="card"><div class="nm">AI Made Practical Workshop</div>
  <div class="dt">Wed 7 Oct &middot; 17h00 to 19h30</div>
  <div class="pill"><b>&euro;20</b> &middot; includes a drink</div></div>
{ROWS}
<div class="foot"><div class="cta">Register today</div>
  <div class="u">{URL}</div><div class="w">All welcome &middot; Lagos</div></div>
</div>"""
    return render("event-A-1080x1920.html", page(css, body))

def build_B(kind, w, h, fname):
    if kind == "story":
        pad, logo, eb, h1, hook, photo, nm, dt, pill, ctp, rg, rn, rm, rp, cta, u, wf, cm = \
            "58px 86px 70px", 152, 34, 94, 52, 230, 50, 44, 42, "26px 40px 30px", 12, 44, 31, 48, 54, 40, 34, 28
    elif kind == "post":  # 1080x1350
        pad, logo, eb, h1, hook, photo, nm, dt, pill, ctp, rg, rn, rm, rp, cta, u, wf, cm = \
            "28px 82px 28px", 108, 29, 72, 42, 150, 42, 38, 36, "20px 36px 24px", 10, 38, 28, 42, 46, 35, 31, 16
    else:  # fb square 1080x1080
        pad, logo, eb, h1, hook, photo, nm, dt, pill, ctp, rg, rn, rm, rp, cta, u, wf, cm = \
            "22px 66px 24px", 92, 25, 58, 35, 132, 38, 33, 32, "16px 32px 20px", 8, 34, 25, 38, 40, 31, 28, 12
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;
  background:radial-gradient(130% 95% at 50% 8%,#FFF9F0 0%,#FDEBDC 48%,#F7D9BE 100%);
  color:#2B1F18;display:flex;flex-direction:column;align-items:center;text-align:center;padding:{pad};}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:{logo}px;object-fit:contain;}}
.eyebrow{{color:#A84A2C;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:{eb}px;margin-top:6px;}}
h1{{font-family:'DM Serif Display',serif;font-size:{h1}px;line-height:1;margin-top:6px;}}
.hook{{display:inline-block;background:#B8593A;color:#FBF6EE;font-weight:700;font-size:{hook}px;
  margin-top:16px;padding:{int(hook*0.32)}px {int(hook*0.8)}px;border-radius:999px;box-shadow:0 10px 26px rgba(184,89,58,.3);}}
.card{{width:100%;flex:none;background:#fff;border-radius:26px;overflow:hidden;margin-top:{cm}px;
  box-shadow:0 16px 40px rgba(43,31,24,.14);}}
.hhphoto{{height:{photo}px;background-image:url('{PEOPLE}');background-size:cover;background-position:center 40%;}}
.cardtext{{padding:{ctp};border-top:10px solid #C19D5F;}}
.card .nm{{font-family:'DM Serif Display',serif;font-size:{nm}px;color:#2B1F18;}}
.card .dt{{color:#2B1F18;font-weight:700;font-size:{dt}px;margin-top:10px;}}
.pill{{display:inline-block;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:{pill}px;border-radius:999px;padding:14px 36px;margin-top:16px;}}
.pill b{{color:#F4E7CF;}}
.rows{{width:100%;flex:none;display:flex;flex-direction:column;gap:{rg}px;margin-top:{cm-6}px;}}
.row{{background:#fff;border-radius:18px;padding:18px 28px;display:flex;align-items:center;justify-content:space-between;
  box-shadow:0 8px 22px rgba(43,31,24,.09);border-left:10px solid #B8593A;text-align:left;}}
.row.s{{border-left-color:#617C7B;}}
.rn{{font-family:'DM Serif Display',serif;font-size:{rn}px;color:#2B1F18;}}
.rm{{color:#6a5f52;font-weight:700;font-size:{rm}px;margin-top:4px;}}
.rp{{font-family:'DM Serif Display',serif;font-size:{rp}px;}}.rp.b{{color:#B8593A;}}.rp.t{{color:#617C7B;}}
.foot{{margin-top:auto;padding-top:{cm-4}px;display:flex;flex-direction:column;align-items:center;}}
.cta{{background:linear-gradient(135deg,#C4674B,#B8593A);color:#FBF6EE;font-weight:700;font-size:{cta}px;
  border-radius:999px;padding:{int(cta*0.48)}px {int(cta*1.2)}px;box-shadow:0 14px 34px rgba(184,89,58,.4);}}
.u{{color:#2B1F18;font-weight:700;font-size:{u}px;margin-top:14px;}}
.w{{color:#7a4a33;font-weight:600;font-size:{wf}px;margin-top:6px;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<img class="logo" src="{LOGO}">
<div class="eyebrow">You're invited</div>
<h1>AI Happy Hour &amp; Workshop</h1>
<div class="hook">Want to use AI smarter?</div>
<div class="card"><div class="hhphoto"></div>
  <div class="cardtext"><div class="nm">AI Made Practical Workshop</div>
    <div class="dt">Wed 7 Oct &middot; 17h00 to 19h30</div>
    <div class="pill"><b>&euro;20</b> &middot; includes a drink</div></div></div>
{ROWS}
<div class="foot"><div class="cta">Register today</div>
  <div class="u">{URL}</div><div class="w">All welcome &middot; Lagos</div></div>
</div>"""
    return render(fname, page(css, body), w, h)

if __name__ == "__main__":
    build_B("story", 1080, 1920, "event-story-1080x1920.html")
    build_B("post", 1080, 1350, "event-post-1080x1350.html")
    build_B("fb", 1080, 1080, "event-fb-1080x1080.html")
    print("done")
