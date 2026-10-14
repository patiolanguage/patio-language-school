#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tue 13 Oct 2026: day after the free Mandarin taster. Colourful photo collage in
Patio colours with a participant quote: "It's so good. It's so easy. I love it!"

Photos: taster photos in Documents/Patio Language/Patio Pix (Claire, 2026-10-13).
Quote: said by a course participant, given by Claire. No name.

Outputs (social/Mandarin/thanks/):
  thanks-ig-1080x1350.png      Instagram, with register link
  thanks-fb-1080x1350.png      Facebook, no link on the image
  thanks-story-1080x1920.png   Story, bottom kept clear for the link sticker
"""
import os, subprocess
import build_mandarin as bm

PIX = r"C:\Users\Claire\Documents\Patio Language\Patio Pix"
OUT = os.path.join(bm.SOCIAL, "Mandarin", "thanks")
os.makedirs(OUT, exist_ok=True)

def pic(name):
    return bm.b64_photo(os.path.join(PIX, name))

A = pic("michelle 2 tone.jpeg")      # Michelle holding the wǒ card, waving
B = pic("michelle tones.jpeg")       # group at the table, Michelle teaching
C = pic("my cards.jpeg")             # handwritten pinyin cards
D = pic("michelle note cards.jpeg")  # Michelle with cards spread on the table

FMT = {
    "ig":    dict(w=1080, h=1350, top=330, ph=480, quote=70, q_top=845, link=True, safe=40, head=40),
    "fb":    dict(w=1080, h=1350, top=330, ph=480, quote=70, q_top=845, link=False, safe=40, head=40),
    "story": dict(w=1080, h=1920, top=540, ph=520, quote=78, q_top=1095, link=False, safe=330, head=230),
}

def page(fmt):
    """Teal background (Claire 2026-10-13: grid too beige). Thanks to students and Michelle."""
    f = FMT[fmt]
    W, H, t, ph = f["w"], f["h"], f["top"], f["ph"]
    half = (ph - 20) // 2
    foot_txt = "Contact us for the Mandarin schedule &middot; +351 928 129 560"
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#617C7B;color:#FBF6EE;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.blob1{{position:absolute;width:560px;height:560px;border-radius:50%;background:#E9C58B;opacity:.28;left:-200px;top:{t+ph-320}px;}}
.blob2{{position:absolute;width:460px;height:460px;border-radius:50%;background:#B8593A;opacity:.35;right:-170px;top:{t-150}px;}}
.head{{position:absolute;left:50px;right:50px;top:{f['head']}px;}}
.head .row{{display:flex;justify-content:space-between;align-items:flex-start;}}
.head img{{height:84px;}}
.head h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:62px;line-height:1;text-align:right;}}
.head h1 i{{color:#E9C58B;}}
.head p{{margin-top:18px;font-size:38px;line-height:1.25;font-weight:700;color:#FBF6EE;}}
.head p span{{color:#F6DCC0;font-weight:600;}}
.f{{position:absolute;background:#FBF6EE;padding:12px;border-radius:14px;box-shadow:0 16px 34px rgba(0,0,0,.28);}}
.f img{{width:100%;height:100%;object-fit:cover;border-radius:8px;display:block;}}
.a{{left:44px;top:{t}px;width:470px;height:{ph}px;transform:rotate(-2.5deg);border-bottom:14px solid #B8593A;}}
.b{{left:536px;top:{t+6}px;width:500px;height:{half}px;transform:rotate(2deg);border-bottom:14px solid #C19D5F;}}
.c{{left:540px;top:{t+half+28}px;width:240px;height:{half}px;transform:rotate(-2deg);border-bottom:14px solid #E9C58B;}}
.d{{left:796px;top:{t+half+20}px;width:240px;height:{half}px;transform:rotate(3deg);border-bottom:14px solid #B8593A;}}
.quote{{position:absolute;left:50px;right:50px;top:{f['q_top']}px;background:#FBF6EE;color:#2B1F18;border-radius:28px;padding:30px 44px 26px;
  box-shadow:0 16px 36px rgba(0,0,0,.25);}}
.quote .q{{font-family:'DM Serif Display',serif;font-size:{f['quote']}px;line-height:1.02;}}
.quote .q b{{color:#B8593A;font-weight:400;}}
.quote .q i{{color:#B8593A;white-space:nowrap;}}
.quote .pt{{font-family:'DM Serif Display',serif;font-style:italic;font-size:{f['quote']*0.56:.0f}px;color:#4a4038;margin-top:10px;}}
.quote .by{{white-space:nowrap;font-weight:700;font-size:32px;letter-spacing:.05em;text-transform:uppercase;color:#617C7B;margin-top:12px;}}
.foot{{position:absolute;left:50px;right:50px;bottom:{f['safe']}px;background:#B8593A;color:#FBF6EE;border-radius:999px;padding:18px 30px;
  font-weight:700;font-size:32px;text-align:center;box-shadow:0 10px 24px rgba(0,0,0,.2);}}
</style></head><body><div class="bar"></div><div class="blob1"></div><div class="blob2"></div>
<div class="head">
  <div class="row"><img src="{bm.LOGO_WHITE}"><h1><i>Mandarin Night</i><br>at Patio was a success!</h1></div>
  <p>Thank you, Michelle &amp; students!<br><span>Obrigada, Michelle e alunos!</span></p>
</div>
<div class="f a"><img src="{A}" style="object-position:center 30%"></div>
<div class="f b"><img src="{B}" style="object-position:center 35%"></div>
<div class="f c"><img src="{C}" style="object-position:center"></div>
<div class="f d"><img src="{D}" style="object-position:center 20%"></div>
<div class="quote">
  <div class="q"><b>&ldquo;</b>Mandarin is so good. It&rsquo;s so easy. <i>I love it!</i><b>&rdquo;</b></div>
  <div class="pt">&ldquo;O mandarim é tão bom. É tão fácil. Adoro!&rdquo;</div>
  <div class="by">Mandarin student &middot; Estudante de mandarim</div>
</div>
<div class="foot">{foot_txt}</div>
</body></html>"""

def render(fmt):
    f = FMT[fmt]
    name = f"thanks-{fmt}-{f['w']}x{f['h']}"
    path = os.path.join(OUT, name + ".html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(page(fmt))
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={f['w']},{f['h']}", "--virtual-time-budget=6000",
        f"--screenshot={os.path.join(OUT, name + '.png')}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", name + ".png")

if __name__ == "__main__":
    for fmt in FMT:
        render(fmt)
