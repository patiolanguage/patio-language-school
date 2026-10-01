#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build images for the Mandarin Google Form (same style as form-header-ai.png).

Outputs (social/):
  form-header-mandarin.png   1600x400  Forms header: Patio room + Hong Kong, logo, headline
  form-teacher-mandarin.png  1600x600  Image item: Michelle's photo + "Meet your teacher"

Google Forms does not let a script set the header or theme, so these are
uploaded by hand in the form editor (Customize theme > Header > Upload).
Brand is "Patio", no accent. No em or en dashes.
"""
import base64, io, os, subprocess
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64_png(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

def b64_photo(path):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

LOGO_WHITE = b64_png(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
ROOM = b64_photo(os.path.join(IMG, "mandarin-hero.jpg"))
HK = b64_photo(os.path.join(IMG, "mandarin-hk-1.jpg"))
MICHELLE = b64_photo(os.path.join(IMG, "michelle.jpg"))

FONTS = ('<meta charset="UTF-8">'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700'
         '&family=DM+Serif+Display:ital@0;1&family=Noto+Serif+SC:wght@600&display=swap" rel="stylesheet">')

def render(fname, w, h):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}", "--virtual-time-budget=6000",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

def write(fname, html):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

def header():
    html = f"""<!DOCTYPE html><html><head>{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1600px;height:400px;overflow:hidden;background:#2B1F18}}
.halves{{position:absolute;inset:0;display:flex}}
.halves img{{width:50%;height:100%;object-fit:cover}}
.halves img:last-child{{object-position:center 70%}}
.seam{{position:absolute;top:0;bottom:0;left:50%;width:3px;transform:translateX(-50%);background:rgba(251,246,238,.85)}}
.scrim{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(43,31,24,.55),rgba(43,31,24,.6) 60%,rgba(43,31,24,.75))}}
.bar{{position:absolute;top:0;left:0;right:0;height:10px;background:linear-gradient(90deg,#C19D5F,#B8593A)}}
.c{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;text-align:center}}
.logo{{height:96px;filter:drop-shadow(0 3px 10px rgba(0,0,0,.55))}}
.eyebrow{{color:#F0D4A6;font-family:Barlow,sans-serif;font-weight:700;letter-spacing:.24em;font-size:26px;text-shadow:0 1px 4px rgba(0,0,0,.9)}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;color:#FBF6EE;font-size:58px;line-height:1;text-shadow:0 2px 10px rgba(0,0,0,.6)}}
h1 .a{{color:#E9C58B;font-style:italic}}
h1 .zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:50px;margin-left:18px}}
</style></head><body>
<div class="halves"><img src="{ROOM}"><img src="{HK}"></div><div class="seam"></div><div class="scrim"></div><div class="bar"></div>
<div class="c"><img class="logo" src="{LOGO_WHITE}">
<div class="eyebrow">PATIO MANDARIN &middot; LAGOS &middot; FALL 2026</div>
<h1>Learn Mandarin <span class="a">with a smile</span>.<span class="zh">你好</span></h1></div>
</body></html>"""
    return write("form-header-mandarin.html", html)

def teacher():
    html = f"""<!DOCTYPE html><html><head>{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1600px;height:600px;overflow:hidden}}
body{{background:#FBF6EE;font-family:Barlow,sans-serif;color:#2B1F18;display:flex;align-items:center;gap:70px;padding:0 110px;position:relative}}
.bar{{position:absolute;top:0;left:0;right:0;height:10px;background:linear-gradient(90deg,#C19D5F,#B8593A)}}
img{{width:400px;height:400px;border-radius:50%;object-fit:cover;flex:none;box-shadow:0 10px 30px rgba(43,31,24,.25);border:8px solid #fff}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.2em;font-size:28px}}
h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:82px;line-height:1.02;margin-top:10px}}
h2 .a{{color:#B8593A;font-style:italic}}
p{{font-size:34px;font-weight:500;color:#4a4038;line-height:1.35;margin-top:22px;max-width:820px}}
</style></head><body><div class="bar"></div>
<img src="{MICHELLE}">
<div><div class="eyebrow">YOUR TEACHER &middot; A TUA PROFESSORA</div>
<h2>Michelle <span class="a">Kanner</span></h2>
<p>Years of living and working in Taiwan, Singapore, Hong Kong and China. Simple, practical and fun lessons.</p></div>
</body></html>"""
    return write("form-teacher-mandarin.html", html)

if __name__ == "__main__":
    render(header(), 1600, 400)
    render(teacher(), 1600, 600)
