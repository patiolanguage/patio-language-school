#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Second IG story frame for the event: host (Arek) + 'Tap to register'.
Clean bright brand look matching event-story (Option B). 1080x1920.
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

LOGO = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
AREK = b64(os.path.join(IMG, "arek.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display&display=swap" rel="stylesheet">')

URL = "patiolanguage.pt/ai"

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{width:{W}px;height:{H}px;}}
.c{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Barlow',sans-serif;
  background:radial-gradient(130% 95% at 50% 10%,#FFF9F0 0%,#FDEBDC 48%,#F7D9BE 100%);
  color:#2B1F18;display:flex;flex-direction:column;align-items:center;text-align:center;padding:150px 92px 230px;}}
.bar{{position:absolute;top:0;left:0;right:0;height:16px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{height:112px;object-fit:contain;}}
.eyebrow{{color:#A84A2C;font-weight:700;letter-spacing:.22em;text-transform:uppercase;font-size:34px;margin-top:26px;}}
.ring{{width:560px;height:560px;border-radius:50%;margin-top:52px;
  background:linear-gradient(135deg,#C19D5F,#B8593A);padding:12px;box-shadow:0 18px 50px rgba(43,31,24,.25);}}
.ring img{{width:100%;height:100%;border-radius:50%;display:block;background:#2B1F18;}}
.name{{font-family:'DM Serif Display',serif;font-size:110px;line-height:1;margin-top:44px;}}
.role{{color:#4f6a69;font-weight:700;font-size:40px;margin-top:16px;}}
.bio{{color:#3f372f;font-size:46px;font-weight:500;line-height:1.38;margin-top:34px;max-width:900px;}}
.foot{{margin-top:auto;display:flex;flex-direction:column;align-items:center;}}
.tap{{display:flex;align-items:center;gap:22px;background:linear-gradient(135deg,#C4674B,#B8593A);
  color:#FBF6EE;font-weight:700;font-size:58px;border-radius:999px;padding:30px 66px;
  box-shadow:0 16px 40px rgba(184,89,58,.45);}}
.tap .arrow{{font-size:58px;line-height:1;}}
.u{{color:#2B1F18;font-weight:700;font-size:40px;margin-top:20px;}}
"""

BODY = f"""<div class="c"><div class="bar"></div>
<img class="logo" src="{LOGO}">
<div class="eyebrow">Meet your host</div>
<div class="ring"><img src="{AREK}"></div>
<div class="name">Arek Adeoye</div>
<div class="role">Patio Practical AI</div>
<div class="bio">25 years in software. He teaches AI in plain language, hands-on, so anyone can use it with confidence.</div>
<div class="foot">
  <div class="tap"><span class="arrow">&#128071;</span><span>Tap to register</span></div>
  <div class="u">{URL}</div>
</div>
</div>"""

def main():
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{CSS}</style></head><body>{BODY}</body></html>'
    hp = os.path.join(SOCIAL, "event-story-frame2-1080x1920.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html)
    png = hp.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        "--default-background-color=00000000", f"--screenshot={png}", hp],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    main()
