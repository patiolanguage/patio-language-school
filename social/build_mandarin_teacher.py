#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Meet the teacher post, Mon 5 Oct 2026. Michelle Kanner. EN and PT.

All facts come from Michelle's bio on /mandarin/ and /pt/mandarim/.
Quote is her own line from the bio.

Outputs (social/Mandarin/teacher/):
  teacher-{en,pt}-ig-1080x1350.png
  teacher-{en,pt}-story-1080x1920.png
  teacher-{en,pt}-fb-1080x1080.png

Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Mandarin", "teacher")
os.makedirs(OUT, exist_ok=True)
HK = bm.b64_photo(os.path.join(bm.IMG, "mandarin-hk-1.jpg"))

COPY = {
    "en": dict(
        pill="Meet the teacher",
        hello="Hi, I&rsquo;m",
        role="Your Mandarin teacher at Patio",
        quote="Learning a language should be simple, practical and <span>fun</span>.",
        facts=["Years in Taiwan, Singapore, Hong&nbsp;Kong and China",
               "University of Cambridge graduate",
               "Feng Shui Master"],
        tk_k="Meet Michelle",
        tk_d="Free taster &middot; Mon 12 Oct &middot; 18h30",
        tk_u="patiolanguage.pt/taster",
    ),
    "pt": dict(
        pill="Conheça a professora",
        hello="Olá, sou a",
        role="A sua professora de mandarim no Patio",
        quote="Aprender uma língua deve ser simples, prático e <span>divertido</span>.",
        facts=["Anos em Taiwan, Singapura, Hong&nbsp;Kong e China",
               "Licenciada pela Universidade de Cambridge",
               "Mestre de Feng Shui"],
        tk_k="Conheça a Michelle",
        tk_d="Aula grátis &middot; Seg 12 out &middot; 18h30",
        tk_u="patiolanguage.pt/taster",
    ),
}

FMT = {
    "ig":    dict(w=1080, h=1350, top=40, bottom=44, photo=330, mich=380, name=96, quote=46, fact=28, tk=30, gap=22),
    "story": dict(w=1080, h=1920, top=130, bottom=280, photo=400, mich=420, name=116, quote=58, fact=36, tk=36, gap=36),
    "fb":    dict(w=1080, h=1080, top=36, bottom=36, photo=250, mich=290, name=76, quote=36, fact=24, tk=26, gap=12),
}

def page(lang, fmt):
    c, f = COPY[lang], FMT[fmt]
    m = f["mich"]
    facts = "".join(f'<div class="fact"><i></i><span>{t}</span></div>' for t in c["facts"])
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{f['w']}px;height:{f['h']}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.wrap{{position:absolute;left:56px;right:56px;top:{f['top']}px;bottom:{f['bottom']}px;display:flex;flex-direction:column;align-items:center;text-align:center;}}
.top{{position:relative;width:100%;height:{f['photo']}px;flex:none;}}
.top .ph{{width:100%;height:100%;object-fit:cover;object-position:center 45%;border-radius:30px;display:block;box-shadow:0 14px 34px rgba(43,31,24,.16);}}
.top .logo{{position:absolute;top:24px;left:28px;height:{f['photo']*0.22:.0f}px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.55));}}
.top .pill{{position:absolute;top:28px;right:28px;background:#B8593A;color:#FBF6EE;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  font-size:{f['fact']-1}px;padding:10px 22px;border-radius:999px;box-shadow:0 6px 16px rgba(0,0,0,.25);}}
.mich{{position:absolute;left:50%;transform:translateX(-50%);bottom:-{m*0.62:.0f}px;width:{m}px;height:{m}px;border-radius:50%;overflow:hidden;
  border:12px solid #FBF6EE;box-shadow:0 14px 34px rgba(0,0,0,.22);}}
.mich img{{width:100%;height:100%;object-fit:cover;object-position:center 30%;}}
.hello{{margin-top:{m*0.62+18:.0f}px;font-family:'DM Serif Display',serif;font-style:italic;font-size:{f['name']*0.42:.0f}px;color:#B8593A;}}
.name{{font-family:'DM Serif Display',serif;font-size:{f['name']}px;line-height:1;}}
.role{{font-size:{f['fact']+2}px;font-weight:600;color:#617C7B;letter-spacing:.04em;margin-top:8px;}}
.quote{{margin-top:{f['gap']}px;font-family:'DM Serif Display',serif;font-size:{f['quote']}px;line-height:1.15;max-width:92%;}}
.quote span{{color:#B8593A;font-style:italic;}}
.quote:before{{content:"\\201C";color:#C19D5F;}}
.quote:after{{content:"\\201D";color:#C19D5F;}}
.facts{{margin-top:{f['gap']}px;display:flex;flex-direction:column;gap:{f['gap']*0.45:.0f}px;align-items:center;}}
.fact{{display:flex;align-items:center;gap:14px;background:#fff;border-radius:999px;padding:9px 24px 9px 14px;font-size:{f['fact']}px;font-weight:600;
  box-shadow:0 6px 16px rgba(43,31,24,.07);}}
.fact i{{width:{f['fact']*0.55:.0f}px;height:{f['fact']*0.55:.0f}px;border-radius:50%;background:#C19D5F;display:block;flex:none;}}
.ticket{{margin-top:auto;background:#B8593A;color:#FBF6EE;border-radius:20px;padding:8px;box-shadow:0 10px 26px rgba(184,89,58,.35);transform:rotate(-1.5deg);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:14px;padding:12px 34px;display:flex;align-items:center;gap:26px;}}
.ticket .k{{white-space:nowrap;font-family:'DM Serif Display',serif;font-size:{f['tk']*1.35:.0f}px;line-height:1;}}
.ticket .r{{text-align:left;}}
.ticket .d{{white-space:nowrap;font-size:{f['tk']*0.9:.0f}px;font-weight:700;}}
.ticket .u{{font-size:{f['tk']*0.8:.0f}px;font-weight:600;color:#F6DCC0;margin-top:2px;}}
</style></head><body>
<div class="bar"></div>
<div class="wrap">
  <div class="top">
    <img class="ph" src="{HK}">
    <img class="logo" src="{bm.LOGO_WHITE}">
    <div class="pill">{c['pill']}</div>
    <div class="mich"><img src="{bm.MICHELLE}"></div>
  </div>
  <div class="hello">{c['hello']}</div>
  <div class="name">Michelle Kanner</div>
  <div class="role">{c['role']}</div>
  <div class="quote">{c['quote']}</div>
  <div class="facts">{facts}</div>
  <div class="ticket"><div class="in"><div class="k">{c['tk_k']}</div>
    <div class="r"><div class="d">{c['tk_d']}</div><div class="u">{c['tk_u']}</div></div></div></div>
</div>
</body></html>"""

def render(lang, fmt):
    f = FMT[fmt]
    name = f"teacher-{lang}-{fmt}-{f['w']}x{f['h']}"
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
