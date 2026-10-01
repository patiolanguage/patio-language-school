#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build the Mandarin launch set (print flyer + IG post + IG story).

Facts (confirmed by Claire 2026-09-24):
  Morning group:   Mon & Wed, 9h15 to 10h45, week of 19 Oct to week of 14 Dec.
  Afternoon group: Tue & Thu, 15h00 to 16h30, same weeks.
  No class on public holidays. EUR 11 per hour, but NO prices on printed flyers.
  Teacher: Michelle Kanner (photo + one line). Registration: patiolanguage.pt/mandarin-register (QR).
  Tone taken from the teacher's own poster: warm, fun, "with a smile".

Outputs (social/):
  mandarin-flyer-a5.html   -> Patio-Mandarin-Flyer.pdf   (print, A5, no prices)
  mandarin-ig-1080x1350.png                              (Instagram portrait)
  mandarin-story-1080x1920.png                           (Instagram story)
  mandarin-fb-1080x1080.png                              (Facebook post)

House style: DM Serif Display + Barlow. Brand is "Patio", no accent.
No em or en dashes.
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
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=86)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

LOGO_WHITE = b64_png(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
LOGO_COLOR = b64_png(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
QR = b64_png(os.path.join(IMG, "qr-mandarin-register.png"))  # -> patiolanguage.pt/mandarin-register
PIX = r"C:\Users\Claire\Documents\Patio Language\Patio Pix"
PHOTO_ROOM = b64_photo(os.path.join(IMG, "mandarin-hero.jpg"))             # Patio room with students
PHOTO_HK = b64_photo(os.path.join(PIX, "skyline hong kong.jpeg"))          # Michelle's Hong Kong photo
PHOTO_ROOM_TALL = b64_photo(os.path.join(PIX, "room pic with students.jpeg"))
MICHELLE = b64_photo(os.path.join(IMG, "michelle.jpg"))
MICHELLE_CHINA = b64_photo(os.path.join(IMG, "michelle-china.jpg"))  # close-up in China, for the IG post
REGISTER = "patiolanguage.pt/mandarin-register"

FONTS = ('<meta charset="UTF-8">'
         '<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
         '&family=DM+Serif+Display:ital@0;1&family=Noto+Serif+SC:wght@600&display=swap" rel="stylesheet">')

# Shared copy
EYEBROW = "New at Patio &middot; Mandarin"
TITLE = 'Learn Mandarin <span class="a">with a smile</span>.'
SUB = ('Small, friendly groups in Lagos. Speak from the very first class, '
       'with a teacher who makes it <b>fun</b>.<br>All levels welcome.')
GROUPS = [
    ("Morning group", "Mondays &amp; Wednesdays", "9h15 to 10h45", "19 Oct to 16 Dec", ""),
    ("Afternoon group", "Tuesdays &amp; Thursdays", "15h00 to 16h30", "20 Oct to 17 Dec", " s"),
]

def write(fname, html):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

def render_png(fname, w, h):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=6000",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

def render_pdf(fname, pdfname):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={os.path.join(SOCIAL, pdfname)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", pdfname)


# =====================================================================
# PRINT FLYER  (A5 portrait, no prices)
# =====================================================================
def flyer():
    cards = "".join(
        f'<div class="card{cls}"><div class="tag">{tag}</div>'
        f'<div class="t">{days}</div>'
        f'<div class="when">{time}<br><span>{dates}</span></div></div>'
        for tag, days, time, dates, cls in GROUPS)
    html = f"""<!DOCTYPE html><html><head>{FONTS}<style>
@page{{size:148mm 210mm;margin:0;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:148mm;height:210mm;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}}
.sheet{{position:relative;width:148mm;height:210mm;overflow:hidden;display:flex;flex-direction:column;}}
.hero{{position:relative;height:44mm;overflow:hidden;background:#2B1F18;flex:none;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2.6mm;}}
.halves{{position:absolute;inset:0;display:flex;}}
.halves img{{width:50%;height:100%;object-fit:cover;}}
.seam{{position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);width:.6mm;
  background:rgba(251,246,238,.85);z-index:2;}}
.scrim{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.55) 0%, rgba(43,31,24,.45) 55%, rgba(43,31,24,.72) 100%);}}
.bar{{position:absolute;top:0;left:0;right:0;height:4mm;background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}}
.hero .logo{{height:13mm;object-fit:contain;position:relative;z-index:2;filter:drop-shadow(0 1mm 3mm rgba(0,0,0,.55));}}
.hero .eyebrow{{position:relative;z-index:2;color:#F0D4A6;font-weight:700;letter-spacing:.24em;
  text-transform:uppercase;font-size:3mm;text-shadow:0 1px 3px rgba(0,0,0,.9);}}
.nihao{{position:relative;z-index:2;display:flex;align-items:baseline;gap:3mm;color:#FBF6EE;
  text-shadow:0 1mm 3mm rgba(0,0,0,.6);}}
.nihao .zh{{font-family:'Noto Serif SC',serif;font-size:11mm;font-weight:600;line-height:1;}}
.nihao .py{{font-family:'DM Serif Display',serif;font-style:italic;font-size:6mm;color:#E9C58B;}}
.body{{flex:1;padding:5mm 11mm 6mm;display:flex;flex-direction:column;}}
.title{{font-family:'DM Serif Display',serif;font-size:8.2mm;line-height:1.05;text-align:center;}}
.title .a{{color:#B8593A;font-style:italic;}}
.sub{{text-align:center;color:#4a4038;font-size:3.5mm;font-weight:500;line-height:1.32;margin-top:3mm;}}
.sub b{{color:#B8593A;font-weight:700;}}
.cards{{display:flex;gap:4mm;margin-top:4mm;}}
.card{{flex:1;background:#fff;border-radius:2.6mm;padding:3.4mm 4.4mm;box-shadow:0 3mm 8mm rgba(43,31,24,.07);
  border-top:1.8mm solid #617C7B;}}
.card.s{{border-top-color:#B8593A;}}
.card .tag{{font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:2.4mm;color:#4f6a69;}}
.card.s .tag{{color:#B8593A;}}
.card .t{{font-family:'DM Serif Display',serif;font-size:4.6mm;line-height:1.05;margin-top:1.2mm;}}
.card .when{{font-size:4mm;font-weight:700;margin-top:2.4mm;line-height:1.3;}}
.card .when span{{color:#726651;font-weight:600;font-size:3.3mm;}}
.common{{text-align:center;color:#726651;font-size:3.1mm;font-weight:600;margin-top:3mm;}}
.limited{{text-align:center;color:#B8593A;font-size:3.4mm;font-weight:700;margin-top:1.6mm;}}
.easy{{margin-top:2.4mm;text-align:center;font-size:3.3mm;font-weight:600;color:#2B1F18;}}
.easy b{{color:#7A3B52;}}
.teacher{{margin-top:3mm;display:flex;align-items:center;gap:4mm;background:#fff;border-radius:2.6mm;padding:3mm 4mm;box-shadow:0 3mm 8mm rgba(43,31,24,.07);border-left:1.8mm solid #C19D5F;}}
.teacher img{{width:16mm;height:16mm;border-radius:50%;object-fit:cover;flex:none;}}
.teacher .k{{font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:2.4mm;color:#B8593A;}}
.teacher .n{{font-family:'DM Serif Display',serif;font-size:5mm;line-height:1.1;}}
.teacher .d{{font-size:3mm;color:#4a4038;font-weight:500;line-height:1.3;margin-top:.6mm;}}
.cta{{margin-top:auto;background:#617C7B;color:#FBF6EE;border-radius:2.6mm;padding:3mm 5mm;
  display:flex;align-items:center;gap:5mm;}}
.cta .l{{flex:1;}}
.cta .h{{font-family:'DM Serif Display',serif;font-size:5.6mm;}}
.cta .u{{font-size:3.5mm;font-weight:700;margin-top:.8mm;}}
.cta .scan{{font-size:2.9mm;font-weight:600;color:#EAF0EF;margin-top:1.4mm;}}
.cta .qr{{flex:none;width:20mm;height:20mm;object-fit:contain;border-radius:1.6mm;background:#fff;padding:1mm;}}
.foot{{margin-top:2.8mm;display:flex;justify-content:space-between;align-items:flex-end;gap:4mm;}}
.contact{{font-size:2.95mm;line-height:1.6;color:#37302a;font-weight:500;}}
.contact b{{color:#B8593A;font-weight:700;}}
.logo2{{height:11mm;object-fit:contain;flex:none;}}
</style></head><body><div class="sheet">
<div class="hero">
  <div class="halves"><img src="{PHOTO_ROOM}"><img src="{PHOTO_HK}"></div>
  <div class="seam"></div><div class="scrim"></div><div class="bar"></div>
  <img class="logo" src="{LOGO_WHITE}">
  <div class="nihao"><span class="zh">你好</span><span class="py">n&#464; h&#462;o</span></div>
  <div class="eyebrow">{EYEBROW}</div>
</div>
<div class="body">
  <div class="title">{TITLE}</div>
  <div class="sub">{SUB}</div>
  <div class="cards">{cards}</div>
  <div class="common">Small groups &middot; 90 minute classes &middot; No classes on public holidays</div>
  <div class="easy">Easier than you think: <b>no verb conjugations, no tenses, no gendered nouns.</b></div>
  <div class="teacher"><img src="{MICHELLE}"><div><div class="k">Your teacher</div><div class="n">Michelle Kanner</div><div class="d">Years of living and working in Taiwan, Singapore, Hong Kong and China.</div></div></div>
  <div class="limited">&rarr; Limited spots, reserve yours now</div>
  <div class="cta">
    <div class="l">
      <div class="h">Register now</div>
      <div class="u">{REGISTER}</div>
      <div class="scan">or scan the code &middot; WhatsApp +351 928 129 560</div>
    </div>
    <img class="qr" src="{QR}">
  </div>
  <div class="foot">
    <div class="contact">
      patiolanguage.pt &middot; patiolanguage@gmail.com &middot; <b>@patiolanguage</b><br>
      Pra&ccedil;a do Poder Local, Lote 14, Loja C, Lagos
    </div>
    <img class="logo2" src="{LOGO_COLOR}">
  </div>
</div>
</div></body></html>"""
    return write("mandarin-flyer-a5.html", html)


# =====================================================================
# INSTAGRAM  (house photo style: full bleed, warm scrim, content bottom left)
# =====================================================================
def social(w, h, out):
    story = h > 1500
    square = w == h
    top_pad = 150 if story else 70
    bottom_pad = 240 if story else (56 if square else 80)
    lines = "".join(f'<div class="ln"><b>{days}</b> &middot; {time}</div>'
                    for _, days, time, _, _ in GROUPS)
    photo = PHOTO_ROOM_TALL if story else PHOTO_HK
    badge = (f'<div class="badge"><img src="{MICHELLE_CHINA}">'
                              f'<span><b>Teacher</b> &middot; Michelle Kanner</span></div>')
    html = f"""<!DOCTYPE html><html><head>{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{w}px;height:{h}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;position:relative;background:#2B1F18;}}
.photo{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}}
.scrim{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.10) 0%, rgba(43,31,24,.30) 25%, rgba(43,31,24,.82) 45%, rgba(43,31,24,.96) 100%);}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{position:absolute;top:{top_pad}px;left:70px;height:110px;filter:drop-shadow(0 4px 12px rgba(0,0,0,.5));}}
.content{{position:absolute;left:70px;right:70px;bottom:{bottom_pad}px;color:#FBF6EE;}}
.zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:{92 if square else 120}px;line-height:1;color:#FBF6EE;}}
.zh span{{font-family:'DM Serif Display',serif;font-style:italic;font-weight:400;font-size:56px;color:#E9C58B;margin-left:22px;}}
.eyebrow{{color:#C19D5F;text-shadow:0 2px 6px rgba(0,0,0,.6);font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:{26 if square else 30}px;margin-top:{20 if square else 34}px;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:{104 if story else (80 if square else 96)}px;line-height:1.02;margin-top:{8 if square else 14}px;}}
h1 .a{{color:#E9C58B;font-style:italic;}}
.sub{{font-size:{33 if square else 38}px;font-weight:500;color:#F1E9DA;margin-top:{14 if square else 22}px;line-height:1.25;}}
.times{{margin-top:{14 if square else 26}px;}}
.ln{{font-size:{32 if square else 36}px;font-weight:600;color:#E9C58B;line-height:1.45;}}
.ln b{{color:#FBF6EE;}}
.badge{{position:absolute;top:{150 if story else (50 if square else 60)}px;right:70px;display:flex;flex-direction:column;align-items:center;gap:14px;}}
.badge img{{width:{340 if story else (230 if square else 300)}px;height:{340 if story else (230 if square else 300)}px;border-radius:50%;object-fit:cover;border:8px solid #FBF6EE;box-shadow:0 10px 30px rgba(0,0,0,.45);}}
.badge span{{background:rgba(43,31,24,.82);color:#FBF6EE;font-weight:700;font-size:26px;letter-spacing:.06em;padding:8px 20px;border-radius:999px;}}
.badge span b{{color:#E9C58B;font-weight:700;}}
.pill{{display:inline-block;margin-top:{22 if square else 36}px;background:#B8593A;color:#FBF6EE;font-weight:700;
  font-size:32px;padding:18px 38px;border-radius:999px;}}
</style></head><body>
<img class="photo" src="{photo}"><div class="scrim"></div><div class="bar"></div>
<img class="logo" src="{LOGO_WHITE}">
{badge}
<div class="content">
  <div class="zh">你好<span>n&#464; h&#462;o</span></div>
  <div class="eyebrow">{EYEBROW}</div>
  <h1>{TITLE}</h1>
  <div class="sub">Small, friendly groups in Lagos with Michelle Kanner.<br>Starts 19 October. All levels welcome.</div>
  <div class="times">{lines}</div>
  <div class="pill">Register: {REGISTER}</div>
</div>
</body></html>"""
    return write(out, html)


if __name__ == "__main__":
    render_pdf(flyer(), "Patio-Mandarin-Flyer.pdf")
    render_png(social(1080, 1350, "mandarin-ig-1080x1350.html"), 1080, 1350)
    render_png(social(1080, 1920, "mandarin-story-1080x1920.html"), 1080, 1920)
    render_png(social(1080, 1080, "mandarin-fb-1080x1080.html"), 1080, 1080)
