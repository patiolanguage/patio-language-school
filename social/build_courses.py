#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patio Language School - Autumn course promos: Beginner A1 and B1+.

Renders three formats each: IG post 1080x1350, IG story 1080x1920, FB post 1080x1080.
Matches the Patio Instagram grid: full bleed Lagos photo, warm scrim, gold eyebrow,
white and gold DM Serif headline, white sub, gold times line, terracotta pill CTA.
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

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

SCRIMS = {
    "post": ("linear-gradient(180deg, rgba(43,31,24,.46) 0%, rgba(43,31,24,0) 22%,"
        " rgba(43,31,24,0) 36%, rgba(43,31,24,.80) 72%, rgba(43,31,24,.94) 100%)"),
    "story": ("linear-gradient(180deg, rgba(43,31,24,.34) 0%, rgba(43,31,24,0) 24%,"
        " rgba(43,31,24,0) 46%, rgba(43,31,24,.60) 64%, rgba(43,31,24,.94) 86%, rgba(43,31,24,.99) 100%)"),
    "square": ("linear-gradient(180deg, rgba(43,31,24,.42) 0%, rgba(43,31,24,.10) 14%,"
        " rgba(43,31,24,.30) 34%, rgba(43,31,24,.86) 64%, rgba(43,31,24,.98) 100%)"),
}

W = 1080

def build(fname, H, photo, focus, c, eyebrow, head_a, head_b, sub, meta):
    bg = b64(os.path.join(IMG, photo), "image/jpeg")
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Barlow',sans-serif;}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{focus};}}
.scrim{{position:absolute;inset:0;background:{SCRIMS[c['scrim']]};}}
.topbar{{position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,{P['gold']},{P['terracota']});}}
.logo{{position:absolute;top:{c['logo_top']}px;left:64px;height:{c['logo']}px;object-fit:contain;
  filter:drop-shadow(0 2px 10px rgba(0,0,0,.35));}}
.content{{position:absolute;left:64px;right:64px;bottom:{c['bottom']}px;}}
.eyebrow{{color:{P['gold_soft']};font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  font-size:{c['eyebrow']}px;margin-bottom:16px;text-shadow:0 2px 12px rgba(0,0,0,.5);}}
.headline{{font-family:'DM Serif Display',serif;color:{P['white']};font-size:{c['headline']}px;
  line-height:0.98;text-shadow:0 3px 22px rgba(0,0,0,.55);}}
.headline .a{{color:{P['gold_soft']};font-style:italic;}}
.sub{{color:{P['cream']};font-size:{c['sub']}px;font-weight:600;margin-top:26px;
  line-height:1.28;max-width:{c['submax']}ch;text-shadow:0 2px 14px rgba(0,0,0,.6);}}
.meta{{color:{P['gold_soft']};font-size:{c['meta']}px;font-weight:700;margin-top:24px;
  line-height:1.28;text-shadow:0 2px 12px rgba(0,0,0,.55);}}
.cta{{display:inline-block;margin-top:{c['ctagap']}px;background:{P['terracota']};color:{P['cream']};
  font-weight:800;font-size:{c['cta']}px;padding:{int(c['cta']*0.6)}px {int(c['cta']*1.35)}px;
  border-radius:60px;box-shadow:0 8px 26px rgba(0,0,0,.32);}}
"""
    body = (f'<div class="canvas">'
        f'<img class="bg" src="{bg}">'
        f'<div class="scrim"></div>'
        f'<div class="topbar"></div>'
        f'<img class="logo" src="{LOGO_WHITE}">'
        f'<div class="content">'
        f'<div class="eyebrow">{eyebrow}</div>'
        f'<div class="headline">{head_a}<br><span class="a">{head_b}</span></div>'
        f'<div class="sub">{sub}</div>'
        f'<div class="meta">{meta}</div>'
        f'<div class="cta">patiolanguage.pt &rarr;</div>'
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

POST = dict(scrim="post", logo=108, logo_top=52, bottom=70, eyebrow=32, headline=108,
    sub=44, meta=36, cta=42, ctagap=38, submax=18)
STORY = dict(scrim="story", logo=112, logo_top=150, bottom=330, eyebrow=36, headline=118,
    sub=46, meta=38, cta=48, ctagap=42, submax=18)
SQUARE = dict(scrim="square", logo=92, logo_top=44, bottom=52, eyebrow=28, headline=80,
    sub=34, meta=30, cta=38, ctagap=30, submax=22)

# (slug, photo, focus, eyebrow, head_a, head_b, sub, meta)
COURSES = [
    ("courses-beginner", "lagos-dona-ana.jpg", "center 40%",
        "Now enrolling &middot; 21 September", "Start Portuguese", "from zero.",
        "Small, friendly groups for total beginners.",
        "Mon &amp; Wed &middot; 9h15 &nbsp;or&nbsp; Tue &amp; Thu &middot; 18h30 &nbsp;&middot;&nbsp; &euro;11/hr"),
    ("courses-b1plus", "lagos-hero.jpg", "center 45%",
        "Now enrolling &middot; 21 September", "Take your Portuguese", "further.",
        "For confident speakers ready to sound more natural.",
        "Mon &amp; Wed &middot; 11h00&ndash;12h30 &nbsp;&middot;&nbsp; small group &nbsp;&middot;&nbsp; &euro;11/hr"),
    ("courses-beginner-roompic", "ai-room.jpg", "center 35%",
        "Now enrolling &middot; 21 September", "Start Portuguese", "from zero.",
        "Small, friendly groups for total beginners in Lagos.",
        "Mon &amp; Wed &middot; 9h15 &nbsp;or&nbsp; Tue &amp; Thu &middot; 18h30 &nbsp;&middot;&nbsp; &euro;11/hr"),
    ("courses-beginner-pt", "space-classroom.jpg", "center 40%",
        "Inscri&ccedil;&otilde;es abertas &middot; 21 de setembro", "Comece portugu&ecirc;s", "do zero.",
        "Grupos pequenos e acolhedores para principiantes.",
        "Seg &amp; Qua &middot; 9h15 &nbsp;ou&nbsp; Ter &amp; Qui &middot; 18h30 &nbsp;&middot;&nbsp; &euro;11/h"),
    ("courses-beginner-room", "space-classroom.jpg", "center 40%",
        "Now enrolling &middot; 21 September", "Start Portuguese", "from zero.",
        "Small, friendly groups for total beginners.",
        "Mon &amp; Wed &middot; 9h15 &nbsp;or&nbsp; Tue &amp; Thu &middot; 18h30 &nbsp;&middot;&nbsp; &euro;11/hr"),
    ("courses-b1plus-pt", "lagos-hero.jpg", "center 45%",
        "Inscri&ccedil;&otilde;es abertas &middot; 21 de setembro", "Leve o seu portugu&ecirc;s", "mais longe.",
        "Para quem j&aacute; fala e quer soar mais natural.",
        "Seg &amp; Qua &middot; 11h00&ndash;12h30 &nbsp;&middot;&nbsp; pequeno grupo &nbsp;&middot;&nbsp; &euro;11/h"),
]
FORMATS = [("ig-1080x1350", 1350, POST), ("story-1080x1920", 1920, STORY), ("fb-1080x1080", 1080, SQUARE)]

if __name__ == "__main__":
    for slug, photo, focus, eb, ha, hb, sub, meta in COURSES:
        for suffix, H, cfg in FORMATS:
            render(build(f"{slug}-{suffix}.html", H, photo, focus, cfg, eb, ha, hb, sub, meta))
    print("done")
