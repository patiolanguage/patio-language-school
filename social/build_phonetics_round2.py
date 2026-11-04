#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Phonetics Workshop, second round: Mon 23 + Fri 27 November 2026, 8h30 to 10h30,
€45, or €40 for Patio students. Bilingual (PT first, EN second), same look as round one.

Reuses the round-one builders and only swaps the wording:
  build_phonetics_launch  -> social posts (IG, FB, Story) + WhatsApp image
  build_phonetics_flyer   -> A5 print flyer
  build_phonetics_fbevent -> Facebook event cover

Outputs (social/Phonetics/round2/):
  phonetics2-bi-{ig,story,fb}-*.png, phonetics2-wa-wa-1080x1350.png
  Patio-Phonetics2-Flyer-A5-BI.pdf / .png
  phonetics2-fb-event-cover-1920x1005.png
Brand is "Patio", no accent. No em or en dashes.
"""
import os, subprocess
import build_mandarin as bm
import build_phonetics_launch as L
import build_phonetics_flyer as F

OUT = os.path.join(bm.SOCIAL, "Phonetics", "round2")
os.makedirs(OUT, exist_ok=True)

TAG, NEW = "Novas datas", "New dates"
DATES_PT, DATES_EN = "23 e 27 de novembro", "23 &amp; 27 November"
TIME_PT, TIME_EN = "8h30 às 10h30", "8h30 to 10h30"

# ---- social posts --------------------------------------------------------
L.OUT = OUT
base = dict(L.COPY["bi"])
base.update(
    tag=TAG, new=NEW,
    info_d=DATES_PT,
    info_t=f"{DATES_EN} &middot; {TIME_EN}",
    tk_k="45&nbsp;&euro;",
    tk_d="Alunos &middot; Students 40&nbsp;&euro;",
    tk_u="WhatsApp +351&nbsp;928&nbsp;129&nbsp;560",
)
L.COPY["2bi"] = base
wa = dict(L.COPY["wa"])
wa.update(tag=TAG, new=NEW, info_d=DATES_PT, info_t=TIME_PT,
          tk_k="45&nbsp;&euro;", tk_d="40&nbsp;&euro; alunos Patio",
          addr=L.ADDR_FULL)
L.COPY["2wa"] = wa

def render_posts():
    for fmt in ("ig", "story", "fb"):
        L.render("2bi", fmt)
    L.render("2wa", "wa")
    # tidy names: phonetics-2bi-... -> phonetics2-bi-...
    for f in os.listdir(OUT):
        if f.startswith("phonetics-2"):
            new = "phonetics2-" + f[len("phonetics-2"):]
            os.replace(os.path.join(OUT, f), os.path.join(OUT, new))

# ---- A5 print flyer ------------------------------------------------------
def render_flyer():
    c = dict(F.COPY["BI"])
    c.update(tag=TAG, new=NEW, d=DATES_PT, t=f"{DATES_EN} &middot; {TIME_EN}",
             k="45&nbsp;&euro;", kd="Alunos &middot; Students 40&nbsp;&euro;")
    name = "Patio-Phonetics2-Flyer-A5-BI"
    path = os.path.join(OUT, name + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(F.html(c))
    pdf = os.path.join(OUT, name + ".pdf")
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=6000", f"--print-to-pdf={pdf}", path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import pypdfium2 as pdfium
    doc = pdfium.PdfDocument(pdf)
    print("  pages:", len(doc))
    doc[0].render(scale=150 / 72).to_pil().save(os.path.join(OUT, name + ".png"))
    print("rendered", name)

# ---- Facebook event cover ------------------------------------------------
def render_event_cover():
    import build_phonetics_fbevent as E
    h = E.html
    h = h.replace('<span class="tg">New</span>at Patio', f'<span class="tg">{TAG}</span>{NEW}')
    h = h.replace('<div class="f">2 &amp; 6 November</div><div class="f">9h15 to 10h45</div><div class="f t">&euro;35</div>',
                  f'<div class="f">{DATES_EN}</div><div class="f">{TIME_EN}</div><div class="f t">&euro;45 &middot; students &euro;40</div>')
    h = h.replace(".row{{display:flex;align-items:center;gap:18px;margin-top:34px}}".replace("{{","{").replace("}}","}"),
                  ".row{display:flex;flex-wrap:wrap;align-items:center;gap:18px;margin-top:34px}")
    h = h.replace(".f{background:#fff;", ".f{white-space:nowrap;background:#fff;")
    h = h.replace(".addr{margin-left:20px;", ".addr{flex-basis:100%;margin-left:0;margin-top:4px;")
    base = os.path.join(OUT, "phonetics2-fb-event-cover-1920x1005")
    with open(base + ".html", "w", encoding="utf-8") as f:
        f.write(h)
    subprocess.run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
        f"--window-size={E.W},{E.H}", "--virtual-time-budget=6000", f"--screenshot={base}.png", base + ".html"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", os.path.basename(base) + ".png")

if __name__ == "__main__":
    render_posts()
    render_flyer()
    render_event_cover()
