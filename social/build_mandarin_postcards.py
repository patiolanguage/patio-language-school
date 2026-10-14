#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fri 9 Oct 2026: "Postcards from Guangzhou". Countdown to the free taster (Mon 12 Oct).

Photos: a friend's trip to Guangzhou, in social/Mandarin/Pictures. The Canton Tower
places them in Guangzhou. Each photo carries one phrase you would use there.

Slides 1080x1350, EN and PT on each. No dots or swipe hints, so the same images
work as a Facebook photo post. Facebook version of slide 4 has no link on the image.

Outputs (social/Mandarin/postcards/):
  postcard-{1..4}-1080x1350.png
  postcard-4-fb-1080x1350.png   slide 4 without the link, for Facebook
"""
import os, subprocess
import build_mandarin as bm

PICS = os.path.join(bm.SOCIAL, "Mandarin", "Pictures")
OUT = os.path.join(bm.SOCIAL, "Mandarin", "postcards")
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350

def pic(name):
    return bm.b64_photo(os.path.join(PICS, name))

CSS = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);z-index:3;}}
.card{{position:absolute;left:56px;right:56px;top:50px;height:790px;background:#fff;padding:18px 18px 0;border-radius:10px;
  box-shadow:0 18px 40px rgba(43,31,24,.18);transform:rotate(-1.2deg);}}
.card img{{width:100%;height:708px;object-fit:cover;border-radius:4px;display:block;}}
.card .cap{{height:62px;display:flex;align-items:center;justify-content:space-between;padding:0 6px;font-weight:700;font-size:28px;color:#4a4038;letter-spacing:.05em;}}
.card .cap b{{font-family:'Noto Serif SC',serif;font-weight:600;color:#2B1F18;font-size:30px;letter-spacing:0;}}
.stamp{{position:absolute;top:30px;right:30px;width:150px;height:150px;border-radius:50%;background:#B8593A;color:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(10deg);border:5px dashed rgba(251,246,238,.75);
  box-shadow:0 8px 20px rgba(0,0,0,.25);text-align:center;}}
.stamp b{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:46px;line-height:1;}}
.stamp span{{font-weight:700;font-size:17px;letter-spacing:.12em;text-transform:uppercase;margin-top:6px;}}
.logo{{position:absolute;left:84px;top:84px;height:86px;z-index:2;filter:drop-shadow(0 2px 8px rgba(0,0,0,.55));}}
.text{{position:absolute;left:56px;right:56px;top:880px;bottom:50px;display:flex;flex-direction:column;}}
.zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:110px;line-height:1.05;}}
.py{{font-family:'DM Serif Display',serif;font-style:italic;font-size:72px;color:#B8593A;line-height:1.1;}}
.mean{{display:flex;gap:14px;margin-top:20px;flex-wrap:wrap;}}
.mean span{{font-size:48px;font-weight:700;background:#F1E9DA;border-radius:999px;padding:8px 26px;}}
.mean span.pt{{background:#E4ECEB;color:#3f5a59;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:108px;line-height:1.02;}}
h1 .a{{color:#B8593A;font-style:italic;white-space:nowrap;}}
h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:70px;line-height:1.1;color:#4a4038;margin-top:12px;}}
h2 .a{{color:#B8593A;font-style:italic;white-space:nowrap;}}
/* countdown slide */
.cd{{position:absolute;left:56px;right:56px;top:90px;bottom:60px;display:flex;flex-direction:column;}}
.cd .head{{display:flex;justify-content:space-between;align-items:center;}}
.cd .head img{{height:90px;}}
.big{{margin-top:80px;font-family:'DM Serif Display',serif;font-size:158px;line-height:.95;}}
.big .a{{color:#B8593A;font-style:italic;}}
.big2{{font-family:'DM Serif Display',serif;font-size:100px;line-height:1.05;color:#4a4038;margin-top:14px;}}
.big2 .a{{color:#B8593A;font-style:italic;}}
.sub{{font-size:48px;font-weight:600;color:#2B1F18;margin-top:50px;line-height:1.3;}}
.sub b{{color:#3f5a59;}}
.ticket{{margin-top:auto;background:#B8593A;color:#FBF6EE;border-radius:26px;padding:10px;transform:rotate(-1.5deg);box-shadow:0 14px 34px rgba(184,89,58,.35);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:18px;padding:34px 34px;display:flex;align-items:center;gap:28px;}}
.ticket img{{width:230px;height:230px;border-radius:50%;object-fit:cover;object-position:center 30%;border:6px solid #FBF6EE;flex:none;}}
.ticket .k{{white-space:nowrap;font-family:'DM Serif Display',serif;font-size:80px;line-height:1;}}
.ticket .d{{font-size:52px;font-weight:700;margin-top:10px;}}
.ticket .d2{{font-size:44px;font-weight:600;margin-top:4px;}}
.ticket .u{{font-size:48px;font-weight:700;margin-top:14px;background:#FBF6EE;color:#B8593A;display:inline-block;padding:6px 22px;border-radius:999px;}}
</style>"""

def page(body):
    return f'<!DOCTYPE html><html><head>{bm.FONTS}{CSS}</head><body><div class="bar"></div>{body}</body></html>'

def postcard(photo, caption, text, pos="center"):
    return page(f"""
<div class="card"><img src="{pic(photo)}" style="object-position:{pos}">
  <div class="cap"><span>POSTCARD FROM GUANGZHOU &middot; PHOTO: CRAIG</span><b>广州</b></div>
  <div class="stamp"><b>广州</b><span>Guǎngzhōu</span></div></div>
<img class="logo" src="{bm.LOGO_WHITE}">
<div class="text">{text}</div>""")

def slides(fb=False):
    # Cover: full bleed photo, few words, so the grid tile reads as a photo
    s1 = f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
body{{position:relative;font-family:'Barlow',sans-serif;}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;}}
.fade{{position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(43,31,24,0) 0%,rgba(43,31,24,.55) 55%,rgba(43,31,24,.8) 100%);}}
.logo{{position:absolute;top:56px;left:56px;height:96px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.5));}}
.stamp{{position:absolute;top:50px;right:56px;width:190px;height:190px;border-radius:50%;background:#B8593A;color:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(10deg);border:6px dashed rgba(251,246,238,.8);
  box-shadow:0 10px 26px rgba(0,0,0,.3);}}
.stamp b{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:62px;line-height:1;}}
.stamp span{{font-weight:700;font-size:21px;letter-spacing:.12em;text-transform:uppercase;margin-top:8px;}}
.txt{{position:absolute;left:56px;right:56px;bottom:64px;color:#FBF6EE;text-shadow:0 2px 14px rgba(0,0,0,.45);}}
.txt h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:112px;line-height:1;}}
.txt h1 i{{color:#E9C58B;white-space:nowrap;}}
.txt p{{font-weight:700;font-size:30px;letter-spacing:.08em;text-transform:uppercase;margin-top:18px;color:#F6DCC0;}}
</style></head><body>
<img class="ph" src="{pic('tall tower.jpeg')}"><div class="fade"></div>
<img class="logo" src="{bm.LOGO_WHITE}">
<div class="stamp"><b>广州</b><span>Guǎngzhōu</span></div>
<div class="txt"><h1>Postcards from <i>Guangzhou</i></h1><p>Photos: Craig &middot; Swipe &rarr;</p></div>
</body></html>"""
    s2 = postcard("anime coffee upright.jpeg", "", """
  <div class="zh">我要一杯咖啡</div>
  <div class="py">wǒ yào yì bēi kāfēi</div>
  <div class="mean"><span>I&rsquo;d like a coffee</span><span class="pt">Queria um café</span></div>""", "52% 50%")
    s3 = postcard("better river picture.jpeg", "", """
  <div class="zh">真漂亮!</div>
  <div class="py">zhēn piàoliang!</div>
  <div class="mean"><span>So beautiful!</span><span class="pt">Que bonito!</span></div>""", "center 55%")
    link = "" if fb else '<div class="u">patiolanguage.pt/taster</div>'
    s4 = page(f"""
<div class="cd">
  <div class="head"><img src="{bm.LOGO_COLOR}"></div>
  <div class="big"><span class="a">3</span> days to go.</div>
  <div class="big2">Faltam <span class="a">3</span> dias.</div>
  <div class="sub">Say your first words in Mandarin, free.<br><b>Diga as suas primeiras palavras em mandarim, grátis.</b></div>
  <div class="ticket"><div class="in"><img src="{bm.MICHELLE}"><div>
    <div class="k">Free taster<br>Aula grátis</div>
    <div class="d">Mon 12 Oct &middot; 18h30</div>
    <div class="d2">Seg 12 out &middot; with Michelle</div>
    {link}</div></div></div>
</div>""")
    return [s1, s2, s3, s4]

def render(html, name):
    path = os.path.join(OUT, name + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}", "--virtual-time-budget=6000",
        f"--screenshot={os.path.join(OUT, name + '.png')}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", name + ".png")


# =====================================================================
# STORIES  (1080x1920, full photo, Instagram safe zones top 250 / bottom 340)
# =====================================================================
SW, SH = 1080, 1920

STORY_CSS = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{SW}px;height:{SH}px;overflow:hidden;}}
body{{position:relative;font-family:'Barlow',sans-serif;background:#2B1F18;}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}}
.top{{position:absolute;left:0;right:0;top:0;height:520px;background:linear-gradient(180deg,rgba(43,31,24,.55),rgba(43,31,24,0));}}
.fade{{position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(180deg,rgba(43,31,24,0) 0%,rgba(43,31,24,.6) 50%,rgba(43,31,24,.85) 100%);}}
.logo{{position:absolute;top:260px;left:60px;height:100px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.5));}}
.stamp{{position:absolute;top:250px;right:60px;width:190px;height:190px;border-radius:50%;background:#B8593A;color:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(10deg);border:6px dashed rgba(251,246,238,.8);box-shadow:0 10px 26px rgba(0,0,0,.3);}}
.stamp b{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:62px;line-height:1;}}
.stamp span{{font-weight:700;font-size:21px;letter-spacing:.12em;text-transform:uppercase;margin-top:8px;}}
.txt{{position:absolute;left:60px;right:60px;bottom:400px;color:#FBF6EE;text-shadow:0 2px 14px rgba(0,0,0,.45);}}
.txt h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:124px;line-height:1;}}
.txt h1 i{{color:#E9C58B;white-space:nowrap;}}
.txt .zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:120px;line-height:1.05;}}
.txt .py{{font-family:'DM Serif Display',serif;font-style:italic;font-size:80px;color:#E9C58B;line-height:1.1;}}
.txt .m{{font-size:52px;font-weight:700;margin-top:14px;}}
.txt .m span{{color:#F6DCC0;font-weight:600;}}
.credit{{font-weight:700;font-size:30px;letter-spacing:.08em;text-transform:uppercase;margin-top:20px;color:#F6DCC0;}}
.ticket{{margin-top:40px;background:#B8593A;border-radius:26px;padding:10px;transform:rotate(-1.5deg);box-shadow:0 14px 34px rgba(0,0,0,.35);text-shadow:none;}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:18px;padding:26px 30px;display:flex;align-items:center;gap:28px;}}
.ticket img{{width:200px;height:200px;border-radius:50%;object-fit:cover;object-position:center 30%;border:6px solid #FBF6EE;flex:none;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:76px;line-height:1;}}
.ticket .d{{font-size:46px;font-weight:700;margin-top:10px;}}
</style>"""

def story(photo, body, pos="center"):
    return (f'<!DOCTYPE html><html><head>{bm.FONTS}{STORY_CSS}</head><body>'
            f'<img class="ph" src="{pic(photo)}" style="object-position:{pos}"><div class="top"></div><div class="fade"></div>'
            f'<img class="logo" src="{bm.LOGO_WHITE}"><div class="stamp"><b>广州</b><span>Guǎngzhōu</span></div>'
            f'<div class="txt">{body}</div></body></html>')

def stories():
    return [
        story("tall tower.jpeg", """<h1>Postcards from <i>Guangzhou</i></h1>
          <div class="credit">Photos: Craig &middot; Tap &rarr;</div>""", "center 30%"),
        story("anime coffee upright.jpeg", """<div class="zh">我要一杯咖啡</div><div class="py">wǒ yào yì bēi kāfēi</div>
          <div class="m">I&rsquo;d like a coffee <span>&middot; Queria um café</span></div>"""),
        story("better river picture.jpeg", """<div class="zh">真漂亮!</div><div class="py">zhēn piàoliang!</div>
          <div class="m">So beautiful! <span>&middot; Que bonito!</span></div>"""),
        story("another river with tall buildings.jpeg", f"""<h1>Learn more, <i>free</i>.</h1>
          <div class="ticket"><div class="in"><img src="{bm.MICHELLE}"><div>
            <div class="k">Aula grátis</div><div class="d">Seg 12 out &middot; Mon 12 Oct &middot; 18h30</div></div></div></div>"""),
    ]

def render_stories():
    for n, html in enumerate(stories(), start=1):
        name = f"postcard-story-{n}-{SW}x{SH}"
        path = os.path.join(OUT, name + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--window-size={SW},{SH}", "--virtual-time-budget=6000",
            f"--screenshot={os.path.join(OUT, name + '.png')}", path],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("rendered", name + ".png")


# =====================================================================
# FACEBOOK  one image collage, 1080x1350. Facebook crops multi photo posts,
# so all postcards go in one image that Facebook shows in full. No link.
# =====================================================================
def fb_collage():
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.head{{position:absolute;left:50px;right:50px;top:40px;display:flex;justify-content:space-between;align-items:center;}}
.head img{{height:80px;}}
.head h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:64px;line-height:1;text-align:right;}}
.head h1 i{{color:#B8593A;}}
.grid{{position:absolute;left:50px;right:50px;top:200px;height:850px;display:grid;grid-template-columns:1.1fr 1fr;grid-template-rows:1fr 1fr;gap:18px;}}
.p{{position:relative;border-radius:18px;overflow:hidden;box-shadow:0 10px 26px rgba(43,31,24,.15);}}
.p img{{width:100%;height:100%;object-fit:cover;display:block;}}
.p.big{{grid-row:1 / span 2;}}
.p .lab{{position:absolute;left:0;right:0;bottom:0;padding:60px 18px 16px;background:linear-gradient(180deg,rgba(43,31,24,0),rgba(43,31,24,.85));color:#FBF6EE;}}
.p .lab b{{display:block;font-family:'Noto Serif SC',serif;font-weight:600;font-size:46px;line-height:1.05;}}
.p .lab i{{display:block;font-family:'DM Serif Display',serif;font-size:32px;color:#E9C58B;}}
.p .lab span{{display:block;font-size:26px;font-weight:700;margin-top:2px;}}
.stamp{{position:absolute;top:18px;left:18px;width:120px;height:120px;border-radius:50%;background:#B8593A;color:#FBF6EE;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg);border:4px dashed rgba(251,246,238,.8);}}
.stamp b{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:40px;line-height:1;}}
.stamp span{{font-weight:700;font-size:14px;letter-spacing:.1em;text-transform:uppercase;margin-top:4px;}}
.credit{{position:absolute;left:50px;top:1062px;font-size:24px;font-weight:700;letter-spacing:.08em;color:#726651;text-transform:uppercase;}}
.ticket{{position:absolute;left:50px;right:50px;bottom:44px;background:#B8593A;color:#FBF6EE;border-radius:24px;padding:9px;transform:rotate(-1deg);box-shadow:0 12px 30px rgba(184,89,58,.32);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:17px;padding:18px 26px;display:flex;align-items:center;gap:26px;}}
.ticket img{{width:150px;height:150px;border-radius:50%;object-fit:cover;object-position:center 30%;border:5px solid #FBF6EE;flex:none;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:58px;line-height:1;}}
.ticket .d{{font-size:38px;font-weight:700;margin-top:8px;}}
</style></head><body><div class="bar"></div>
<div class="head"><img src="{bm.LOGO_COLOR}"><h1>Postcards from<br><i>Guangzhou</i></h1></div>
<div class="grid">
  <div class="p big"><img src="{pic('tall tower.jpeg')}" style="object-position:center 30%"><div class="stamp"><b>广州</b><span>Guǎngzhōu</span></div></div>
  <div class="p"><img src="{pic('anime coffee upright.jpeg')}" style="object-position:52% 45%"><div class="lab"><b>我要一杯咖啡</b><i>wǒ yào yì bēi kāfēi</i><span>I&rsquo;d like a coffee &middot; Queria um café</span></div></div>
  <div class="p"><img src="{pic('better river picture.jpeg')}" style="object-position:center 60%"><div class="lab"><b>真漂亮!</b><i>zhēn piàoliang!</i><span>So beautiful! &middot; Que bonito!</span></div></div>
</div>
<div class="credit">Photos: Craig</div>
<div class="ticket"><div class="in"><img src="{bm.MICHELLE}"><div>
  <div class="k">3 days to go &middot; Faltam 3 dias</div><div class="d">Free taster &middot; Aula grátis &middot; Mon 12 Oct &middot; 18h30</div></div></div></div>
</body></html>"""


if __name__ == "__main__":
    for n, html in enumerate(slides(), start=1):
        render(html, f"postcard-{n}-{W}x{H}")
    render(slides(fb=True)[3], f"postcard-4-fb-{W}x{H}")
    render_stories()
    render(fb_collage(), f"postcards-fb-collage-{W}x{H}")
