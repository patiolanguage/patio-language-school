#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bright A5 flyer for the Patio AI workshops, styled like the program flyer.

Arek is the hero at the top (big photo + short bio). Then the Happy Hour band,
two workshop cards, and a teal register band with the QR.
Brand: DM Serif Display + Barlow. No em/en dashes.
Outputs a print-ready A5 PDF and a shareable PNG.
"""
import base64, os, subprocess
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

W, H = 1488, 2111  # A5 portrait, ~255 dpi

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
AREK = b64(os.path.join(IMG, "arek.png"))
QR = b64(os.path.join(IMG, "qr-ai-register.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

URL = "patiolanguage.pt/ai"

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.f{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Barlow',sans-serif;
  background:#FBF6EE;color:#2B1F18;display:flex;flex-direction:column;padding:0 78px 40px;}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
/* header */
.top{{display:flex;align-items:center;justify-content:center;gap:26px;padding-top:44px;}}
.top img{{height:78px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.2em;text-transform:uppercase;font-size:29px;}}
/* hero: Arek */
.hero{{display:flex;align-items:center;gap:52px;margin-top:24px;
  background:#FFF9F0;border:3px solid #F0E2CC;border-radius:30px;padding:36px 48px;}}
.ring{{width:400px;height:400px;flex:none;border-radius:50%;
  background:linear-gradient(135deg,#C19D5F,#B8593A);padding:11px;box-shadow:0 16px 40px rgba(43,31,24,.20);}}
.ring img{{width:100%;height:100%;border-radius:50%;display:block;background:#2B1F18;}}
.htxt{{flex:1;}}
.heye{{color:#B8593A;font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:31px;}}
.hname{{font-family:'DM Serif Display',serif;font-size:84px;line-height:1;margin-top:6px;}}
.hbio{{font-size:36px;font-weight:500;line-height:1.3;margin-top:14px;color:#4a4038;}}
/* headline */
.headline{{font-family:'DM Serif Display',serif;font-size:66px;line-height:1.04;text-align:center;margin-top:22px;}}
.headline .a{{color:#B8593A;font-style:italic;}}
/* happy hour band */
.hh{{background:#2B1F18;color:#FBF6EE;border-radius:28px;border-left:16px solid #C19D5F;
  padding:32px 46px;display:flex;align-items:center;gap:28px;margin-top:22px;}}
.hh .l{{flex:1;}}
.hh .tag{{color:#C19D5F;font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:29px;}}
.hh .nm{{font-family:'DM Serif Display',serif;font-size:62px;line-height:1;margin-top:6px;}}
.hh .mt{{font-weight:600;font-size:36px;margin-top:12px;color:#Eadfce;}}
.hh .pr{{font-family:'DM Serif Display',serif;color:#C19D5F;font-size:96px;line-height:.9;flex:none;text-align:right;}}
.hh .pr small{{display:block;font-family:'Barlow';font-size:26px;font-weight:600;color:#b7ac99;letter-spacing:.05em;}}
/* two cards */
.two{{display:flex;gap:30px;margin-top:22px;}}
.card{{flex:1;background:#fff;border-radius:26px;border-top:14px solid #617C7B;padding:36px 38px;
  box-shadow:0 14px 34px rgba(43,31,24,.10);}}
.card.b{{border-top-color:#B8593A;}}
.card .tag{{font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:27px;color:#4f6a69;}}
.card.b .tag{{color:#B8593A;}}
.card .nm{{font-family:'DM Serif Display',serif;font-size:60px;line-height:1;margin-top:8px;}}
.card .mt{{font-weight:700;font-size:33px;margin-top:14px;color:#2B1F18;}}
.card .pr{{font-family:'DM Serif Display',serif;font-size:76px;line-height:1;margin-top:14px;color:#617C7B;}}
.card.b .pr{{color:#B8593A;}}
.card .ds{{font-size:33px;font-weight:500;line-height:1.32;margin-top:14px;color:#6a5f52;}}
/* sessions line */
.sess{{text-align:center;margin-top:20px;}}
.sess .a{{color:#5a5047;font-weight:600;font-size:35px;}}
.sess .b{{color:#B8593A;font-weight:700;font-size:40px;margin-top:8px;}}
/* register band */
.reg{{background:linear-gradient(135deg,#5f7c7b,#42605e);color:#FBF6EE;border-radius:28px;
  padding:34px 50px;display:flex;align-items:center;gap:48px;margin-top:20px;}}
.reg .rl{{flex:1;}}
.reg .rt{{font-family:'DM Serif Display',serif;font-size:70px;line-height:1;}}
.reg .ru{{font-size:44px;font-weight:700;margin-top:12px;color:#F0D4A6;}}
.reg .rs{{font-size:32px;font-weight:500;margin-top:8px;color:#EAF1EF;}}
.qr{{width:270px;height:270px;flex:none;background:#fff;border-radius:22px;padding:16px;}}
.qr img{{width:100%;height:100%;display:block;}}
/* contact */
.contact{{display:flex;align-items:flex-end;justify-content:space-between;margin-top:20px;padding:0 6px;}}
.contact .ct{{font-size:31px;font-weight:500;line-height:1.5;color:#2B1F18;}}
.contact .ct b{{color:#B8593A;font-weight:700;}}
.contact img{{height:76px;object-fit:contain;}}
"""

def body_html(show_price=True):
    hh_price = '<div class="pr">&euro;20<small>credited to a course</small></div>' if show_price else ''
    b_price = '<div class="pr">&euro;249</div>' if show_price else ''
    s_price = '<div class="pr">&euro;149</div>' if show_price else ''
    hh_mt = ("Wed 7 Oct &middot; 17h00 to 19h30 &middot; Patio, Lagos" if show_price
             else "Wed 7 Oct &middot; 17h00 to 19h30 &middot; includes a drink, credited to a course")
    return f"""<div class="f"><div class="bar"></div>
  <div class="top"><img src="{LOGO_COLOR}"><span class="eyebrow">Patio Practical AI &middot; Lagos</span></div>

  <div class="hero">
    <div class="ring"><img src="{AREK}"></div>
    <div class="htxt">
      <div class="heye">Meet your host</div>
      <div class="hname">Arek Adeoye</div>
      <div class="hbio">25 years in software, building real-world AI tools. He teaches in plain language, hands-on. He created these workshops after friends and family kept asking how to actually use AI in their work and daily life.</div>
    </div>
  </div>

  <div class="headline">Project-based AI you can <span class="a">use right away</span>.</div>

  <div class="hh">
    <div class="l"><div class="tag">Start here &middot; Happy Hour</div>
      <div class="nm">AI Made Practical</div>
      <div class="mt">{hh_mt}</div></div>
    {hh_price}
  </div>

  <div class="two">
    <div class="card"><div class="tag">Project workshop</div>
      <div class="nm">AI for Business</div>
      <div class="mt">Wed 14 Oct to 4 Nov &middot; 18h00 to 20h00</div>
      {b_price}
      <div class="ds">Apply it to your own business. Leave with a workflow ready to use and a 30-day plan.</div></div>
    <div class="card b"><div class="tag">Project workshop</div>
      <div class="nm">AI Made Simple</div>
      <div class="mt">Fri 16 Oct to 6 Nov &middot; 15h00 to 17h00</div>
      {s_price}
      <div class="ds">Work on tasks from your own life. From curious to confident in 30 days.</div></div>
  </div>

  <div class="sess">
    <div class="a">Four weekly two-hour sessions &middot; Bring your own device</div>
    <div class="b">Limited spots, reserve yours now</div>
  </div>

  <div class="reg">
    <div class="rl"><div class="rt">Register now</div>
      <div class="ru">{URL}</div>
      <div class="rs">or scan the code to sign up</div></div>
    <div class="qr"><img src="{QR}"></div>
  </div>

  <div class="contact">
    <div class="ct"><b>WhatsApp +351 928 129 560</b> &middot; patiolanguage@gmail.com<br>
      <b>@patiolanguage</b> &middot; Praca do Poder Local, Lote 14, Loja C, Lagos</div>
    <img src="{LOGO_COLOR}">
  </div>
</div>"""

def build(show_price, suffix):
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{CSS}</style></head><body>{body_html(show_price)}</body></html>'
    html_path = os.path.join(SOCIAL, f"ai-flyer-new{suffix}.html")
    png_path = os.path.join(SOCIAL, f"Patio-AI-Workshops-Flyer{suffix}.png")
    pdf_path = os.path.join(SOCIAL, f"Patio-AI-Workshops-Flyer{suffix}.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        "--default-background-color=00000000",
        f"--screenshot={png_path}", html_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png_path)
    im = Image.open(png_path).convert("RGB")
    im.save(pdf_path, "PDF", resolution=255.0)
    print("wrote", pdf_path)

def main():
    build(True, "")
    build(False, "-noprices")

if __name__ == "__main__":
    main()
