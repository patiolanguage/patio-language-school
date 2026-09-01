#!/usr/bin/env python3
"""Countdown-to-term mini-series for Patio Language School.
Term starts Mon 21 Sep 2026. Three weekly posts, each a countdown badge +
one useful European Portuguese phrase (arc: Let's begin -> I'm learning -> See you soon).
IG portrait 1080x1350 + FB square 1080x1080. Photos: meia / cliffs / sunrise.
"""
import base64, subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = r"C:/Users/Claire/AppData/Local/Temp/claude/C--Users-Claire-Patio-Language-School/88f610bb-f525-46f5-a1d6-72da4b27f0b0/scratchpad"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = r"C:/Users/Claire/Patio Language School/assets/img/Patio-Language-School-Logo-White.png"

GOLD = "#D8B778"; TERRA = "#B8593A"; CREAM = "#FBF6EE"

def b64(p):
    with open(p, "rb") as f: return base64.b64encode(f.read()).decode()

LOGO_B64 = b64(LOGO)
IMGS = {k: b64(os.path.join(SCRATCH, k + ".jpg")) for k in ("sun", "cliffs", "meia")}

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700'
    '&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

def overlay(img):
    return (f"linear-gradient(180deg,"
            f"rgba(43,31,24,.55) 0%,rgba(43,31,24,.12) 22%,"
            f"rgba(43,31,24,.10) 44%,rgba(43,31,24,.58) 70%,rgba(43,31,24,.95) 100%),"
            f"url(data:image/jpeg;base64,{IMGS[img]})")

def page(w, h, body, img, pos):
    css = f"""
    *{{margin:0;padding:0;box-sizing:border-box}}
    html,body{{width:{w}px;height:{h}px;overflow:hidden}}
    .card{{position:relative;width:{w}px;height:{h}px;
      background-image:{overlay(img)};background-size:cover;background-position:{pos};
      font-family:'Barlow',sans-serif;color:{CREAM};overflow:hidden}}
    .logo{{position:absolute;top:60px;left:72px;width:240px;
      filter:drop-shadow(0 2px 14px rgba(0,0,0,.6))}}
    .badge{{position:absolute;top:66px;right:70px;border:2px solid {GOLD};color:{GOLD};
      font-weight:700;font-size:23px;letter-spacing:3px;text-transform:uppercase;
      padding:11px 20px;border-radius:999px;background:rgba(43,31,24,.32);
      text-shadow:0 1px 6px rgba(0,0,0,.5)}}
    .wrap{{position:absolute;left:72px;right:72px;bottom:74px}}
    .eyebrow{{font-weight:600;font-size:25px;letter-spacing:5px;text-transform:uppercase;
      color:{GOLD};margin-bottom:20px;text-shadow:0 2px 12px rgba(0,0,0,.55)}}
    .phrase{{font-family:'DM Serif Display',serif;line-height:.98;
      text-shadow:0 3px 24px rgba(0,0,0,.6)}}
    .gloss{{font-weight:500;margin-top:24px;text-shadow:0 2px 12px rgba(0,0,0,.65)}}
    .foot{{font-weight:500;margin-top:34px;text-shadow:0 2px 12px rgba(0,0,0,.7)}}
    .gold{{color:{GOLD}}}
    """
    return (f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head>'
            f'<body><div class="card">'
            f'<img class="logo" src="data:image/png;base64,{LOGO_B64}">{body}</div></body></html>')

POSTS = [
 {"tag":"1", "badge":"3 weeks to go", "img":"meia", "pos":"center 45%",
  "ig":"Vamos<br>come&ccedil;ar.", "ig_sz":128, "fb":"Vamos come&ccedil;ar.", "fb_sz":80,
  "pron":"VAH&#8209;mosh &nbsp;koo&#8209;meh&#8209;SAR", "mean":"&ldquo;Let&rsquo;s begin.&rdquo;"},
 {"tag":"2", "badge":"2 weeks to go", "img":"cliffs", "pos":"center 55%",
  "ig":"Estou a<br>aprender.", "ig_sz":120, "fb":"Estou a aprender.", "fb_sz":78,
  "pron":"SHTOH &nbsp;a &nbsp;a&#8209;pren&#8209;DER", "mean":"&ldquo;I&rsquo;m learning.&rdquo;"},
 {"tag":"3", "badge":"1 week to go", "img":"sun", "pos":"center 42%",
  "ig":"At&eacute; j&aacute;!", "ig_sz":172, "fb":"At&eacute; j&aacute;!", "fb_sz":124,
  "pron":"a&#8209;TEH &nbsp;ZHAH", "mean":"&ldquo;See you soon!&rdquo;"},
]

FOOT = ('<div class="foot" style="font-size:30px;font-weight:400">'
        '<span class="gold" style="font-weight:600">Fall term starts 21 September</span>'
        '&nbsp; &middot; &nbsp;patiolanguage.pt</div>')

def body(p, fmt):
    sz = p["ig_sz"] if fmt == "ig" else p["fb_sz"]
    phr = p["ig"] if fmt == "ig" else p["fb"]
    gsz = 38 if fmt == "ig" else 33
    bottom = 74 if fmt == "ig" else 58
    return f"""
    <div class="badge">{p['badge']}</div>
    <div class="wrap" style="bottom:{bottom}px">
      <div class="eyebrow">Countdown to class</div>
      <div class="phrase" style="font-size:{sz}px">{phr}</div>
      <div class="gloss" style="font-size:{gsz}px">
        <span class="gold" style="font-weight:600">{p['pron']}</span>
        &nbsp;&middot;&nbsp; {p['mean']}
      </div>
      {FOOT}
    </div>"""

def render(name, w, h, bd, img, pos):
    html = page(w, h, bd, img, pos)
    hp = os.path.join(HERE, "_tmp_" + name + ".html")
    with open(hp, "w", encoding="utf-8") as f: f.write(html)
    out = os.path.join(HERE, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={w},{h}",
        "--virtual-time-budget=5000", f"--screenshot={out}",
        "file:///" + hp.replace("\\", "/")], check=True, capture_output=True)
    os.remove(hp)
    print("built", out)

for p in POSTS:
    render(f"patio-countdown-{p['tag']}-ig-1080x1350", 1080, 1350, body(p, "ig"), p["img"], p["pos"])
    render(f"patio-countdown-{p['tag']}-fb-1080x1080", 1080, 1080, body(p, "fb"), p["img"], p["pos"])
print("done")
