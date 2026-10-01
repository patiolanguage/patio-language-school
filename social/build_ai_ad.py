#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Super-simple 2-slide IG/FB ad for the Patio AI workshops (1080x1920).

Slide 1: clean, enticing (brand + headline + photo + Learn more button).
Slide 2: same photo blurred with a centered call-to-action card.
Brand: DM Serif Display + Barlow. No em/en dashes.
"""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H = 1080, 1920

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
PHOTO = b64(os.path.join(IMG, "ai-workshop-photo.jpg"), "image/jpeg")

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800'
    '&family=DM+Serif+Display&display=swap" rel="stylesheet">')

LINK_SVG = ('<svg width="42" height="42" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>'
    '<path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>')

def page(css, body):
    return f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'

def render(fname, html, w=W, h=H):
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--default-background-color=00000000",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)


TXT = {
  "en": dict(eyebrow="Patio Practical AI &middot; Lagos", title="AI for Life &amp; Business",
             sub="Practical, hands-on workshops in Lagos", meta="Small groups, leave with results",
             btn="Learn more"),
  "pt": dict(eyebrow="Patio Practical AI &middot; Lagos", title="IA para a Vida e o Negócio",
             sub="Workshops práticos e presenciais em Lagos", meta="Grupos pequenos, sai com resultados",
             btn="Sabe mais"),
}

def creative(kind, w, h, fname, lang="en", show_button=True, cta=None):
    t = TXT[lang]
    P = {
      "story": dict(top="120px 96px 0", logo=132, eb=50, h1=120, sub=80, rule="148px 10px",
                    meta=52, photo=880, btn=60, btnpad="38px 72px", btnbot=150),
      "ig":    dict(top="80px 84px 0", logo=112, eb=44, h1=96, sub=64, rule="132px 9px",
                    meta=46, photo=560, btn=52, btnpad="32px 60px", btnbot=90),
      "fb":    dict(top="60px 74px 0", logo=96, eb=38, h1=80, sub=52, rule="116px 8px",
                    meta=42, photo=430, btn=46, btnpad="28px 52px", btnbot=70),
    }[kind]
    rw, rh = P["rule"].split()
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;
  background:linear-gradient(180deg,#FDFBF6 0%,#F6EFE3 100%);}}
.top{{padding:{P['top']};}}
.logo{{height:{P['logo']}px;object-fit:contain;}}
.eyebrow{{color:#B8593A;font-weight:700;letter-spacing:.18em;text-transform:uppercase;font-size:{P['eb']}px;margin-top:36px;}}
h1{{color:#2B1F18;font-weight:800;font-size:{P['h1']}px;line-height:1.01;margin-top:22px;letter-spacing:-.01em;}}
h1 .sub{{display:block;font-weight:500;font-size:{P['sub']}px;color:#3f372f;margin-top:14px;}}
.rule{{width:{rw};height:{rh};background:#617C7B;border-radius:6px;margin-top:38px;}}
.meta{{color:#5a5047;font-weight:700;font-size:{P['meta']}px;margin-top:34px;}}
.photo{{position:absolute;left:0;right:0;bottom:0;height:{P['photo']}px;background-image:url('{PHOTO}');
  background-size:cover;background-position:center 40%;}}
.photo::before{{content:"";position:absolute;top:-1px;left:0;right:0;height:170px;
  background:linear-gradient(180deg,#F6EFE3 0%,rgba(246,239,227,0) 100%);}}
.btn{{position:absolute;left:50%;transform:translateX(-50%);bottom:{P['btnbot']}px;
  display:flex;align-items:center;gap:22px;background:#fff;color:#2B1F18;
  font-weight:700;font-size:{P['btn']}px;padding:{P['btnpad']};border-radius:999px;
  box-shadow:0 18px 46px rgba(0,0,0,.28);}}
.btn svg{{color:#617C7B;}}
"""
    label = cta or t["btn"]
    btn_html = f'<div class="btn">{LINK_SVG}<span>{label}</span></div>' if show_button else ''
    body = f"""<div class="c">
  <div class="top">
    <img class="logo" src="{LOGO_COLOR}">
    <div class="eyebrow">{t['eyebrow']}</div>
    <h1>{t['title']}<span class="sub">{t['sub']}</span></h1>
    <div class="rule"></div>
    <div class="meta">{t['meta']}</div>
  </div>
  <div class="photo"></div>
  {btn_html}
</div>"""
    render(fname, page(css, body), w, h)


def slide2(kind, w, h, fname, lang="en"):
    t = TXT[lang]
    C = {
      "story": dict(cw=820, pad="80px 72px 72px", logo=128, ct=82, cs=50, cb=60, url=42),
      "ig":    dict(cw=830, pad="72px 66px 64px", logo=120, ct=76, cs=47, cb=56, url=41),
      "fb":    dict(cw=880, pad="60px 60px 56px", logo=110, ct=68, cs=43, cb=52, url=39),
    }[kind]
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{w}px;height:{h}px;}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;font-family:'Barlow',sans-serif;
  background:#2B1F18;}}
.bg{{position:absolute;inset:-60px;background-image:url('{PHOTO}');background-size:cover;
  background-position:center 40%;filter:blur(26px) brightness(.7);}}
.scrim{{position:absolute;inset:0;background:rgba(43,31,24,.34);}}
.card{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:{C['cw']}px;
  background:#fff;border-radius:44px;padding:{C['pad']};text-align:center;
  box-shadow:0 30px 80px rgba(0,0,0,.4);}}
.card .logo{{height:{C['logo']}px;object-fit:contain;}}
.card .t{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:{C['ct']}px;line-height:1.03;margin-top:30px;}}
.card .s{{color:#6a5f52;font-weight:500;font-size:{C['cs']}px;margin-top:18px;}}
.card .btn{{display:block;background:#B8593A;color:#fff;font-weight:700;font-size:{C['cb']}px;
  padding:36px;border-radius:22px;margin-top:48px;}}
.card .url{{color:#9a8f7f;font-weight:600;font-size:{C['url']}px;margin-top:28px;letter-spacing:.02em;}}
"""
    body = f"""<div class="c">
  <div class="bg"></div><div class="scrim"></div>
  <div class="card">
    <img class="logo" src="{LOGO_COLOR}">
    <div class="t">{t['title']}</div>
    <div class="s">{t['meta']}</div>
    <div class="btn">{t['btn']}</div>
    <div class="url">patiolanguage.pt/ai</div>
  </div>
</div>"""
    render(fname, page(css, body), w, h)


if __name__ == "__main__":
    # Slide 1 (creative)
    creative("story", 1080, 1920, "ai-ad-story-1080x1920.html", lang="en", show_button=True)
    creative("ig", 1080, 1350, "ai-ad-igpost-1080x1350.html", lang="en", show_button=True)
    creative("fb", 1080, 1080, "ai-ad-fbpost-pt-1080x1080.html", lang="pt", show_button=False)
    creative("fb", 1080, 1080, "ai-ad-fbpost-en-1080x1080.html", lang="en", show_button=False)
    # Slide 2 (blurred CTA end card) in all sizes
    slide2("story", 1080, 1920, "ai-ad-slide2-story-1080x1920.html", lang="en")
    slide2("ig", 1080, 1350, "ai-ad-slide2-igpost-1080x1350.html", lang="en")
    slide2("fb", 1080, 1080, "ai-ad-slide2-fbpost-pt-1080x1080.html", lang="pt")
    # WhatsApp message image (slide 1, with the link shown as the CTA)
    creative("ig", 1080, 1350, "ai-ad-whatsapp-1080x1350.html", lang="en",
             show_button=True, cta="patiolanguage.pt/ai")
    print("done")
