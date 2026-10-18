#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Phonetics Workshop launch posts. EN and PT, same light layout as the Mandarin launch.

One workshop in two parts: Mon 2 Nov + Fri 6 Nov, 9h15 to 10h45, €35 total,
taught by Sofia, max 12. Booking by WhatsApp or email.

Hook: "avô ou avó?" (grandfather or grandmother), the sounds that give foreign speakers away,
workshop facts, and a €35 ticket.

Outputs (social/Phonetics/launch/):
  phonetics-{en,pt}-ig-1080x1350.png
  phonetics-{en,pt}-story-1080x1920.png
  phonetics-{en,pt}-fb-1080x1080.png
  phonetics-wa-wa-1080x1350.png       WhatsApp, PT and EN in one image, reply to book
  phonetics-bi-{ig,story,fb}-*.png    bilingual posts, same wording as the A5 print flyer (BI)

Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Phonetics", "launch")
os.makedirs(OUT, exist_ok=True)
PHOTO = bm.b64_photo(os.path.join(bm.IMG, "phonetics-tiles-banner.jpg"))  # letter tiles spelling FONÉTICA (build_phonetics_tiles.py)
ADDR = "Praça do Poder Local, Lote&nbsp;14, Loja&nbsp;C, Lagos"
PIN = ('<svg viewBox="0 0 24 24" width="1em" height="1em"><path fill="#B8593A" d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>')
QR = bm.b64_png(os.path.join(bm.IMG, "qr-whatsapp-phonetics.png"))  # wa.me/351928129560, text "Phonetics Workshop"
QR_LOGO = bm.b64_png(os.path.join(bm.IMG, "qr-whatsapp-phonetics-logo.png"))  # same link, colour Patio logo in the centre
ADDR_FULL = "<b>Patio Language School</b><br>Praça do Poder Local, Lote&nbsp;14, Loja&nbsp;C, Lagos"

COPY = {
    "en": dict(
        tag="New", new="at Patio", qr="Scan to book",
        bubble="avô <i>ou</i> avó?",
        title='Portuguese <span class="a">Phonetics</span> Workshop',
        title2='Sound more <span class="a">Portuguese</span>.',
        easy="The sounds that give foreign speakers away:",
        ticks=["Nasal ão", "The &ldquo;sh&rdquo; s", "lh &middot; nh &middot; r"],
        info_h="2 mornings",
        info_d="Mon 2 &amp; Fri 6 Nov",
        info_t="9h15 to 10h45",
        tk_k="&euro;35",
        tk_d="Both sessions",
        tk_u="Book on WhatsApp<br>+351&nbsp;928&nbsp;129&nbsp;560",
    ),
    "pt": dict(
        tag="Novidade", new="no Patio", qr="Reserve aqui",
        bubble="avô <i>ou</i> avó?",
        title='Workshop de <span class="a">fonética</span> portuguesa',
        title2='Pronuncie como um <span class="a">português</span>.',
        easy="Os sons que denunciam um estrangeiro:",
        ticks=["O ão nasal", "O s que soa &ldquo;ch&rdquo;", "lh &middot; nh &middot; r"],
        info_h="2 manhãs",
        info_d="Seg 2 e Sex 6 nov",
        info_t="9h15 às 10h45",
        tk_k="35&nbsp;&euro;",
        tk_d="As duas sessões",
        tk_u="Reserve: WhatsApp<br>+351&nbsp;928&nbsp;129&nbsp;560",
    ),
    "wa": dict(
        tag="Novidade", new="no Patio", qr="Reserve &middot; Book",
        bubble="avô <i>ou</i> avó?",
        title='Workshop de <span class="a">fonética</span> portuguesa',
        title2='Portuguese <span class="a">Phonetics</span> Workshop',
        easy="Os sons difíceis &middot; The tricky sounds:",
        ticks=["ão", "s = &ldquo;sh&rdquo;", "lh &middot; nh &middot; r"],
        info_h="2 manhãs &middot; 2 mornings",
        info_d="2 e 6 nov",
        info_t="9h15 às 10h45",
        tk_k="35&nbsp;&euro;",
        tk_d="2 sessões",
        tk_u="Responda a esta mensagem para reservar<br>Reply to this message to book",
    ),
    # Bilingual posts, same wording as the A5 print flyer (build_phonetics_flyer.py "BI")
    "bi": dict(
        tag="Novidade", new="no Patio", qr="Reserve &middot; Book",
        title='Workshop de <span class="a">fonética</span> portuguesa',
        title2='Portuguese <span class="a">Phonetics</span> Workshop',
        info_h="2 manhãs &middot; 2 mornings",
        info_d="2 e 6 de novembro",
        info_t="2 &amp; 6 November &middot; 9h15 to 10h45",
        tk_k="35&nbsp;&euro;",
        tk_d="2 sessões &middot; 2 sessions",
        tk_u="WhatsApp +351&nbsp;928&nbsp;129&nbsp;560",
        addr=ADDR_FULL, qr_img=QR_LOGO,
        # longer bilingual text: smaller banner and title so it all fits
        fmt={"ig": dict(photo=220, h1=88, info=46, gap=24), "story": dict(photo=360, h1=100, info=50, gap=36)},
    ),
}

FMT = {
    "ig":    dict(w=1080, h=1350, top=40, bottom=44, photo=185, qr=145, logo=118, pill=46, h1=100, tick=38, info=50, gap=30),
    "story": dict(w=1080, h=1920, top=130, bottom=300, photo=440, qr=210, logo=130, pill=52, h1=110, tick=42, info=54, gap=44, stack=True),
    "wa":    dict(w=1080, h=1350, top=40, bottom=44, photo=240, qr=150, logo=110, pill=42, h1=88, tick=34, info=44, gap=24),
    "fb":    dict(w=1080, h=1080, top=36, bottom=36, photo=150, qr=112, logo=84, pill=38, h1=80, tick=31, info=38, gap=16),
}

def page(lang, fmt):
    c = COPY[lang]
    f = dict(FMT[fmt], **c.get("fmt", {}).get(fmt, {}))
    ticks = "".join(f'<div class="tick"><span>&#10003;</span>{t}</div>' for t in c.get("ticks", []))
    addr, qr_img = c.get("addr", ADDR), c.get("qr_img", QR)
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{f['w']}px;height:{f['h']}px;overflow:hidden;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;position:relative;}}
.bar{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,#617C7B,#C19D5F);}}
.wrap{{position:absolute;left:56px;right:56px;top:{f['top']}px;bottom:{f['bottom']}px;display:flex;flex-direction:column;}}
.top{{position:relative;height:{f['photo']}px;flex:none;}}
.top .ph{{width:100%;height:100%;object-fit:cover;object-position:center 50%;border-radius:30px;display:block;box-shadow:0 14px 34px rgba(43,31,24,.16);}}
.head{{display:flex;align-items:center;justify-content:space-between;margin-bottom:{f['gap']*0.7:.0f}px;flex:none;}}
.head img{{height:{f['logo']}px;display:block;}}
.qr{{flex:none;background:#fff;border-radius:14px;padding:8px 8px 6px;text-align:center;}}
.qr img{{width:{f['qr']}px;height:{f['qr']}px;display:block;}}
.qr div{{font-weight:700;font-size:{f['qr']*0.13:.0f}px;color:#2B1F18;margin-top:2px;}}
.new{{display:flex;align-items:center;gap:16px;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:{f['pill']}px;line-height:1.1;padding:12px 30px 12px 14px;border-radius:999px;box-shadow:0 6px 16px rgba(43,31,24,.15);}}
.new .tg{{background:#C19D5F;color:#2B1F18;font-size:{f['pill']*0.6:.0f}px;letter-spacing:.12em;text-transform:uppercase;padding:8px 16px;border-radius:999px;}}
.bubble{{position:absolute;left:30px;bottom:30px;background:#fff;border-radius:28px;padding:14px 34px 18px;box-shadow:0 10px 26px rgba(0,0,0,.22);}}
.bubble span{{font-family:'DM Serif Display',serif;font-size:{f['h1']*0.62:.0f}px;line-height:1;color:#2B1F18;}}
.bubble i{{color:#B8593A;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:{f['h1']}px;line-height:1.02;margin-top:{f['gap']}px;}}
h1 .a{{color:#B8593A;font-style:italic;}}
.t2{{font-family:'DM Serif Display',serif;font-size:{f['h1']*0.68:.0f}px;line-height:1.05;color:#726651;margin-top:6px;}}
.t2 .a{{color:#B8593A;font-style:italic;}}
.easy{{font-size:{f['tick']*1.15:.0f}px;font-weight:600;color:#4a4038;margin-top:{f['gap']*0.5:.0f}px;}}
.ticks{{display:flex;flex-wrap:wrap;gap:12px;margin-top:{f['gap']*0.5:.0f}px;}}
.tick{{background:#fff;border-radius:999px;padding:10px 22px 10px 12px;font-size:{f['tick']}px;font-weight:600;display:flex;align-items:center;gap:12px;box-shadow:0 6px 16px rgba(43,31,24,.07);}}
.tick span{{width:{f['tick']*1.25:.0f}px;height:{f['tick']*1.25:.0f}px;border-radius:50%;background:#617C7B;color:#fff;display:flex;align-items:center;justify-content:center;font-size:{f['tick']*0.75:.0f}px;}}
.bottom{{margin-top:auto;padding-top:{f['gap']}px;display:flex;flex-direction:column;gap:{f['gap']*0.8:.0f}px;}}
.info{{background:#fff;border-left:12px solid #C19D5F;border-radius:20px;padding:26px 30px;box-shadow:0 8px 24px rgba(43,31,24,.08);}}
.info .h{{font-size:{f['info']*1.0:.0f}px;font-weight:700;letter-spacing:.06em;color:#617C7B;text-transform:uppercase;}}
.info .d{{white-space:nowrap;font-family:'DM Serif Display',serif;font-size:{f['info']*1.5:.0f}px;line-height:1.1;margin-top:4px;}}
.info .t{{font-size:{f['info']*1.1:.0f}px;font-weight:600;color:#726651;margin-top:6px;}}
.info .ad{{display:flex;gap:8px;align-items:flex-start;font-size:{f['info']*0.72:.0f}px;font-weight:600;color:#2B1F18;line-height:1.25;margin-top:12px;padding-top:10px;border-top:2px solid #F1E9DA;}}
.info .ad svg{{flex:none;margin-top:2px;}}
.ticket{{background:#B8593A;color:#FBF6EE;border-radius:20px;padding:8px;box-shadow:0 10px 26px rgba(184,89,58,.35);transform:rotate(-1deg);}}
.ticket .in{{border:3px dashed rgba(251,246,238,.7);border-radius:14px;padding:14px 14px 14px 28px;display:flex;align-items:center;justify-content:space-between;gap:20px;}}
.ticket .l{{display:flex;align-items:baseline;gap:16px;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:{f['info']*1.65:.0f}px;line-height:1;}}
.ticket .d{{font-size:{f['info']*0.88:.0f}px;font-weight:700;white-space:nowrap;}}
.ticket .u{{font-size:{f['info']*0.8:.0f}px;font-weight:700;color:#F6DCC0;line-height:1.25;white-space:nowrap;margin-top:{f['info']*0.3:.0f}px;}}
</style></head><body>
<div class="bar"></div>
<div class="wrap">
  <div class="head"><img src="{bm.LOGO_COLOR}"><div class="new"><span class="tg">{c['tag']}</span>{c['new']}</div></div>
  <div class="top">
    <img class="ph" src="{PHOTO}">
  </div>
  <h1>{c['title']}</h1>
  {('<div class="t2">' + c['title2'] + '</div>') if c.get('title2') else ''}
  <div class="bottom">
    <div class="info"><div class="h">{c['info_h']}</div><div class="d">{c['info_d']}</div><div class="t">{c['info_t']}</div><div class="ad">{PIN}<span>{addr}</span></div></div>
    <div class="ticket"><div class="in"><div><div class="l"><div class="k">{c['tk_k']}</div><div class="d">{c['tk_d']}</div></div><div class="u">{c['tk_u']}</div></div>{'' if lang == 'wa' else '<div class="qr"><img src="' + qr_img + '"><div>' + c['qr'] + '</div></div>'}</div></div>
  </div>
</div>
</body></html>"""

def render(lang, fmt):
    f = FMT[fmt]
    name = f"phonetics-{lang}-{fmt}-{f['w']}x{f['h']}"
    html = os.path.join(OUT, name + ".html")
    with open(html, "w", encoding="utf-8") as fh:
        fh.write(page(lang, fmt))
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={f['w']},{f['h']}",
        "--virtual-time-budget=6000", f"--screenshot={os.path.join(OUT, name + '.png')}", html],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", name + ".png")

if __name__ == "__main__":
    for lang in ("en", "pt"):
        for fmt in ("ig", "story", "fb"):
            render(lang, fmt)
    render("wa", "wa")
    for fmt in ("ig", "story", "fb"):
        render("bi", fmt)
