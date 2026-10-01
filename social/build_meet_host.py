#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build 'Meet your host - Arek Adeoye' set (EN + PT): IG Story, Reel cover, FB post.

Uses Arek's circular headshot (assets/img/arek.png) + his bio.
Brand: DM Serif Display + Barlow; gold #C19D5F, terracota #B8593A,
teal #617C7B, chocolate #2B1F18, cream #FBF6EE. No em/en dashes.
PT is informal (tu). Native proofread (Sofia) recommended before posting.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
AREK = b64(os.path.join(IMG, "arek.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

STR = {
 "en": {
   "suffix": "",
   "eyebrow": "Meet your host",
   "role": "Patio Practical AI &middot; Web Project Studios",
   "bio_short": ("Twenty-five years building software, now focused on making AI genuinely "
                 "useful. He teaches the way he builds: in plain language, hands-on, and "
                 "grounded in what helps."),
   "bio_fb": ("Arek Adeoye has called Lagos home for six years and runs Web Project Studios, "
              "building practical AI tools and automation for real businesses. With twenty-five "
              "years in software, he teaches AI in plain language and hands-on, and designed "
              "these workshops so anyone can use it confidently in everyday life and work."),
   "reel_title": 'The <span class="a">person</span><br>behind the AI',
   "reel_tag": "Practical AI, in plain language.",
   "register": "Register",
 },
 "pt": {
   "suffix": "-pt",
   "eyebrow": "Conhece o teu formador",
   "role": "Patio Practical AI &middot; Web Project Studios",
   "bio_short": ("Vinte e cinco anos a criar software, agora focado em tornar a IA "
                 "verdadeiramente útil. Ensina como constrói: em linguagem simples, com "
                 "mãos na massa e centrado no que realmente ajuda."),
   "bio_fb": ("O Arek Adeoye vive em Lagos há seis anos e dirige a Web Project Studios, "
              "criando ferramentas de IA e automação para empresas reais. Com vinte e cinco "
              "anos em software, ensina IA em linguagem simples e com mãos na massa, e criou "
              "estes workshops para que qualquer pessoa a use com confiança no dia a dia e no trabalho."),
   "reel_title": 'As <span class="a">pessoas</span><br>por trás da IA',
   "reel_tag": "IA prática, em linguagem simples.",
   "register": "Inscreve-te",
 },
}
URL = "patiolanguage.pt/ai"

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

BG_LIGHT = "background:radial-gradient(125% 90% at 50% 16%,#FEF6F1 0%,#F8E6DB 55%,#F0D3C2 100%);"
BG_TEAL = "background:radial-gradient(120% 85% at 50% 20%,#6f8988 0%,#5c7574 55%,#49605f 100%);"


def story(s):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:1080px;height:1920px;}}
.c{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Barlow',sans-serif;{BG_LIGHT}
  color:#2B1F18;display:flex;flex-direction:column;align-items:center;text-align:center;padding:170px 92px 240px;}}
.bar{{position:absolute;top:0;left:0;right:0;height:18px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:100px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.24em;text-transform:uppercase;font-size:32px;margin-top:28px;}}
.mid{{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;}}
.ring{{width:560px;height:560px;border-radius:50%;background:linear-gradient(135deg,#C19D5F,#B8593A);
  padding:9px;box-shadow:0 14px 40px rgba(43,31,24,.25);}}
.ring img{{width:100%;height:100%;border-radius:50%;display:block;background:#2B1F18;}}
.name{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:116px;line-height:1;margin-top:48px;}}
.role{{color:#4f6a69;font-weight:700;font-size:40px;margin-top:18px;}}
.bio{{color:#3f372f;font-size:48px;font-weight:500;line-height:1.42;margin-top:38px;}}
.url{{color:#726651;font-size:33px;font-weight:700;margin-top:8px;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<img class="logo" src="{LOGO_COLOR}">
<div class="eyebrow">{s['eyebrow']}</div>
<div class="mid">
  <div class="ring"><img src="{AREK}"></div>
  <div class="name">Arek Adeoye</div>
  <div class="role">{s['role']}</div>
  <div class="bio">{s['bio_short']}</div>
</div>
<div class="url">{URL}</div>
</div>"""
    render(f"meet-host-ig-story-1080x1920{s['suffix']}.html", page(css, body), 1080, 1920)


def reel(s):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:1080px;height:1920px;}}
.c{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Barlow',sans-serif;{BG_TEAL}
  color:#FBF6EE;display:flex;flex-direction:column;align-items:center;text-align:center;padding:190px 90px 240px;}}
.bar{{position:absolute;top:0;left:0;right:0;height:18px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{color:#F0D4A6;font-weight:700;letter-spacing:.28em;text-transform:uppercase;font-size:34px;}}
.title{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:126px;line-height:.98;margin-top:20px;}}
.title .a{{color:#F0D4A6;font-style:italic;}}
.ring{{width:620px;height:620px;border-radius:50%;background:#FBF6EE;
  padding:12px;box-shadow:0 16px 50px rgba(0,0,0,.35);margin-top:58px;}}
.ring img{{width:100%;height:100%;border-radius:50%;display:block;background:#2B1F18;}}
.name{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:90px;line-height:1;margin-top:52px;}}
.tag{{color:#FBF0DF;font-size:58px;font-weight:600;line-height:1.15;margin-top:24px;}}
.logo{{height:74px;object-fit:contain;margin-top:auto;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<div class="eyebrow">{s['eyebrow']}</div>
<div class="title">{s['reel_title']}</div>
<div class="ring"><img src="{AREK}"></div>
<div class="name">Arek Adeoye</div>
<div class="tag">{s['reel_tag']}</div>
<img class="logo" src="{LOGO_WHITE}">
</div>"""
    render(f"meet-host-reel-1080x1920{s['suffix']}.html", page(css, body), 1080, 1920)


def fb(s):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:1080px;height:1080px;}}
.c{{position:relative;width:1080px;height:1080px;overflow:hidden;font-family:'Barlow',sans-serif;
  {BG_TEAL}color:#FBF6EE;padding:88px 80px 76px;display:flex;flex-direction:column;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{color:#F0D4A6;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:26px;}}
.row{{display:flex;align-items:center;gap:44px;margin-top:30px;}}
.ring{{width:360px;height:360px;flex:none;border-radius:50%;background:#FBF6EE;
  padding:9px;box-shadow:0 10px 30px rgba(0,0,0,.28);}}
.ring img{{width:100%;height:100%;border-radius:50%;display:block;background:#2B1F18;}}
.who .name{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:90px;line-height:1;}}
.who .role{{color:#F0D4A6;font-weight:700;font-size:33px;margin-top:12px;}}
.bio{{color:#F3E7D3;font-size:39px;font-weight:500;line-height:1.44;margin-top:40px;}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;}}
.cta{{color:#FBF6EE;font-weight:700;font-size:32px;}}
.cta span{{color:#F0D4A6;}}
.logo{{height:58px;object-fit:contain;}}
"""
    body = f"""<div class="c"><div class="bar"></div>
<div class="eyebrow">{s['eyebrow']}</div>
<div class="row">
  <div class="ring"><img src="{AREK}"></div>
  <div class="who"><div class="name">Arek Adeoye</div>
    <div class="role">{s['role']}</div></div>
</div>
<div class="bio">{s['bio_fb']}</div>
<div class="foot">
  <div class="cta">{s['register']} <span>{URL}</span></div>
  <img class="logo" src="{LOGO_WHITE}">
</div>
</div>"""
    render(f"meet-host-fb-1080x1080{s['suffix']}.html", page(css, body), 1080, 1080)


if __name__ == "__main__":
    for lang in ("en", "pt"):
        s = STR[lang]
        story(s); reel(s); fb(s)
    print("done")
