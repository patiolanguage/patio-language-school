#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build Patio Language School LinkedIn personal-profile banner (1584x396)."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700;800&display=swap" rel="stylesheet">')

# ---- personal profile banner (centered stack) ----
PROFILE = dict(w=1584, h=396)
PROFILE_CSS = """
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{w}px;height:{h}px;}}
.canvas{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:#EDE8DF;
  font-family:'Barlow',sans-serif;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:20px;}}
.logo{{height:132px;object-fit:contain;display:block;}}
.pt{{color:#B8593A;font-weight:800;font-size:52px;letter-spacing:.10em;line-height:1;}}
.tag{{color:#3B342C;font-weight:600;font-size:25px;letter-spacing:.14em;line-height:1;}}
.dots{{display:flex;gap:20px;margin-top:6px;}}
.dot{{width:19px;height:19px;border-radius:50%;}}
.d1{{background:#C19D5F;}} .d2{{background:#B8593A;}}
.d3{{background:#617C7B;}} .d4{{background:#726651;}}
"""

def build_profile(fname):
    css = PROFILE_CSS.format(**PROFILE)
    body = (f'<div class="canvas">'
        f'<img class="logo" src="{LOGO_COLOR}">'
        f'<div class="pt">EUROPEAN PORTUGUESE</div>'
        f'<div class="tag">LANGUAGE SCHOOL &amp; CULTURAL COMMUNITY &middot; LAGOS</div>'
        f'<div class="dots"><span class="dot d1"></span><span class="dot d2"></span>'
        f'<span class="dot d3"></span><span class="dot d4"></span></div>'
        f'</div>')
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname, PROFILE["w"], PROFILE["h"]

# ---- company page cover (horizontal: logo left, text right) ----
COMPANY = dict(w=1128, h=191)
COMPANY_CSS = """
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{w}px;height:{h}px;}}
.canvas{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:#EDE8DF;
  font-family:'Barlow',sans-serif;display:flex;align-items:center;justify-content:center;
  gap:40px;padding:0 60px;}}
.logo{{height:118px;object-fit:contain;display:block;}}
.divider{{width:3px;height:104px;background:#C19D5F;border-radius:2px;opacity:.7;}}
.text{{display:flex;flex-direction:column;gap:12px;}}
.pt{{color:#B8593A;font-weight:800;font-size:40px;letter-spacing:.08em;line-height:1;}}
.tag{{color:#3B342C;font-weight:600;font-size:19px;letter-spacing:.12em;line-height:1;}}
.dots{{display:flex;gap:15px;margin-top:5px;}}
.dot{{width:15px;height:15px;border-radius:50%;}}
.d1{{background:#C19D5F;}} .d2{{background:#B8593A;}}
.d3{{background:#617C7B;}} .d4{{background:#726651;}}
"""

def build_company(fname):
    css = COMPANY_CSS.format(**COMPANY)
    body = (f'<div class="canvas">'
        f'<img class="logo" src="{LOGO_COLOR}">'
        f'<div class="divider"></div>'
        f'<div class="text">'
        f'<div class="pt">EUROPEAN PORTUGUESE</div>'
        f'<div class="tag">LANGUAGE SCHOOL &amp; CULTURAL COMMUNITY &middot; LAGOS</div>'
        f'<div class="dots"><span class="dot d1"></span><span class="dot d2"></span>'
        f'<span class="dot d3"></span><span class="dot d4"></span></div>'
        f'</div></div>')
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname, COMPANY["w"], COMPANY["h"]

def render(fname, w, h):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    render(*build_profile("linkedin-banner-1584x396.html"))
    render(*build_company("linkedin-company-cover-1128x191.html"))
    print("done")
