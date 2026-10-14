#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sat 10 Oct 2026: free taster reminder, 2 days before. Everyone welcome.

Short version (Claire 2026-10-08: "way too many words"). One question, four tags,
Michelle, the date. Facts: free, 45 min, Mon 12 Oct 18h30, no experience needed.

Outputs (social/Mandarin/expect/):
  expect-{en,pt}-ig-1080x1350.png      Instagram, with link
  expect-{en,pt}-fb-1080x1350.png      Facebook, no link on the image
  expect-{en,pt}-story-1080x1920.png   Story, space at the bottom for the link sticker
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Mandarin", "expect")
os.makedirs(OUT, exist_ok=True)

COPY = {
    "en": dict(
        eyebrow="Everyone welcome",
        title='Never tried <span class="a">Mandarin</span>?<br>Perfect.',
        tags=["Free", "45 minutes", "No experience", "Bring a friend"],
        who="with Michelle",
        when="Mon 12 Oct &middot; 18h30",
        link="patiolanguage.pt/taster",
    ),
    "pt": dict(
        eyebrow="Todos são bem-vindos",
        title='Nunca experimentou <span class="a">mandarim</span>?<br>Perfeito.',
        tags=["Grátis", "45 minutos", "Sem experiência", "Traga um amigo"],
        who="com a Michelle",
        when="Seg 12 out &middot; 18h30",
        link="patiolanguage.pt/taster",
    ),
}

FMT = {
    "ig":    dict(w=1080, h=1350, top=56, bottom=56, h1=120, tag=50, mich=300),
    "fb":    dict(w=1080, h=1350, top=56, bottom=56, h1=120, tag=50, mich=300),
    "story": dict(w=1080, h=1920, top=170, bottom=300, h1=118, tag=52, mich=320),
}

def page(lang, fmt):
    c, f = COPY[lang], FMT[fmt]
    tags = "".join(f'<span>{t}</span>' for t in c["tags"])
    link = "" if fmt == "fb" else f'<div class="u">{c["link"]}</div>'
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{f['w']}px;height:{f['h']}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.wrap{{position:absolute;left:60px;right:60px;top:{f['top']}px;bottom:{f['bottom']}px;display:flex;flex-direction:column;}}
.head{{display:flex;justify-content:space-between;align-items:center;}}
.head img{{height:90px;}}
.eyebrow{{background:#617C7B;color:#FBF6EE;font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:32px;padding:12px 26px;border-radius:999px;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:{f['h1']}px;line-height:1.0;margin-top:60px;}}
h1 .a{{color:#B8593A;font-style:italic;}}
.tags{{display:flex;flex-wrap:wrap;gap:16px;margin-top:50px;}}
.tags span{{background:#fff;border-radius:999px;padding:14px 32px;font-size:{f['tag']}px;font-weight:700;box-shadow:0 8px 22px rgba(43,31,24,.08);border:3px solid #E9C58B;}}
.ticket{{margin-top:auto;background:#B8593A;color:#FBF6EE;border-radius:28px;padding:10px;transform:rotate(-1.5deg);box-shadow:0 14px 34px rgba(184,89,58,.35);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:20px;padding:26px 30px;display:flex;align-items:center;gap:30px;}}
.ticket img{{width:{f['mich']*0.75:.0f}px;height:{f['mich']*0.75:.0f}px;border-radius:50%;object-fit:cover;object-position:center 30%;border:7px solid #FBF6EE;flex:none;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:{f['tag']*1.4:.0f}px;line-height:1;white-space:nowrap;}}
.ticket .w{{font-family:'DM Serif Display',serif;font-style:italic;font-size:{f['tag']*1.1:.0f}px;color:#F6DCC0;margin-top:6px;}}
.ticket .u{{font-size:{f['tag']*0.9:.0f}px;font-weight:700;margin-top:14px;background:#FBF6EE;color:#B8593A;display:inline-block;padding:6px 22px;border-radius:999px;}}
</style></head><body><div class="bar"></div><div class="wrap">
  <div class="head"><img src="{bm.LOGO_COLOR}"><div class="eyebrow">{c['eyebrow']}</div></div>
  <h1>{c['title']}</h1>
  <div class="tags">{tags}</div>
  <div class="ticket"><div class="in"><img src="{bm.MICHELLE}"><div>
    <div class="k">{c['when']}</div><div class="w">{c['who']}</div>{link}</div></div></div>
</div></body></html>"""

def render(lang, fmt):
    f = FMT[fmt]
    name = f"expect-{lang}-{fmt}-{f['w']}x{f['h']}"
    path = os.path.join(OUT, name + ".html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(page(lang, fmt))
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={f['w']},{f['h']}", "--virtual-time-budget=6000",
        f"--screenshot={os.path.join(OUT, name + '.png')}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", name + ".png")

if __name__ == "__main__":
    for lang in ("en", "pt"):
        for fmt in ("ig", "fb", "story"):
            render(lang, fmt)
