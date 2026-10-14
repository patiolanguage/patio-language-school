#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""New AI Happy Hour & Workshop creative - warm 'evening invite' look (terracotta).
IG post (1080x1350), Story (1080x1920), FB post (1080x1080). No em/en dashes.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
PEOPLE = b64(os.path.join(IMG, "ai-workshop-photo.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display&display=swap" rel="stylesheet">')
URL = "patiolanguage.pt/ai"
BG = "background:radial-gradient(135% 100% at 50% 0%,#C56A47 0%,#A84A2C 48%,#7C3620 100%);"

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


def build(kind, w, h, fname):
    P = {
      "story": dict(pad="140px 84px 150px", logo=150, eb=36, cheers=84, h1=100, hook=50,
                    photo=250, nm=52, dt=48, pill=44, rn=46, rm=32, rp=50, cta=56, url=42, gap=30),
      "post":  dict(pad="44px 78px 40px", logo=116, eb=30, cheers=60, h1=76, hook=42,
                    photo=168, nm=44, dt=40, pill=38, rn=40, rm=28, rp=44, cta=48, url=37, gap=18),
      "fb":    dict(pad="28px 64px 28px", logo=96, eb=26, cheers=50, h1=58, hook=36,
                    photo=130, nm=37, dt=34, pill=33, rn=34, rm=25, rp=38, cta=42, url=33, gap=12),
    }[kind]
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;{BG}
  color:#FBF6EE;display:flex;flex-direction:column;align-items:center;text-align:center;padding:{P['pad']};}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;background:linear-gradient(90deg,#F0D4A6,#EBB65E);}}
.logo{{height:{P['logo']}px;object-fit:contain;}}
.eyebrow{{color:#F6D9AE;font-weight:700;letter-spacing:.24em;text-transform:uppercase;font-size:{P['eb']}px;margin-top:10px;}}
.cheers{{font-size:{P['cheers']}px;line-height:1;margin-top:8px;}}
h1{{font-family:'DM Serif Display',serif;font-size:{P['h1']}px;line-height:1.0;margin-top:6px;color:#FFF7EC;}}
.hook{{display:inline-block;background:#FBF6EE;color:#A84A2C;font-weight:700;font-size:{P['hook']}px;
  margin-top:16px;padding:{int(P['hook']*0.32)}px {int(P['hook']*0.82)}px;border-radius:999px;box-shadow:0 10px 26px rgba(0,0,0,.22);}}
.card{{width:100%;flex:none;background:#FFFDF9;color:#2B1F18;border-radius:28px;overflow:hidden;margin-top:{P['gap']}px;
  box-shadow:0 20px 46px rgba(0,0,0,.26);}}
.photo{{height:{P['photo']}px;background-image:url('{PEOPLE}');background-size:cover;background-position:center 40%;}}
.ct{{padding:{int(P['gap']*0.9)}px {P['gap']+8}px {P['gap']}px;border-top:10px solid #C19D5F;}}
.nm{{font-family:'DM Serif Display',serif;font-size:{P['nm']}px;}}
.dt{{font-weight:700;font-size:{P['dt']}px;margin-top:8px;}}
.pill{{display:inline-block;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:{P['pill']}px;
  border-radius:999px;padding:12px 32px;margin-top:14px;}}
.pill b{{color:#F4E7CF;}}
.ws{{display:flex;gap:{int(P['gap']*0.5)}px;margin-top:{int(P['gap']*0.7)}px;}}
.chip{{flex:1;background:#FBF4E9;border-radius:16px;padding:{int(P['gap']*0.55)}px {int(P['gap']*0.6)}px;
  text-align:left;border-top:8px solid #B8593A;}}
.chip.t{{border-top-color:#617C7B;}}
.chip .cn{{font-family:'DM Serif Display',serif;font-size:{P['rn']}px;line-height:1;}}
.chip .cm{{color:#6a5f52;font-weight:700;font-size:{P['rm']}px;margin-top:4px;}}
.chip .cp{{font-family:'DM Serif Display',serif;font-size:{P['rp']}px;color:#B8593A;margin-top:4px;}}
.chip.t .cp{{color:#4f6a69;}}
.foot{{margin-top:auto;padding-top:{P['gap']}px;display:flex;flex-direction:column;align-items:center;}}
.cta{{background:#FBF6EE;color:#A84A2C;font-weight:700;font-size:{P['cta']}px;border-radius:999px;
  padding:{int(P['cta']*0.5)}px {int(P['cta']*1.3)}px;box-shadow:0 14px 34px rgba(0,0,0,.28);}}
.u{{color:#F6D9AE;font-weight:700;font-size:{P['url']}px;margin-top:14px;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<img class="logo" src="{LOGO_WHITE}">
<div class="eyebrow">You're invited</div>
<div class="cheers">&#129346;</div>
<h1>AI Happy Hour &amp; Workshop</h1>
<div class="hook">Want to use AI smarter?</div>
<div class="card">
  <div class="photo"></div>
  <div class="ct">
    <div class="nm">AI Made Practical Workshop</div>
    <div class="dt">Wed 7 Oct &middot; 17h00 to 19h30</div>
    <div class="pill"><b>&euro;20</b> &middot; includes a drink</div>
    <div class="ws">
      <div class="chip"><div class="cn">AI for Business</div><div class="cm">from 14 Oct</div><div class="cp">&euro;249</div></div>
      <div class="chip t"><div class="cn">AI Made Simple</div><div class="cm">from 16 Oct</div><div class="cp">&euro;149</div></div>
    </div>
  </div>
</div>
<div class="foot"><div class="cta">Register today</div><div class="u">{URL}</div></div>
</div>"""
    render(fname, page(css, body), w, h)


if __name__ == "__main__":
    build("story", 1080, 1920, "event2-story-1080x1920.html")
    build("post", 1080, 1350, "event2-post-1080x1350.html")
    build("fb", 1080, 1080, "event2-fb-1080x1080.html")
    print("done")
