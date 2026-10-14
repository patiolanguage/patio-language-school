#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Phonetics Workshop A5 print flyer (148 x 210 mm), EN and PT.
Same content as the launch posts (build_phonetics_launch.py): classroom photo,
Patio logo, title, dates + address, €35 box, WhatsApp QR.

Outputs (social/Phonetics/print/):
  Patio-Phonetics-Flyer-A5-EN.pdf / .png
  Patio-Phonetics-Flyer-A5-PT.pdf / .png
Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm

OUT = os.path.join(bm.SOCIAL, "Phonetics", "print")
os.makedirs(OUT, exist_ok=True)
PHOTO = bm.b64_photo(os.path.join(bm.IMG, "phonetics-tiles-banner.jpg"))
QR = bm.b64_png(os.path.join(bm.IMG, "qr-whatsapp-phonetics.png"))
ADDR = "Praça do Poder Local, Lote&nbsp;14, Loja&nbsp;C, Lagos"
PIN = ('<svg viewBox="0 0 24 24" width="1em" height="1em"><path fill="#B8593A" d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>')

COPY = {
    "EN": dict(
        tag="New", new="at Patio",
        title='Portuguese <span class="a">Phonetics</span> Workshop',
        sub='Sound more <span class="a">Portuguese</span>.',
        h="2 mornings", d="Mon 2 &amp; Fri 6 November", t="9h15 to 10h45",
        k="&euro;35", kd="Both sessions",
        scan="Scan to book on WhatsApp", phone="+351 928 129 560",
    ),
    "PT": dict(
        tag="Novidade", new="no Patio",
        title='Workshop de <span class="a">fonética</span> portuguesa',
        sub='Pronuncie como um <span class="a">português</span>.',
        h="2 manhãs", d="Seg 2 e sex 6 de novembro", t="9h15 às 10h45",
        k="35&nbsp;&euro;", kd="As duas sessões",
        scan="Leia para reservar no WhatsApp", phone="+351 928 129 560",
    ),
}

def html(c):
    return f"""<!DOCTYPE html><html><head>{bm.FONTS}<style>
@page{{size:148mm 210mm;margin:0;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:148mm;height:210mm;}}
body{{font-family:'Barlow',sans-serif;background:#FBF6EE;color:#2B1F18;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
.sheet{{position:relative;width:148mm;height:210mm;overflow:hidden;display:flex;flex-direction:column;padding:9mm 9mm 8mm;}}
.bar{{position:absolute;top:0;left:0;right:0;height:3mm;background:linear-gradient(90deg,#617C7B,#C19D5F);}}
.head{{display:flex;align-items:center;justify-content:space-between;}}
.head img{{height:15mm;display:block;}}
.new{{display:flex;align-items:center;gap:2.2mm;background:#617C7B;color:#FBF6EE;font-weight:700;font-size:5.6mm;line-height:1.1;padding:1.6mm 4mm 1.6mm 1.8mm;border-radius:99mm;}}
.new .tg{{background:#C19D5F;color:#2B1F18;font-size:3.4mm;letter-spacing:.12em;text-transform:uppercase;padding:1.1mm 2.4mm;border-radius:99mm;}}
.ph{{margin-top:5mm;height:36mm;flex:none;width:100%;object-fit:cover;object-position:center 50%;border-radius:4mm;display:block;}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:12mm;line-height:1.0;margin-top:5mm;}}
h1 .a,.sub .a{{color:#B8593A;font-style:italic;}}
.sub{{font-family:'DM Serif Display',serif;font-size:8mm;line-height:1.1;color:#726651;margin-top:2mm;margin-bottom:4mm;}}
.info{{margin-top:auto;position:relative;top:0;background:#fff;border-left:2.4mm solid #C19D5F;border-radius:3mm;padding:4mm 5mm;}}
.info .h{{font-size:4.4mm;font-weight:700;letter-spacing:.06em;color:#617C7B;text-transform:uppercase;}}
.info .d{{font-family:'DM Serif Display',serif;font-size:8.6mm;line-height:1.1;margin-top:.8mm;}}
.info .t{{font-size:5.4mm;font-weight:600;color:#726651;margin-top:.6mm;}}
.info .ad{{display:flex;gap:1.6mm;align-items:center;font-size:4.2mm;font-weight:600;margin-top:2.4mm;padding-top:2mm;border-top:.4mm solid #F1E9DA;}}
.book{{margin-top:4mm;}}
.ticket{{background:#B8593A;color:#FBF6EE;border-radius:3mm;padding:1.4mm;}}
.ticket .in{{border:.5mm dashed rgba(251,246,238,.7);border-radius:2mm;padding:2.4mm 2.4mm 2.4mm 5mm;display:flex;align-items:center;justify-content:space-between;gap:4mm;}}
.ticket .k{{font-family:'DM Serif Display',serif;font-size:13mm;line-height:1;}}
.ticket .kd{{font-size:5.4mm;font-weight:700;margin-top:1mm;}}
.ticket .ph2{{font-size:4.6mm;font-weight:700;color:#F6DCC0;margin-top:2.4mm;}}
.qr{{flex:none;width:38mm;background:#fff;border-radius:2mm;padding:2mm 2mm 1.4mm;text-align:center;color:#2B1F18;}}
.qr img{{width:34mm;height:34mm;display:block;}}
.qr div{{font-size:3.3mm;font-weight:700;line-height:1.2;margin-top:.6mm;}}
</style></head><body><div class="sheet"><div class="bar"></div>
  <div class="head"><img src="{bm.LOGO_COLOR}"><div class="new"><span class="tg">{c['tag']}</span>{c['new']}</div></div>
  <img class="ph" src="{PHOTO}">
  <h1>{c['title']}</h1>
  <div class="sub">{c['sub']}</div>
  <div class="info"><div class="h">{c['h']}</div><div class="d">{c['d']}</div><div class="t">{c['t']}</div>
    <div class="ad">{PIN}<span>{ADDR}</span></div></div>
  <div class="book">
    <div class="ticket"><div class="in"><div><div class="k">{c['k']}</div><div class="kd">{c['kd']}</div><div class="ph2">WhatsApp {c['phone']}</div></div>
      <div class="qr"><img src="{QR}"><div>{c['scan']}</div></div></div></div>
  </div>
</div></body></html>"""

if __name__ == "__main__":
    for lang, c in COPY.items():
        name = f"Patio-Phonetics-Flyer-A5-{lang}"
        path = os.path.join(OUT, name + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html(c))
        subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
            "--virtual-time-budget=6000", f"--print-to-pdf={os.path.join(OUT, name + '.pdf')}", path],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # PNG preview rendered from the PDF itself, 150 dpi
        import pypdfium2 as pdfium
        pdf = pdfium.PdfDocument(os.path.join(OUT, name + ".pdf"))
        print("  pages:", len(pdf))
        pdf[0].render(scale=150 / 72).to_pil().save(os.path.join(OUT, name + ".png"))
        print("rendered", name)
