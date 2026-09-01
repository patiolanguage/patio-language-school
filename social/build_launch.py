#!/usr/bin/env python3
"""'Starts today' launch post to cap the countdown-to-term series.
Same phrase-card look as build_countdown.py, but on a real classroom photo
(class-standing.jpg) as the payoff. IG 1080x1350 + FB 1080x1080.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMGDIR = r"C:/Users/Claire/Patio Language School/assets/img"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = os.path.join(IMGDIR, "Patio-Language-School-Logo-White.png")

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMG_B64 = b64(os.path.join(IMGDIR, "class-standing.jpg"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay():
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.50) 0%,rgba(43,31,24,.10) 22%,"
            f"rgba(43,31,24,.12) 44%,rgba(43,31,24,.62) 70%,rgba(43,31,24,.96) 100%),"
            f"url(data:image/jpeg;base64,{IMG_B64})")

def page(w, h, body, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay()};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:60px;left:72px;width:240px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.6))}}
    .badge{{position:absolute;top:66px;right:70px;border:2px solid {GOLD};color:{GOLD};
      font-weight:700;font-size:23px;letter-spacing:3px;text-transform:uppercase;
      padding:11px 20px;border-radius:999px;background:rgba(43,31,24,.32);
      text-shadow:0 1px 6px rgba(0,0,0,.5)}}
    .wrap{{position:absolute;left:72px;right:72px;}}
    .eyebrow{{font-weight:600;font-size:25px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:20px;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
    .phrase{{font-family:'DM Serif Display',serif;line-height:.98;
      text-shadow:0 3px 24px rgba(0,0,0,.65)}}
    .gloss{{font-weight:500;margin-top:24px;text-shadow:0 2px 12px rgba(0,0,0,.7)}}
    .foot{{font-weight:500;margin-top:34px;text-shadow:0 2px 12px rgba(0,0,0,.75)}}
    .gold{{color:{GOLD}}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

FOOT = ('<div class="foot" style="font-size:30px;font-weight:400">'
        '<span class="gold" style="font-weight:600">It&rsquo;s not too late to join</span>'
        '&nbsp; &middot; &nbsp;patiolanguage.pt</div>')

def body(fmt):
    if fmt == "ig":
        sz, phr, bottom, gsz = 130, "Come&ccedil;amos<br>hoje.", 74, 38
    else:
        sz, phr, bottom, gsz = 82, "Come&ccedil;amos hoje.", 58, 33
    return f"""
    <div class="badge">It&rsquo;s here</div>
    <div class="wrap" style="bottom:{bottom}px">
      <div class="eyebrow">Fall term begins today</div>
      <div class="phrase" style="font-size:{sz}px">{phr}</div>
      <div class="gloss" style="font-size:{gsz}px">
        <span class="gold" style="font-weight:600">koo&#8209;meh&#8209;SAH&#8209;moosh &nbsp;OH&#8209;zheh</span>
        &nbsp;&middot;&nbsp; &ldquo;We begin today.&rdquo;
      </div>
      {FOOT}
    </div>"""

for name, w, h, fmt, pos in [
    ("patio-countdown-launch-ig-1080x1350", 1080, 1350, "ig", "center 24%"),
    ("patio-countdown-launch-fb-1080x1080", 1080, 1080, "fb", "center 22%"),
]:
    html = page(w, h, body(fmt), pos)
    hp = os.path.join(HERE, "_tmp_" + name + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    os.remove(hp)
    print("built", out)
print("done")
