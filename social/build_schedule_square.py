#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patio schedule graphic as a square Instagram post (1080x1080, 1:1)."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))
QR = b64(os.path.join(IMG, "qr-contact.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700;800&family=DM+Serif+Display&display=swap" rel="stylesheet">')

W, H = 1080, 1080

CLS = {
    "A1": ("#C19D5F", "#2B1F18"),
    "A1.2": ("#B8593A", "#FBF6EE"),
    "A2": ("#617C7B", "#FBF6EE"),
    "B1+": ("#79835F", "#FBF6EE"),
    "Conversação": ("#726651", "#FBF6EE"),
    "Oficinas tem\u00e1ticas": ("#8C6B45", "#FBF6EE"),
}

DAYS = ["Segunda", "Ter\u00e7a", "Quarta", "Quinta", "Sexta"]

SLOTS = [
    ("9h15", "10h45", [("A1", "AM"), "A2", ("A1", "AM"), "A2", "Oficinas tem\u00e1ticas"]),
    ("11h00", "12h30", ["B1+", "A1.2", "B1+", "A1.2", "Conversa\u00e7\u00e3o"]),
    ("18h30", "20h00", ["", ("A1", "PM"), "", ("A1", "PM"), ""]),
]

def cell(entry):
    if not entry:
        return '<td class="cell"><span class="empty"></span></td>'
    if isinstance(entry, tuple):
        cls, tag = entry[0], entry[1]
        bg, fg = CLS[cls]
    else:
        cls, tag = entry, None
        bg, fg = CLS[cls]
    size = "class-lg" if len(cls) <= 5 else "class-sm"
    tag_html = f'<span class="ampm">{tag}</span>' if tag else ''
    return (f'<td class="cell"><span class="chip {size}" '
            f'style="background:{bg};color:{fg};">{cls}{tag_html}</span></td>')

def build(fname):
    head = '<tr><th class="corner"></th>'
    for pt in DAYS:
        head += f'<th class="day"><span class="day-pt">{pt}</span></th>'
    head += '</tr>'
    rows = ""
    for a, b, classes in SLOTS:
        rows += (f'<tr><th class="time"><span class="t1">{a}</span>'
                 f'<span class="tdash">&ndash;</span><span class="t2">{b}</span></th>'
                 + "".join(cell(c) for c in classes) + '</tr>')
    legend = "".join(
        f'<span class="leg"><span class="dot" style="background:{CLS[c][0]}"></span>{lbl}</span>'
        for c, lbl in [("A1","A1 &middot; Beginner"),("A1.2","A1.2 &middot; Elementary"),
                       ("A2","A2 &middot; Pre-Interm."),("B1+","B1+ &middot; Interm."),
                       ("Oficinas tem\u00e1ticas","Workshops"),("Conversa\u00e7\u00e3o","Conversation")])
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#FBF6EE;
  font-family:'Barlow',sans-serif;padding:34px 40px 26px;display:flex;flex-direction:column;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:11px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{text-align:center;color:#726651;font-weight:700;letter-spacing:.2em;
  text-transform:uppercase;font-size:17px;}}
.title{{text-align:center;font-family:'DM Serif Display',serif;color:#2B1F18;
  font-size:44px;line-height:1.02;margin-top:4px;}}
.title .a{{color:#B8593A;font-style:italic;}}
.note{{text-align:center;color:#8a7d6c;font-size:17px;font-weight:600;margin-top:5px;}}
table{{width:100%;border-collapse:separate;border-spacing:7px;margin-top:14px;table-layout:fixed;}}
th.corner{{width:96px;}}
th.day{{background:#2B1F18;border-radius:11px;color:#FBF6EE;height:66px;
  text-align:center;vertical-align:middle;padding:0 4px;}}
.day-pt{{display:block;font-family:'DM Serif Display',serif;font-size:21px;line-height:1;}}
th.time{{width:96px;background:#EEE4D2;border-radius:11px;color:#2B1F18;
  text-align:center;vertical-align:middle;height:132px;}}
.t1,.t2{{display:block;font-size:22px;font-weight:800;line-height:1.12;}}
.tdash{{display:block;color:#B8593A;font-weight:800;font-size:15px;line-height:1;}}
td.cell{{vertical-align:middle;}}
.chip{{display:flex;flex-direction:column;align-items:center;justify-content:center;
  height:132px;border-radius:11px;font-weight:800;box-shadow:0 3px 9px rgba(43,31,24,.10);
  padding:0 3px;text-align:center;overflow:hidden;}}
.ampm{{font-size:15px;font-weight:700;letter-spacing:.12em;margin-top:4px;opacity:.82;}}
.empty{{display:block;height:132px;border-radius:11px;background:#F0E8DA;
  box-shadow:inset 0 0 0 2px rgba(43,31,24,.05);}}
.class-lg{{font-size:34px;letter-spacing:.02em;}}
.class-sm{{font-size:17px;line-height:1.15;}}
.legend{{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 18px;margin-top:14px;}}
.leg{{display:flex;align-items:center;gap:7px;color:#4a4038;font-size:17px;font-weight:600;}}
.dot{{width:14px;height:14px;border-radius:50%;display:inline-block;}}
.divider{{width:100%;height:1px;background:#e6dac5;margin:14px 0 12px;}}
.info{{display:flex;align-items:center;gap:22px;}}
.details{{flex:1;display:flex;flex-direction:column;gap:9px;}}
.drow{{display:flex;align-items:flex-start;gap:12px;}}
.dlabel{{flex:none;width:88px;color:#B8593A;font-weight:800;font-size:17px;
  letter-spacing:.05em;text-transform:uppercase;padding-top:2px;}}
.dvals{{flex:1;display:flex;flex-direction:column;gap:4px;}}
.pline{{color:#2B1F18;font-size:18px;font-weight:600;line-height:1.2;}}
.pline b{{color:#B8593A;font-weight:800;}}
.pnote{{color:#8a7d6c;font-size:14px;font-weight:600;font-style:italic;margin-top:1px;}}
.qr{{flex:none;display:flex;flex-direction:column;align-items:center;gap:5px;}}
.qr img{{width:118px;height:118px;border-radius:10px;background:#fff;padding:7px;
  box-shadow:0 4px 12px rgba(43,31,24,.12);}}
.qrlabel{{color:#726651;font-weight:700;font-size:14px;letter-spacing:.02em;}}
.foot{{margin-top:auto;display:flex;align-items:center;justify-content:center;gap:12px;padding-top:12px;}}
.foot img{{height:34px;}}
.foot span{{color:#726651;font-weight:600;font-size:18px;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Patio Language School</div>'
        f'<div class="title">Learn Portuguese at <span class="a">Patio</span></div>'
        f'<div class="note">Classes &middot; 21 September &ndash; 18 December 2026</div>'
        f'<table>{head}{rows}</table>'
        f'<div class="legend">{legend}</div>'
        f'<div class="divider"></div>'
        f'<div class="info">'
        f'<div class="details">'
        f'<div class="drow"><span class="dlabel">Prices</span><div class="dvals">'
        f'<div class="pline">Group Classes &nbsp;<b>&euro;11 / hour</b></div>'
        f'<div class="pnote">Mon/Wed &middot; 37.5 hours &nbsp;&middot;&nbsp; Tue/Thu &middot; 34.5 hours</div>'
        f'<div class="pline">Workshops &amp; Conversation &nbsp;<b>drop-in &euro;20 &middot; 5-pack &euro;85</b></div>'
        f'<div class="pline">Private lessons &nbsp;<b>on request</b></div>'
        f'</div></div>'
        f'<div class="drow"><span class="dlabel">Where</span><div class="dvals">'
        f'<div class="pline">Pra&ccedil;a do Poder Local, Lote 14, Loja C &middot; 8600-524 Lagos</div>'
        f'</div></div>'
        f'</div>'
        f'<div class="qr"><img src="{QR}"><span class="qrlabel">Scan to get in touch</span></div>'
        f'</div>'
        f'<div class="foot"><img src="{LOGO_COLOR}"><span>patiolanguage.pt</span></div>'
        f'</div>')
    html = f'<!DOCTYPE html><html><head>{FONTS}<style>{css}</style></head><body>{body}</body></html>'
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

def render(fname):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", f"--window-size={W},{H}",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    render(build("schedule-ig-square-1080x1080.html"))
    print("done")
