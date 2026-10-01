#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Social versions of the AI workshops flyer: FB post, IG post, IG story.

Same content and look as Patio-AI-Workshops-Flyer: Arek hero, Happy Hour band,
two workshop cards, and a teal register band with the QR. Reflowed per format.
Brand: DM Serif Display + Barlow. No em/en dashes.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
AREK = b64(os.path.join(IMG, "arek.png"))
QR = b64(os.path.join(IMG, "qr-ai-register.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

URL = "patiolanguage.pt/ai"
BIO = ("25 years in software, building real-world AI tools. He teaches in plain "
       "language, hands-on, and created these workshops so anyone can use AI with confidence.")
BIO_SHORT = ("25 years in software. He builds real-world AI tools and teaches in "
             "plain language, hands-on.")

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def render(fname, html, w, h):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--default-background-color=00000000",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)


def build(kind, w, h, show_price=True, show_links=True, suffix=""):
    # per-format sizing
    P = {
      "story": dict(pad="0 74px 66px", logo=74, eb=27, photo=300, hname=78, hbio=39,
                    hhtag=27, hhnm=58, hhmt=33, hhpr=88, ctag=25, cnm=52, cmt=31, cpr=66, cds=31,
                    rt=64, ru=42, rs=30, qr=250, gap=26, cardpad="30px 34px", hhpad="30px 42px"),
      "ig":    dict(pad="0 66px 46px", logo=64, eb=24, photo=225, hname=62, hbio=32,
                    hhtag=24, hhnm=48, hhmt=29, hhpr=72, ctag=22, cnm=44, cmt=27, cpr=56, cds=27,
                    rt=54, ru=37, rs=27, qr=210, gap=18, cardpad="24px 28px", hhpad="24px 36px"),
      "fb":    dict(pad="0 58px 40px", logo=58, eb=22, photo=190, hname=54, hbio=30,
                    hhtag=21, hhnm=42, hhmt=26, hhpr=60, ctag=20, cnm=40, cmt=26, cpr=50, cds=24,
                    rt=48, ru=33, rs=25, qr=180, gap=13, cardpad="20px 26px", hhpad="20px 30px"),
    }[kind]
    bio = BIO_SHORT if kind == "fb" else BIO
    show_desc = (kind != "fb")
    hh_price = '<div class="pr">&euro;20<small>credited to a course</small></div>' if show_price else ''
    b_price = '<div class="pr">&euro;249</div>' if show_price else ''
    s_price = '<div class="pr">&euro;149</div>' if show_price else ''
    hh_mt = ("Wed 7 Oct &middot; 17h00 to 19h30" if show_price
             else "Wed 7 Oct &middot; 17h00 to 19h30 &middot; includes a drink")
    if show_links:
        reg_html = (f'<div class="reg"><div class="rl"><div class="rt">Register now</div>'
                    f'<div class="ru">{URL}</div>'
                    f'<div class="rs">Limited spots &middot; scan to sign up</div></div>'
                    f'<div class="qr"><img src="{QR}"></div></div>')
    else:
        reg_html = ('<div class="reg"><div class="rl"><div class="rt">Register now</div>'
                    '<div class="ru">Sign-up link in the comments below</div>'
                    '<div class="rs">Limited spots to keep groups small</div></div></div>')
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.f{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;
  background:radial-gradient(120% 80% at 50% 0%,#FEFCF7 0%,#FBF6EE 45%,#F3E6D0 100%);
  color:#2B1F18;display:flex;flex-direction:column;padding:{P['pad']};}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.top{{display:flex;align-items:center;justify-content:center;gap:22px;padding-top:{P['gap']+14}px;}}
.top img{{height:{P['logo']}px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.2em;text-transform:uppercase;font-size:{P['eb']}px;}}
/* hero */
.hero{{display:flex;align-items:center;gap:38px;margin-top:{P['gap']}px;
  background:#FFF9F0;border:3px solid #F0E2CC;border-radius:26px;padding:28px 34px;}}
.ring{{width:{P['photo']}px;height:{P['photo']}px;flex:none;border-radius:50%;
  background:linear-gradient(135deg,#C19D5F,#B8593A);padding:8px;box-shadow:0 12px 30px rgba(43,31,24,.18);}}
.ring img{{width:100%;height:100%;border-radius:50%;display:block;background:#2B1F18;}}
.htxt{{flex:1;}}
.heye{{color:#B8593A;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:{P['eb']}px;}}
.hname{{font-family:'DM Serif Display',serif;font-size:{P['hname']}px;line-height:1;margin-top:4px;}}
.hbio{{font-size:{P['hbio']}px;font-weight:500;line-height:1.3;margin-top:12px;color:#4a4038;}}
/* happy hour */
.hh{{background:#2B1F18;color:#FBF6EE;border-radius:24px;border-left:14px solid #C19D5F;
  padding:{P['hhpad']};display:flex;align-items:center;gap:24px;margin-top:{P['gap']}px;}}
.hh .l{{flex:1;}}
.hh .tag{{color:#C19D5F;font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:{P['hhtag']}px;}}
.hh .nm{{font-family:'DM Serif Display',serif;font-size:{P['hhnm']}px;line-height:1;margin-top:5px;}}
.hh .mt{{font-weight:600;font-size:{P['hhmt']}px;margin-top:10px;color:#Eadfce;}}
.hh .pr{{font-family:'DM Serif Display',serif;color:#C19D5F;font-size:{P['hhpr']}px;line-height:.9;flex:none;text-align:right;}}
.hh .pr small{{display:block;font-family:'Barlow';font-size:{int(P['hhmt']*0.7)}px;font-weight:600;color:#b7ac99;}}
/* two cards */
.two{{display:flex;gap:{P['gap']}px;margin-top:{P['gap']}px;}}
.card{{flex:1;background:#fff;border-radius:22px;border-top:12px solid #617C7B;padding:{P['cardpad']};
  box-shadow:0 12px 30px rgba(43,31,24,.10);}}
.card.b{{border-top-color:#B8593A;}}
.card .tag{{font-weight:700;letter-spacing:.05em;text-transform:uppercase;font-size:{P['ctag']}px;color:#4f6a69;}}
.card.b .tag{{color:#B8593A;}}
.card .nm{{font-family:'DM Serif Display',serif;font-size:{P['cnm']}px;line-height:1;margin-top:6px;}}
.card .mt{{font-weight:700;font-size:{P['cmt']}px;margin-top:10px;color:#2B1F18;}}
.card .pr{{font-family:'DM Serif Display',serif;font-size:{P['cpr']}px;line-height:1;margin-top:10px;color:#617C7B;}}
.card.b .pr{{color:#B8593A;}}
.card .ds{{font-size:{P['cds']}px;font-weight:500;line-height:1.28;margin-top:10px;color:#6a5f52;}}
/* register */
.reg{{background:linear-gradient(135deg,#5f7c7b,#42605e);color:#FBF6EE;border-radius:24px;
  padding:30px 40px;display:flex;align-items:center;gap:36px;margin-top:auto;}}
.reg .rl{{flex:1;}}
.reg .rt{{font-family:'DM Serif Display',serif;font-size:{P['rt']}px;line-height:1;}}
.reg .ru{{font-size:{P['ru']}px;font-weight:700;margin-top:10px;color:#F0D4A6;}}
.reg .rs{{font-size:{P['rs']}px;font-weight:500;margin-top:6px;color:#EAF1EF;}}
.qr{{width:{P['qr']}px;height:{P['qr']}px;flex:none;background:#fff;border-radius:18px;padding:14px;}}
.qr img{{width:100%;height:100%;display:block;}}
"""
    body = f"""<div class="f"><div class="bar"></div>
  <div class="top"><img src="{LOGO_COLOR}"><span class="eyebrow">Patio Practical AI &middot; Lagos</span></div>
  <div class="hero">
    <div class="ring"><img src="{AREK}"></div>
    <div class="htxt"><div class="heye">Meet your host</div>
      <div class="hname">Arek Adeoye</div>
      <div class="hbio">{bio}</div></div>
  </div>
  <div class="hh"><div class="l"><div class="tag">Start here &middot; Happy Hour</div>
      <div class="nm">AI Made Practical</div>
      <div class="mt">{hh_mt}</div></div>
    {hh_price}</div>
  <div class="two">
    <div class="card"><div class="tag">Project workshop</div>
      <div class="nm">AI for Business</div>
      <div class="mt">Wed 14 Oct to 4 Nov &middot; 18h00 to 20h00</div>
      {b_price}
      {'<div class="ds">Leave with a workflow ready to use and a 30-day plan.</div>' if show_desc else ''}</div>
    <div class="card b"><div class="tag">Project workshop</div>
      <div class="nm">AI Made Simple</div>
      <div class="mt">Fri 16 Oct to 6 Nov &middot; 15h00 to 17h00</div>
      {s_price}
      {'<div class="ds">From curious to confident in 30 days.</div>' if show_desc else ''}</div>
  </div>
  {reg_html}
</div>"""
    render(f"ai-flyer-{kind}-{w}x{h}{suffix}.html", page(css, body), w, h)


if __name__ == "__main__":
    for kind, w, h in (("story", 1080, 1920), ("ig", 1080, 1350), ("fb", 1080, 1080)):
        build(kind, w, h, show_price=True, suffix="")
        build(kind, w, h, show_price=False, suffix="-noprices")
    # FB flyer with no links baked in (for posting; link goes in the caption/comment)
    build("fb", 1080, 1080, show_price=True, show_links=False, suffix="-nolinks")
    build("fb", 1080, 1080, show_price=False, show_links=False, suffix="-noprices-nolinks")
    print("done")
