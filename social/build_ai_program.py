#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build the full 'Practical AI at Patio' PROGRAM set (IG + flyer + FB).

Promotes the whole program: the Happy Hour kick-off + two project-based
workshops (AI for Business, AI Made Simple), led by Claire's message.

Layout: photo branding band (logo + eyebrow) up top, then the message as a
big headline on cream, then the three offerings and the register CTA.

Facts (confirmed by Claire 2026-09-17):
  Kick-off: "AI Made Practical" Happy Hour, Wed 7 Oct,
            17h00 to 19h30, EUR 20 (credited to a workshop if booked within 7 days).
  AI for Business: Wednesdays Oct 14, 21, 28 & Nov 4, 18h00 to 20h00, EUR 249.
  AI Made Simple:  Fridays  Oct 16, 23, 30 & Nov 6, 15h00 to 17h00, EUR 149.
  All: four weekly two-hour sessions, small groups, bring your own device.
  CTA: register interest at patiolanguage.pt/ai + WhatsApp/email.
  Message: "Learn AI in a way that actually helps you live, work and feel
            confident in Portugal."

Outputs (social/):
  ai-program-flyer-a5.html -> Patio-AI-Program-Flyer.pdf  (print, A5 portrait)
  ai-program-ig-1080x1350.png    (Instagram portrait)
  ai-program-fb-1080x1080.png    (Facebook square)

House style: DM Serif Display + Barlow; gold #C19D5F, terracota #B8593A,
teal #617C7B, chocolate #2B1F18, galao #726651, cream #FBF6EE.
Brand: name is always "Patio" (no accent). NO em/en dashes (use "to", commas, &).
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
QR = b64_png(os.path.join(IMG, "qr-ai-register.png"))  # -> forms.gle register form
# Split banner: two of Claire's own Patio room photos, side by side.
PHOTO_A = b64_photo(os.path.join(IMG, "ai-room-photo.jpg"))  # long room pic vertical
PHOTO_B = b64_photo(os.path.join(IMG, "ai-lagos.jpg"))       # Praia Dona Ana, Lagos coast

# The message headline (accent phrase set in terracotta italic).
MSG = 'Project-based AI you can <span class="a">use right away</span>.'
# Supporting promise + scarcity line.
SUB = ('Hands-on and practical, so you leave with '
       '<b>confidence, clarity and time back</b>.<br>No tech background needed.')
LIMITED = 'Limited Spots, Reserve Yours Now'

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def write(fname, html):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

def render_png(fname, w, h):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--default-background-color=00000000",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

def render_pdf(fname, pdfname):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        f"--print-to-pdf={os.path.join(SOCIAL, pdfname)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", pdfname)


# =====================================================================
# PRINT FLYER  (A5 portrait)
# =====================================================================
def flyer(show_prices=True, out="ai-program-flyer-a5.html"):
    price_biz = '<div class="price">&euro;249</div>' if show_prices else ''
    price_simple = '<div class="price">&euro;149</div>' if show_prices else ''
    happy_note = ('Your &euro;20 counts toward any workshop you book within 7 days.'
                  if show_prices else 'Fully credited toward any workshop you book within 7 days.')
    happy_price = ('<div class="price"><div class="p">&euro;20</div><div class="s">ticket</div></div>'
                   if show_prices else '')
    css = """
@page{size:148mm 210mm;margin:0;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:148mm;height:210mm;}
body{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}
.sheet{position:relative;width:148mm;height:210mm;overflow:hidden;display:flex;flex-direction:column;}
.hero{position:relative;height:32mm;overflow:hidden;background:#2B1F18;flex:none;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2.4mm;}
.halves{position:absolute;inset:0;display:flex;}
.halves img{width:50%;height:100%;object-fit:cover;}
.halves img:first-child{object-position:center 54%;}
.halves img:last-child{object-position:center 42%;}
.seam{position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);width:.6mm;
  background:rgba(251,246,238,.85);z-index:2;}
.hero .scrim{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.62) 0%, rgba(43,31,24,.52) 55%, rgba(43,31,24,.72) 100%);}
.bar{position:absolute;top:0;left:0;right:0;height:4mm;background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}
.hero .logo{height:13mm;object-fit:contain;position:relative;z-index:2;filter:drop-shadow(0 1mm 3mm rgba(0,0,0,.55));}
.hero .eyebrow{position:relative;z-index:2;color:#F0D4A6;font-weight:700;letter-spacing:.24em;
  text-transform:uppercase;font-size:2.8mm;text-shadow:0 1px 3px rgba(0,0,0,.9);}
.body{flex:1;padding:6mm 11mm 7mm;display:flex;flex-direction:column;}
.title{font-family:'DM Serif Display',serif;font-size:8.6mm;line-height:1.06;text-align:center;color:#2B1F18;}
.title .a{color:#B8593A;font-style:italic;}
.sub{text-align:center;color:#4a4038;font-size:3.5mm;font-weight:500;line-height:1.32;margin-top:3.5mm;}
.sub b{color:#B8593A;font-weight:700;}
.happy{margin-top:3.6mm;background:#2B1F18;color:#FBF6EE;border-radius:2.6mm;padding:4mm 5mm;
  display:flex;align-items:center;gap:4mm;border-left:2.4mm solid #C19D5F;}
.happy .l{flex:1;}
.happy .tag{color:#E9C58C;font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:2.4mm;}
.happy .t{font-family:'DM Serif Display',serif;font-size:5mm;line-height:1.05;margin-top:1mm;}
.happy .m{font-size:3.1mm;font-weight:600;color:#EBDCC4;margin-top:1.4mm;}
.happy .m b{color:#FBF6EE;}
.happy .note{font-size:2.7mm;color:#C9BCA9;margin-top:1.2mm;line-height:1.3;}
.happy .price{flex:none;text-align:center;}
.happy .price .p{font-family:'DM Serif Display',serif;font-size:9mm;line-height:1;color:#E9C58C;}
.happy .price .s{font-size:2.5mm;color:#C9BCA9;font-weight:600;}
.cards{display:flex;gap:4mm;margin-top:3.2mm;}
.card{flex:1;background:#fff;border-radius:2.6mm;padding:3.8mm 4mm;box-shadow:0 3mm 8mm rgba(43,31,24,.07);
  border-top:1.8mm solid #617C7B;display:flex;flex-direction:column;}
.card.s{border-top-color:#B8593A;}
.card .tag{font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:2.2mm;color:#4f6a69;}
.card.s .tag{color:#B8593A;}
.card .t{font-family:'DM Serif Display',serif;font-size:5mm;line-height:1.02;margin-top:1mm;color:#2B1F18;}
.card .when{font-size:2.9mm;font-weight:700;color:#2B1F18;margin-top:2mm;line-height:1.25;}
.card .when span{color:#726651;font-weight:600;}
.card .price{font-family:'DM Serif Display',serif;font-size:5.4mm;color:#4f6a69;margin-top:1.4mm;}
.card.s .price{color:#B8593A;}
.card .d{font-size:2.85mm;color:#4a4038;font-weight:500;line-height:1.3;margin-top:2mm;}
.common{text-align:center;color:#726651;font-size:2.9mm;font-weight:600;margin-top:3.2mm;}
.limited{text-align:center;color:#B8593A;font-size:3.2mm;font-weight:700;margin-top:1.6mm;letter-spacing:.01em;}
.cta{margin-top:auto;background:#617C7B;color:#FBF6EE;border-radius:2.6mm;padding:2.8mm 5mm;
  display:flex;align-items:center;gap:5mm;text-align:left;}
.cta .l{flex:1;}
.cta .h{font-family:'DM Serif Display',serif;font-size:5.2mm;}
.cta .u{font-size:3.4mm;font-weight:700;margin-top:.8mm;color:#FBF6EE;letter-spacing:.02em;}
.cta .scan{font-size:2.8mm;font-weight:600;color:#EAF0EF;margin-top:1.4mm;}
.cta .qr{flex:none;width:19mm;height:19mm;object-fit:contain;border-radius:1.6mm;}
.foot{margin-top:2.6mm;display:flex;justify-content:space-between;align-items:flex-end;gap:4mm;}
.contact{font-size:2.95mm;line-height:1.6;color:#37302a;font-weight:500;}
.contact b{color:#B8593A;font-weight:700;}
.logo2{height:11mm;object-fit:contain;flex:none;}
"""
    body = f"""<div class="sheet">
<div class="hero">
  <div class="halves"><img src="{PHOTO_A}"><img src="{PHOTO_B}"></div>
  <div class="seam"></div><div class="scrim"></div>
  <div class="bar"></div>
  <img class="logo" src="{LOGO_WHITE}">
  <div class="eyebrow">Patio Practical AI &middot; Lagos</div>
</div>
<div class="body">
  <div class="title">{MSG}</div>
  <div class="sub">{SUB}</div>

  <div class="happy">
    <div class="l">
      <div class="tag">Start here &middot; Happy Hour</div>
      <div class="t">AI Made Practical</div>
      <div class="m"><b>Wed 7 Oct</b> &middot; 17h00 to 19h30 &middot; Patio, Lagos</div>
      <div class="note">{happy_note}</div>
    </div>
    {happy_price}
  </div>

  <div class="cards">
    <div class="card">
      <div class="tag">Project-based workshop</div>
      <div class="t">AI for Business</div>
      <div class="when">Wednesdays<br><span>Oct 14, 21, 28 &amp; Nov 4 &middot; 18h00 to 20h00</span></div>
      {price_biz}
      <div class="d">Apply it to your own business. Leave with one workflow ready to use,
      three prioritised AI opportunities and a 30 day action plan.</div>
    </div>
    <div class="card s">
      <div class="tag">Project-based workshop</div>
      <div class="t">AI Made Simple</div>
      <div class="when">Fridays<br><span>Oct 16, 23, 30 &amp; Nov 6 &middot; 15h00 to 17h00</span></div>
      {price_simple}
      <div class="d">Work on tasks from your own life. From curious to confident in 30 days,
      with guidance at your shoulder.</div>
    </div>
  </div>
  <div class="common">Four weekly two-hour sessions &middot; Bring your own device</div>
  <div class="limited">&rarr; {LIMITED}</div>

  <div class="cta">
    <div class="l">
      <div class="h">Register now</div>
      <div class="u">patiolanguage.pt/ai</div>
      <div class="scan">or scan the code to sign up</div>
    </div>
    <img class="qr" src="{QR}">
  </div>
  <div class="foot">
    <div class="contact">
      WhatsApp <b>+351 928 129 560</b> &middot; patiolanguage@gmail.com<br>
      <b>@patiolanguage</b> &middot; Pra&ccedil;a do Poder Local, Lote 14, Loja C, Lagos
    </div>
    <img class="logo2" src="{LOGO_COLOR}">
  </div>
</div>
</div>"""
    return write(out, page(css, body))


# =====================================================================
# SOCIAL  (photo branding band + cream body: headline, rows, cta)
# =====================================================================
def social(fname, W, H, hero_h, title_fs, sub_fs, row_t_fs, row_m_fs, price_fs, cta_fs, obj_pos,
           contact_line=True):
    def row(tag, tagcol, title, when, price, accent, note=""):
        note_html = f'<div class="rnote">{note}</div>' if note else ''
        return (f'<div class="row" style="border-left-color:{accent}">'
            f'<div class="rl"><div class="rtag" style="color:{tagcol}">{tag}</div>'
            f'<div class="rt">{title}</div><div class="rm">{when}</div>{note_html}</div>'
            f'<div class="rp" style="color:{accent}">{price}</div></div>')
    rows = (
        row("Happy Hour &middot; start here", "#a97e2f", "AI Made Practical",
            "Wed 7 Oct &middot; 17h00 to 19h30", "&euro;20", "#C19D5F",
            note="Your &euro;20 counts toward any workshop.")
        + row("Wednesdays &middot; project workshop", "#4f6a69", "AI for Business",
            "Oct 14, 21, 28 &amp; Nov 4 &middot; 18h00 to 20h00", "&euro;249", "#617C7B")
        + row("Fridays &middot; project workshop", "#B8593A", "AI Made Simple",
            "Oct 16, 23, 30 &amp; Nov 6 &middot; 15h00 to 17h00", "&euro;149", "#B8593A")
    )
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;display:flex;flex-direction:column;}}
.hero{{position:relative;height:{hero_h}px;overflow:hidden;background:#2B1F18;flex:none;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:{int(W*0.016)}px;}}
.halves{{position:absolute;inset:0;display:flex;}}
.halves img{{width:50%;height:100%;object-fit:cover;}}
.halves img:first-child{{object-position:{obj_pos};}}
.halves img:last-child{{object-position:center 42%;}}
.seam{{position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);
  width:{max(2,int(W*0.003))}px;background:rgba(251,246,238,.85);z-index:2;}}
.hero .scrim{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.60) 0%, rgba(43,31,24,.50) 55%, rgba(43,31,24,.72) 100%);}}
.bar{{position:absolute;top:0;left:0;right:0;height:{max(12,int(W*0.014))}px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}}
.hero .logo{{height:{int(W*0.092)}px;object-fit:contain;position:relative;z-index:2;
  filter:drop-shadow(0 2px 12px rgba(0,0,0,.5));}}
.hero .eyebrow{{position:relative;z-index:2;color:#F0D4A6;font-weight:700;letter-spacing:.22em;
  text-transform:uppercase;font-size:{cta_fs}px;text-shadow:0 1px 3px rgba(0,0,0,.9);}}
.body{{flex:1;padding:{int(W*0.04)}px {int(W*0.065)}px {int(W*0.028)}px;display:flex;flex-direction:column;}}
.title{{font-family:'DM Serif Display',serif;font-size:{title_fs}px;line-height:1.07;text-align:center;color:#2B1F18;}}
.title .a{{color:#B8593A;font-style:italic;}}
.sub{{text-align:center;color:#4a4038;font-size:{sub_fs}px;font-weight:500;line-height:1.32;
  margin-top:{int(W*0.025)}px;}}
.sub b{{color:#B8593A;font-weight:700;}}
.rows{{margin-top:{int(W*0.03)}px;display:flex;flex-direction:column;gap:{int(W*0.018)}px;}}
.row{{background:#fff;border-radius:{int(W*0.018)}px;border-left:{int(W*0.009)}px solid #C19D5F;
  padding:{int(W*0.024)}px {int(W*0.035)}px;box-shadow:0 8px 20px rgba(43,31,24,.07);
  display:flex;align-items:center;gap:{int(W*0.03)}px;}}
.rl{{flex:1;}}
.rtag{{font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:{int(row_m_fs*0.82)}px;}}
.rt{{font-family:'DM Serif Display',serif;font-size:{row_t_fs}px;line-height:1.0;margin-top:{int(W*0.006)}px;color:#2B1F18;}}
.rm{{font-size:{row_m_fs}px;font-weight:600;color:#5a5047;margin-top:{int(W*0.006)}px;}}
.rnote{{font-size:{int(row_m_fs*0.88)}px;font-weight:700;color:#B8593A;margin-top:{int(W*0.006)}px;}}
.rp{{flex:none;font-family:'DM Serif Display',serif;font-size:{price_fs}px;line-height:1;}}
.common{{text-align:center;color:#726651;font-size:{cta_fs}px;font-weight:600;margin-top:{int(W*0.02)}px;}}
.limited{{text-align:center;color:#B8593A;font-size:{int(cta_fs*1.1)}px;font-weight:700;margin-top:{int(W*0.01)}px;}}
.cta{{margin-top:auto;background:#617C7B;color:#FBF6EE;border-radius:{int(W*0.018)}px;
  padding:{int(W*0.024)}px {int(W*0.04)}px;text-align:center;}}
.cta .h{{font-family:'DM Serif Display',serif;font-size:{int(cta_fs*1.5)}px;line-height:1.05;}}
.cta .u{{font-size:{int(cta_fs*1.15)}px;font-weight:700;margin-top:{int(W*0.006)}px;}}
.contact{{text-align:center;font-size:{cta_fs}px;font-weight:600;color:#37302a;margin-top:{int(W*0.016)}px;line-height:1.4;}}
.contact b{{color:#B8593A;font-weight:700;}}
"""
    body = f"""<div class="canvas">
<div class="hero">
  <div class="halves"><img src="{PHOTO_A}"><img src="{PHOTO_B}"></div>
  <div class="seam"></div><div class="scrim"></div>
  <div class="bar"></div>
  <img class="logo" src="{LOGO_WHITE}">
  <div class="eyebrow">Patio Practical AI &middot; Lagos</div>
</div>
<div class="body">
  <div class="title">{MSG}</div>
  <div class="sub">{SUB}</div>
  <div class="rows">{rows}</div>
  <div class="common">Four weekly two-hour sessions &middot; Bring your own device</div>
  <div class="limited">&rarr; {LIMITED}</div>
  <div class="cta">
    <div class="h">Register now</div>
    <div class="u">patiolanguage.pt/ai &middot; WhatsApp +351 928 129 560</div>
  </div>
  {'<div class="contact"><b>@patiolanguage</b> &middot; patiolanguage@gmail.com</div>' if contact_line else ''}
</div>
</div>"""
    return write(fname, page(css, body)), W, H


# =====================================================================
# INSTAGRAM STORY  (1080 x 1920, safe margins for the IG interface)
# =====================================================================
def story(fname="ai-program-story-1080x1920.html"):
    W, H = 1080, 1920
    def row(tag, tagcol, title, when, price, accent):
        return (f'<div class="row" style="border-left-color:{accent}">'
            f'<div class="rl"><div class="rtag" style="color:{tagcol}">{tag}</div>'
            f'<div class="rt">{title}</div><div class="rm">{when}</div></div>'
            f'<div class="rp" style="color:{accent}">{price}</div></div>')
    rows = (
        row("Happy Hour &middot; start here", "#a97e2f", "AI Made Practical",
            "Wed 7 Oct &middot; 17h00 to 19h30", "&euro;20", "#C19D5F")
        + row("Wednesdays &middot; project workshop", "#4f6a69", "AI for Business",
            "Oct 14, 21, 28 &amp; Nov 4 &middot; 18h00 to 20h00", "&euro;249", "#617C7B")
        + row("Fridays &middot; project workshop", "#B8593A", "AI Made Simple",
            "Oct 16, 23, 30 &amp; Nov 6 &middot; 15h00 to 17h00", "&euro;149", "#B8593A")
    )
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;display:flex;flex-direction:column;}}
.hero{{position:relative;height:560px;overflow:hidden;background:#2B1F18;flex:none;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;padding-top:80px;}}
.halves{{position:absolute;inset:0;display:flex;}}
.halves img{{width:50%;height:100%;object-fit:cover;}}
.halves img:first-child{{object-position:center 54%;}}
.halves img:last-child{{object-position:center 42%;}}
.seam{{position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);width:3px;
  background:rgba(251,246,238,.85);z-index:2;}}
.scrim{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.66) 0%, rgba(43,31,24,.48) 55%, rgba(43,31,24,.74) 100%);}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}}
.hero .logo{{height:104px;object-fit:contain;position:relative;z-index:2;filter:drop-shadow(0 2px 12px rgba(0,0,0,.5));}}
.hero .eyebrow{{position:relative;z-index:2;color:#F0D4A6;font-weight:700;letter-spacing:.24em;
  text-transform:uppercase;font-size:28px;text-shadow:0 1px 3px rgba(0,0,0,.9);}}
.body{{flex:1;padding:52px 84px 190px;display:flex;flex-direction:column;}}
.title{{font-family:'DM Serif Display',serif;font-size:70px;line-height:1.05;text-align:center;color:#2B1F18;}}
.title .a{{color:#B8593A;font-style:italic;}}
.sub{{text-align:center;color:#4a4038;font-size:33px;font-weight:500;line-height:1.34;margin-top:24px;}}
.sub b{{color:#B8593A;font-weight:700;}}
.rows{{margin-top:40px;display:flex;flex-direction:column;gap:22px;}}
.row{{background:#fff;border-radius:22px;border-left:11px solid #C19D5F;padding:30px 38px;
  box-shadow:0 8px 22px rgba(43,31,24,.08);display:flex;align-items:center;gap:30px;}}
.rl{{flex:1;}}
.rtag{{font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:23px;}}
.rt{{font-family:'DM Serif Display',serif;font-size:50px;line-height:1.0;margin-top:8px;color:#2B1F18;}}
.rm{{font-size:29px;font-weight:600;color:#5a5047;margin-top:8px;}}
.rp{{flex:none;font-family:'DM Serif Display',serif;font-size:64px;line-height:1;}}
.limited{{text-align:center;color:#B8593A;font-size:34px;font-weight:700;margin-top:34px;}}
.cta{{margin-top:auto;background:#617C7B;color:#FBF6EE;border-radius:22px;padding:34px 40px;text-align:center;}}
.cta .h{{font-family:'DM Serif Display',serif;font-size:52px;line-height:1.04;}}
.cta .u{{font-size:31px;font-weight:700;margin-top:10px;}}
.cta .hint{{font-size:27px;font-weight:600;color:#EAF0EF;margin-top:12px;}}
"""
    body = f"""<div class="canvas">
<div class="hero">
  <div class="halves"><img src="{PHOTO_A}"><img src="{PHOTO_B}"></div>
  <div class="seam"></div><div class="scrim"></div><div class="bar"></div>
  <img class="logo" src="{LOGO_WHITE}">
  <div class="eyebrow">Patio Practical AI &middot; Lagos</div>
</div>
<div class="body">
  <div class="title">{MSG}</div>
  <div class="sub">{SUB}</div>
  <div class="rows">{rows}</div>
  <div class="limited">&rarr; {LIMITED}</div>
  <div class="cta">
    <div class="h">Register now</div>
    <div class="u">patiolanguage.pt/ai</div>
    <div class="hint">Tap the link to sign up</div>
  </div>
</div>
</div>"""
    return write(fname, page(css, body)), W, H


if __name__ == "__main__":
    render_pdf(flyer(), "Patio-AI-Program-Flyer.pdf")
    render_pdf(flyer(show_prices=False, out="ai-program-flyer-a5-noprices.html"),
               "Patio-AI-Program-Flyer-no-prices.pdf")

    fn, w, h = social("ai-program-ig-1080x1350.html", 1080, 1350, hero_h=300,
        title_fs=53, sub_fs=27, row_t_fs=42, row_m_fs=25, price_fs=52, cta_fs=23, obj_pos="center 54%")
    render_png(fn, w, h)

    fn, w, h = social("ai-program-fb-1080x1080.html", 1080, 1080, hero_h=162,
        title_fs=42, sub_fs=24, row_t_fs=37, row_m_fs=22, price_fs=45, cta_fs=22, obj_pos="center 54%",
        contact_line=False)
    render_png(fn, w, h)

    fn, w, h = story()
    render_png(fn, w, h)
    print("done")
