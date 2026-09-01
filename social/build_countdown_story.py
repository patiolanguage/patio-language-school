#!/usr/bin/env python3
"""IG Story versions (1080x1920) of the countdown-to-term series + launch.
4 stories: 3 weeks / 2 weeks / 1 week / starts-today. Story safe zones applied.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-White.png")

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"
W, H = 1080, 1920

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMGS = {k: b64(os.path.join(SCRATCH, k + ".jpg")) for k in ("sun", "cliffs", "meia")}
IMGS["class"] = b64(os.path.join(IMGDIR, "class-standing.jpg"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay(img):
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.55) 0%,rgba(43,31,24,.10) 17%,"
            f"rgba(43,31,24,.08) 40%,rgba(43,31,24,.52) 64%,rgba(43,31,24,.95) 100%),"
            f"url(data:image/jpeg;base64,{IMGS[img]})")

def page(body, img, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{W}px;height:{H}px;overflow:hidden}}
    .card{{position:relative;width:{W}px;height:{H}px;
      background-image:{overlay(img)};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:130px;left:80px;width:260px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.6))}}
    .badge{{position:absolute;top:140px;right:80px;border:2px solid {GOLD};color:{GOLD};
      font-weight:700;font-size:25px;letter-spacing:3px;text-transform:uppercase;
      padding:12px 22px;border-radius:999px;background:rgba(43,31,24,.32);
      text-shadow:0 1px 6px rgba(0,0,0,.5)}}
    .wrap{{position:absolute;left:80px;right:80px;bottom:270px}}
    .eyebrow{{font-weight:600;font-size:27px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:22px;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .phrase{{font-family:'DM Serif Display',serif;line-height:.98;
      text-shadow:0 3px 24px rgba(0,0,0,.65)}}
    .gloss{{font-weight:500;margin-top:28px;text-shadow:0 2px 12px rgba(0,0,0,.7)}}
    .foot{{font-weight:500;margin-top:40px;font-size:32px;text-shadow:0 2px 12px rgba(0,0,0,.75)}}
    .gold{{color:{GOLD}}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

TERM_FOOT = ('<div class="foot" style="font-weight:400">'
             '<span class="gold" style="font-weight:600">Fall term starts 21 September</span>'
             '&nbsp; &middot; &nbsp;patiolanguage.pt</div>')
LAUNCH_FOOT = ('<div class="foot" style="font-weight:400">'
               '<span class="gold" style="font-weight:600">It&rsquo;s not too late to join</span>'
               '&nbsp; &middot; &nbsp;patiolanguage.pt</div>')

POSTS = [
 {"name":"1", "badge":"3 weeks to go", "eb":"Countdown to class", "img":"meia", "pos":"center 45%",
  "phrase":"Vamos<br>come&ccedil;ar.", "sz":150, "pron":"VAH&#8209;mosh &nbsp;koo&#8209;meh&#8209;SAR",
  "mean":"&ldquo;Let&rsquo;s begin.&rdquo;", "foot":TERM_FOOT},
 {"name":"2", "badge":"2 weeks to go", "eb":"Countdown to class", "img":"cliffs", "pos":"58% 58%",
  "phrase":"Estou a<br>aprender.", "sz":140, "pron":"SHTOH &nbsp;a &nbsp;a&#8209;pren&#8209;DER",
  "mean":"&ldquo;I&rsquo;m learning.&rdquo;", "foot":TERM_FOOT},
 {"name":"3", "badge":"1 week to go", "eb":"Countdown to class", "img":"sun", "pos":"72% 42%",
  "phrase":"At&eacute; j&aacute;!", "sz":200, "pron":"a&#8209;TEH &nbsp;ZHAH",
  "mean":"&ldquo;See you soon!&rdquo;", "foot":TERM_FOOT},
 {"name":"launch", "badge":"It&rsquo;s here", "eb":"Fall term begins today", "img":"class", "pos":"center 24%",
  "phrase":"Come&ccedil;amos<br>hoje.", "sz":150, "pron":"koo&#8209;meh&#8209;SAH&#8209;moosh &nbsp;OH&#8209;zheh",
  "mean":"&ldquo;We begin today.&rdquo;", "foot":LAUNCH_FOOT},
]

for p in POSTS:
    body = f"""
    <div class="badge">{p['badge']}</div>
    <div class="wrap">
      <div class="eyebrow">{p['eb']}</div>
      <div class="phrase" style="font-size:{p['sz']}px">{p['phrase']}</div>
      <div class="gloss" style="font-size:42px">
        <span class="gold" style="font-weight:600">{p['pron']}</span>
        &nbsp;&middot;&nbsp; {p['mean']}
      </div>
      {p['foot']}
    </div>"""
    html = page(body, p["img"], p["pos"])
    hp = os.path.join(HERE, "_tmp_cd_" + p["name"] + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, f"patio-countdown-{p['name']}-ig-story-1080x1920.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    os.remove(hp)
    print("built", out)
print("done")
