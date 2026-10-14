#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sunday 4 Oct 2026 carousel: "Your first 3 words in Mandarin". EN and PT on every slide.

Slides (1080x1350, also fine for Facebook):
  1 cover, 2 nǐ hǎo, 3 xièxie, 4 zàijiàn, 5 free taster CTA.

Outputs: social/Mandarin/words/words-{1..5}-1080x1350.png
         social/Mandarin/words/words-fb-1080x1080.png (Facebook, one image, all 3 words)
Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Mandarin", "words")
os.makedirs(OUT, exist_ok=True)
HK = bm.b64_photo(os.path.join(bm.IMG, "mandarin-hk-2.jpg"))
W, H = 1080, 1350

WORDS = [
    ("你好", "nǐ hǎo", "hello", "olá",
     "Literally “you good”.", "À letra: “tu bem”."),
    ("谢谢", "xièxie", "thank you", "obrigado / obrigada",
     "The second syllable is soft, almost whispered.", "A segunda sílaba é suave, quase sussurrada."),
    ("再见", "zàijiàn", "goodbye", "adeus",
     "Literally “again see”.", "À letra: “outra vez ver”."),
]

CSS = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{position:absolute;top:44px;left:56px;height:84px;}}
.count{{position:absolute;top:66px;right:56px;font-weight:700;letter-spacing:.16em;color:#B8593A;font-size:32px;}}
.dots{{position:absolute;bottom:44px;left:0;right:0;display:flex;justify-content:center;gap:14px;}}
.dots i{{width:14px;height:14px;border-radius:50%;background:#E3D6C0;display:block;}}
.dots i.on{{background:#B8593A;}}
.swipe{{position:absolute;bottom:84px;right:56px;font-weight:700;font-size:36px;color:#617C7B;}}
/* cover */
.ph{{position:absolute;left:56px;right:56px;top:160px;height:600px;width:calc(100% - 112px);object-fit:cover;object-position:center 35%;border-radius:30px;box-shadow:0 14px 34px rgba(43,31,24,.16);}}
.badge{{position:absolute;top:190px;right:86px;background:#B8593A;color:#FBF6EE;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:32px;padding:12px 26px;border-radius:999px;}}
.cover{{position:absolute;left:56px;right:56px;top:810px;}}
.cover h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:120px;line-height:1.0;}}
.cover h1 .a{{color:#B8593A;font-style:italic;}}
.cover h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:68px;line-height:1.1;color:#4a4038;margin-top:18px;}}
.cover h2 .a{{color:#B8593A;font-style:italic;}}
/* word */
.card{{position:absolute;left:56px;right:56px;top:170px;bottom:150px;background:#fff;border-radius:34px;box-shadow:0 14px 34px rgba(43,31,24,.08);
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:40px;border-top:16px solid #C19D5F;}}
.zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:270px;line-height:1.05;}}
.py{{font-family:'DM Serif Display',serif;font-style:italic;font-size:120px;color:#B8593A;margin-top:6px;}}
.mean{{margin-top:34px;display:flex;gap:18px;align-items:center;flex-wrap:wrap;justify-content:center;}}
.mean span{{font-size:54px;font-weight:700;background:#F1E9DA;border-radius:999px;padding:10px 30px;}}
.mean span.pt{{background:#E4ECEB;color:#3f5a59;}}
.tip{{margin-top:40px;font-size:42px;color:#2B1F18;font-weight:600;line-height:1.3;}}
.tip b{{color:#3f5a59;}}
/* cta */
.cta{{position:absolute;left:56px;right:56px;top:170px;}}
.cta h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:100px;line-height:1.02;}}
.cta h1 .a{{color:#B8593A;font-style:italic;}}
.cta h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:64px;line-height:1.1;color:#4a4038;margin-top:14px;}}
.ticket{{margin-top:56px;background:#B8593A;color:#FBF6EE;border-radius:26px;padding:10px;transform:rotate(-2deg);box-shadow:0 14px 34px rgba(184,89,58,.35);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:18px;padding:30px 36px;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:80px;line-height:1;}}
.ticket .d{{font-size:48px;font-weight:700;margin-top:14px;}}
.ticket .d2{{font-size:40px;font-weight:600;color:#FBF6EE;margin-top:4px;}}
.ticket .u{{font-size:46px;font-weight:700;margin-top:18px;background:#FBF6EE;color:#B8593A;display:inline-block;padding:8px 24px;border-radius:999px;}}
.after{{margin-top:44px;font-size:40px;font-weight:600;color:#2B1F18;line-height:1.4;}}
.after b{{color:#617C7B;}}
.mich{{margin-top:44px;display:flex;align-items:center;gap:28px;}}
.mich img{{width:200px;height:200px;border-radius:50%;object-fit:cover;object-position:center 30%;border:8px solid #fff;box-shadow:0 10px 26px rgba(0,0,0,.18);}}
.mich .n{{font-family:'DM Serif Display',serif;font-size:56px;}}
.mich .r{{font-size:38px;font-weight:600;color:#4a4038;margin-top:4px;}}
.mich .b{{font-family:'DM Serif Display',serif;font-style:italic;font-size:46px;color:#B8593A;margin-top:8px;}}
</style>"""

REEL_CSS = """<style>
html,body{width:1080px;height:1920px;}
.stage{position:absolute;left:0;top:300px;width:1080px;height:1350px;}
.sound{position:absolute;top:200px;left:0;right:0;text-align:center;}
.sound span{display:inline-block;background:#B8593A;color:#FBF6EE;font-family:'Barlow',sans-serif;font-weight:700;font-size:46px;
  padding:16px 38px;border-radius:999px;box-shadow:0 10px 26px rgba(184,89,58,.35);}
.stage{top:330px !important;}
</style>"""

def frame(n, body, swipe=True, reel=False):
    """reel=True: 1080x1920 frame for the audio Reel, no swipe hint, counter or dots."""
    if reel:
        return (f'<!DOCTYPE html><html><head>{bm.FONTS}{CSS}{REEL_CSS}</head><body><div class="bar"></div>'
                f'<div class="sound"><span>&#128266; Ligue o som &middot; Turn the sound on</span></div>'
                f'<div class="stage"><img class="logo" src="{bm.LOGO_COLOR}">{body}</div></body></html>')
    dots = "".join(f'<i class="{"on" if k == n else ""}"></i>' for k in range(1, 6))
    sw = '<div class="swipe">Deslize / Swipe &rarr;</div>' if swipe else ""
    return (f'<!DOCTYPE html><html><head>{bm.FONTS}{CSS}</head><body><div class="bar"></div>'
            f'<img class="logo" src="{bm.LOGO_COLOR}"><div class="count">{n}/5</div>'
            f'{body}{sw}<div class="dots">{dots}</div></body></html>')

def slides(reel=False):
    out = [frame(1, f"""
<img class="ph" src="{HK}"><div class="badge">Mini aula &middot; Mini lesson</div>
<div class="cover">
  <h1>Your first <span class="a">3 words</span> in Mandarin.</h1>
  <h2>As suas primeiras <span class="a">3 palavras</span> em mandarim.</h2>
</div>""", reel=reel)]
    for i, (zh, py, en, pt, tip_en, tip_pt) in enumerate(WORDS, start=2):
        out.append(frame(i, f"""
<div class="card">
  <div class="zh">{zh}</div>
  <div class="py">{py}</div>
  <div class="mean"><span>{en}</span><span class="pt">{pt}</span></div>
  <div class="tip">{tip_en}<br><b>{tip_pt}</b></div>
</div>""", reel=reel))
    out.append(frame(5, f"""
<div class="cta">
  <h1>Want to learn <span class="a">more</span>?</h1>
  <h2>Quer aprender <span class="a">mais</span>?</h2>
  <div class="ticket"><div class="in">
    <div class="k">Free taster &middot; Aula grátis</div>
    <div class="d">Monday 12 October &middot; 18h30</div>
    <div class="d2">Segunda, 12 de outubro &middot; with Michelle Kanner</div>
    <div class="u">patiolanguage.pt/taster</div>
  </div></div>
  <div class="after">Mandarin classes start 19 October.<br><b>As aulas de mandarim começam a 19 de outubro.</b></div>
  <div class="mich"><img src="{bm.MICHELLE}"><div><div class="n">Michelle Kanner</div><div class="r">Your teacher &middot; A sua professora</div><div class="b">Até dia 12! See you on the 12th!</div></div></div>
</div>""", swipe=False, reel=reel))
    return out

def fb_single():
    """One square image for Facebook: all 3 words plus the taster. No swipe hints."""
    S = 1080
    cards = "".join(f"""<div class="w"><div class="zh">{zh}</div><div class="py">{py}</div>
      <div class="m"><span>{en}</span><span class="pt">{pt.split(' / ')[0]}</span></div></div>""" for zh, py, en, pt, _, _ in WORDS)
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{S}px;height:{S}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.wrap{{position:absolute;left:56px;right:56px;top:40px;bottom:44px;display:flex;flex-direction:column;}}
.head{{display:flex;justify-content:space-between;align-items:center;}}
.head img{{height:78px;}}
.badge{{background:#B8593A;color:#FBF6EE;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:22px;padding:9px 20px;border-radius:999px;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:72px;line-height:1.02;margin-top:26px;}}
h1 .a{{color:#B8593A;font-style:italic;}}
h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:40px;line-height:1.1;color:#726651;margin-top:6px;}}
h2 .a{{color:#B8593A;font-style:italic;}}
.cards{{display:flex;gap:20px;margin-top:36px;}}
.w{{flex:1;background:#fff;border-radius:24px;border-top:10px solid #C19D5F;padding:40px 10px 40px;text-align:center;box-shadow:0 10px 26px rgba(43,31,24,.08);}}
.w .zh{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:132px;line-height:1.05;}}
.w .py{{font-family:'DM Serif Display',serif;font-style:italic;font-size:56px;color:#B8593A;margin-top:2px;}}
.w .m{{display:flex;flex-direction:column;align-items:center;gap:10px;margin-top:24px;}}
.w .m span{{font-size:30px;font-weight:700;background:#F1E9DA;border-radius:999px;padding:5px 18px;}}
.w .m span.pt{{background:#E4ECEB;color:#3f5a59;}}
.ticket{{margin-top:auto;background:#B8593A;color:#FBF6EE;border-radius:24px;padding:9px;box-shadow:0 12px 30px rgba(184,89,58,.32);transform:rotate(-1.2deg);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:17px;padding:16px 26px;display:flex;align-items:center;gap:24px;}}
.ticket img{{width:118px;height:118px;border-radius:50%;object-fit:cover;object-position:center 30%;border:5px solid #FBF6EE;flex:none;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:44px;line-height:1.05;}}
.ticket .d{{font-size:27px;font-weight:700;margin-top:6px;}}
.ticket .u{{font-size:25px;font-weight:600;color:#F6DCC0;margin-top:2px;}}
</style></head><body><div class="bar"></div><div class="wrap">
  <div class="head"><img src="{bm.LOGO_COLOR}"><div class="badge">Mini aula &middot; Mini lesson</div></div>
  <h1>Your first <span class="a">3 words</span> in Mandarin.</h1>
  <h2>As suas primeiras <span class="a">3 palavras</span> em mandarim.</h2>
  <div class="cards">{cards}</div>
  <div class="ticket"><div class="in"><img src="{bm.MICHELLE}"><div>
    <div class="k">Learn more, free &middot; Aula grátis</div>
    <div class="d">Mon 12 Oct &middot; Seg 12 out &middot; 18h30 &middot; with Michelle</div>
    <div class="u">patiolanguage.pt/taster</div></div></div></div>
</div></body></html>"""


def reel_cover():
    """Reel cover, 1080x1920. Everything sits inside the middle 1080x1440,
    the part the Instagram profile grid shows (y 240 to 1680)."""
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1080px;height:1920px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.safe{{position:absolute;left:60px;right:60px;top:280px;height:1360px;display:flex;flex-direction:column;}}
.head{{display:flex;justify-content:space-between;align-items:center;}}
.head img{{height:92px;}}
.badge{{background:#B8593A;color:#FBF6EE;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:30px;padding:12px 26px;border-radius:999px;}}
.ph{{position:relative;margin-top:30px;height:560px;flex:none;}}
.ph img.bg{{width:100%;height:100%;object-fit:cover;object-position:center 35%;border-radius:32px;display:block;box-shadow:0 14px 34px rgba(43,31,24,.16);}}
.zh{{position:absolute;left:34px;bottom:30px;background:#fff;border-radius:26px;padding:14px 30px;display:flex;align-items:baseline;gap:16px;box-shadow:0 10px 26px rgba(0,0,0,.2);}}
.zh b{{font-family:'Noto Serif SC',serif;font-weight:600;font-size:84px;line-height:1;}}
.zh i{{font-family:'DM Serif Display',serif;font-size:52px;color:#B8593A;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:124px;line-height:.98;margin-top:44px;}}
h1 .a{{color:#B8593A;font-style:italic;}}
h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:66px;line-height:1.08;color:#4a4038;margin-top:16px;}}
h2 .a{{color:#B8593A;font-style:italic;}}
.sound{{margin-top:auto;display:inline-flex;align-self:flex-start;align-items:center;gap:14px;background:#B8593A;color:#FBF6EE;font-weight:700;font-size:40px;padding:14px 30px;border-radius:999px;}}
</style></head><body><div class="bar"></div>
<div class="safe">
  <div class="head"><img src="{bm.LOGO_COLOR}"><div class="badge">Mini aula &middot; Mini lesson</div></div>
  <div class="ph"><img class="bg" src="{HK}"><div class="zh"><b>你好</b><i>nǐ hǎo</i></div></div>
  <h1>Your first <span class="a">3 words</span> in Mandarin.</h1>
  <h2>As suas primeiras <span class="a">3 palavras</span> em mandarim.</h2>
  <div class="sound">&#128266; Ligue o som &middot; Turn the sound on</div>
</div></body></html>"""


if __name__ == "__main__":
    for n, html in enumerate(slides(), start=1):
        name = f"words-{n}-{W}x{H}"
        path = os.path.join(OUT, name + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--window-size={W},{H}", "--virtual-time-budget=6000",
            f"--screenshot={os.path.join(OUT, name + '.png')}", path],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("rendered", name + ".png")
    # Facebook: one square image, all 3 words
    path = os.path.join(OUT, "words-fb-1080x1080.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(fb_single())
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", "--window-size=1080,1080", "--virtual-time-budget=6000",
        f"--screenshot={path.replace('.html', '.png')}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered words-fb-1080x1080.png")
