#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patio Language School - Free level check promo, bright grid style.

Renders three formats: IG post 1080x1350, IG story 1080x1920, FB post 1080x1080.
Big text, few words. Full bleed photo of Sofia, warm scrim, gold eyebrow,
white and gold DM Serif headline, two tick points, terracotta pill CTA.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

PALETTE = {
    "chocolate": "#2B1F18", "cream": "#FBF6EE", "gold": "#C19D5F",
    "gold_soft": "#E9C58B", "terracota": "#B8593A", "white": "#FFFFFF",
}
P = PALETTE

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
BG = b64(os.path.join(IMG, "class-conversation.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

SCRIMS = {
    "post": ("linear-gradient(180deg, rgba(43,31,24,.34) 0%, rgba(43,31,24,0) 16%,"
        " rgba(43,31,24,.42) 38%, rgba(43,31,24,.90) 62%, rgba(43,31,24,.98) 100%)"),
    "story": ("linear-gradient(180deg, rgba(43,31,24,.30) 0%, rgba(43,31,24,0) 22%,"
        " rgba(43,31,24,0) 42%, rgba(43,31,24,.55) 60%, rgba(43,31,24,.94) 84%, rgba(43,31,24,.99) 100%)"),
    "square": ("linear-gradient(180deg, rgba(43,31,24,.40) 0%, rgba(43,31,24,.08) 14%,"
        " rgba(43,31,24,.55) 34%, rgba(43,31,24,.92) 62%, rgba(43,31,24,.99) 100%)"),
}

def build(fname, W, H, c):
    ticks = ["No test, just a chat", "15 minutes"]
    lis = "".join(
        f'<div class="row"><span class="tick">&#10003;</span><span class="rt">{t}</span></div>'
        for t in ticks)
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Barlow',sans-serif;}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{c['objpos']};}}
.scrim{{position:absolute;inset:0;background:{SCRIMS[c['scrim']]};}}
.topbar{{position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,{P['gold']},{P['terracota']});}}
.logo{{position:absolute;top:{c['logo_top']}px;left:64px;height:{c['logo']}px;object-fit:contain;
  filter:drop-shadow(0 2px 10px rgba(0,0,0,.4));}}
.content{{position:absolute;left:64px;right:64px;bottom:{c['bottom']}px;}}
.eyebrow{{color:{P['gold_soft']};font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  font-size:{c['eyebrow']}px;margin-bottom:16px;text-shadow:0 2px 14px rgba(0,0,0,.6);}}
.headline{{font-family:'DM Serif Display',serif;color:{P['white']};font-size:{c['headline']}px;
  line-height:0.95;text-shadow:0 3px 24px rgba(0,0,0,.65);}}
.headline .a{{color:{P['gold_soft']};font-style:italic;}}
.list{{margin-top:{c['listgap']}px;display:flex;flex-direction:column;gap:{c['rowgap']}px;}}
.row{{display:flex;align-items:center;gap:22px;}}
.tick{{flex:none;width:{c['tick']}px;height:{c['tick']}px;border-radius:50%;background:{P['gold']};
  color:{P['chocolate']};font-size:{int(c['tick']*0.58)}px;font-weight:700;display:flex;
  align-items:center;justify-content:center;font-family:'DM Serif Display',serif;
  box-shadow:0 4px 16px rgba(0,0,0,.4);}}
.rt{{color:{P['white']};font-size:{c['rt']}px;font-weight:700;line-height:1.15;
  text-shadow:0 2px 14px rgba(0,0,0,.65);}}
.cta{{display:inline-block;margin-top:{c['ctagap']}px;background:{P['terracota']};color:{P['cream']};
  font-weight:800;font-size:{c['cta']}px;padding:{int(c['cta']*0.56)}px {int(c['cta']*1.24)}px;
  border-radius:70px;box-shadow:0 8px 28px rgba(0,0,0,.4);}}
"""
    body = (f'<div class="canvas">'
        f'<img class="bg" src="{BG}">'
        f'<div class="scrim"></div>'
        f'<div class="topbar"></div>'
        f'<img class="logo" src="{LOGO_WHITE}">'
        f'<div class="content">'
        f'<div class="eyebrow">Free &middot; with Sofia</div>'
        f'<div class="headline">Find your<br>level, <span class="a">free.</span></div>'
        f'<div class="list">{lis}</div>'
        f'<div class="cta">Message us to book</div>'
        f'</div></div>')
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname, W, H

def render(spec):
    fname, W, H = spec
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

POST = dict(objpos="center 18%", scrim="post", logo=104, logo_top=50, bottom=74,
    eyebrow=35, headline=122, listgap=40, rowgap=26, tick=62, rt=44, cta=50, ctagap=44)
STORY = dict(objpos="center 26%", scrim="story", logo=112, logo_top=150, bottom=330,
    eyebrow=38, headline=132, listgap=44, rowgap=28, tick=68, rt=48, cta=56, ctagap=48)
SQUARE = dict(objpos="center 22%", scrim="square", logo=92, logo_top=44, bottom=54,
    eyebrow=30, headline=92, listgap=28, rowgap=20, tick=54, rt=38, cta=44, ctagap=32)

if __name__ == "__main__":
    render(build("levelcheck-bright-ig-1080x1350.html", 1080, 1350, POST))
    render(build("levelcheck-bright-story-1080x1920.html", 1080, 1920, STORY))
    render(build("levelcheck-bright-fb-1080x1080.html", 1080, 1080, SQUARE))
    print("done")
