#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mandarin launch posts, light and friendly version. EN and PT.

Replaces the dark full bleed launch posts from build_mandarin.py for social.
Claire 2026-10-01: old posts too dark and hard to read.

Hook: Michelle says nǐ hǎo, "Mandarin is easier than you think", three ticks,
course facts, and a free taster ticket (Mon 12 Oct 18h30, patiolanguage.pt/taster).

Outputs (social/Mandarin/launch/):
  mandarin-{en,pt}-ig-1080x1350.png
  mandarin-{en,pt}-story-1080x1920.png
  mandarin-{en,pt}-fb-1080x1080.png

Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Mandarin", "launch")
os.makedirs(OUT, exist_ok=True)
HK = bm.b64_photo(os.path.join(bm.IMG, "mandarin-hk-2.jpg"))

COPY = {
    "en": dict(
        new="New &middot; Mandarin classes",
        bubble="Nǐ hǎo!",
        name="Michelle Kanner",
        role="Your teacher. Years living in Taiwan, Singapore, Hong&nbsp;Kong and China.",
        title='Learn <span class="a">Mandarin</span> in Lagos.',
        easy="Small group classes. Easier than you think:",
        ticks=["No verb conjugations", "No tenses", "No gendered nouns"],
        info_h="All levels welcome",
        info_d="Starts 19 October",
        info_t="Mon &amp; Wed 9h15 &middot; Tue &amp; Thu 15h00",
        tk_k="Free taster",
        tk_d="Mon 12 Oct &middot; 18h30",
        tk_u="patiolanguage.pt/taster",
    ),
    "pt": dict(
        new="Novidade &middot; Aulas de mandarim",
        bubble="Nǐ hǎo!",
        name="Michelle Kanner",
        role="A sua professora. Viveu anos em Taiwan, Singapura, Hong&nbsp;Kong e&nbsp;China.",
        title='Aprenda <span class="a">mandarim</span> em Lagos.',
        easy="Aulas em pequenos grupos. Mais fácil do que pensa:",
        ticks=["Sem conjugações", "Sem tempos verbais", "Sem género"],
        info_h="Todos os níveis",
        info_d="Começa a 19 de outubro",
        info_t="Seg e Qua 9h15 &middot; Ter e Qui 15h00",
        tk_k="Aula grátis",
        tk_d="Seg 12 out &middot; 18h30",
        tk_u="patiolanguage.pt/taster",
    ),
}

# Per format sizes
FMT = {
    "ig":    dict(w=1080, h=1350, top=40, bottom=44, photo=560, mich=290, h1=100, tick=31, name=40, role=25, info=30, gap=26),
    "story": dict(w=1080, h=1920, top=130, bottom=300, photo=540, mich=320, h1=104, tick=36, name=46, role=28, info=34, gap=40),
    "fb":    dict(w=1080, h=1080, top=36, bottom=36, photo=400, mich=230, h1=80, tick=27, name=34, role=22, info=26, gap=16),
}

def page(lang, fmt):
    c, f = COPY[lang], FMT[fmt]
    m = f["mich"]
    ticks = "".join(f'<div class="tick"><span>&#10003;</span>{t}</div>' for t in c["ticks"])
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{f['w']}px;height:{f['h']}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.wrap{{position:absolute;left:56px;right:56px;top:{f['top']}px;bottom:{f['bottom']}px;display:flex;flex-direction:column;}}
.top{{position:relative;height:{f['photo']}px;flex:none;}}
.top .ph{{width:100%;height:100%;object-fit:cover;object-position:center 35%;border-radius:30px;display:block;box-shadow:0 14px 34px rgba(43,31,24,.16);}}
.top .logo{{position:absolute;top:26px;left:30px;height:{f['mich']*0.33:.0f}px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.55));}}
.top .new{{position:absolute;top:30px;right:30px;background:#B8593A;color:#FBF6EE;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  font-size:{f['role']+1}px;padding:10px 22px;border-radius:999px;box-shadow:0 6px 16px rgba(0,0,0,.25);}}
.mich{{position:absolute;left:28px;bottom:-{m*0.5:.0f}px;width:{m}px;height:{m}px;border-radius:50%;overflow:hidden;border:9px solid #FBF6EE;box-shadow:0 10px 26px rgba(0,0,0,.25);}}
.mich img{{width:100%;height:100%;object-fit:cover;object-position:center 30%;}}
.bubble{{position:absolute;left:{m+60}px;bottom:{m*0.12:.0f}px;background:#fff;border-radius:28px;padding:14px 30px 16px;
  box-shadow:0 10px 26px rgba(0,0,0,.18);display:flex;align-items:baseline;gap:14px;}}
.bubble:before{{content:"";position:absolute;left:-18px;bottom:22px;border-width:14px 22px 14px 0;border-style:solid;border-color:transparent #fff transparent transparent;}}
.bubble .zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:{f['h1']*0.62:.0f}px;line-height:1;}}
.bubble .py{{font-family:'DM Serif Display',serif;font-style:italic;font-size:{f['h1']*0.48:.0f}px;color:#B8593A;}}
.who{{min-height:{m*0.5+14:.0f}px;padding-left:{m+60}px;padding-top:16px;flex:none;}}
.who .n{{font-family:'DM Serif Display',serif;font-size:{f['name']}px;line-height:1.05;}}
.who .r{{font-size:{f['role']}px;font-weight:500;color:#726651;line-height:1.3;margin-top:4px;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:{f['h1']}px;line-height:1.02;margin-top:{f['gap']}px;}}
h1 .a{{color:#B8593A;font-style:italic;}}
.easy{{font-size:{f['tick']*1.15:.0f}px;font-weight:600;color:#4a4038;margin-top:{f['gap']*0.5:.0f}px;}}
.ticks{{display:flex;flex-wrap:wrap;gap:12px;margin-top:{f['gap']*0.5:.0f}px;}}
.tick{{background:#fff;border-radius:999px;padding:10px 22px 10px 12px;font-size:{f['tick']}px;font-weight:600;display:flex;align-items:center;gap:12px;
  box-shadow:0 6px 16px rgba(43,31,24,.07);}}
.tick span{{width:{f['tick']*1.25:.0f}px;height:{f['tick']*1.25:.0f}px;border-radius:50%;background:#617C7B;color:#fff;display:flex;align-items:center;justify-content:center;font-size:{f['tick']*0.75:.0f}px;}}
.bottom{{margin-top:auto;display:flex;gap:18px;align-items:stretch;}}
.info{{flex:1.25;background:#fff;border-left:12px solid #C19D5F;border-radius:20px;padding:18px 24px;box-shadow:0 8px 24px rgba(43,31,24,.08);}}
.info .h{{font-size:{f['info']*0.82:.0f}px;font-weight:700;letter-spacing:.06em;color:#617C7B;text-transform:uppercase;}}
.info .d{{font-family:'DM Serif Display',serif;font-size:{f['info']*1.25:.0f}px;line-height:1.1;margin-top:4px;}}
.info .t{{font-size:{f['info']*0.85:.0f}px;font-weight:600;color:#726651;margin-top:6px;}}
.ticket{{flex:1;background:#B8593A;color:#FBF6EE;border-radius:20px;padding:8px;box-shadow:0 10px 26px rgba(184,89,58,.35);transform:rotate(-2deg);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:14px;height:100%;padding:12px 18px;display:flex;flex-direction:column;justify-content:center;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:{f['info']*1.3:.0f}px;line-height:1;}}
.ticket .d{{font-size:{f['info']*0.95:.0f}px;font-weight:700;margin-top:8px;}}
.ticket .u{{font-size:{f['info']*0.72:.0f}px;font-weight:600;color:#F6DCC0;margin-top:6px;}}
</style></head><body>
<div class="bar"></div>
<div class="wrap">
  <div class="top">
    <img class="ph" src="{HK}">
    <img class="logo" src="{bm.LOGO_WHITE}">
    <div class="new">{c['new']}</div>
    <div class="mich"><img src="{bm.MICHELLE}"></div>
    <div class="bubble"><span class="zh">你好!</span><span class="py">{c['bubble']}</span></div>
  </div>
  <div class="who"><div class="n">{c['name']}</div><div class="r">{c['role']}</div></div>
  <h1>{c['title']}</h1>
  <div class="easy">{c['easy']}</div>
  <div class="ticks">{ticks}</div>
  <div class="bottom">
    <div class="info"><div class="h">{c['info_h']}</div><div class="d">{c['info_d']}</div><div class="t">{c['info_t']}</div></div>
    <div class="ticket"><div class="in"><div class="k">{c['tk_k']}</div><div class="d">{c['tk_d']}</div><div class="u">{c['tk_u']}</div></div></div>
  </div>
</div>
</body></html>"""

def render(lang, fmt):
    f = FMT[fmt]
    name = f"mandarin-{lang}-{fmt}-{f['w']}x{f['h']}"
    html = os.path.join(OUT, name + ".html")
    with open(html, "w", encoding="utf-8") as fh:
        fh.write(page(lang, fmt))
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={f['w']},{f['h']}",
        "--virtual-time-budget=6000", f"--screenshot={os.path.join(OUT, name + '.png')}", html],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", name + ".png")

if __name__ == "__main__":
    for lang in ("en", "pt"):
        for fmt in ("ig", "story", "fb"):
            render(lang, fmt)
