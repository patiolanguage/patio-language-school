#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patio Language School - Practical AI sign up, bilingual, bright grid style.

Renders IG post 1080x1350, IG story 1080x1920, FB post 1080x1080.
Big text, few words. Full bleed room photo, warm scrim, gold eyebrow,
bilingual DM Serif headline (EN white, PT gold), bilingual sub, terracotta pill CTA.
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
BG = b64(os.path.join(IMG, "ai-room.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

SCRIMS = {
    "post": ("linear-gradient(180deg, rgba(43,31,24,.44) 0%, rgba(43,31,24,.06) 18%,"
        " rgba(43,31,24,.38) 42%, rgba(43,31,24,.88) 68%, rgba(43,31,24,.97) 100%)"),
    "story": ("linear-gradient(180deg, rgba(43,31,24,.34) 0%, rgba(43,31,24,0) 22%,"
        " rgba(43,31,24,.30) 46%, rgba(43,31,24,.72) 66%, rgba(43,31,24,.96) 86%, rgba(43,31,24,.99) 100%)"),
    "square": ("linear-gradient(180deg, rgba(43,31,24,.46) 0%, rgba(43,31,24,.12) 14%,"
        " rgba(43,31,24,.48) 36%, rgba(43,31,24,.90) 64%, rgba(43,31,24,.99) 100%)"),
}

W = 1080

def build(fname, H, c):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Barlow',sans-serif;}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;}}
.scrim{{position:absolute;inset:0;background:{SCRIMS[c['scrim']]};}}
.topbar{{position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,{P['gold']},{P['terracota']});}}
.logo{{position:absolute;top:{c['logo_top']}px;left:64px;height:{c['logo']}px;object-fit:contain;
  filter:drop-shadow(0 2px 10px rgba(0,0,0,.4));}}
.content{{position:absolute;left:64px;right:64px;bottom:{c['bottom']}px;}}
.eyebrow{{color:{P['gold_soft']};font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  font-size:{c['eyebrow']}px;margin-bottom:16px;text-shadow:0 2px 14px rgba(0,0,0,.6);}}
.headline{{font-family:'DM Serif Display',serif;color:{P['white']};font-size:{c['headline']}px;
  line-height:1.0;text-shadow:0 3px 24px rgba(0,0,0,.65);}}
.headline .a{{color:{P['gold_soft']};font-style:italic;}}
.sub{{color:{P['cream']};font-size:{c['sub']}px;font-weight:600;margin-top:24px;line-height:1.3;
  text-shadow:0 2px 14px rgba(0,0,0,.65);}}
.sub .pt{{color:{P['gold_soft']};font-style:italic;}}
.cta{{display:inline-block;margin-top:{c['ctagap']}px;background:{P['terracota']};color:{P['cream']};
  font-weight:800;font-size:{c['cta']}px;padding:{int(c['cta']*0.58)}px {int(c['cta']*1.2)}px;
  border-radius:70px;box-shadow:0 8px 28px rgba(0,0,0,.4);}}
"""
    body = (f'<div class="canvas">'
        f'<img class="bg" src="{BG}">'
        f'<div class="scrim"></div>'
        f'<div class="topbar"></div>'
        f'<img class="logo" src="{LOGO_WHITE}">'
        f'<div class="content">'
        f'<div class="eyebrow">Practical AI &middot; Lagos</div>'
        f'<div class="headline">AI made simple.<br><span class="a">IA sem complica&ccedil;&otilde;es.</span></div>'
        f'<div class="sub">Everyday AI classes. No tech background.<br>'
        f'<span class="pt">Aulas de IA para o dia a dia. Sem saber de tecnologia.</span></div>'
        f'<div class="cta">Message us AI &middot; Escreva-nos IA</div>'
        f'</div></div>')
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname, H

def render(spec):
    fname, H = spec
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

POST = dict(scrim="post", logo=104, logo_top=52, bottom=72, eyebrow=32, headline=94, sub=34, cta=38, ctagap=40)
STORY = dict(scrim="story", logo=112, logo_top=150, bottom=330, eyebrow=36, headline=104, sub=38, cta=42, ctagap=44)
SQUARE = dict(scrim="square", logo=92, logo_top=44, bottom=54, eyebrow=28, headline=76, sub=30, cta=34, ctagap=30)

if __name__ == "__main__":
    render(build("ai-signup-ig-1080x1350.html", 1350, POST))
    render(build("ai-signup-story-1080x1920.html", 1920, STORY))
    render(build("ai-signup-fb-1080x1080.html", 1080, SQUARE))
    print("done")
