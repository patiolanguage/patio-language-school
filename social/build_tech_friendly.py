#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Senior-friendly 'Tech Made Friendly' flyer + FB post. Large, warm, plain language.
A5 print (PDF+PNG) and a Facebook post (1080x1350). No em/en dashes.
"""
import base64, os, subprocess
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

LOGO = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display&display=swap" rel="stylesheet">')

ITEMS = [
    ("&#128241;", "WhatsApp &amp; Facebook", "Keep in touch with family"),
    ("&#128205;", "Google Maps", "Get around with confidence"),
    ("&#128247;", "Photos &amp; files", "Save, find and share them"),
    ("&#128274;", "Updates &amp; staying safe", "Keep your phone safe"),
    ("&#129302;", "AI made simple", "A patient helper for it all"),
]

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

def items_html(em, nm, ds):
    out = []
    for e, n, d in ITEMS:
        out.append(f'<div class="item"><div class="em">{e}</div>'
                   f'<div class="it"><div class="in">{n}</div><div class="id">{d}</div></div></div>')
    return '<div class="items">' + "".join(out) + '</div>'


def build(kind, w, h, fname):
    if kind == "a5":
        pad, logo, eb, title, sub, datef, intro, em, inm, idd, foot, cta, gap, dtext = \
            "80px 104px 72px", 144, 38, 122, 52, 48, 40, 86, 60, 46, 42, 48, 34, \
            "&#128197; Wednesday 28 October &middot; 17h00 to 19h00"
    else:  # fb post 1080x1350
        pad, logo, eb, title, sub, datef, intro, em, inm, idd, foot, cta, gap, dtext = \
            "24px 70px 20px", 90, 28, 76, 36, 32, 30, 54, 44, 33, 29, 33, 13, \
            "&#128197; Wed 28 Oct &middot; 17h00 to 19h00"
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;
  background:radial-gradient(130% 95% at 50% 8%,#FFF9F0 0%,#FBF0E1 52%,#F3DEC6 100%);
  color:#2B1F18;display:flex;flex-direction:column;align-items:center;text-align:center;padding:{pad};}}
.bar{{position:absolute;top:0;left:0;right:0;height:18px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:{logo}px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:{eb}px;margin-top:20px;}}
h1{{font-family:'DM Serif Display',serif;font-size:{title}px;line-height:1.0;margin-top:10px;color:#3b5553;}}
.sub{{color:#2B1F18;font-weight:700;font-size:{sub}px;line-height:1.3;margin-top:14px;max-width:900px;}}
.date{{display:inline-block;background:#3b5553;color:#FBF6EE;font-weight:700;font-size:{datef}px;
  border-radius:999px;padding:{int(datef*0.4)}px {int(datef*0.9)}px;margin-top:16px;}}
.price{{color:#B8593A;font-weight:700;font-size:{datef}px;margin-top:12px;}}
.intro{{color:#5a5047;font-weight:500;font-size:{intro}px;line-height:1.34;margin-top:12px;max-width:900px;}}
.items{{width:100%;display:flex;flex-direction:column;gap:{gap-6}px;margin-top:{gap}px;}}
.item{{display:flex;align-items:center;gap:26px;background:#fff;border-radius:22px;
  padding:{int(gap*0.7)}px {gap}px;box-shadow:0 10px 26px rgba(43,31,24,.08);
  border-left:12px solid #617C7B;text-align:left;}}
.item:nth-child(odd){{border-left-color:#C19D5F;}}
.item:nth-child(5){{border-left-color:#B8593A;}}
.em{{font-size:{em}px;line-height:1;flex:none;width:{int(em*1.25)}px;text-align:center;}}
.in{{font-family:'DM Serif Display',serif;font-size:{inm}px;line-height:1.05;color:#2B1F18;}}
.id{{color:#5a5047;font-weight:600;font-size:{idd}px;margin-top:4px;}}
.foot{{margin-top:auto;padding-top:{gap}px;width:100%;}}
.cta{{background:#3b5553;color:#FBF6EE;border-radius:22px;padding:{int(cta*0.56)}px {cta}px;
  font-weight:700;font-size:{cta}px;line-height:1.35;box-shadow:0 14px 34px rgba(43,31,24,.22);}}
.cta span{{color:#F0D4A6;}}
.contact{{color:#2B1F18;font-weight:700;font-size:{foot}px;margin-top:18px;line-height:1.4;}}
.contact b{{color:#B8593A;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<img class="logo" src="{LOGO}">
<div class="eyebrow">At Patio &middot; Lagos</div>
<h1>Tech Made Friendly</h1>
<div class="sub">Stay connected, confident and up to date, together.</div>
<div class="date">{dtext}</div>
<div class="price">&euro;20</div>
<div class="intro">A relaxed get-together at Patio. A small, friendly group, and no question is too small.</div>
{items_html(em, inm, idd)}
<div class="foot">
  <div class="cta">Reserve your place &middot; <span>WhatsApp +351 928 129 560</span><br>patiolanguage.pt</div>
</div>
</div>"""
    render(fname, page(css, body), w, h)
    if kind == "a5":
        im = Image.open(os.path.join(SOCIAL, fname.replace(".html", ".png"))).convert("RGB")
        im.save(os.path.join(SOCIAL, "Tech-Made-Friendly-Flyer-A5.pdf"), "PDF", resolution=255.0)
        print("wrote A5 pdf")


if __name__ == "__main__":
    build("a5", 1488, 2104, "Tech-Made-Friendly-Flyer-A5.html")
    build("fb", 1080, 1350, "tech-made-friendly-fb-1080x1350.html")
    print("done")
