#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""Sound of the week" carousels x3 for the Phonetics Workshop. EN and PT on every slide.
Same format as the Mandarin "first 3 words" carousel (build_mandarin_words.py).

One carousel per sound on the launch flyer:
  1  O ão nasal        não, mão, cão
  2  O s que soa "ch"  Lagos, pastel de nata, dois
  3  lh, nh e r        trabalho, vinho, rua

Slides (1080x1350): 1 cover, 2-4 one word each, 5 workshop CTA.
Audio Reels can be added later from Sofia's WhatsApp voice notes, one per word.

Outputs: social/Phonetics/sounds/sounds{1..3}-{1..5}-1080x1350.png
         social/Phonetics/sounds/sounds{1..3}-fb-1080x1080.png  (Facebook, one image)
Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Phonetics", "sounds")
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350

# word, sounds like, meaning EN, tip EN, tip PT
SETS = [
    dict(
        key="ao", n=1,
        title_en='The nasal <span class="a">ão</span>', title_pt='O <span class="a">ão</span> nasal',
        sub_en="Say “ow”, then send it through your nose.",
        sub_pt="Diga “ow” e deixe o som sair pelo nariz.",
        bubble="não",
        words=[
            ("não", "nowng", "no", "The most useful word in Portugal.", "A palavra mais útil em Portugal."),
            ("mão", "mowng", "hand", "Same sound, new letter.", "O mesmo som, outra letra."),
            ("cão", "kowng", "dog", "Not “cow”. Hum it through your nose.", "Não é “cow”. Faça o som pelo nariz."),
        ],
    ),
    dict(
        key="s", n=2,
        title_en='The <span class="a">“sh”</span> s', title_pt='O s que soa <span class="a">“ch”</span>',
        sub_en="At the end of a syllable, s sounds like “sh”.",
        sub_pt="No fim de uma sílaba, o s soa “ch”.",
        bubble="Lagos",
        words=[
            ("Lagos", "LAH-goosh", "our town", "Locals never say “Lah-gos”.", "Ninguém cá diz “Lá-gos”."),
            ("pastel de nata", "push-TEL de NAH-tuh", "custard tart", "The s before t becomes “sh”.", "O s antes do t soa “ch”."),
            ("dois", "doysh", "two", "Handy at the café: dois cafés.", "Útil no café: dois cafés."),
        ],
    ),
    dict(
        key="lhnhr", n=3,
        title_en='<span class="a">lh</span>, <span class="a">nh</span> and <span class="a">r</span>',
        title_pt='<span class="a">lh</span>, <span class="a">nh</span> e <span class="a">r</span>',
        sub_en="Three sounds English doesn’t quite have.",
        sub_pt="Três sons que o inglês não tem.",
        bubble="vinho",
        words=[
            ("trabalho", "truh-BAH-lyoo", "work", "lh is like the “lli” in million.", "O lh soa como “lli” em million."),
            ("vinho", "VEE-nyoo", "wine", "nh is like the “ny” in canyon.", "O nh soa como “ny” em canyon."),
            ("rua", "HROO-uh", "street", "An r at the start comes from the throat.", "O r no início vem da garganta."),
        ],
    ),
]

CSS = f"""<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#617C7B,#C19D5F);}}
.logo{{position:absolute;top:44px;left:56px;height:84px;}}
.count{{position:absolute;top:66px;right:56px;font-weight:700;letter-spacing:.16em;color:#617C7B;font-size:34px;}}
.dots{{position:absolute;bottom:44px;left:0;right:0;display:flex;justify-content:center;gap:14px;}}
.dots i{{width:14px;height:14px;border-radius:50%;background:#E3D6C0;display:block;}}
.dots i.on{{background:#617C7B;}}
.swipe{{position:absolute;bottom:84px;right:56px;font-weight:700;font-size:36px;color:#617C7B;}}
/* cover */
.ph{{position:absolute;left:56px;right:56px;top:160px;height:290px;width:calc(100% - 112px);object-fit:cover;object-position:center 50%;border-radius:30px;box-shadow:0 14px 34px rgba(43,31,24,.16);}}
.bub{{position:absolute;left:86px;top:560px;background:#fff;border-radius:26px;padding:12px 32px 16px;box-shadow:0 10px 26px rgba(0,0,0,.2);
  font-family:'DM Serif Display',serif;font-size:76px;line-height:1;}}
.badge{{position:absolute;left:56px;top:476px;display:flex;align-items:center;gap:24px;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:58px;line-height:1.05;padding:16px 44px 16px 18px;border-radius:40px;}}
.badge .tg{{background:#C19D5F;color:#2B1F18;font-size:44px;padding:20px 22px;border-radius:30px;align-self:stretch;display:flex;align-items:center;}}
.badge small{{display:block;font-size:40px;font-weight:600;color:#DDE7E6;margin-top:4px;}}
.cover{{position:absolute;left:56px;right:56px;top:650px;}}
.cover h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:144px;line-height:1.0;}}
.cover h1 .a,.cover h2 .a{{color:#B8593A;font-style:italic;}}
.cover h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:86px;line-height:1.1;color:#726651;margin-top:10px;}}
.cover .how{{margin-top:30px;font-size:64px;font-weight:700;line-height:1.22;}}
.cover .how b{{color:#3f5a59;}}
/* word */
.card{{position:absolute;left:56px;right:56px;top:170px;bottom:150px;background:#fff;border-radius:34px;box-shadow:0 14px 34px rgba(43,31,24,.08);
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:40px;border-top:16px solid #C19D5F;}}
.wd{{font-family:'DM Serif Display',serif;font-size:270px;line-height:1.0;}}
.wd.mid{{font-size:210px;}}
.wd.long{{font-size:164px;}}
.like{{margin-top:22px;font-size:40px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#617C7B;}}
.say{{font-family:'DM Serif Display',serif;font-style:italic;font-size:104px;color:#B8593A;line-height:1.05;}}
.say.long{{font-size:80px;}}
.mean{{margin-top:44px;}}
.mean span{{font-size:68px;font-weight:700;background:#F1E9DA;border-radius:999px;padding:12px 40px;}}
.tip{{margin-top:52px;font-size:58px;color:#2B1F18;font-weight:600;line-height:1.3;}}
.tip b{{color:#3f5a59;}}
/* cta */
.cta{{position:absolute;left:56px;right:56px;top:170px;}}
.cta h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:112px;line-height:1.02;}}
.cta h1 .a,.cta h2 .a{{color:#B8593A;font-style:italic;}}
.cta h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:72px;line-height:1.1;color:#726651;margin-top:14px;}}
.ticket{{margin-top:50px;background:#B8593A;color:#FBF6EE;border-radius:26px;padding:10px;transform:rotate(-2deg);box-shadow:0 14px 34px rgba(184,89,58,.35);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:18px;padding:34px 40px;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:94px;line-height:1.0;}}
.ticket .k2{{font-family:'DM Serif Display',serif;font-size:62px;line-height:1.05;margin-top:6px;color:#F6DCC0;}}
.ticket .d{{font-size:60px;font-weight:700;margin-top:22px;}}
.ticket .d2{{font-size:52px;font-weight:600;margin-top:6px;}}
.ticket .p{{font-family:'DM Serif Display',serif;font-size:96px;line-height:1;margin-top:24px;}}
.ticket .p small{{font-family:'Barlow',sans-serif;font-size:50px;font-weight:700;margin-left:14px;}}
.ticket .u{{font-size:54px;font-weight:700;margin-top:24px;background:#FBF6EE;color:#B8593A;display:inline-block;padding:10px 28px;border-radius:999px;}}
</style>"""

REEL_CSS = """<style>
html,body{width:1080px;height:1920px;}
.stage{position:absolute;left:0;top:330px;width:1080px;height:1350px;}
.sound{position:absolute;top:200px;left:0;right:0;text-align:center;}
.sound span{display:inline-block;background:#B8593A;color:#FBF6EE;font-family:'Barlow',sans-serif;font-weight:700;font-size:46px;
  padding:16px 38px;border-radius:999px;box-shadow:0 10px 26px rgba(184,89,58,.35);}
</style>"""

def frame(n, body, swipe=True, reel=False):
    """reel=True: 1080x1920 frame for the audio Reel (build_phonetics_reel.py), no swipe hint or dots."""
    if reel:
        return (f'<!DOCTYPE html><html><head>{bm.FONTS}{CSS}{REEL_CSS}</head><body><div class="bar"></div>'
                f'<div class="sound"><span>&#128266; Ligue o som &middot; Turn the sound on</span></div>'
                f'<div class="stage"><img class="logo" src="{bm.LOGO_COLOR}">{body}</div></body></html>')
    dots = "".join(f'<i class="{"on" if k == n else ""}"></i>' for k in range(1, 6))
    sw = '<div class="swipe">Deslize / Swipe &rarr;</div>' if swipe else ""
    return (f'<!DOCTYPE html><html><head>{bm.FONTS}{CSS}</head><body><div class="bar"></div>'
            f'<img class="logo" src="{bm.LOGO_COLOR}"><div class="count">{n}/5</div>'
            f'{body}{sw}<div class="dots">{dots}</div></body></html>')

def slides(s, reel=False):
    out = [frame(1, f"""
<img class="ph" src="{bm.b64_photo(os.path.join(bm.IMG, 'phonetics-tiles-' + s['key'] + '.jpg'))}">
<div class="badge"><span class="tg">{s['n']}/3</span><div>Sound of the week<small>Som da semana</small></div></div>
<div class="cover">
  <h1>{s['title_en']}.</h1>
  <h2>{s['title_pt']}.</h2>
  <div class="how">{s['sub_en']}<br><b>{s['sub_pt']}</b></div>
</div>""", reel=reel)]
    for i, (wd, like, mean, tip_en, tip_pt) in enumerate(s["words"], start=2):
        lw = " long" if len(wd) > 10 else " mid" if len(wd) > 6 else ""
        ls = " long" if len(like) > 12 else ""
        out.append(frame(i, f"""
<div class="card">
  <div class="wd{lw}">{wd}</div>
  <div class="mean"><span>{mean}</span></div>
  <div class="tip">{tip_en}<br><b>{tip_pt}</b></div>
</div>""", reel=reel))
    out.append(frame(5, """
<div class="cta">
  <h1>Practise these sounds <span class="a">with Sofia</span>.</h1>
  <h2>Pratique estes sons <span class="a">com a Sofia</span>.</h2>
  <div class="ticket"><div class="in">
    <div class="k">Phonetics Workshop</div>
    <div class="k2">Workshop de fonética</div>
    <div class="d">2 &amp; 6 November &middot; 9h15 to 10h45</div>
    <div class="d2">2 e 6 de novembro &middot; 9h15 às 10h45</div>
    <div class="p">&euro;35<small>2 sessions &middot; 2 sessões</small></div>
    <div class="u">WhatsApp +351 928 129 560</div>
  </div></div>
</div>""", swipe=False, reel=reel))
    return out

def fb_single(s):
    """One square image for Facebook: the sound, its 3 words and the workshop."""
    S = 1080
    cards = "".join(f"""<div class="w"><div class="wd">{wd}</div>
      <div class="m">{mean}</div></div>""" for wd, like, mean, _, _ in s["words"])
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{S}px;height:{S}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#617C7B,#C19D5F);}}
.wrap{{position:absolute;left:56px;right:56px;top:40px;bottom:44px;display:flex;flex-direction:column;}}
.head{{display:flex;justify-content:space-between;align-items:center;}}
.head img{{height:78px;}}
.badge{{display:flex;align-items:center;gap:12px;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:28px;padding:8px 22px 8px 10px;border-radius:999px;}}
.badge .tg{{background:#C19D5F;color:#2B1F18;font-size:20px;letter-spacing:.12em;padding:6px 12px;border-radius:999px;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:84px;line-height:1.02;margin-top:24px;}}
h1 .a,h2 .a{{color:#B8593A;font-style:italic;}}
h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:52px;line-height:1.1;color:#726651;margin-top:4px;}}
.how{{font-size:32px;font-weight:600;margin-top:14px;}}
.cards{{display:flex;gap:20px;margin-top:30px;flex:1;margin-bottom:34px;}}
.w{{flex:1;background:#fff;border-radius:24px;border-top:10px solid #C19D5F;padding:40px 12px;text-align:center;box-shadow:0 10px 26px rgba(43,31,24,.08);
  display:flex;flex-direction:column;align-items:center;justify-content:center;}}
.w .wd{{font-family:'DM Serif Display',serif;font-size:80px;line-height:1.05;}}
.w .say{{white-space:nowrap;font-family:'DM Serif Display',serif;font-style:italic;font-size:34px;color:#B8593A;margin-top:8px;line-height:1.1;}}
.w .m{{font-size:34px;font-weight:700;background:#F1E9DA;border-radius:999px;padding:5px 18px;margin-top:16px;}}
.ticket{{margin-top:auto;background:#B8593A;color:#FBF6EE;border-radius:24px;padding:9px;box-shadow:0 12px 30px rgba(184,89,58,.32);transform:rotate(-1.2deg);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:17px;padding:18px 28px;display:flex;align-items:center;justify-content:space-between;gap:20px;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:58px;line-height:1.0;}}
.ticket .d{{font-size:30px;font-weight:700;margin-top:8px;}}
.ticket .u{{font-size:28px;font-weight:600;color:#F6DCC0;margin-top:4px;}}
.ticket .p{{font-family:'DM Serif Display',serif;font-size:80px;line-height:1;flex:none;}}
</style></head><body><div class="bar"></div><div class="wrap">
  <div class="head"><img src="{bm.LOGO_COLOR}"><div class="badge"><span class="tg">{s['n']}/3</span>Sound of the week</div></div>
  <h1>{s['title_en']}.</h1>
  <h2>{s['title_pt']}.</h2>
  <div class="how">{s['sub_en']}</div>
  <div class="cards">{cards}</div>
  <div class="ticket"><div class="in"><div>
    <div class="k">Phonetics Workshop</div>
    <div class="d">2 &amp; 6 November &middot; 9h15 to 10h45</div>
    <div class="u">With Sofia &middot; both sessions &middot; WhatsApp +351 928 129 560</div></div>
    <div class="p">&euro;35</div></div></div>
</div></body></html>"""

def render(html, name, w, h):
    path = os.path.join(OUT, name + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}", "--virtual-time-budget=6000",
        f"--screenshot={os.path.join(OUT, name + '.png')}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", name + ".png")

if __name__ == "__main__":
    for s in SETS:
        for n, html in enumerate(slides(s), start=1):
            render(html, f"sounds{s['n']}-{n}-{W}x{H}", W, H)
        render(fb_single(s), f"sounds{s['n']}-fb-1080x1080", 1080, 1080)
