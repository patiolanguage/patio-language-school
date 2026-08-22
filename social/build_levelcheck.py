#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patio Language School - Free Level Check promo (IG 1080x1350)."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
SOFIA = b64(os.path.join(IMG, "class-conversation.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

W, H = 1080, 1350

def build(fname):
    ticks = [
        "No test &mdash; just a relaxed chat",
        "In person or on WhatsApp, 15 minutes",
        "Your level, plus the class that fits you",
    ]
    lis = "".join(
        f'<div class="row"><span class="tick">&#10003;</span><span class="rt">{t}</span></div>'
        for t in ticks)
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#2B1F18;
  font-family:'Barlow',sans-serif;padding:120px 92px 66px;
  display:flex;flex-direction:column;align-items:center;text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:60px;left:0;right:0;color:#E0A868;font-weight:700;
  letter-spacing:.22em;text-transform:uppercase;font-size:24px;}}
.badge{{display:inline-block;background:#B8593A;color:#FBF6EE;font-weight:800;
  letter-spacing:.14em;text-transform:uppercase;font-size:24px;padding:11px 26px;
  border-radius:40px;margin-bottom:26px;}}
.headline{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:92px;line-height:1.0;}}
.headline .a{{color:#E0A868;font-style:italic;}}
.sub{{color:#F1E3CE;font-size:34px;font-weight:500;margin-top:24px;line-height:1.42;}}
.list{{margin-top:34px;display:flex;flex-direction:column;gap:24px;align-items:flex-start;
  align-self:center;}}
.photo{{width:100%;height:250px;object-fit:cover;object-position:center 30%;
  border-radius:20px;border:5px solid #C19D5F;margin-top:36px;
  box-shadow:0 14px 34px rgba(0,0,0,.4);}}
.row{{display:flex;align-items:center;gap:22px;text-align:left;}}
.tick{{flex:none;width:52px;height:52px;border-radius:50%;background:#C19D5F;color:#2B1F18;
  font-size:30px;font-weight:700;display:flex;align-items:center;justify-content:center;
  font-family:'DM Serif Display',serif;}}
.rt{{color:#FBF6EE;font-size:33px;font-weight:600;line-height:1.25;}}
.contact{{margin-top:auto;width:100%;}}
.cta{{display:inline-block;background:#C19D5F;color:#2B1F18;font-weight:800;font-size:37px;
  padding:26px 56px;border-radius:60px;letter-spacing:.01em;}}
.line{{color:#EBDCC4;font-size:31px;font-weight:600;margin-top:24px;letter-spacing:.01em;}}
.line .g{{color:#E0A868;}}
.logo{{height:54px;object-fit:contain;display:block;margin:34px auto 0;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Before we open &middot; Lagos</div>'
        f'<div class="badge">Free</div>'
        f'<div class="headline">Find your level,<br><span class="a">free.</span></div>'
        f'<div class="sub">A friendly level check with Sofia &mdash; find out where you stand and which class is right for you.</div>'
        f'<div class="list">{lis}</div>'
        f'<img class="photo" src="{SOFIA}">'
        f'<div class="contact">'
        f'<div class="cta">Message us to book</div>'
        f'<div class="line">patiolanguage.pt &nbsp;&middot;&nbsp; WhatsApp <span class="g">+351 928 129 560</span></div>'
        f'<img class="logo" src="{LOGO_WHITE}"></div></div>')
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

def render(fname):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    render(build("levelcheck-ig-1080x1350.html"))
    print("done")
