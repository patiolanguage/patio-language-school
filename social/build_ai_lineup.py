#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""'AI Workshops in Lagos' lineup post (EN + PT): IG, FB, Story.

A screen-friendly version of the flyer: the full programme (Happy Hour taster
plus the two four-week workshops) with dates and prices, in big readable type.

Brand: DM Serif Display + Barlow; gold #C19D5F, terracota #B8593A,
teal #617C7B, chocolate #2B1F18, cream #FBF6EE. No em/en dashes.
PT informal (tu), "no Patio". Native proofread (Sofia) recommended.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

URL = "patiolanguage.pt/ai"
CREAM = "background:radial-gradient(125% 90% at 50% 12%,#FEFCF7 0%,#FBF6EE 45%,#F3E6D0 100%);"

STR = {
 "en": {"suffix": "",
   "eyebrow": "Patio Practical AI &middot; Lagos",
   "title": "AI Workshops in Lagos",
   "sub": "Small groups. Hands-on. In plain English.",
   "cards": [
     ("#C19D5F", "Start here &middot; Happy Hour", "AI Made Practical",
      "Wed 7 Oct &middot; 17h00 to 19h30", "Includes a drink, credited to any course", "&euro;20"),
     ("#B8593A", "4-week workshop &middot; for work", "AI for Business",
      "Wed 14 Oct to 4 Nov &middot; 18h00 to 20h00", "Work smarter and win back hours", "&euro;249"),
     ("#617C7B", "4-week workshop &middot; for everyone", "AI Made Simple",
      "Fri 16 Oct to 6 Nov &middot; 15h00 to 17h00", "From curious to confident", "&euro;149"),
   ],
   "foot": "Limited spots &middot; Bring your own device"},
 "pt": {"suffix": "-pt",
   "eyebrow": "Patio Practical AI &middot; Lagos",
   "title": "Workshops de IA em Lagos",
   "sub": "Grupos pequenos. Prática. Dados em inglês.",
   "cards": [
     ("#C19D5F", "Começa aqui &middot; Happy Hour", "AI Made Practical",
      "Qua 7 out &middot; 17h00 às 19h30", "Inclui uma bebida, descontado em qualquer curso", "&euro;20"),
     ("#B8593A", "Workshop de 4 semanas &middot; trabalho", "AI for Business",
      "Qua 14 out a 4 nov &middot; 18h00 às 20h00", "Trabalha melhor e ganha horas", "&euro;249"),
     ("#617C7B", "Workshop de 4 semanas &middot; para todos", "AI Made Simple",
      "Sex 16 out a 6 nov &middot; 15h00 às 17h00", "De curioso a confiante", "&euro;149"),
   ],
   "foot": "Vagas limitadas &middot; Traz o teu portátil"},
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

def cards_html(cards):
    out = []
    for ac, tag, name, meta, note, price in cards:
        out.append(f'''<div class="card" style="border-left-color:{ac};">
  <div class="cl">
    <div class="tag" style="color:{ac};">{tag}</div>
    <div class="cname">{name}</div>
    <div class="cmeta">{meta}</div>
    <div class="cnote">{note}</div>
  </div>
  <div class="cr"><div class="price" style="color:{ac};">{price}</div></div>
</div>''')
    return '<div class="cards">' + "".join(out) + '</div>'


def build(s, fmt):
    kind, w, h = fmt
    if kind == "story":
        pad, title_fs, sub_fs, tag_fs, name_fs, meta_fs, note_fs, price_fs, cpad, gap = \
            "150px 84px 180px", 82, 40, 27, 58, 38, 33, 76, "34px 40px", 26
    elif kind == "ig":
        pad, title_fs, sub_fs, tag_fs, name_fs, meta_fs, note_fs, price_fs, cpad, gap = \
            "60px 74px 56px", 76, 37, 25, 52, 35, 30, 70, "28px 36px", 22
    else:  # fb square
        pad, title_fs, sub_fs, tag_fs, name_fs, meta_fs, note_fs, price_fs, cpad, gap = \
            "46px 66px 44px", 62, 32, 23, 44, 30, 27, 58, "22px 30px", 16
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;{CREAM}
  color:#2B1F18;display:flex;flex-direction:column;align-items:center;text-align:center;padding:{pad};}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:{80 if kind!='fb' else 66}px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.2em;text-transform:uppercase;font-size:25px;margin-top:18px;}}
h1{{font-family:'DM Serif Display',serif;font-size:{title_fs}px;line-height:1.02;margin-top:10px;}}
.sub{{color:#4a4038;font-size:{sub_fs}px;font-weight:600;margin-top:12px;}}
.cards{{width:100%;display:flex;flex-direction:column;gap:{gap}px;margin-top:{gap+12}px;}}
.card{{background:#fff;border-radius:22px;border-left:12px solid #C19D5F;padding:{cpad};
  box-shadow:0 12px 30px rgba(43,31,24,.10);display:flex;align-items:center;gap:24px;text-align:left;}}
.cl{{flex:1;}}
.tag{{font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:{tag_fs}px;}}
.cname{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:{name_fs}px;line-height:1.0;margin-top:6px;}}
.cmeta{{color:#2B1F18;font-weight:700;font-size:{meta_fs}px;margin-top:10px;}}
.cnote{{color:#6a5f52;font-weight:500;font-size:{note_fs}px;margin-top:4px;}}
.cr{{flex:none;}}
.price{{font-family:'DM Serif Display',serif;font-size:{price_fs}px;line-height:1;}}
.foot{{margin-top:auto;padding-top:{gap+8}px;}}
.foot .note{{color:#B8593A;font-weight:700;font-size:{sub_fs-2}px;}}
.foot .url{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:{sub_fs+14}px;margin-top:6px;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<img class="logo" src="{LOGO_COLOR}">
<div class="eyebrow">{s['eyebrow']}</div>
<h1>{s['title']}</h1>
<div class="sub">{s['sub']}</div>
{cards_html(s['cards'])}
<div class="foot">
  <div class="note">{s['foot']}</div>
  <div class="url">{URL}</div>
</div>
</div>"""
    render(f"ai-lineup-{kind}-{w}x{h}{s['suffix']}.html", page(css, body), w, h)


if __name__ == "__main__":
    for lang in ("en", "pt"):
        s = STR[lang]
        build(s, ("ig", 1080, 1350))
        build(s, ("fb", 1080, 1080))
        build(s, ("story", 1080, 1920))
    print("done")
