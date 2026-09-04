#!/usr/bin/env python3
"""Window 'opening hours' sign for Patio Language School (A4 portrait).
Brand style: cream ground, chocolate text, gold/terracotta accents, colour logo.
Outputs a preview PNG and a print-ready A4 PDF (vector text). Portuguese.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-Color.png")

CREAM = "#FBF6EE"; CHOC = "#2B1F18"; GOLD = "#C19D5F"; TERRA = "#B8593A"; GALAO = "#726651"

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()
LOGO_B64 = b64(LOGO)

HTML = f"""<!DOCTYPE html><html><head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
<style>
  @page {{ size: A4; margin: 0; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:100%; height:100%; }}
  .sign {{
    width:100vw; height:100vh; background:{CREAM}; color:{CHOC};
    font-family:'Barlow',sans-serif; text-align:center;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    padding:9vw 8vw; border:1.1vw solid {CHOC}; outline:0.5vw solid {GOLD}; outline-offset:-2.0vw;
  }}
  .logo {{ width:52vw; margin-bottom:5vw; }}
  .title {{ font-weight:700; font-size:3.3vw; letter-spacing:0.5vw; text-transform:uppercase; color:{GALAO}; }}
  .rule {{ width:26vw; height:0.5vw; background:{GOLD}; margin:4vw 0 6vw; }}
  .days {{ font-family:'DM Serif Display',serif; font-size:7.2vw; line-height:1.05; }}
  .hours {{ font-family:'DM Serif Display',serif; font-size:9.5vw; color:{TERRA}; margin-top:1vw; }}
  .note {{ font-size:2.9vw; color:{GALAO}; margin-top:3.2vw; font-weight:500; }}
  .rule2 {{ width:60vw; height:0.18vw; background:rgba(43,31,24,.18); margin:6vw 0; }}
  .sun {{ font-family:'DM Serif Display',serif; font-size:6vw; }}
  .sun b {{ color:{TERRA}; font-weight:400; }}
  .foot {{ margin-top:7vw; font-weight:600; font-size:2.9vw; letter-spacing:0.2vw; color:{CHOC}; }}
  .foot span {{ color:{GALAO}; font-weight:500; }}
</style></head>
<body><div class="sign">
  <img class="logo" src="data:image/png;base64,{LOGO_B64}">
  <div class="title">Hor&aacute;rio de Funcionamento</div>
  <div class="rule"></div>
  <div class="days">Segunda-feira a s&aacute;bado</div>
  <div class="hours">das 9h00 &agrave;s 20h00</div>
  <div class="note">Atendimento presencial mediante marca&ccedil;&atilde;o pr&eacute;via.</div>
  <div class="rule2"></div>
  <div class="sun">Domingo &nbsp; <b>Encerrado</b></div>
  <div class="foot">patiolanguage.pt &nbsp;&middot;&nbsp; <span>+351 928 129 560</span></div>
</div></body></html>"""

hp = os.path.join(HERE, "_tmp_hours.html")
with open(hp, "w", encoding="utf-8") as f: f.write(HTML)
url = "file:///" + hp.replace("\\", "/")

# Preview PNG (A4 ratio, ~180 dpi)
png = os.path.join(HERE, "patio-hours-sign-A4.png")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
    "--force-device-scale-factor=1", "--window-size=1488,2105",
    "--virtual-time-budget=5000", f"--screenshot={png}", url], check=True, capture_output=True)
print("built", png)

# Print-ready A4 PDF (vector text)
pdf = os.path.join(HERE, "patio-hours-sign-A4.pdf")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
    "--virtual-time-budget=5000", f"--print-to-pdf={pdf}", url], check=True, capture_output=True)
print("built", pdf)
os.remove(hp)
print("done")
