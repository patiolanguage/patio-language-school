#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build the 6-slide Instagram Story sequence for Patio Practical AI (1080x1920).

BRIGHT version: light, warm brand backgrounds (cream + soft gold/teal/terracotta
tints), dark text, bigger type. Brand: DM Serif Display + Barlow.
Praia gold #C19D5F, Terracota #B8593A, Mar teal #617C7B, Chocolate #2B1F18,
Galao #726651, cream #FBF6EE. No em/en dashes. Safe margins for the IG UI.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H = 1080, 1920

def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

BASE = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Barlow',sans-serif;
  color:#2B1F18;}}
.bar{{position:absolute;top:0;left:0;right:0;height:18px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:5;}}
.wrap{{position:absolute;inset:0;z-index:4;display:flex;flex-direction:column;
  align-items:center;text-align:center;padding:165px 92px 250px;}}
.logo{{height:100px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.24em;text-transform:uppercase;
  font-size:30px;margin-top:28px;}}
.main{{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;}}
.dm{{font-family:'DM Serif Display',serif;}}
.foot{{width:100%;}}
"""

def page(css, body):
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{BASE}{css}</style></head>'
            f'<body>{body}</body></html>')

def render(fname, html):
    path = os.path.join(SOCIAL, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        "--default-background-color=00000000",
        f"--screenshot={os.path.join(SOCIAL, png)}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

# soft, bright brand backgrounds
CREAM   = "background:radial-gradient(125% 90% at 50% 16%,#FEFCF7 0%,#FBF6EE 45%,#F3E6D0 100%);"
GOLD    = "background:radial-gradient(125% 90% at 50% 16%,#FDF7EA 0%,#F7EAD1 55%,#EBD6AE 100%);"
PEACH   = "background:radial-gradient(125% 90% at 50% 16%,#FEF6F1 0%,#F8E6DB 55%,#F0D3C2 100%);"
SAGE    = "background:radial-gradient(125% 90% at 50% 16%,#F4F7F5 0%,#E7EFEC 55%,#D6E3DF 100%);"


# ---- Slide 1: Hook ----
def s1():
    css = """
h1{color:#2B1F18;font-size:110px;line-height:1.03;}
h1 .a{color:#B8593A;font-style:italic;}
.sub{color:#4a4038;font-size:46px;font-weight:500;line-height:1.4;margin-top:38px;}
"""
    body = f"""<div class="canvas"><div class="scrim" style="{CREAM}position:absolute;inset:0;"></div>
<div class="bar"></div>
<div class="wrap">
  <img class="logo" src="{LOGO_COLOR}">
  <div class="eyebrow">Patio Practical AI</div>
  <div class="main">
    <h1 class="dm">AI does not have to be <span class="a">complicated</span>.</h1>
    <div class="sub">It just needs to be explained clearly.</div>
  </div>
</div></div>"""
    render("ai-story-1-hook.html", page(css, body))

# ---- Slide 2: Three ways ----
def s2():
    css = """
h1{color:#2B1F18;font-size:82px;line-height:1.06;}
h1 .a{color:#B8593A;font-style:italic;}
.list{margin-top:58px;display:flex;flex-direction:column;gap:28px;width:100%;}
.item{background:#fff;border-radius:24px;padding:36px 38px;font-size:40px;font-weight:600;
  color:#2B1F18;box-shadow:0 12px 30px rgba(43,31,24,.10);border-left:12px solid #C19D5F;}
.item:nth-child(2){border-left-color:#617C7B;}
.item:nth-child(3){border-left-color:#B8593A;}
"""
    body = f"""<div class="canvas"><div class="scrim" style="{GOLD}position:absolute;inset:0;"></div>
<div class="bar"></div>
<div class="wrap">
  <img class="logo" src="{LOGO_COLOR}">
  <div class="eyebrow">Practical AI &middot; Lagos</div>
  <div class="main">
    <h1 class="dm">Three ways to get started with <span class="a">AI in Lagos</span></h1>
    <div class="list">
      <div class="item">In person &middot; small groups &middot; practical learning</div>
      <div class="item">No technical background needed</div>
      <div class="item">Bring your own device</div>
    </div>
  </div>
</div></div>"""
    render("ai-story-2-ways.html", page(css, body))

# ---- Slide 3: Happy Hour ----
def s3():
    css = """
.tag{color:#a9772f;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:30px;}
h1{color:#2B1F18;font-size:120px;line-height:1.0;margin-top:14px;}
.when{color:#2B1F18;font-size:46px;font-weight:700;margin-top:24px;}
.sub{color:#4a4038;font-size:40px;font-weight:500;line-height:1.4;margin-top:30px;}
.price{margin-top:38px;background:#617C7B;color:#FBF6EE;border-radius:22px;padding:30px 38px;
  font-size:36px;font-weight:600;line-height:1.4;}
.price b{color:#F4E7CF;}
"""
    body = f"""<div class="canvas"><div class="scrim" style="{PEACH}position:absolute;inset:0;"></div>
<div class="bar"></div>
<div class="wrap">
  <img class="logo" src="{LOGO_COLOR}">
  <div class="eyebrow">Start here &middot; Happy Hour</div>
  <div class="main">
    <div class="tag">&#10024; AI Made Practical</div>
    <h1 class="dm">Happy Hour</h1>
    <div class="when">Wed 7 Oct &middot; 17h00 to 19h30</div>
    <div class="sub">A relaxed introduction to AI in<br>everyday life and work.</div>
    <div class="price"><b>&euro;20</b>, including a drink<br>Fully redeemable toward a course (within 7 days)</div>
  </div>
</div></div>"""
    render("ai-story-3-happyhour.html", page(css, body))

# ---- Slide 4: AI Made Simple ----
def s4():
    css = """
.tag{color:#4f6a69;font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:28px;}
h1{color:#2B1F18;font-size:100px;line-height:1.0;margin-top:12px;}
.meta{color:#5a5047;font-size:40px;font-weight:600;margin-top:24px;}
.price{font-family:'DM Serif Display',serif;color:#617C7B;font-size:88px;margin-top:12px;}
.sub{color:#4a4038;font-size:40px;font-weight:500;line-height:1.4;margin-top:32px;}
.sub b{color:#2B1F18;}
"""
    body = f"""<div class="canvas"><div class="scrim" style="{SAGE}position:absolute;inset:0;"></div>
<div class="bar"></div>
<div class="wrap">
  <img class="logo" src="{LOGO_COLOR}">
  <div class="eyebrow">Project workshop &middot; for everyone</div>
  <div class="main">
    <div class="tag">&#128218; AI Made Simple</div>
    <h1 class="dm">AI Made Simple</h1>
    <div class="meta">Fridays &middot; 16 Oct to 6 Nov &middot; 15h00 to 17h00</div>
    <div class="price">&euro;149</div>
    <div class="sub"><b>Use AI confidently in daily life:</b><br>emails &middot; summaries &middot; images &middot; practical tools</div>
  </div>
</div></div>"""
    render("ai-story-4-simple.html", page(css, body))

# ---- Slide 5: AI for Business ----
def s5():
    css = """
.tag{color:#a9772f;font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:28px;}
h1{color:#2B1F18;font-size:100px;line-height:1.0;margin-top:12px;}
.meta{color:#5a5047;font-size:40px;font-weight:600;margin-top:24px;}
.price{font-family:'DM Serif Display',serif;color:#B8593A;font-size:88px;margin-top:12px;}
.sub{color:#4a4038;font-size:40px;font-weight:500;line-height:1.42;margin-top:32px;}
.sub b{color:#2B1F18;}
"""
    body = f"""<div class="canvas"><div class="scrim" style="{GOLD}position:absolute;inset:0;"></div>
<div class="bar"></div>
<div class="wrap">
  <img class="logo" src="{LOGO_COLOR}">
  <div class="eyebrow">Project workshop &middot; for work</div>
  <div class="main">
    <div class="tag">&#128188; AI for Business</div>
    <h1 class="dm">AI for Business</h1>
    <div class="meta">Wednesdays &middot; 14 Oct to 4 Nov &middot; 18h00 to 20h00</div>
    <div class="price">&euro;249</div>
    <div class="sub"><b>For owners, freelancers and professionals.</b><br>Work smarter, save time, and simplify workflows.</div>
  </div>
</div></div>"""
    render("ai-story-5-business.html", page(css, body))

# ---- Slide 6: CTA ----
def s6():
    css = """
h1{color:#2B1F18;font-size:128px;line-height:1.0;}
h1 .a{color:#B8593A;font-style:italic;}
.sub{color:#4a4038;font-size:44px;font-weight:600;line-height:1.4;margin-top:36px;}
.note{color:#B8593A;font-size:36px;font-weight:700;margin-top:32px;}
.url{color:#2B1F18;font-size:40px;font-weight:700;margin-top:44px;}
.handle{color:#726651;font-size:33px;font-weight:600;margin-top:10px;}
"""
    body = f"""<div class="canvas"><div class="scrim" style="{PEACH}position:absolute;inset:0;"></div>
<div class="bar"></div>
<div class="wrap">
  <img class="logo" src="{LOGO_COLOR}">
  <div class="eyebrow">Patio Practical AI &middot; Lagos</div>
  <div class="main">
    <h1 class="dm">Want to <span class="a">join</span>?</h1>
    <div class="sub">Tap the link to sign up,<br>or send us a message. &#10024;</div>
    <div class="note">Limited spots, to keep it small and practical.</div>
    <div class="url">patiolanguage.pt/ai</div>
    <div class="handle">@patiolanguage &middot; WhatsApp +351 928 129 560</div>
  </div>
</div></div>"""
    render("ai-story-6-cta.html", page(css, body))


if __name__ == "__main__":
    s1(); s2(); s3(); s4(); s5(); s6()
    print("done")
