#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build 'AI Made Practical' kick-off workshop marketing set for Patio.

Photo-led, minimal-copy version: hero photo of the Patio space, prominent white
logo up top, big headline, and only the essentials (date, time, price, contact).

Launch workshop of the Patio Practical AI Series (see AI-with-Arek proposal).
Wednesday 23 September 2026, 19h00 to 21h00, EUR 20 (rolls into a course).

Outputs (social/):
  ai-workshop-flyer-a5.html  -> Patio-AI-Workshop-Flyer.pdf  (print, A5 portrait)
  ai-workshop-ig-1080x1350.png    (Instagram portrait)
  ai-workshop-fb-1080x1080.png    (Facebook square)
  ai-workshop-story-1080x1920.png (Instagram / WhatsApp story)

House style: DM Serif Display headings + Barlow body; Praia gold #C19D5F,
Terracota #B8593A, Mar teal #617C7B, Chocolate #2B1F18, cream #FBF6EE.
Brand: name is always "Patio" (no accent). NO em/en dashes (use "to" for ranges).
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
    """Load, fix EXIF rotation, re-encode as JPEG data URI."""
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=86)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

LOGO_WHITE = b64_png(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
LOGO_COLOR = b64_png(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
# Hero photo: Pexels (Matheus Bertelli), free commercial license, no attribution
# required. pexels.com/photo/18999469 . People working on laptops in a workshop.
PHOTO = b64_photo(os.path.join(IMG, "ai-workshop-photo.jpg"))

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
# SOCIAL: full-bleed photo hero + bottom scrim (chocolate)
# =====================================================================
def social(fname, W, H, logo_h, title_fs, sub_fs, fact_fs, contact_fs,
           pad_bottom, obj_pos="center 32%"):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{obj_pos};}}
.scrim{{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.74) 0%, rgba(43,31,24,.30) 24%, rgba(43,31,24,.34) 46%,
  rgba(43,31,24,.86) 72%, rgba(43,31,24,.97) 100%);}}
.bar{{position:absolute;top:0;left:0;right:0;height:{max(12,int(W*0.014))}px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}}
.head{{position:absolute;top:{int(H*0.055)}px;left:0;right:0;z-index:2;
  display:flex;flex-direction:column;align-items:center;gap:{int(logo_h*0.34)}px;}}
.logo{{height:{logo_h}px;object-fit:contain;filter:drop-shadow(0 2px 12px rgba(0,0,0,.45));}}
.eyebrow{{color:#E9C58C;font-weight:700;letter-spacing:.24em;text-transform:uppercase;
  font-size:{fact_fs}px;text-shadow:0 1px 8px rgba(0,0,0,.6);}}
.wrap{{position:absolute;left:0;right:0;bottom:0;z-index:2;
  padding:0 {int(W*0.08)}px {pad_bottom}px;text-align:center;}}
.title{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:{title_fs}px;line-height:.96;
  text-shadow:0 2px 18px rgba(0,0,0,.65);}}
.title .a{{color:#E9C58C;font-style:italic;}}
.sub{{color:#F3E7D3;font-size:{sub_fs}px;font-weight:500;line-height:1.36;margin-top:{int(sub_fs*0.7)}px;
  text-shadow:0 1px 10px rgba(0,0,0,.6);}}
.facts{{display:inline-flex;align-items:center;gap:{int(fact_fs*0.9)}px;margin-top:{int(sub_fs*1.0)}px;
  color:#FBF6EE;font-family:'DM Serif Display',serif;font-size:{int(fact_fs*1.5)}px;
  text-shadow:0 1px 10px rgba(0,0,0,.6);}}
.facts .d{{color:#E9C58C;font-family:'Barlow';font-weight:700;}}
.note{{color:#E9C58C;font-size:{fact_fs}px;font-weight:600;margin-top:{int(fact_fs*0.9)}px;
  letter-spacing:.01em;text-shadow:0 1px 8px rgba(0,0,0,.6);}}
.contact{{color:#EBDCC4;font-size:{contact_fs}px;font-weight:600;line-height:1.5;
  margin-top:{int(fact_fs*1.4)}px;text-shadow:0 1px 8px rgba(0,0,0,.6);}}
.contact b{{color:#FBF6EE;font-weight:700;}}
"""
    body = f"""<div class="canvas">
<img class="bg" src="{PHOTO}"><div class="scrim"></div>
<div class="bar"></div>
<div class="head">
  <img class="logo" src="{LOGO_WHITE}">
  <div class="eyebrow">Practical AI &middot; Kick-off Workshop</div>
</div>
<div class="wrap">
  <div class="title">AI Made <span class="a">Practical</span></div>
  <div class="sub">A friendly, hands-on intro to what AI<br>can really do. No tech background needed.</div>
  <div class="facts">Wed 23 Sep <span class="d">&middot;</span> 19h to 21h <span class="d">&middot;</span> &euro;20</div>
  <div class="note">Your &euro;20 rolls into any Patio AI course.</div>
  <div class="contact"><b>patiolanguage.pt</b> &middot; <b>@patiolanguage</b><br>WhatsApp +351 928 129 560</div>
</div>
</div>"""
    return write(fname, page(css, body)), W, H


# =====================================================================
# PRINT FLYER  (A5 portrait): photo band on top, trimmed copy below
# =====================================================================
def flyer():
    css = """
@page{size:148mm 210mm;margin:0;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:148mm;height:210mm;}
body{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}
.sheet{position:relative;width:148mm;height:210mm;overflow:hidden;display:flex;flex-direction:column;}
.hero{position:relative;height:96mm;overflow:hidden;background:#2B1F18;}
.hero img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 42%;}
.hero .scrim{position:absolute;inset:0;background:linear-gradient(180deg,
  rgba(43,31,24,.72) 0%, rgba(43,31,24,.52) 20%, rgba(43,31,24,.20) 44%,
  rgba(43,31,24,.34) 66%, rgba(43,31,24,.93) 100%);}
.bar{position:absolute;top:0;left:0;right:0;height:4mm;
  background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}
.hero .top{position:absolute;top:10mm;left:0;right:0;z-index:2;
  display:flex;flex-direction:column;align-items:center;gap:3mm;}
.hero .logo{height:16mm;object-fit:contain;filter:drop-shadow(0 1mm 3mm rgba(0,0,0,.5));}
.hero .eyebrow{color:#F0D4A6;font-weight:700;letter-spacing:.24em;text-transform:uppercase;
  font-size:2.9mm;text-shadow:0 1px 3px rgba(0,0,0,.9),0 0 12px rgba(0,0,0,.7);}
.hero .title{position:absolute;left:0;right:0;bottom:7mm;z-index:2;text-align:center;
  font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:16mm;line-height:.98;
  text-shadow:0 1mm 5mm rgba(0,0,0,.6);}
.hero .title .a{color:#E9C58C;font-style:italic;}
.body{flex:1;padding:8mm 13mm 8mm;display:flex;flex-direction:column;text-align:center;}
.sub{color:#4a4038;font-size:4.4mm;font-weight:500;line-height:1.4;}
.facts{display:flex;justify-content:center;gap:6mm;margin-top:6mm;padding:5mm 0;
  border-top:.4mm solid #2B1F18;border-bottom:.3mm solid #D8C9B3;}
.facts .m{}
.facts .k{color:#726651;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:2.4mm;}
.facts .v{font-family:'DM Serif Display',serif;font-size:5mm;line-height:1.1;margin-top:1.4mm;}
.covers{margin-top:6mm;color:#37302a;font-size:3.7mm;font-weight:600;line-height:1.5;}
.covers b{color:#B8593A;}
.credit{margin-top:auto;background:#617C7B;color:#FBF6EE;border-radius:3mm;padding:4mm 5mm;
  display:flex;align-items:center;gap:4mm;text-align:left;}
.credit .p{font-family:'DM Serif Display',serif;font-size:11mm;line-height:1;color:#F4E7CF;flex:none;}
.credit .t{font-size:3.7mm;font-weight:500;line-height:1.3;}
.foot{margin-top:5mm;padding-top:3.5mm;border-top:.3mm solid #D8C9B3;
  display:flex;justify-content:space-between;align-items:flex-end;gap:4mm;text-align:left;}
.contact{font-size:3.1mm;line-height:1.65;color:#37302a;font-weight:500;}
.contact b{color:#B8593A;font-weight:700;}
.logo2{height:13mm;object-fit:contain;flex:none;}
"""
    body = f"""<div class="sheet">
<div class="hero">
  <img class="bg" src="{PHOTO}"><div class="scrim"></div>
  <div class="bar"></div>
  <div class="top">
    <img class="logo" src="{LOGO_WHITE}">
    <div class="eyebrow">Practical AI &middot; Kick-off Workshop</div>
  </div>
  <div class="title">AI Made <span class="a">Practical</span></div>
</div>
<div class="body">
  <div class="sub">A friendly, hands-on evening on what AI can really do for your
  everyday life and work. No technical background needed, just bring your laptop or phone.</div>
  <div class="facts">
    <div class="m"><div class="k">When</div><div class="v">Wed 23 Sep<br>19h to 21h</div></div>
    <div class="m"><div class="k">Where</div><div class="v">Patio<br>Lagos</div></div>
    <div class="m"><div class="k">Ticket</div><div class="v">&euro;20</div></div>
    <div class="m"><div class="k">Group</div><div class="v">Up to 12</div></div>
  </div>
  <div class="covers">Try AI for <b>email, research, documents, images</b> and more.</div>
  <div class="credit">
    <div class="p">&euro;20</div>
    <div class="t">Your &euro;20 ticket rolls into any four-week Patio AI course if you enrol within seven days.</div>
  </div>
  <div class="foot">
    <div class="contact">
      <b>patiolanguage.pt</b> &middot; patiolanguage@gmail.com<br>
      WhatsApp <b>+351 928 129 560</b> &middot; <b>@patiolanguage</b><br>
      Pra&ccedil;a do Poder Local, Lote 14, Loja C, Lagos
    </div>
    <img class="logo2" src="{LOGO_COLOR}">
  </div>
</div>
</div>"""
    return write("ai-workshop-flyer-a5.html", page(css, body))


if __name__ == "__main__":
    render_pdf(flyer(), "Patio-AI-Workshop-Flyer.pdf")

    fn, w, h = social("ai-workshop-ig-1080x1350.html", 1080, 1350,
        logo_h=118, title_fs=104, sub_fs=33, fact_fs=27, contact_fs=25,
        pad_bottom=90, obj_pos="center 42%")
    render_png(fn, w, h)

    fn, w, h = social("ai-workshop-fb-1080x1080.html", 1080, 1080,
        logo_h=104, title_fs=92, sub_fs=30, fact_fs=25, contact_fs=24,
        pad_bottom=74, obj_pos="center 46%")
    render_png(fn, w, h)

    fn, w, h = social("ai-workshop-story-1080x1920.html", 1080, 1920,
        logo_h=132, title_fs=118, sub_fs=37, fact_fs=31, contact_fs=29,
        pad_bottom=210, obj_pos="center 44%")
    render_png(fn, w, h)
    print("done")
