#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build Patio Language School call-to-action carousel (IG, 1080x1350)."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
COVER_PHOTO = b64(os.path.join(IMG, "class-standing.jpg"), "image/jpeg")
FOUNDERS = b64(os.path.join(IMG, "founders-together.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

W, H = 1080, 1350

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def write(fname, html):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

# ---------- Slide 1: cover (photo + scrim) ----------
def slide_cover(fname):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 40%;}}
.scrim{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.60) 0%, rgba(43,31,24,.28) 28%, rgba(43,31,24,.55) 60%, rgba(43,31,24,.95) 100%);}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}}
.eyebrow{{position:absolute;top:60px;left:0;right:0;text-align:center;color:#FBF6EE;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:25px;text-shadow:0 1px 8px rgba(0,0,0,.5);z-index:2;}}
.overlay{{position:absolute;left:0;right:0;bottom:0;padding:0 96px 62px;text-align:center;z-index:2;}}
.headline{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:96px;line-height:1.02;
  text-shadow:0 2px 16px rgba(0,0,0,.6);}}
.headline .a{{color:#E0A868;font-style:italic;}}
.sub{{color:#F1E3CE;font-size:36px;font-weight:500;margin-top:28px;line-height:1.4;
  text-shadow:0 1px 10px rgba(0,0,0,.55);}}
.swipe{{color:#E0A868;font-weight:700;font-size:30px;letter-spacing:.05em;margin-top:40px;
  text-shadow:0 1px 8px rgba(0,0,0,.5);}}
.logo{{height:56px;display:block;margin:42px auto 0;object-fit:contain;}}
"""
    body = (f'<div class="canvas"><img class="bg" src="{COVER_PHOTO}"><div class="scrim"></div>'
        f'<div class="bar"></div>'
        f'<div class="eyebrow">Now enrolling &middot; Lagos, Portugal</div>'
        f'<div class="overlay">'
        f'<div class="headline">Speak Portuguese,<br><span class="a">for real</span></div>'
        f'<div class="sub">Small, friendly classes<br>opening this September</div>'
        f'<div class="swipe">See how to join &rarr;</div>'
        f'<img class="logo" src="{LOGO_WHITE}"></div></div>')
    return write(fname, page(css, body))

# ---------- Slide 2: what we offer ----------
def slide_offer(fname):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#FBF6EE;padding:150px 90px 90px;
  display:flex;flex-direction:column;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:70px;left:0;right:0;text-align:center;color:#726651;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:24px;}}
.title{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:74px;line-height:1.02;
  text-align:center;margin-bottom:52px;}}
.title .a{{color:#B8593A;font-style:italic;}}
.cards{{flex:1;display:flex;flex-direction:column;gap:34px;}}
.card{{background:#fff;border-radius:26px;padding:52px 54px;
  box-shadow:0 10px 30px rgba(43,31,24,.08);flex:1;display:flex;flex-direction:column;
  justify-content:center;border-top:10px solid #C19D5F;}}
.card.b{{border-top-color:#617C7B;}}
.ct{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:58px;line-height:1.05;}}
.tag{{color:#B8593A;font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase;
  margin-top:14px;}}
.card.b .tag{{color:#617C7B;}}
.cdesc{{color:#4a4038;font-size:35px;font-weight:500;margin-top:18px;line-height:1.38;}}
.logo{{height:52px;object-fit:contain;display:block;margin:44px auto 0;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Two ways to learn</div>'
        f'<div class="title">Find your <span class="a">fit</span></div>'
        f'<div class="cards">'
        f'<div class="card"><div class="ct">Group classes</div>'
        f'<div class="tag">Learn together</div>'
        f'<div class="cdesc">Small groups, every level &mdash; learn alongside others.</div></div>'
        f'<div class="card b"><div class="ct">Private lessons</div>'
        f'<div class="tag">One-to-one</div>'
        f'<div class="cdesc">Just you and your teacher, moving at exactly your pace.</div></div>'
        f'</div><img class="logo" src="{LOGO_COLOR}"></div>')
    return write(fname, page(css, body))

# ---------- Slide 3: why Patio ----------
def slide_why(fname):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#617C7B;padding:150px 96px 90px;
  display:flex;flex-direction:column;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:70px;left:0;right:0;text-align:center;color:#EBDCC4;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:24px;}}
.title{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:76px;line-height:1.02;
  text-align:center;margin-bottom:64px;}}
.title .a{{color:#E7C99A;font-style:italic;}}
.list{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:46px;}}
.row{{display:flex;align-items:flex-start;gap:30px;}}
.tick{{flex:none;width:64px;height:64px;border-radius:50%;background:#FBF6EE;color:#B8593A;
  font-size:38px;font-weight:700;display:flex;align-items:center;justify-content:center;
  font-family:'DM Serif Display',serif;margin-top:2px;}}
.rt{{color:#FBF6EE;font-size:39px;font-weight:600;line-height:1.32;}}
.rt b{{color:#F4E7CF;font-weight:700;}}
.logo{{height:52px;object-fit:contain;display:block;margin:52px auto 0;}}
"""
    rows = [
        "<b>European Portuguese</b>, the way it is really spoken here",
        "Warm, patient teaching that adapts to <b>you</b>",
        "A relaxed community &mdash; not a classroom grind",
    ]
    lis = "".join(f'<div class="row"><div class="tick">&#10003;</div><div class="rt">{r}</div></div>' for r in rows)
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Why Patio</div>'
        f'<div class="title">Learning that <span class="a">feels good</span></div>'
        f'<div class="list">{lis}</div>'
        f'<img class="logo" src="{LOGO_WHITE}"></div>')
    return write(fname, page(css, body))

# ---------- Slide 4: how to join (CTA, founders photo) ----------
def slide_join(fname):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;padding:150px 96px 76px;
  display:flex;flex-direction:column;align-items:center;text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:66px;left:0;right:0;color:#E0A868;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:24px;}}
.photo{{width:210px;height:210px;border-radius:50%;object-fit:cover;object-position:center 30%;
  border:6px solid #C19D5F;margin-bottom:34px;}}
.title{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:82px;line-height:1.02;}}
.title .a{{color:#E0A868;font-style:italic;}}
.sub{{color:#F1E3CE;font-size:35px;font-weight:500;margin-top:22px;line-height:1.4;}}
.contact{{margin-top:auto;width:100%;}}
.cta{{display:inline-block;background:#B8593A;color:#FBF6EE;font-weight:700;font-size:38px;
  padding:26px 60px;border-radius:60px;letter-spacing:.01em;}}
.line{{color:#EBDCC4;font-size:33px;font-weight:600;margin-top:30px;letter-spacing:.01em;}}
.line .g{{color:#E0A868;}}
.logo{{height:56px;object-fit:contain;display:block;margin:40px auto 0;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Ready to start?</div>'
        f'<img class="photo" src="{FOUNDERS}">'
        f'<div class="title">Save your spot<br>for <span class="a">September</span></div>'
        f'<div class="sub">Message us and we will help you<br>find the right class.</div>'
        f'<div class="contact">'
        f'<div class="cta">patiolanguage.pt</div>'
        f'<div class="line">WhatsApp <span class="g">+351 928 129 560</span></div>'
        f'<div class="line">Follow <span class="g">@patiolanguage</span></div>'
        f'<img class="logo" src="{LOGO_WHITE}"></div></div>')
    return write(fname, page(css, body))

def render(fname):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    files = [
        slide_cover("cta-1-cover-ig-1080x1350.html"),
        slide_offer("cta-2-offer-ig-1080x1350.html"),
        slide_why("cta-3-why-ig-1080x1350.html"),
        slide_join("cta-4-join-ig-1080x1350.html"),
    ]
    for f in files:
        render(f)
    print("done")
