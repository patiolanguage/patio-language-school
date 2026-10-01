#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build the free Mandarin taster set, EN and PT.

Facts (confirmed by Claire 2026-10-01):
  Free taster, Monday 12 October 2026, 18h30 to 19h15, at Patio.
  Led by Michelle Kanner. Sign up by WhatsApp +351 928 129 560.

Outputs (social/Mandarin/taster/):
  taster-{en,pt}-ig-1080x1350.png     Instagram post
  taster-{en,pt}-story-1080x1920.png  Instagram story and WhatsApp status
  taster-{en,pt}-fb-1080x1080.png     Facebook post and WhatsApp chat
  Patio-Mandarin-Taster-Flyer.pdf     A5 print, bilingual, WhatsApp QR
  qr-taster-whatsapp.png              QR to the WhatsApp chat
  taster-whatsapp-1080x1350.png       WhatsApp chats and groups, bilingual, reply to book

Reuses helpers and photos from build_mandarin.py. Brand is "Patio", no accent.
No em or en dashes.
"""
import base64, io, os, urllib.parse
import qrcode
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Mandarin", "taster")
os.makedirs(OUT, exist_ok=True)

PHONE = "+351 928 129 560"
WA_TEXT = "Free Mandarin Taster 12 Oct"
WA_LINK = "https://wa.me/351928129560?text=" + urllib.parse.quote(WA_TEXT)

def make_qr():
    q = qrcode.QRCode(border=2, box_size=12, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(WA_LINK)
    q.make(fit=True)
    img = q.make_image(fill_color="#2B1F18", back_color="white")
    path = os.path.join(OUT, "qr-taster-whatsapp.png")
    img.save(path)
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

COPY = {
    "en": dict(
        eyebrow="Free taster &middot; Mandarin",
        title='Try Mandarin, <span class="a">free</span>.',
        sub="45 minutes with Michelle Kanner.<br>No experience needed.",
        day="Monday 12 October",
        time="18h30 to 19h15",
        seats="Save a seat.<br>Limited places.",
        pill=f"WhatsApp {PHONE}",
        badge="<b>Teacher</b> &middot; Michelle Kanner",
        stamp="Free", stamp_small="Taster class",
    ),
    "pt": dict(
        eyebrow="Aula grátis &middot; Mandarim",
        title='Experimente o mandarim, <span class="a">grátis</span>.',
        sub="45 minutos com Michelle Kanner.<br>Não precisa de experiência.",
        day="Segunda, 12 de outubro",
        time="18h30 às 19h15",
        seats="Reserve já.<br>Lugares limitados.",
        pill=f"WhatsApp {PHONE}",
        badge="<b>Professora</b> &middot; Michelle Kanner",
        stamp="Grátis", stamp_small="Aula<br>experimental",
    ),
}

def write(fname, html):
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path

def render_png(path, w, h):
    import subprocess
    png = path.replace(".html", ".png")
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=6000", f"--screenshot={png}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", os.path.basename(png))

def render_pdf(path, pdfname):
    import subprocess
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=6000", f"--print-to-pdf={os.path.join(OUT, pdfname)}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", pdfname)


# =====================================================================
# SOCIAL  (light card: cream background, framed photo, big FREE stamp)
# =====================================================================
def social(lang, w, h, out):
    c = COPY[lang]
    story = h > 1500
    square = w == h
    pad = 64
    photo_h = 580 if story else (300 if square else 500)
    stamp = 300 if story else (210 if square else 260)
    mich = 220 if story else (150 if square else 180)
    h1 = 100 if story else (62 if square else 84)
    sub = 40 if story else (30 if square else 34)
    when = 50 if story else (36 if square else 42)
    gap = 1.4 if story else (0.6 if square else 1)
    top = 110 if story else 36
    html = f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{w}px;height:{h}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.wrap{{position:absolute;left:{pad}px;right:{pad}px;top:{top}px;bottom:{220 if story else 40}px;display:flex;flex-direction:column;}}
.head{{display:flex;justify-content:space-between;align-items:center;height:{90 if square else 110}px;}}
.head .logo{{height:{80 if square else 96}px;}}
.head .zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:{52 if square else 60}px;color:#2B1F18;}}
.head .zh span{{font-family:'DM Serif Display',serif;font-style:italic;font-weight:400;font-size:{32 if square else 36}px;color:#B8593A;margin-left:12px;}}
.pic{{position:relative;height:{photo_h}px;margin-top:{18 if square else 26}px;flex:none;}}
.pic .ph{{width:100%;height:100%;object-fit:cover;object-position:center 40%;border-radius:28px;display:block;
  box-shadow:0 14px 34px rgba(43,31,24,.18);}}
.stamp{{position:absolute;left:-14px;bottom:-{stamp//3}px;width:{stamp}px;height:{stamp}px;border-radius:50%;
  background:#B8593A;color:#FBF6EE;display:flex;flex-direction:column;align-items:center;justify-content:center;
  transform:rotate(-10deg);box-shadow:0 12px 30px rgba(184,89,58,.45);border:6px solid #FBF6EE;}}
.stamp .big{{font-family:'DM Serif Display',serif;font-size:{stamp*0.27:.0f}px;line-height:1;}}
.stamp .small{{text-align:center;max-width:80%;line-height:1.25;font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:{stamp*0.085:.0f}px;margin-top:6px;color:#F6DCC0;}}
.mich{{position:absolute;right:24px;bottom:-{mich//2}px;display:flex;flex-direction:column;align-items:center;gap:8px;}}
.mich img{{width:{mich}px;height:{mich}px;border-radius:50%;object-fit:cover;border:7px solid #FBF6EE;box-shadow:0 8px 22px rgba(0,0,0,.25);}}
.mich span{{background:#2B1F18;color:#FBF6EE;font-weight:700;font-size:{20 if square else 23}px;padding:6px 16px;border-radius:999px;white-space:nowrap;}}
.mich span b{{color:#E9C58B;}}
.text{{margin-top:{stamp*0.62 if not square else stamp*0.55:.0f}px;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:{24 if square else 28}px;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:{h1}px;line-height:1.02;margin-top:{8*gap:.0f}px;}}
h1 .a{{color:#B8593A;font-style:italic;}}
.sub{{font-size:{sub}px;font-weight:500;color:#4a4038;margin-top:{16*gap:.0f}px;line-height:1.25;}}
.when{{margin-top:{22*gap:.0f}px;background:#fff;border-left:12px solid #C19D5F;border-radius:18px;padding:{14 if square else 20}px 26px;
  box-shadow:0 8px 24px rgba(43,31,24,.08);}}
.when .d{{font-size:{when}px;font-weight:700;line-height:1.15;}}
.when .t{{font-size:{when*0.8:.0f}px;font-weight:700;color:#B8593A;margin-top:4px;}}
.when .t span{{color:#726651;font-weight:600;}}
.foot{{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:20px;}}
.pill{{background:#617C7B;color:#FBF6EE;font-weight:700;font-size:{27 if square else 31}px;padding:{16 if square else 20}px 34px;border-radius:999px;}}
.seats{{color:#B8593A;font-weight:700;font-size:{24 if square else 28}px;text-align:right;}}
</style></head><body>
<div class="bar"></div>
<div class="wrap">
  <div class="head"><img class="logo" src="{bm.LOGO_COLOR}"><div class="zh">你好<span>n&#464; h&#462;o</span></div></div>
  <div class="pic">
    <img class="ph" src="{bm.PHOTO_HK}">
    <div class="stamp"><div class="big">{c['stamp']}</div><div class="small">{c['stamp_small']}</div></div>
    <div class="mich"><img src="{bm.MICHELLE_CHINA}"><span>{c['badge']}</span></div>
  </div>
  <div class="text">
    <div class="eyebrow">{c['eyebrow']}</div>
    <h1>{c['title']}</h1>
    <div class="sub">{c['sub']}</div>
    <div class="when"><div class="d">{c['day']}</div><div class="t">{c['time']} <span>&middot; Patio Language School, Lagos</span></div></div>
  </div>
  <div class="foot"><div class="pill">{c['pill']}</div><div class="seats">{c['seats']}</div></div>
</div>
</body></html>"""
    return write(out, html)


# =====================================================================
# PRINT FLYER  (A5, bilingual, WhatsApp QR)
# =====================================================================
def flyer(qr):
    en, pt = COPY["en"], COPY["pt"]
    html = f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
@page{{size:148mm 210mm;margin:0;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:148mm;height:210mm;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}}
.sheet{{width:148mm;height:210mm;overflow:hidden;display:flex;flex-direction:column;}}
.hero{{position:relative;height:58mm;flex:none;background:#2B1F18;overflow:hidden;}}
.hero .ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}}
.hero .scrim{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(43,31,24,.05) 40%,rgba(43,31,24,.55));}}
.bar{{position:absolute;top:0;left:0;right:0;height:4mm;background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}}
.hero .logo{{position:absolute;top:7mm;left:9mm;height:11mm;z-index:2;filter:drop-shadow(0 .5mm 2mm rgba(0,0,0,.5));}}
.hero .free{{position:absolute;left:9mm;bottom:5mm;z-index:2;}}
.hero .free .tag{{display:inline-block;background:#B8593A;color:#FBF6EE;font-family:'DM Serif Display',serif;font-size:8mm;line-height:1;padding:2mm 5mm 2.4mm;border-radius:2mm;transform:rotate(-4deg);box-shadow:0 1mm 4mm rgba(0,0,0,.35);border:.8mm solid #FBF6EE;}}
.hero .free .zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:11mm;color:#FBF6EE;line-height:1;margin-top:3mm;text-shadow:0 .5mm 3mm rgba(0,0,0,.6);}}
.hero .free .zh span{{font-family:'DM Serif Display',serif;font-style:italic;font-weight:400;font-size:6.5mm;color:#E9C58B;margin-left:3mm;}}
.hero .m{{position:absolute;right:9mm;bottom:7mm;width:30mm;height:30mm;border-radius:50%;object-fit:cover;border:1.4mm solid #FBF6EE;z-index:2;}}
.body{{flex:1;padding:6mm 10mm 6mm;display:flex;flex-direction:column;}}
.cols{{display:flex;gap:6mm;}}
.col{{flex:1;}}
.col .k{{font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:2.5mm;color:#B8593A;}}
.col h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:6.6mm;line-height:1.05;margin-top:1.2mm;}}
.col h1 .a{{color:#B8593A;font-style:italic;}}
.col p{{font-size:3.3mm;color:#4a4038;font-weight:500;line-height:1.35;margin-top:2mm;}}
.when{{margin-top:5mm;background:#fff;border-radius:2.6mm;padding:4mm 5mm;border-left:1.8mm solid #C19D5F;box-shadow:0 3mm 8mm rgba(43,31,24,.07);}}
.when .d{{font-family:'DM Serif Display',serif;font-size:6mm;line-height:1.1;}}
.when .d2{{font-size:3.6mm;font-weight:600;color:#726651;margin-top:.8mm;}}
.when .t{{font-size:4.6mm;font-weight:700;color:#B8593A;margin-top:1.6mm;}}
.limited{{text-align:center;color:#B8593A;font-size:3.4mm;font-weight:700;margin-top:3.5mm;}}
.next{{text-align:center;font-family:'DM Serif Display',serif;font-size:4.6mm;line-height:1.3;margin-top:auto;}}
.next span{{color:#726651;}}
.cta{{margin-top:auto;background:#617C7B;color:#FBF6EE;border-radius:2.6mm;padding:3.4mm 5mm;display:flex;align-items:center;gap:5mm;}}
.cta .l{{flex:1;}}
.cta .h{{font-family:'DM Serif Display',serif;font-size:5.2mm;line-height:1.15;}}
.cta .u{{font-size:4.2mm;font-weight:700;margin-top:1.2mm;}}
.cta .s{{font-size:2.9mm;font-weight:600;color:#EAF0EF;margin-top:1.2mm;}}
.cta .qr{{flex:none;width:24mm;height:24mm;border-radius:1.6mm;background:#fff;padding:1mm;}}
.foot{{margin-top:3mm;display:flex;justify-content:space-between;align-items:flex-end;gap:4mm;}}
.contact{{font-size:2.9mm;line-height:1.6;color:#37302a;font-weight:500;}}
.contact b{{color:#B8593A;}}
.logo2{{height:10mm;}}
</style></head><body><div class="sheet">
<div class="hero">
  <img class="ph" src="{bm.PHOTO_HK}"><div class="scrim"></div><div class="bar"></div>
  <img class="logo" src="{bm.LOGO_WHITE}">
  <div class="free"><div class="tag">Grátis &middot; Free</div>
    <div class="zh">你好<span>n&#464; h&#462;o</span></div></div>
  <img class="m" src="{bm.MICHELLE_CHINA}">
</div>
<div class="body">
  <div class="cols">
    <div class="col"><div class="k">{pt['eyebrow']}</div><h1>{pt['title']}</h1>
      <p>Uma aula experimental de 45 minutos com Michelle Kanner, na Patio Language School. Não precisa de experiência.</p></div>
    <div class="col"><div class="k">{en['eyebrow']}</div><h1>{en['title']}</h1>
      <p>A 45 minute taster class with Michelle Kanner at Patio Language School. No experience needed.</p></div>
  </div>
  <div class="when">
    <div class="d">{pt['day']}</div>
    <div class="d2">{en['day']}</div>
    <div class="t">18h30 às 19h15 &nbsp;&middot;&nbsp; Patio Language School, Lagos</div>
  </div>
  <div class="limited">&rarr; Lugares limitados &middot; Limited seats</div>
  <div class="next">Gostou? O curso começa a 19 de outubro.<br><span>Liked it? The course starts 19 October.</span></div>
  <div class="cta">
    <div class="l">
      <div class="h">Reserve pelo WhatsApp<br>Save a seat on WhatsApp</div>
      <div class="u">{PHONE}</div>
      <div class="s">Leia o código &middot; Scan the code</div>
    </div>
    <img class="qr" src="{qr}">
  </div>
  <div class="foot">
    <div class="contact">patiolanguage.pt &middot; <b>@patiolanguage</b><br>
      Pra&ccedil;a do Poder Local, Lote 14, Loja C, Lagos</div>
    <img class="logo2" src="{bm.LOGO_COLOR}">
  </div>
</div>
</div></body></html>"""
    return write("taster-flyer-a5.html", html)


# =====================================================================
# WHATSAPP  (one bilingual image for chats and groups, reply to book)
# =====================================================================
def whatsapp(w=1080, h=1350, out="taster-whatsapp-1080x1350.html"):
    html = f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{w}px;height:{h}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.wrap{{position:absolute;left:64px;right:64px;top:36px;bottom:40px;display:flex;flex-direction:column;}}
.head{{display:flex;justify-content:space-between;align-items:center;height:100px;}}
.head .logo{{height:88px;}}
.head .zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:56px;}}
.head .zh span{{font-family:'DM Serif Display',serif;font-style:italic;font-weight:400;font-size:34px;color:#B8593A;margin-left:12px;}}
.pic{{position:relative;height:420px;margin-top:20px;flex:none;}}
.pic .ph{{width:100%;height:100%;object-fit:cover;object-position:center 45%;border-radius:28px;display:block;box-shadow:0 14px 34px rgba(43,31,24,.18);}}
.stamp{{position:absolute;left:-14px;bottom:-80px;width:240px;height:240px;border-radius:50%;background:#B8593A;color:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);
  box-shadow:0 12px 30px rgba(184,89,58,.45);border:6px solid #FBF6EE;}}
.stamp .big{{font-family:'DM Serif Display',serif;font-size:58px;line-height:1;}}
.stamp .big2{{font-family:'DM Serif Display',serif;font-style:italic;font-size:42px;line-height:1;color:#F6DCC0;margin-top:4px;}}
.mich{{position:absolute;right:24px;bottom:-80px;display:flex;flex-direction:column;align-items:center;gap:8px;}}
.mich img{{width:165px;height:165px;border-radius:50%;object-fit:cover;border:7px solid #FBF6EE;box-shadow:0 8px 22px rgba(0,0,0,.25);}}
.mich span{{background:#2B1F18;color:#FBF6EE;font-weight:700;font-size:22px;padding:6px 16px;border-radius:999px;}}
.text{{margin-top:150px;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:66px;line-height:1.05;}}
h1 .a{{color:#B8593A;font-style:italic;}}
h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:46px;line-height:1.1;color:#726651;margin-top:6px;}}
h2 .a{{color:#B8593A;font-style:italic;}}
.sub{{font-size:28px;font-weight:500;color:#4a4038;margin-top:14px;line-height:1.3;}}
.when{{margin-top:22px;background:#fff;border-left:12px solid #C19D5F;border-radius:18px;padding:16px 26px;box-shadow:0 8px 24px rgba(43,31,24,.08);}}
.when .d{{font-size:38px;font-weight:700;line-height:1.15;}}
.when .d span{{color:#726651;font-weight:600;font-size:30px;}}
.when .t{{font-size:32px;font-weight:700;color:#B8593A;margin-top:4px;}}
.when .t span{{color:#726651;font-weight:600;}}
.reply{{margin-top:auto;background:#617C7B;color:#FBF6EE;border-radius:22px;padding:20px 30px;display:flex;align-items:center;gap:22px;}}
.reply .ic{{flex:none;width:72px;height:72px;border-radius:50%;background:#FBF6EE;color:#617C7B;display:flex;align-items:center;justify-content:center;font-size:40px;}}
.reply .l1{{font-family:'DM Serif Display',serif;font-size:36px;line-height:1.1;}}
.reply .l2{{font-size:26px;font-weight:600;color:#EAF0EF;margin-top:4px;}}
</style></head><body>
<div class="bar"></div>
<div class="wrap">
  <div class="head"><img class="logo" src="{bm.LOGO_COLOR}"><div class="zh">你好<span>n&#464; h&#462;o</span></div></div>
  <div class="pic">
    <img class="ph" src="{bm.PHOTO_HK}">
    <div class="stamp"><div class="big">Grátis</div><div class="big2">Free</div></div>
    <div class="mich"><img src="{bm.MICHELLE_CHINA}"><span>Michelle Kanner</span></div>
  </div>
  <div class="text">
    <h1>Experimente o mandarim, <span class="a">grátis</span>.</h1>
    <h2>Try Mandarin, <span class="a">free</span>.</h2>
    <div class="sub">45 minutos com Michelle Kanner &middot; 45 minutes with Michelle Kanner<br>Não precisa de experiência &middot; No experience needed.</div>
    <div class="when"><div class="d">Segunda, 12 de outubro <span>&middot; Monday 12 October</span></div>
      <div class="t">18h30 às 19h15 <span>&middot; Patio Language School, Lagos</span></div></div>
  </div>
  <div class="reply"><div class="ic">&#128172;</div><div>
    <div class="l1">Responda para reservar o seu lugar</div>
    <div class="l2">Reply to save your seat &middot; Lugares limitados &middot; Limited places</div></div></div>
</div>
</body></html>"""
    return write(out, html)


if __name__ == "__main__":
    qr = make_qr()
    for lang in ("en", "pt"):
        render_png(social(lang, 1080, 1350, f"taster-{lang}-ig-1080x1350.html"), 1080, 1350)
        render_png(social(lang, 1080, 1920, f"taster-{lang}-story-1080x1920.html"), 1080, 1920)
        render_png(social(lang, 1080, 1080, f"taster-{lang}-fb-1080x1080.html"), 1080, 1080)
    render_png(whatsapp(), 1080, 1350)
    render_pdf(flyer(qr), "Patio-Mandarin-Taster-Flyer.pdf")
    print("WhatsApp link:", WA_LINK)
