#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wolfgang testimonial IG carousel: quote slide (refs yesterday) + CTA slide. 1080x1350."""
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
CTA_PHOTO = b64(os.path.join(IMG, "class-conversation.jpg"), "image/jpeg")

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

# ---------- Slide 1: testimonial (refs yesterday) ----------
def slide_quote(fname):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:150px 108px;text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:70px;left:0;right:0;text-align:center;
  color:#726651;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:24px;}}
.since{{position:absolute;top:112px;left:0;right:0;text-align:center;
  color:#B8593A;font-weight:600;font-style:italic;font-size:27px;font-family:'DM Serif Display',serif;}}
.mark{{font-family:'DM Serif Display',serif;color:#C19D5F;font-size:170px;
  line-height:.4;height:80px;margin-bottom:6px;}}
.quote{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:45px;
  line-height:1.32;font-style:italic;}}
.rule{{width:70px;height:4px;background:#B8593A;border-radius:3px;margin:40px auto 26px;}}
.name{{color:#B8593A;font-weight:700;font-size:36px;letter-spacing:.01em;}}
.role{{color:#726651;font-weight:600;font-size:25px;letter-spacing:.14em;
  text-transform:uppercase;margin-top:10px;}}
.logo{{position:absolute;bottom:60px;left:0;right:0;margin:0 auto;height:56px;
  display:block;object-fit:contain;}}
.count{{position:absolute;bottom:64px;right:72px;color:#726651;font-weight:700;
  font-size:26px;letter-spacing:.1em;}}
"""
    quote = ("I greatly value my private lessons with Sofia Nabais. She works systematically "
        "with excellent materials, and explains tricky grammar with patience and clarity. "
        "She happily follows the questions that come up, and loves pointing you to the culture "
        "too: writers, architecture, regional food, concerts. Professional and deeply personable, "
        "she leaves me motivated after every lesson.")
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">What our students say</div>'
        f'<div class="since">One more, after yesterday&rsquo;s</div>'
        f'<div class="mark">&ldquo;</div>'
        f'<div class="quote">{quote}</div>'
        f'<div class="rule"></div>'
        f'<div class="name">Wolfgang Helmut Pump</div>'
        f'<div class="role">Private student &middot; Germany</div>'
        f'<img class="logo" src="{LOGO_COLOR}">'
        f'<div class="count">1/2</div>'
        f'</div>')
    return write(fname, page(css, body))

# ---------- Slide 2: CTA (contact / register) ----------
def slide_cta(fname):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;padding:132px 90px 60px;
  display:flex;flex-direction:column;align-items:center;text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:60px;left:0;right:0;color:#E0A868;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:24px;}}
.stars{{color:#E0A868;font-size:40px;letter-spacing:.12em;margin-bottom:18px;}}
.title{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:78px;line-height:1.02;}}
.title .a{{color:#E0A868;font-style:italic;}}
.sub{{color:#F1E3CE;font-size:32px;font-weight:500;margin-top:20px;line-height:1.4;}}
.photo{{width:100%;height:322px;object-fit:cover;object-position:center 32%;
  border-radius:22px;border:5px solid #C19D5F;margin:34px 0 32px;
  box-shadow:0 14px 34px rgba(0,0,0,.4);}}
.msg{{color:#F1E3CE;font-size:31px;font-weight:500;margin-bottom:22px;}}
.cta{{display:inline-block;background:#B8593A;color:#FBF6EE;font-weight:700;font-size:37px;
  padding:24px 56px;border-radius:60px;letter-spacing:.01em;}}
.line{{color:#EBDCC4;font-size:31px;font-weight:600;margin-top:22px;letter-spacing:.01em;}}
.line .g{{color:#E0A868;}}
.logo{{height:54px;object-fit:contain;display:block;margin:32px auto 0;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Now enrolling &middot; Lagos</div>'
        f'<div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<div class="title">Want lessons like <span class="a">these?</span></div>'
        f'<div class="sub">Private lessons and small group classes<br>in European Portuguese &middot; Lagos</div>'
        f'<img class="photo" src="{CTA_PHOTO}">'
        f'<div class="msg">Message us to register your interest</div>'
        f'<div class="cta">patiolanguage.pt</div>'
        f'<div class="line">WhatsApp <span class="g">+351 928 129 560</span></div>'
        f'<div class="line">Follow <span class="g">@patiolanguage</span></div>'
        f'<img class="logo" src="{LOGO_WHITE}"></div>')
    return write(fname, page(css, body))

def render(fname):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    render(slide_quote("wolfgang-1-testimonial-ig-1080x1350.html"))
    render(slide_cta("wolfgang-2-cta-ig-1080x1350.html"))
    print("done")
