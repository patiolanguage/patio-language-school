#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patio schedule graphic for Instagram/Facebook Stories (1080x1920, 9:16)."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO_COLOR = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700;800&family=DM+Serif+Display&display=swap" rel="stylesheet">')

W, H = 1080, 1920

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
  font-family:'Barlow',sans-serif;padding:190px 54px 220px;display:flex;flex-direction:column;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:16px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{text-align:center;color:#726651;font-weight:700;letter-spacing:.22em;
  text-transform:uppercase;font-size:26px;}}
.title{{text-align:center;font-family:'DM Serif Display',serif;color:#2B1F18;
  font-size:82px;line-height:1.02;margin-top:10px;}}
.title .a{{color:#B8593A;font-style:italic;}}
.note{{text-align:center;color:#8a7d6c;font-size:28px;font-weight:600;margin-top:16px;}}
table{{width:100%;border-collapse:separate;border-spacing:11px;margin-top:44px;table-layout:fixed;}}
th.corner{{width:120px;}}
th.day{{background:#2B1F18;border-radius:14px;color:#FBF6EE;height:104px;
  text-align:center;vertical-align:middle;padding:0 4px;}}
.day-pt{{display:block;font-family:'DM Serif Display',serif;font-size:26px;line-height:1;}}
th.time{{width:120px;background:#EEE4D2;border-radius:14px;color:#2B1F18;
  text-align:center;vertical-align:middle;height:210px;}}
.t1,.t2{{display:block;font-size:29px;font-weight:800;line-height:1.15;}}
.tdash{{display:block;color:#B8593A;font-weight:800;font-size:20px;line-height:1;}}
td.cell{{vertical-align:middle;}}
.chip{{display:flex;flex-direction:column;align-items:center;justify-content:center;
  height:210px;border-radius:14px;font-weight:800;box-shadow:0 3px 10px rgba(43,31,24,.10);
  padding:0 4px;text-align:center;overflow:hidden;}}
.ampm{{font-size:22px;font-weight:700;letter-spacing:.14em;margin-top:7px;opacity:.82;}}
.empty{{display:block;height:210px;border-radius:14px;background:#F0E8DA;
  box-shadow:inset 0 0 0 2px rgba(43,31,24,.05);}}
.class-lg{{font-size:48px;letter-spacing:.02em;}}
.class-sm{{font-size:25px;line-height:1.2;}}
.legend{{display:flex;flex-wrap:wrap;justify-content:center;gap:14px 30px;margin-top:40px;}}
.leg{{display:flex;align-items:center;gap:10px;color:#4a4038;font-size:25px;font-weight:600;}}
.dot{{width:20px;height:20px;border-radius:50%;display:inline-block;}}
.cta{{margin-top:auto;text-align:center;}}
.cta .big{{font-family:'DM Serif Display',serif;color:#2B1F18;font-size:52px;line-height:1.05;}}
.cta .big .a{{color:#B8593A;font-style:italic;}}
.pill{{display:inline-block;margin-top:26px;background:#B8593A;color:#FBF6EE;
  font-weight:800;font-size:34px;letter-spacing:.02em;padding:22px 52px;border-radius:44px;}}
.foot{{display:flex;align-items:center;justify-content:center;gap:16px;margin-top:34px;}}
.foot img{{height:52px;}}
.foot span{{color:#726651;font-weight:700;font-size:30px;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Patio Language School</div>'
        f'<div class="title">Our fall schedule<br>is here</div>'
        f'<div class="note">Learn Portuguese in Lagos &middot; 21 Sep &ndash; 18 Dec 2026</div>'
        f'<table>{head}{rows}</table>'
        f'<div class="legend">{legend}</div>'
        f'<div class="cta">'
        f'<div class="big">Applications are <span class="a">open</span></div>'
        f'<div class="pill">Apply at patiolanguage.pt</div>'
        f'<div class="foot"><img src="{LOGO_COLOR}"><span>patiolanguage.pt</span></div>'
        f'</div>'
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
    render(build("schedule-story-1080x1920.html"))
    print("done")
