#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Letter tile "flat lay" banner for the Phonetics Workshop, drawn in HTML/CSS
(no stock photo). Cream and wooden tiles on a light plank table spell FONÉTICA,
with the workshop sounds (ão, lh, nh, r, s) scattered around.

Output: assets/img/phonetics-tiles-banner.jpg  (3600 x 1400, print quality)
The important part sits in the middle so any wide crop works; the top right
corner is kept quiet because the QR code sits there.
"""
import os, random, subprocess
import build_mandarin as bm

W, H = 1800, 700          # CSS px, rendered at 2x
OUT = os.path.join(bm.IMG, "phonetics-tiles-banner.jpg")
OUT_SOCIAL = os.path.join(bm.IMG, "phonetics-tiles-banner-social.jpg")  # word kept left of the QR
TMP = os.path.join(bm.SOCIAL, "Phonetics", "tiles-banner.html")
random.seed(7)

# tile styles: (background, text colour, edge colour)
CREAM = ("linear-gradient(145deg,#FFF8EA,#F1E3C8)", "#2B1F18", "#D9C6A3")
OAK   = ("linear-gradient(145deg,#D9B98A,#C19D5F)", "#2B1F18", "#9C7B45")
WALNUT= ("linear-gradient(145deg,#8A6446,#6B4A33)", "#FBF6EE", "#4E3524")
TERRA = ("linear-gradient(145deg,#C96A4A,#B8593A)", "#FBF6EE", "#8E4129")
TEAL  = ("linear-gradient(145deg,#748F8E,#617C7B)", "#FBF6EE", "#47605F")

def tile(x, y, txt, style, size=150, rot=0, font=None, z=1):
    bg, fg, edge = style
    fs = size * (0.62 if len(txt) == 1 else 0.46 if len(txt) == 2 else 0.36)
    fam = font or "'DM Serif Display',serif"
    return (f'<div class="t" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;'
            f'transform:rotate({rot}deg);background:{bg};color:{fg};box-shadow:0 {size*0.05:.0f}px 0 {edge},'
            f'0 {size*0.12:.0f}px {size*0.18:.0f}px rgba(43,31,24,.28);z-index:{z};font-family:{fam};font-size:{fs:.0f}px;">'
            f'<span>{txt}</span></div>')

def build(x0=None, size=170, gap=22, word="FONÉTICA", styles=None):
    random.seed(7)
    tiles = []
    # Hero word, slightly uneven, centred
    if isinstance(word, str):
        word = list(word)
    styles = styles or [CREAM, OAK, CREAM, TERRA, CREAM, WALNUT, CREAM, OAK]
    total = len(word) * size + (len(word) - 1) * gap
    x0 = (W - total) / 2 if x0 is None else x0
    y0 = H / 2 - size / 2 - 10
    for i, (ch, st) in enumerate(zip(word, styles)):
        tiles.append(tile(x0 + i * (size + gap), y0 + random.uniform(-14, 14), ch, st, size, random.uniform(-5, 5), z=3))

    # Scattered sound tiles around the word (top-right left fairly clear for the QR)
    scatter = [
        (70, 40, "ão", TERRA, 150, -9), (330, 70, "lh", CREAM, 120, 7), (560, 20, "s", WALNUT, 110, -4),
        (820, 55, "Ã", CREAM, 120, 10), (1060, 30, "nh", OAK, 130, -6),
        (40, 520, "r", OAK, 120, 8), (250, 560, "nh", CREAM, 140, -7), (520, 540, "ê", TEAL, 110, 5),
        (760, 575, "ão", CREAM, 130, -3), (1010, 545, "lh", WALNUT, 140, 9), (1270, 560, "ó", CREAM, 115, -8),
        (1500, 520, "r", TERRA, 130, 6), (1660, 590, "s", CREAM, 100, -10),
        (-40, 250, "ç", CREAM, 120, 12), (1700, 230, "ô", OAK, 120, -12),
    ]
    for x, y, t, st, sz, r in scatter:
        tiles.append(tile(x, y, t, st, sz, r, z=2))

    html = f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
    *{{margin:0;padding:0;box-sizing:border-box;}}
    html,body{{width:{W}px;height:{H}px;overflow:hidden;}}
    body{{position:relative;
      background:
        repeating-linear-gradient(90deg, rgba(160,130,90,.10) 0 2px, transparent 2px 300px),
        repeating-linear-gradient(0deg, rgba(150,120,80,.035) 0 1px, transparent 1px 7px),
        radial-gradient(ellipse at 30% 40%, #FFFDF8, #F4EBDC 70%, #EADDC6);}}
    .t{{position:absolute;border-radius:16%;display:flex;align-items:center;justify-content:center;line-height:1;}}
    .t span{{transform:translateY(-3%);}}
    .light{{position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.35),transparent 45%,rgba(43,31,24,.06));z-index:9;pointer-events:none;}}
    </style></head><body>{''.join(tiles)}<div class="light"></div></body></html>"""

    return html

def render(html, out):
    with open(TMP, "w", encoding="utf-8") as f:
        f.write(html)
    png = out.replace(".jpg", ".png")
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2", f"--window-size={W},{H}", "--virtual-time-budget=6000",
        f"--screenshot={png}", TMP], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    from PIL import Image
    Image.open(png).convert("RGB").save(out, quality=92)
    os.remove(png)
    print("saved", out)

if __name__ == "__main__":
    render(build(), OUT)
    # Social posts: QR sits top right over the photo, and the Story crop trims ~180px each side,
    # so the word fits between x 200 and 1240.
    render(build(x0=200, size=116, gap=16), OUT_SOCIAL)
    # Sound of the week carousel covers (968x520 crop shows roughly x 250 to 1550)
    for name, word, styles, size in [
        ("ao", ["N", "Ã", "O"], [CREAM, TERRA, OAK], 230),
        ("s", list("LAGOS"), [CREAM, OAK, CREAM, CREAM, TERRA], 190),
        ("lhnhr", ["lh", "nh", "r"], [TERRA, CREAM, WALNUT], 230),
    ]:
        render(build(size=size, gap=30, word=word, styles=styles),
               os.path.join(bm.IMG, f"phonetics-tiles-{name}.jpg"))
