#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FB post for TODAY: AI Made Practical Workshop (terracotta look, Patio photo). 1080x1080."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H = 1080, 1080

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
AREK = b64(os.path.join(IMG, "arek.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display&display=swap" rel="stylesheet">')
URL = "patiolanguage.pt/ai"
BG = "background:radial-gradient(130% 95% at 50% 8%,#FFF9F0 0%,#FBF0E1 50%,#F3DEC6 100%);"

def build(kind, w, h, fname):
    if kind == "fb":  # 1080x1080
        pad,logo,eb,cheers,h1f,hook,cardmt,ctpad,av,host,hsm,when,timef,pill,cta,ctapad,url = \
            "18px 56px 14px",88,29,42,70,36,14,"20px 34px 22px",190,48,28,50,40,39,44,"18px 56px",34
    else:  # story 1080x1920
        pad,logo,eb,cheers,h1f,hook,cardmt,ctpad,av,host,hsm,when,timef,pill,cta,ctapad,url = \
            "150px 80px 150px",130,38,64,92,48,36,"44px 44px 48px",300,66,36,66,54,52,58,"26px 72px",44
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;{BG}
  color:#2B1F18;display:flex;flex-direction:column;align-items:center;text-align:center;padding:{pad};}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:{logo}px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:{eb}px;margin-top:8px;}}
.cheers{{font-size:{cheers}px;line-height:1;margin-top:4px;}}
h1{{font-family:'DM Serif Display',serif;font-size:{h1f}px;line-height:1.0;margin-top:4px;color:#3b5553;}}
.hook{{display:inline-block;background:#52706e;color:#FBF6EE;font-weight:700;font-size:{hook}px;
  margin-top:14px;padding:{int(hook*0.36)}px {int(hook*0.95)}px;border-radius:999px;box-shadow:0 10px 26px rgba(43,31,24,.2);}}
.card{{width:100%;flex:none;border-radius:28px;margin-top:{cardmt}px;border-top:12px solid #C19D5F;
  background:radial-gradient(130% 120% at 50% 0%,#6f8988 0%,#52706e 55%,#3b5553 100%);
  color:#FBF6EE;box-shadow:0 20px 46px rgba(43,31,24,.26);}}
.ct{{padding:{ctpad};}}
.avatar{{width:{av}px;height:{av}px;margin:0 auto;border-radius:50%;
  background:linear-gradient(135deg,#F0D4A6,#C19D5F);padding:{int(av*0.045)}px;box-shadow:0 14px 34px rgba(0,0,0,.3);}}
.avatar img{{width:100%;height:100%;border-radius:50%;display:block;background:#2B1F18;}}
.host{{font-family:'DM Serif Display',serif;font-size:{host}px;margin-top:16px;color:#FFF7EC;}}
.host small{{display:block;font-family:'Barlow';color:#F0D4A6;font-weight:700;font-size:{hsm}px;
  letter-spacing:.06em;text-transform:uppercase;margin-bottom:4px;}}
.when{{font-family:'DM Serif Display',serif;font-size:{when}px;margin-top:18px;color:#FFF7EC;}}
.time{{font-weight:700;font-size:{timef}px;margin-top:8px;color:#EAF1EF;}}
.pill{{display:inline-block;background:#B8593A;color:#FBF6EE;font-weight:700;font-size:{pill}px;
  border-radius:999px;padding:{int(pill*0.34)}px {int(pill*0.92)}px;margin-top:16px;}}
.pill b{{color:#F4E7CF;}}
.foot{{margin-top:auto;padding-top:{18 if kind!='fb' else 14}px;display:flex;flex-direction:column;align-items:center;}}
.cta{{background:#3b5553;color:#FBF6EE;font-weight:700;font-size:{cta}px;border-radius:999px;
  padding:{ctapad};box-shadow:0 14px 34px rgba(43,31,24,.28);}}
.u{{color:#3b5553;font-weight:700;font-size:{url}px;margin-top:12px;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<img class="logo" src="{LOGO_COLOR}">
<div class="eyebrow">Happening today &middot; Lagos</div>
<div class="cheers">&#129346;</div>
<h1>AI Made Practical Workshop</h1>
<div class="hook">Are you curious about AI?</div>
<div class="card">
  <div class="ct">
    <div class="avatar"><img src="{AREK}"></div>
    <div class="host"><small>With your host</small>Arek Adeoye</div>
    <div class="when">Today &middot; Wed 7 Oct</div>
    <div class="time">17h00 to 19h30 &middot; at Patio</div>
    <div class="pill"><b>&euro;20</b> &middot; includes a drink</div>
  </div>
</div>
<div class="foot"><div class="cta">Come along today</div><div class="u">{URL}</div></div>
</div>"""
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'
    hp = os.path.join(SOCIAL, fname)
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html)
    png = os.path.join(SOCIAL, fname.replace(".html", ".png"))
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--default-background-color=00000000", f"--screenshot={png}", hp],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    build("fb", 1080, 1080, "today-fb-1080x1080.html")
    build("story", 1080, 1920, "today-story-1080x1920.html")
