#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wolfgang testimonial + CTA in IG Story (1080x1920) and FB post (1080x1080)."""
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

QUOTE = ("I greatly value my private lessons with Sofia Nabais. She works systematically "
    "with excellent materials, and explains tricky grammar with patience and clarity. "
    "She happily follows the questions that come up, and loves pointing you to the culture "
    "too: writers, architecture, regional food, concerts. Professional and deeply personable, "
    "she leaves me motivated after every lesson.")

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def render(fname, W, H):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

def write(fname, html):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)

# ---------- Testimonial slide ----------
def testimonial(fname, W, H, p):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:{p['pad']};text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:{p['eyeTop']}px;left:0;right:0;text-align:center;
  color:#726651;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:{p['eye']}px;}}
.since{{position:absolute;top:{p['sinceTop']}px;left:0;right:0;text-align:center;
  color:#B8593A;font-weight:600;font-style:italic;font-size:{p['since']}px;font-family:'DM Serif Display',serif;}}
.mark{{font-family:'DM Serif Display',serif;color:#C19D5F;font-size:{p['mark']}px;
  line-height:.4;height:{p['markH']}px;margin-bottom:6px;}}
.quote{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:{p['quote']}px;
  line-height:1.32;font-style:italic;}}
.rule{{width:66px;height:4px;background:#B8593A;border-radius:3px;margin:{p['ruleM']};}}
.name{{color:#B8593A;font-weight:700;font-size:{p['name']}px;letter-spacing:.01em;}}
.role{{color:#726651;font-weight:600;font-size:{p['role']}px;letter-spacing:.14em;
  text-transform:uppercase;margin-top:9px;}}
.logo{{position:absolute;bottom:{p['logoBot']}px;left:0;right:0;margin:0 auto;height:{p['logo']}px;
  display:block;object-fit:contain;}}
.count{{position:absolute;bottom:{p['logoBot']}px;right:72px;color:#726651;font-weight:700;
  font-size:26px;letter-spacing:.1em;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">What our students say</div>'
        f'<div class="since">One more, after yesterday&rsquo;s</div>'
        f'<div class="mark">&ldquo;</div>'
        f'<div class="quote">{QUOTE}</div>'
        f'<div class="rule"></div>'
        f'<div class="name">Wolfgang Helmut Pump</div>'
        f'<div class="role">Private student &middot; Germany</div>'
        f'<img class="logo" src="{LOGO_COLOR}">'
        + (f'<div class="count">1/2</div>' if p.get('count') else '')
        + f'</div>')
    write(fname, page(css, body))
    render(fname, W, H)

# ---------- CTA slide ----------
def cta(fname, W, H, p):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;padding:{p['pad']};
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:{p['eyeTop']}px;left:0;right:0;color:#E0A868;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:{p['eye']}px;}}
.stars{{color:#E0A868;font-size:{p['stars']}px;letter-spacing:.12em;margin-bottom:16px;}}
.title{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:{p['title']}px;line-height:1.03;}}
.title .a{{color:#E0A868;font-style:italic;}}
.sub{{color:#F1E3CE;font-size:{p['sub']}px;font-weight:500;margin-top:18px;line-height:1.4;}}
.photo{{width:100%;height:{p['photo']}px;object-fit:cover;object-position:center 32%;
  border-radius:22px;border:5px solid #C19D5F;margin:{p['photoM']};
  box-shadow:0 14px 34px rgba(0,0,0,.4);}}
.msg{{color:#F1E3CE;font-size:{p['msg']}px;font-weight:500;margin-bottom:{p['msgB']}px;}}
.cta{{display:inline-block;background:#B8593A;color:#FBF6EE;font-weight:700;font-size:{p['ctaF']}px;
  padding:{p['ctaP']};border-radius:60px;letter-spacing:.01em;}}
.line{{color:#EBDCC4;font-size:{p['line']}px;font-weight:600;margin-top:{p['lineM']}px;letter-spacing:.01em;}}
.line .g{{color:#E0A868;}}
.logo{{height:{p['logo']}px;object-fit:contain;display:block;margin:{p['logoM']}px auto 0;}}
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
    write(fname, page(css, body))
    render(fname, W, H)

# ---------- presets ----------
STORY_T = dict(pad="360px 108px", eyeTop=300, eye=24, sinceTop=344, since=27,
    mark=160, markH=76, quote=46, ruleM="40px auto 26px", name=38, role=25,
    logo=58, logoBot=300, count=False)
STORY_C = dict(pad="330px 96px", eyeTop=300, eye=24, stars=42, title=82, sub=33,
    photo=360, photoM="40px 0 36px", msg=32, msgB=22, ctaF=38, ctaP="26px 58px",
    line=32, lineM=24, logo=56, logoM=36)

SQUARE_T = dict(pad="96px 84px", eyeTop=56, eye=21, sinceTop=92, since=23,
    mark=118, markH=54, quote=34, ruleM="26px auto 18px", name=30, role=21,
    logo=46, logoBot=48, count=True)
SQUARE_C = dict(pad="80px 80px", eyeTop=52, eye=21, stars=34, title=62, sub=27,
    photo=250, photoM="26px 0 24px", msg=27, msgB=16, ctaF=32, ctaP="20px 48px",
    line=27, lineM=16, logo=46, logoM=24)

if __name__ == "__main__":
    # Instagram Story 1080x1920
    testimonial("wolfgang-1-testimonial-ig-story-1080x1920.html", 1080, 1920, STORY_T)
    cta("wolfgang-2-cta-ig-story-1080x1920.html", 1080, 1920, STORY_C)
    # Facebook post 1080x1080
    testimonial("wolfgang-1-testimonial-fb-1080x1080.html", 1080, 1080, SQUARE_T)
    cta("wolfgang-2-cta-fb-1080x1080.html", 1080, 1080, SQUARE_C)
    print("done")
