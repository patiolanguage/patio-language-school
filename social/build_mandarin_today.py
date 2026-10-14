#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mon 12 Oct 2026, taster day: "Today / Hoje" set. Bilingual, photo led, few words.

Photo: the Patio room with students (real place, warm, good for the grid).
Facts: free Mandarin taster, today 18h30, Patio Language School, with Michelle.

Outputs (social/Mandarin/today/):
  today-story-1080x1920.png      Instagram and Facebook story, bottom kept clear for the link sticker
  today-fb-1080x1350.png         Facebook post, no link on the image
  today-whatsapp-1080x1350.png   WhatsApp chats and status, "reply to save a seat"
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Mandarin", "today")
os.makedirs(OUT, exist_ok=True)

FMT = {
    "story":    dict(w=1080, h=1920, bottom=380, logo_top=250, big=230, line=58, mich=230,
                     cta=""),
    "fb":       dict(w=1080, h=1350, bottom=70, logo_top=56, big=190, line=50, mich=200,
                     cta="Mon 12 Oct &middot; Seg 12 out"),
    "whatsapp": dict(w=1080, h=1350, bottom=70, logo_top=56, big=190, line=50, mich=200,
                     cta="Responda para reservar &middot; Reply to save a seat"),
}

def page(fmt):
    f = FMT[fmt]
    cta = f'<div class="cta">{f["cta"]}</div>' if f["cta"] else ""
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{f['w']}px;height:{f['h']}px;overflow:hidden;}}
body{{position:relative;font-family:'Barlow',sans-serif;background:#2B1F18;}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 40%;}}
.top{{position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(180deg,rgba(43,31,24,.55),rgba(43,31,24,0));}}
.fade{{position:absolute;left:0;right:0;bottom:0;height:{f['h']*0.68:.0f}px;background:linear-gradient(180deg,rgba(43,31,24,0) 0%,rgba(43,31,24,.7) 40%,rgba(43,31,24,.92) 100%);}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.logo{{position:absolute;top:{f['logo_top']}px;left:60px;height:100px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.5));}}
.free{{position:absolute;top:{f['logo_top']}px;right:60px;background:#B8593A;color:#FBF6EE;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  font-size:30px;padding:14px 28px;border-radius:999px;box-shadow:0 8px 20px rgba(0,0,0,.3);}}
.txt{{position:absolute;left:60px;right:60px;bottom:{f['bottom']}px;color:#FBF6EE;}}
.big{{font-family:'DM Serif Display',serif;font-size:{f['big']}px;line-height:.95;}}
.big i{{color:#E9C58B;}}
.what{{font-family:'DM Serif Display',serif;font-size:{f['line']*1.25:.0f}px;line-height:1.1;margin-top:16px;}}
.what span{{color:#F6DCC0;}}
.row{{display:flex;align-items:center;gap:26px;margin-top:30px;}}
.row img{{width:{f['mich']}px;height:{f['mich']}px;border-radius:50%;object-fit:cover;object-position:center 30%;border:7px solid #FBF6EE;flex:none;}}
.time{{font-size:{f['line']*1.6:.0f}px;font-weight:700;line-height:1;}}
.where{{font-size:{f['line']*0.7:.0f}px;font-weight:600;color:#F6DCC0;margin-top:10px;line-height:1.3;}}
.cta{{display:inline-block;margin-top:30px;background:#FBF6EE;color:#B8593A;font-weight:700;font-size:{f['line']*0.75:.0f}px;padding:14px 30px;border-radius:999px;}}
</style></head><body>
<img class="ph" src="{bm.PHOTO_ROOM_TALL}"><div class="top"></div><div class="fade"></div><div class="bar"></div>
<img class="logo" src="{bm.LOGO_WHITE}"><div class="free">Grátis &middot; Free</div>
<div class="txt">
  <div class="big">Hoje! <i>Today!</i></div>
  <div class="what">Aula grátis de mandarim<br><span>Free Mandarin taster</span></div>
  <div class="row"><img src="{bm.MICHELLE}"><div>
    <div class="time">18h30</div>
    <div class="where">com a Michelle &middot; with Michelle<br>Patio Language School, Lagos</div></div></div>
  {cta}
</div></body></html>"""

def render(fmt):
    f = FMT[fmt]
    name = f"today-{fmt}-{f['w']}x{f['h']}"
    path = os.path.join(OUT, name + ".html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(page(fmt))
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={f['w']},{f['h']}", "--virtual-time-budget=6000",
        f"--screenshot={os.path.join(OUT, name + '.png')}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", name + ".png")

if __name__ == "__main__":
    for fmt in FMT:
        render(fmt)
