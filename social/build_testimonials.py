#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build Patio Language School testimonial social cards (IG carousel + FB post)."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))

def b64jpg(path):
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

COVER_PHOTO = b64jpg(os.path.join(IMG, "class-conversation.jpg"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

# ---- shortened testimonials ----
TESTS = [
    {
        "quote": "Learning a new language can be overwhelming. Sofia makes it easier &mdash; a knowledgeable, patient teacher who adapts each lesson to what the class needs in the moment.",
        "name": "Nancy Lee",
        "role": "Group student",
    },
    {
        "quote": "After four months of private lessons, my wife and I would happily recommend Sofia. Formal but relaxed and professional, and she speaks excellent English.",
        "name": "Simon Mahon",
        "role": "Private student",
    },
    {
        "quote": "Sofia represents everything great about Portugal. A kind, caring teacher who goes above and beyond. Her lessons are fun but challenging &mdash; the perfect introduction to Portuguese.",
        "name": "Alison &amp; Bill Forder",
        "role": "Private students",
    },
]

# ---------- testimonial slide (1080x1350) ----------
def slide_css(w, h, qsize, name_weight=700):
    return f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{w}px;height:{h}px;}}
.canvas{{position:relative;width:{w}px;height:{h}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:130px 110px;text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:66px;left:0;right:0;text-align:center;
  color:#726651;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:24px;}}
.mark{{font-family:'DM Serif Display',serif;color:#C19D5F;font-size:200px;
  line-height:.4;height:96px;margin-bottom:8px;}}
.quote{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:{qsize}px;
  line-height:1.28;font-style:italic;}}
.rule{{width:70px;height:4px;background:#B8593A;border-radius:3px;margin:44px auto 30px;}}
.name{{color:#B8593A;font-weight:{name_weight};font-size:38px;letter-spacing:.01em;}}
.role{{color:#726651;font-weight:600;font-size:26px;letter-spacing:.14em;
  text-transform:uppercase;margin-top:10px;}}
.logo{{position:absolute;bottom:60px;left:0;right:0;margin:0 auto;height:58px;
  display:block;object-fit:contain;}}
.count{{position:absolute;bottom:64px;right:72px;color:#726651;font-weight:700;
  font-size:26px;letter-spacing:.1em;}}
"""

def build_slide(t, idx, total, fname):
    qsize = 58 if len(t["quote"]) < 170 else 54
    nw = t.get("name_weight", 700)
    html = (f'<!DOCTYPE html><html><head>{FONTS}<style>{slide_css(1080,1350,qsize,nw)}</style></head>'
        f'<body><div class="canvas">'
        f'<div class="eyebrow">What our students say</div>'
        f'<div class="mark">&ldquo;</div>'
        f'<div class="quote">{t["quote"]}</div>'
        f'<div class="rule"></div>'
        f'<div class="name">{t["name"]}</div>'
        f'<div class="role">{t["role"]}</div>'
        f'<img class="logo" src="{LOGO_COLOR}">'
        f'<div class="count">{idx}/{total}</div>'
        f'</div></body></html>')
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

# ---------- IG carousel cover (1080x1350) ----------
def build_cover(fname):
    css = """
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1080px;height:1350px;}
.canvas{position:relative;width:1080px;height:1350px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 32%;}
.scrim{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.62) 0%, rgba(43,31,24,.30) 30%, rgba(43,31,24,.55) 62%, rgba(43,31,24,.94) 100%);}
.bar{position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}
.eyebrow{position:absolute;top:60px;left:0;right:0;text-align:center;color:#FBF6EE;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:25px;text-shadow:0 1px 8px rgba(0,0,0,.5);z-index:2;}
.overlay{position:absolute;left:0;right:0;bottom:0;padding:0 100px 60px;text-align:center;z-index:2;}
.stars{color:#E0A868;font-size:52px;letter-spacing:.12em;margin-bottom:24px;
  text-shadow:0 1px 8px rgba(0,0,0,.5);}
.headline{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:98px;line-height:1.02;
  text-shadow:0 2px 16px rgba(0,0,0,.55);}
.headline .a{color:#E0A868;font-style:italic;}
.sub{color:#F1E3CE;font-size:35px;font-weight:500;margin-top:28px;line-height:1.4;
  text-shadow:0 1px 10px rgba(0,0,0,.5);}
.swipe{color:#E0A868;font-weight:700;font-size:30px;letter-spacing:.06em;margin-top:40px;
  text-shadow:0 1px 8px rgba(0,0,0,.5);}
.logo{height:56px;display:block;margin:42px auto 0;object-fit:contain;}
"""
    html = (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
        f'<body><div class="canvas">'
        f'<img class="bg" src="{COVER_PHOTO}">'
        f'<div class="scrim"></div>'
        f'<div class="bar"></div>'
        f'<div class="eyebrow">Patio Language School &middot; Lagos</div>'
        f'<div class="overlay">'
        f'<div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<div class="headline">What our<br>students <span class="a">say</span></div>'
        f'<div class="sub">Real words from people learning<br>Portuguese with Sofia</div>'
        f'<div class="swipe">Swipe to read &rarr;</div>'
        f'<img class="logo" src="{LOGO_WHITE}">'
        f'</div>'
        f'</div></body></html>')
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

# ---------- Facebook post (1080x1080) all three ----------
def build_fb(fname):
    css = """
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1080px;height:1080px;}
.canvas{position:relative;width:1080px;height:1080px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;padding:74px 66px 64px;
  display:flex;flex-direction:column;}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;}
.scrim{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.58) 0%, rgba(43,31,24,.50) 50%, rgba(43,31,24,.66) 100%);}
.bar{position:absolute;top:0;left:0;right:0;height:14px;z-index:3;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}
.head,.cards,.foot{position:relative;z-index:2;}
.head{text-align:center;margin-bottom:30px;}
.eyebrow{color:#E0A868;font-weight:700;letter-spacing:.2em;text-transform:uppercase;font-size:22px;
  text-shadow:0 1px 6px rgba(0,0,0,.5);}
.title{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:60px;line-height:1.02;margin-top:8px;
  text-shadow:0 2px 12px rgba(0,0,0,.55);}
.title .a{color:#E0A868;font-style:italic;}
.cards{flex:1;display:flex;flex-direction:column;gap:20px;}
.card{background:#fff;border-radius:22px;padding:30px 40px;
  box-shadow:0 12px 34px rgba(0,0,0,.30);flex:1;display:flex;flex-direction:column;justify-content:center;
  border-left:8px solid #C19D5F;}
.card:nth-child(2){border-left-color:#B8593A;}
.card:nth-child(3){border-left-color:#617C7B;}
.q{color:#2B1F18;font-size:29px;line-height:1.34;font-style:italic;font-family:'DM Serif Display',serif;}
.n{color:#B8593A;font-weight:700;font-size:25px;margin-top:14px;}
.foot{text-align:center;margin-top:30px;}
.logo{height:48px;object-fit:contain;}
"""
    fb_tests = [
        "Sofia makes learning a new language easier. A knowledgeable, patient teacher who adapts to what the class needs.",
        "After four months of private lessons, my wife and I would happily recommend Sofia. Professional, relaxed, excellent English.",
        "A kind, caring teacher who goes above and beyond. Fun but challenging, and the perfect introduction to Portuguese.",
    ]
    names = ["Nancy Lee", "Simon Mahon", "Alison &amp; Bill Forder"]
    cards = "".join(
        f'<div class="card"><div class="q">&ldquo;{q}&rdquo;</div><div class="n">{n}</div></div>'
        for q, n in zip(fb_tests, names))
    html = (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
        f'<body><div class="canvas">'
        f'<img class="bg" src="{COVER_PHOTO}"><div class="scrim"></div><div class="bar"></div>'
        f'<div class="head"><div class="eyebrow">Patio Language School &middot; Lagos</div>'
        f'<div class="title">What our students <span class="a">say</span></div></div>'
        f'<div class="cards">{cards}</div>'
        f'<div class="foot"><img class="logo" src="{LOGO_WHITE}"></div>'
        f'</div></body></html>')
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

def render(html_name, w, h):
    png = html_name.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        f"--screenshot={os.path.join(SOCIAL, png)}",
        os.path.join(SOCIAL, html_name)], check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    files = []
    files.append((build_cover("testimonial-cover-ig-1080x1350.html"), 1080, 1350))
    for i, t in enumerate(TESTS, 1):
        files.append((build_slide(t, i, 3, f"testimonial-{i}-ig-1080x1350.html"), 1080, 1350))
    files.append((build_fb("testimonials-fb-1080x1080.html"), 1080, 1080))
    for name, w, h in files:
        render(name, w, h)
    print("done")
