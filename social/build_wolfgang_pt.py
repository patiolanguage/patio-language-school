#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wolfgang PT testimonial + CTA in carousel (1080x1350), story (1080x1920), FB (1080x1080)."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
LOGO_WHITE = b64(os.path.join(IMG, "Patio-Language-School-Logo-White.png"))
CTA_PHOTO = b64(os.path.join(IMG, "class-conversation.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

# European Portuguese (matches website /pt/)
QUOTE = ("Valorizo imenso as minhas aulas individuais com a Sofia Nabais. Trabalha de forma "
    "sistem\u00e1tica, com \u00f3timos materiais, e explica a gram\u00e1tica mais dif\u00edcil com paci\u00eancia e "
    "clareza. Segue de bom grado as perguntas que surgem e adora mostrar tamb\u00e9m a cultura: "
    "escritores, arquitetura, cozinha regional, concertos. Profissional e muito atenciosa, "
    "deixa-me motivado depois de cada aula.")
T = dict(
    eyebrow="O que dizem os alunos",
    since="Mais um, depois do de ontem",
    name="Wolfgang Helmut Pump",
    role="Aluno particular &middot; Alemanha",
    cta_eyebrow="Inscri\u00e7\u00f5es abertas &middot; Lagos",
    title_pre="Quer aulas como ", title_accent="estas?",
    sub="Aulas individuais e em pequenos grupos<br>de portugu\u00eas europeu &middot; Lagos",
    msg="Fale connosco para se inscrever",
    l1_pre="WhatsApp ", l1_g="+351 928 129 560",
    l2_pre="Siga ", l2_g="@patiolanguage",
)

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def write(fname, html):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)

def render(fname, W, H):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

def testimonial(fname, W, H, p):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#FBF6EE;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:{p['pad']};text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:{p['eyeTop']}px;left:0;right:0;text-align:center;
  color:#726651;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:{p['eye']}px;}}
.since{{position:absolute;top:{p['sinceTop']}px;left:0;right:0;text-align:center;
  color:#B8593A;font-weight:600;font-style:italic;font-size:{p['since']}px;font-family:'DM Serif Display',serif;}}
.mark{{font-family:'DM Serif Display',serif;color:#C19D5F;font-size:{p['mark']}px;
  line-height:.4;height:{p['markH']}px;margin-bottom:6px;}}
.quote{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:{p['quote']}px;
  line-height:1.32;font-style:italic;}}
.rule{{width:66px;height:4px;background:#B8593A;border-radius:3px;margin:{p['ruleM']};}}
.name{{color:#B8593A;font-weight:700;font-size:{p['name']}px;letter-spacing:.01em;}}
.role{{color:#726651;font-weight:600;font-size:{p['role']}px;letter-spacing:.14em;
  text-transform:uppercase;margin-top:9px;}}
.logo{{position:absolute;bottom:{p['logoBot']}px;left:0;right:0;margin:0 auto;height:{p['logo']}px;
  display:block;object-fit:contain;}}
.count{{position:absolute;bottom:{p['logoBot']}px;right:72px;color:#726651;font-weight:700;
  font-size:26px;letter-spacing:.1em;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">{T["eyebrow"]}</div>'
        f'<div class="since">{T["since"]}</div>'
        f'<div class="mark">&ldquo;</div>'
        f'<div class="quote">{QUOTE}</div>'
        f'<div class="rule"></div>'
        f'<div class="name">{T["name"]}</div>'
        f'<div class="role">{T["role"]}</div>'
        f'<img class="logo" src="{LOGO_COLOR}">'
        + (f'<div class="count">1/2</div>' if p.get('count') else '')
        + f'</div>')
    write(fname, page(css, body))
    render(fname, W, H)

def cta(fname, W, H, p):
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Barlow',sans-serif;background:#2B1F18;padding:{p['pad']};
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{position:absolute;top:{p['eyeTop']}px;left:0;right:0;color:#E0A868;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;font-size:{p['eye']}px;}}
.stars{{color:#E0A868;font-size:{p['stars']}px;letter-spacing:.12em;margin-bottom:16px;}}
.title{{font-family:'DM Serif Display',serif;color:#FBF6EE;font-size:{p['title']}px;line-height:1.03;}}
.title .a{{color:#E0A868;font-style:italic;}}
.sub{{color:#F1E3CE;font-size:{p['sub']}px;font-weight:500;margin-top:18px;line-height:1.4;}}
.photo{{width:100%;height:{p['photo']}px;object-fit:cover;object-position:center 32%;
  border-radius:22px;border:5px solid #C19D5F;margin:{p['photoM']};
  box-shadow:0 14px 34px rgba(0,0,0,.4);}}
.msg{{color:#F1E3CE;font-size:{p['msg']}px;font-weight:500;margin-bottom:{p['msgB']}px;}}
.cta{{display:inline-block;background:#B8593A;color:#FBF6EE;font-weight:700;font-size:{p['ctaF']}px;
  padding:{p['ctaP']};border-radius:60px;letter-spacing:.01em;}}
.line{{color:#EBDCC4;font-size:{p['line']}px;font-weight:600;margin-top:{p['lineM']}px;letter-spacing:.01em;}}
.line .g{{color:#E0A868;}}
.logo{{height:{p['logo']}px;object-fit:contain;display:block;margin:{p['logoM']}px auto 0;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">{T["cta_eyebrow"]}</div>'
        f'<div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<div class="title">{T["title_pre"]}<span class="a">{T["title_accent"]}</span></div>'
        f'<div class="sub">{T["sub"]}</div>'
        f'<img class="photo" src="{CTA_PHOTO}">'
        f'<div class="msg">{T["msg"]}</div>'
        f'<div class="cta">patiolanguage.pt</div>'
        f'<div class="line">{T["l1_pre"]}<span class="g">{T["l1_g"]}</span></div>'
        f'<div class="line">{T["l2_pre"]}<span class="g">{T["l2_g"]}</span></div>'
        f'<img class="logo" src="{LOGO_WHITE}"></div>')
    write(fname, page(css, body))
    render(fname, W, H)

# ---- presets ----
PORTRAIT_T = dict(pad="150px 108px", eyeTop=70, eye=24, sinceTop=112, since=27,
    mark=170, markH=80, quote=44, ruleM="40px auto 26px", name=36, role=25,
    logo=56, logoBot=60, count=True)
PORTRAIT_C = dict(pad="132px 90px 60px", eyeTop=60, eye=24, stars=40, title=78, sub=32,
    photo=322, photoM="34px 0 32px", msg=31, msgB=22, ctaF=37, ctaP="24px 56px",
    line=31, lineM=22, logo=54, logoM=32)

STORY_T = dict(pad="360px 108px", eyeTop=300, eye=24, sinceTop=344, since=27,
    mark=160, markH=76, quote=46, ruleM="40px auto 26px", name=38, role=25,
    logo=58, logoBot=300, count=False)
STORY_C = dict(pad="330px 96px", eyeTop=300, eye=24, stars=42, title=80, sub=33,
    photo=360, photoM="40px 0 36px", msg=32, msgB=22, ctaF=38, ctaP="26px 58px",
    line=32, lineM=24, logo=56, logoM=36)

SQUARE_T = dict(pad="96px 84px", eyeTop=56, eye=21, sinceTop=92, since=23,
    mark=118, markH=54, quote=34, ruleM="26px auto 18px", name=30, role=21,
    logo=46, logoBot=48, count=True)
SQUARE_C = dict(pad="80px 80px", eyeTop=52, eye=21, stars=34, title=60, sub=27,
    photo=250, photoM="26px 0 24px", msg=27, msgB=16, ctaF=32, ctaP="20px 48px",
    line=27, lineM=16, logo=46, logoM=24)

if __name__ == "__main__":
    testimonial("wolfgang-pt-1-testimonial-ig-1080x1350.html", 1080, 1350, PORTRAIT_T)
    cta("wolfgang-pt-2-cta-ig-1080x1350.html", 1080, 1350, PORTRAIT_C)
    testimonial("wolfgang-pt-1-testimonial-ig-story-1080x1920.html", 1080, 1920, STORY_T)
    cta("wolfgang-pt-2-cta-ig-story-1080x1920.html", 1080, 1920, STORY_C)
    testimonial("wolfgang-pt-1-testimonial-fb-1080x1080.html", 1080, 1080, SQUARE_T)
    cta("wolfgang-pt-2-cta-fb-1080x1080.html", 1080, 1080, SQUARE_C)
    print("done")
