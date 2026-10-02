#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sunday 4 Oct 2026 carousel: "Your first 3 words in Mandarin". EN and PT on every slide.

Slides (1080x1350, also fine for Facebook):
  1 cover, 2 nǐ hǎo, 3 xièxie, 4 zàijiàn, 5 free taster CTA.

Outputs: social/Mandarin/words/words-{1..5}-1080x1350.png
Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Mandarin", "words")
os.makedirs(OUT, exist_ok=True)
HK = bm.b64_photo(os.path.join(bm.IMG, "mandarin-hk-2.jpg"))
W, H = 1080, 1350

WORDS = [
    ("你好", "nǐ hǎo", "hello", "olá",
     "Literally “you good”.", "À letra: “tu bem”."),
    ("谢谢", "xièxie", "thank you", "obrigado / obrigada",
     "The second syllable is soft, almost whispered.", "A segunda sílaba é suave, quase sussurrada."),
    ("再见", "zàijiàn", "goodbye", "adeus",
     "Literally “again see”.", "À letra: “outra vez ver”."),
]

CSS = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{position:absolute;top:44px;left:56px;height:84px;}}
.count{{position:absolute;top:66px;right:56px;font-weight:700;letter-spacing:.16em;color:#B8593A;font-size:26px;}}
.dots{{position:absolute;bottom:44px;left:0;right:0;display:flex;justify-content:center;gap:14px;}}
.dots i{{width:14px;height:14px;border-radius:50%;background:#E3D6C0;display:block;}}
.dots i.on{{background:#B8593A;}}
.swipe{{position:absolute;bottom:84px;right:56px;font-weight:700;font-size:28px;color:#617C7B;}}
/* cover */
.ph{{position:absolute;left:56px;right:56px;top:160px;height:600px;width:calc(100% - 112px);object-fit:cover;object-position:center 35%;border-radius:30px;box-shadow:0 14px 34px rgba(43,31,24,.16);}}
.badge{{position:absolute;top:190px;right:86px;background:#B8593A;color:#FBF6EE;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:26px;padding:10px 22px;border-radius:999px;}}
.cover{{position:absolute;left:56px;right:56px;top:810px;}}
.cover h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:112px;line-height:1.0;}}
.cover h1 .a{{color:#B8593A;font-style:italic;}}
.cover h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:58px;line-height:1.1;color:#726651;margin-top:18px;}}
.cover h2 .a{{color:#B8593A;font-style:italic;}}
/* word */
.card{{position:absolute;left:56px;right:56px;top:170px;bottom:150px;background:#fff;border-radius:34px;box-shadow:0 14px 34px rgba(43,31,24,.08);
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:40px;border-top:16px solid #C19D5F;}}
.zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:250px;line-height:1.05;}}
.py{{font-family:'DM Serif Display',serif;font-style:italic;font-size:100px;color:#B8593A;margin-top:6px;}}
.mean{{margin-top:34px;display:flex;gap:18px;align-items:center;flex-wrap:wrap;justify-content:center;}}
.mean span{{font-size:44px;font-weight:700;background:#F1E9DA;border-radius:999px;padding:10px 30px;}}
.mean span.pt{{background:#E4ECEB;color:#3f5a59;}}
.tip{{margin-top:40px;font-size:31px;color:#4a4038;font-weight:500;line-height:1.35;}}
.tip b{{color:#617C7B;}}
/* cta */
.cta{{position:absolute;left:56px;right:56px;top:170px;}}
.cta h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:92px;line-height:1.02;}}
.cta h1 .a{{color:#B8593A;font-style:italic;}}
.cta h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:54px;line-height:1.1;color:#726651;margin-top:14px;}}
.ticket{{margin-top:56px;background:#B8593A;color:#FBF6EE;border-radius:26px;padding:10px;transform:rotate(-2deg);box-shadow:0 14px 34px rgba(184,89,58,.35);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:18px;padding:30px 36px;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:76px;line-height:1;}}
.ticket .d{{font-size:42px;font-weight:700;margin-top:14px;}}
.ticket .d2{{font-size:32px;font-weight:600;color:#F6DCC0;margin-top:4px;}}
.ticket .u{{font-size:40px;font-weight:700;margin-top:18px;background:#FBF6EE;color:#B8593A;display:inline-block;padding:8px 24px;border-radius:999px;}}
.after{{margin-top:48px;font-size:32px;font-weight:600;color:#4a4038;line-height:1.4;}}
.after b{{color:#617C7B;}}
.mich{{margin-top:44px;display:flex;align-items:center;gap:28px;}}
.mich img{{width:200px;height:200px;border-radius:50%;object-fit:cover;object-position:center 30%;border:8px solid #fff;box-shadow:0 10px 26px rgba(0,0,0,.18);}}
.mich .n{{font-family:'DM Serif Display',serif;font-size:48px;}}
.mich .r{{font-size:30px;font-weight:600;color:#726651;margin-top:4px;}}
.mich .b{{font-family:'DM Serif Display',serif;font-style:italic;font-size:38px;color:#B8593A;margin-top:8px;}}
</style>"""

def frame(n, body, swipe=True):
    dots = "".join(f'<i class="{"on" if k == n else ""}"></i>' for k in range(1, 6))
    sw = '<div class="swipe">Deslize / Swipe &rarr;</div>' if swipe else ""
    return (f'<!DOCTYPE html><html><head>{bm.FONTS}{CSS}</head><body><div class="bar"></div>'
            f'<img class="logo" src="{bm.LOGO_COLOR}"><div class="count">{n}/5</div>'
            f'{body}{sw}<div class="dots">{dots}</div></body></html>')

def slides():
    out = [frame(1, f"""
<img class="ph" src="{HK}"><div class="badge">Mini aula &middot; Mini lesson</div>
<div class="cover">
  <h1>Your first <span class="a">3 words</span> in Mandarin.</h1>
  <h2>As suas primeiras <span class="a">3 palavras</span> em mandarim.</h2>
</div>""")]
    for i, (zh, py, en, pt, tip_en, tip_pt) in enumerate(WORDS, start=2):
        out.append(frame(i, f"""
<div class="card">
  <div class="zh">{zh}</div>
  <div class="py">{py}</div>
  <div class="mean"><span>{en}</span><span class="pt">{pt}</span></div>
  <div class="tip">{tip_en}<br><b>{tip_pt}</b></div>
</div>"""))
    out.append(frame(5, f"""
<div class="cta">
  <h1>Want to learn <span class="a">more</span>?</h1>
  <h2>Quer aprender <span class="a">mais</span>?</h2>
  <div class="ticket"><div class="in">
    <div class="k">Free taster &middot; Aula grátis</div>
    <div class="d">Monday 12 October &middot; 18h30</div>
    <div class="d2">Segunda, 12 de outubro &middot; with Michelle Kanner</div>
    <div class="u">patiolanguage.pt/taster</div>
  </div></div>
  <div class="after">Mandarin classes start 19 October at Patio Language School.<br><b>As aulas de mandarim começam a 19 de outubro.</b></div>
  <div class="mich"><img src="{bm.MICHELLE}"><div><div class="n">Michelle Kanner</div><div class="r">Your teacher &middot; A sua professora</div><div class="b">Até dia 12! See you on the 12th!</div></div></div>
</div>""", swipe=False))
    return out

if __name__ == "__main__":
    for n, html in enumerate(slides(), start=1):
        name = f"words-{n}-{W}x{H}"
        path = os.path.join(OUT, name + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--window-size={W},{H}", "--virtual-time-budget=6000",
            f"--screenshot={os.path.join(OUT, name + '.png')}", path],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("rendered", name + ".png")
