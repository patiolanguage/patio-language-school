#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""'Why we teach AI' - SHORT, photo-led version (EN + PT): IG post, FB post, Story.

Minimal words. Photo on top, deep teal panel below with a short serif line.
Richer brand colour to stand out in the IG grid. No em/en dashes.
PT informal (tu). Native proofread (Sofia) recommended.
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
PHOTO = b64(os.path.join(IMG, "ai-workshop-photo.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

TEAL = "background:radial-gradient(120% 120% at 50% 0%,#C46844 0%,#B0522F 52%,#873B24 100%);"
URL = "patiolanguage.pt/ai"

STR = {
 "en": {"suffix": "",
        "eyebrow": "Why we teach AI",
        "l1": "New tool.", "l2": "Same belief.",
        "sub": "Feeling capable in a new place is the whole point.",
        "foot": "Courses start in October &middot; Lagos"},
 "pt": {"suffix": "-pt",
        "eyebrow": "Porque ensinamos IA",
        "l1": "Ferramenta nova.", "l2": "A mesma crença.",
        "sub": "Sentires-te capaz num lugar novo é o que importa.",
        "foot": "Os cursos começam em outubro &middot; Lagos"},
}

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


def build(s, fmt):
    kind, w, h = fmt
    if kind == "story":
        photo_h, eb, hl, sub_fs, foot_fs, ppad = 950, 46, 122, 64, 48, "0 84px 155px"
    elif kind == "ig":
        photo_h, eb, hl, sub_fs, foot_fs, ppad = 630, 42, 110, 60, 44, "0 72px 52px"
    else:  # fb square
        photo_h, eb, hl, sub_fs, foot_fs, ppad = 485, 38, 90, 52, 38, "0 64px 44px"
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;
  display:flex;flex-direction:column;{TEAL}}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;z-index:3;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.photo{{width:100%;height:{photo_h}px;background-image:url('{PHOTO}');
  background-size:cover;background-position:center 38%;position:relative;}}
.photo::after{{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(43,31,24,0) 55%,rgba(135,59,36,.55) 100%);}}
.panel{{flex:1;{TEAL}color:#FBF6EE;display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center;padding:{ppad};}}
.eyebrow{{color:#F0D4A6;font-weight:700;letter-spacing:.26em;text-transform:uppercase;font-size:{eb}px;}}
.hl{{font-family:'DM Serif Display',serif;font-size:{hl}px;line-height:1.0;margin-top:22px;}}
.hl .b{{color:#F0D4A6;font-style:italic;display:block;}}
.sub{{color:#EBF1EE;font-size:{sub_fs}px;font-weight:500;line-height:1.34;margin-top:26px;max-width:820px;}}
.foot{{margin-top:{'54' if kind!='fb' else '40'}px;display:flex;flex-direction:column;align-items:center;gap:20px;}}
.foot .txt{{color:#FBF1E4;font-weight:700;font-size:{foot_fs}px;letter-spacing:.02em;}}
.foot .url{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:{foot_fs+10}px;}}
.logo{{height:{56 if kind!='fb' else 48}px;object-fit:contain;opacity:.95;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<div class="photo"></div>
<div class="panel">
  <div class="eyebrow">{s['eyebrow']}</div>
  <div class="hl">{s['l1']}<span class="b">{s['l2']}</span></div>
  <div class="sub">{s['sub']}</div>
  <div class="foot">
    <div class="url">{URL}</div>
    <div class="txt">{s['foot']}</div>
    <img class="logo" src="{LOGO_WHITE}">
  </div>
</div></div>"""
    render(f"why-short-{kind}-{w}x{h}{s['suffix']}.html", page(css, body), w, h)


if __name__ == "__main__":
    for lang in ("en", "pt"):
        s = STR[lang]
        build(s, ("ig", 1080, 1350))
        build(s, ("fb", 1080, 1080))
        build(s, ("story", 1080, 1920))
    print("done")
