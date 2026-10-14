#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Header image for the Phonetics Workshop Google Form (1600x400, same size as form-header-mandarin.png).
Letter-tile banner on the right, logo + title on cream on the left.
Upload by hand: form editor > Customize theme (palette icon) > Header > Upload.
Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "form-header-phonetics")
TILES = bm.b64_photo(os.path.join(bm.IMG, "phonetics-tiles-banner.jpg"))
html = f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1600px;height:400px;overflow:hidden;background:#FBF6EE;font-family:'Barlow',sans-serif;color:#2B1F18}}
.bar{{position:absolute;top:0;left:0;right:0;height:10px;background:linear-gradient(90deg,#617C7B,#C19D5F);z-index:3}}
.tiles{{position:absolute;right:0;top:0;width:900px;height:400px;object-fit:cover;object-position:62% 50%}}
.fade{{position:absolute;right:560px;top:0;width:340px;height:400px;background:linear-gradient(90deg,#FBF6EE 10%,rgba(251,246,238,0))}}
.left{{position:absolute;left:70px;top:0;bottom:0;width:780px;display:flex;flex-direction:column;justify-content:center}}
.left img{{height:78px;align-self:flex-start}}
.eyebrow{{margin-top:22px;color:#617C7B;font-weight:700;letter-spacing:.18em;font-size:22px;text-transform:uppercase}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:62px;line-height:1.02;margin-top:8px}}
h1 .a{{color:#B8593A;font-style:italic}}
.sub{{font-family:'DM Serif Display',serif;font-size:36px;color:#726651;margin-top:4px}}
.sub .a{{color:#B8593A;font-style:italic}}
</style></head><body><div class="bar"></div>
<img class="tiles" src="{TILES}"><div class="fade"></div>
<div class="left"><img src="{bm.LOGO_COLOR}">
<div class="eyebrow">2 &amp; 6 Nov &middot; 9h15 &middot; Lagos</div>
<h1>Workshop de <span class="a">fonética</span> portuguesa</h1>
<div class="sub">Portuguese <span class="a">Phonetics</span> Workshop</div></div>
</body></html>"""
with open(OUT + ".html", "w", encoding="utf-8") as f:
    f.write(html)
subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
    "--window-size=1600,400", "--virtual-time-budget=6000", f"--screenshot={OUT}.png", OUT + ".html"],
    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("rendered", OUT + ".png")
