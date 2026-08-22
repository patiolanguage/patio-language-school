#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patio Language School weekly schedule grid (1080x1620) - PORTUGUESE version."""
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

W, H = 1080, 1620

# class -> (background color, text color)
CLS = {
    "A1": ("#C19D5F", "#2B1F18"),
    "A1.2": ("#B8593A", "#FBF6EE"),
    "A2": ("#617C7B", "#FBF6EE"),
    "B1+": ("#79835F", "#FBF6EE"),
    "Conversação": ("#726651", "#FBF6EE"),
    "Oficinas tem\u00e1ticas": ("#8C6B45", "#FBF6EE"),
}

DAYS = [("Segunda", "Mon"), ("Ter\u00e7a", "Tue"), ("Quarta", "Wed"),
        ("Quinta", "Thu"), ("Sexta", "Fri")]

# two time rows, one entry per day. tag = manhã / noite
SLOTS = [
    ("9h15", "10h45", [("A1", "Manh\u00e3"), "A2", ("A1", "Manh\u00e3"), "A2", "Oficinas tem\u00e1ticas"]),
    ("11h00", "12h30", ["B1+", "A1.2", "B1+", "A1.2", "Conversa\u00e7\u00e3o"]),
    ("18h30", "20h00", ["", ("A1", "Tarde"), "", ("A1", "Tarde"), ""]),
]

def cell(entry):
    if not entry:
        return '<td class="cell"><span class="empty"></span></td>'
    if isinstance(entry, tuple):
        p = list(entry)
        cls = p[0]
        tag = p[1] if len(p) > 1 else None
        bg = p[2] if len(p) > 2 else CLS[cls][0]
        fg = p[3] if len(p) > 2 else CLS[cls][1]
    else:
        cls, tag = entry, None
        bg, fg = CLS[cls]
    size = "class-lg" if len(cls) <= 5 else "class-sm"
    tag_html = f'<span class="ampm">{tag}</span>' if tag else ''
    return (f'<td class="cell"><span class="chip {size}" '
            f'style="background:{bg};color:{fg};">{cls}{tag_html}</span></td>')

def build(fname):
    head = '<tr><th class="corner"></th>'
    for pt, en in DAYS:
        head += f'<th class="day"><span class="day-pt">{pt}</span></th>'
    head += '</tr>'
    rows = ""
    for a, b, classes in SLOTS:
        rows += (f'<tr><th class="time"><span class="t1">{a}</span>'
                 f'<span class="tdash">&ndash;</span><span class="t2">{b}</span></th>'
                 + "".join(cell(c) for c in classes) + '</tr>')
    legend = "".join(
        f'<span class="leg"><span class="dot" style="background:{CLS[c][0]}"></span>{lbl}</span>'
        for c, lbl in [("A1","A1 &middot; Iniciante"),("A1.2","A1.2 &middot; Elementar"),
                       ("A2","A2 &middot; Pr\u00e9-Interm\u00e9dio"),("B1+","B1+ &middot; Interm\u00e9dio"),
                       ("Oficinas tem\u00e1ticas","Oficinas tem\u00e1ticas"),("Conversa\u00e7\u00e3o","Conversa\u00e7\u00e3o")])
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:#FBF6EE;
  font-family:'Barlow',sans-serif;padding:74px 42px 60px;display:flex;flex-direction:column;}}
.canvas::before{{content:'';position:absolute;top:0;left:0;right:0;height:14px;
  background:linear-gradient(90deg,#C19D5F,#B8593A);}}
.eyebrow{{text-align:center;color:#726651;font-weight:700;letter-spacing:.2em;
  text-transform:uppercase;font-size:23px;}}
.title{{text-align:center;font-family:'DM Serif Display',serif;color:#2B1F18;
  font-size:66px;line-height:1.02;margin-top:8px;}}
.title .a{{color:#B8593A;font-style:italic;}}
.note{{text-align:center;color:#8a7d6c;font-size:23px;font-weight:500;margin-top:12px;}}
table{{width:100%;border-collapse:separate;border-spacing:10px;margin-top:30px;table-layout:fixed;}}
th.corner{{width:116px;}}
th.day{{background:#2B1F18;border-radius:13px;color:#FBF6EE;height:118px;
  text-align:center;vertical-align:middle;padding:0 6px;}}
.day-pt{{display:block;font-family:'DM Serif Display',serif;font-size:29px;line-height:1;}}
.day-en{{display:block;font-size:16px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;
  color:#C19D5F;margin-top:6px;}}
th.time{{width:116px;background:#EEE4D2;border-radius:13px;color:#2B1F18;
  text-align:center;vertical-align:middle;height:224px;}}
.t1,.t2{{display:block;font-size:29px;font-weight:800;line-height:1.15;}}
.tdash{{display:block;color:#B8593A;font-weight:800;font-size:20px;line-height:1;}}
td.cell{{vertical-align:middle;}}
.chip{{display:flex;flex-direction:column;align-items:center;justify-content:center;
  height:224px;border-radius:13px;font-weight:800;box-shadow:0 3px 10px rgba(43,31,24,.10);
  padding:0 4px;text-align:center;overflow:hidden;}}
.ampm{{font-size:22px;font-weight:700;letter-spacing:.08em;margin-top:8px;opacity:.82;}}
.empty{{display:block;height:224px;border-radius:13px;background:#F0E8DA;
  box-shadow:inset 0 0 0 2px rgba(43,31,24,.05);}}
.class-lg{{font-size:46px;letter-spacing:.02em;}}
.class-sm{{font-size:24px;line-height:1.2;}}
.chip.tall{{height:458px;}}
.span-time{{display:block;font-size:19px;font-weight:700;letter-spacing:.05em;margin-top:12px;opacity:.85;}}
.legend{{display:flex;flex-wrap:wrap;justify-content:center;gap:14px 26px;margin-top:32px;}}
.leg{{display:flex;align-items:center;gap:9px;color:#4a4038;font-size:23px;font-weight:600;}}
.dot{{width:19px;height:19px;border-radius:50%;display:inline-block;}}
.divider{{width:100%;height:1px;background:#e6dac5;margin:30px 0 24px;}}
.info{{display:flex;align-items:center;gap:34px;}}
.details{{flex:1;display:flex;flex-direction:column;gap:18px;}}
.drow{{display:flex;align-items:flex-start;gap:16px;}}
.dlabel{{flex:none;width:112px;color:#B8593A;font-weight:800;font-size:23px;
  letter-spacing:.06em;text-transform:uppercase;padding-top:2px;}}
.dvals{{flex:1;display:flex;flex-direction:column;gap:7px;}}
.pline{{color:#2B1F18;font-size:24px;font-weight:600;line-height:1.25;}}
.pline b{{color:#B8593A;font-weight:800;}}
.pline.pbig{{font-size:29px;}}
.pnote{{color:#8a7d6c;font-size:20px;font-weight:600;font-style:italic;margin-top:4px;}}
.qr{{flex:none;display:flex;flex-direction:column;align-items:center;gap:9px;}}
.qr img{{width:176px;height:176px;border-radius:12px;background:#fff;padding:9px;
  box-shadow:0 4px 14px rgba(43,31,24,.12);}}
.qrlabel{{color:#726651;font-weight:700;font-size:20px;letter-spacing:.03em;text-align:center;max-width:200px;}}
.foot{{margin-top:auto;display:flex;align-items:center;justify-content:center;gap:16px;padding-top:26px;}}
.foot img{{height:46px;}}
.foot span{{color:#726651;font-weight:600;font-size:24px;}}
"""
    body = (f'<div class="canvas">'
        f'<div class="eyebrow">Patio Language School</div>'
        f'<div class="title">Aprende portugu&ecirc;s no <span class="a">P&aacute;tio</span></div>'
        f'<div class="note">Aulas &middot; 21 de setembro &ndash; 18 de dezembro de 2026</div>'
        f'<table>{head}{rows}</table>'
        f'<div class="legend">{legend}</div>'
        f'<div class="divider"></div>'
        f'<div class="info">'
        f'<div class="details">'
        f'<div class="drow"><span class="dlabel">Pre&ccedil;os</span><div class="dvals">'
        f'<div class="pline">Aulas de grupo &nbsp;<b>&euro;11 / hora</b></div>'
        f'<div class="pnote">Seg/Qua &middot; 37,5 horas &nbsp;&middot;&nbsp; Ter/Qui &middot; 34,5 horas</div>'
        f'<div class="pline">Oficinas &amp; Conversa&ccedil;&atilde;o &nbsp;<b>avulso &euro;20 &middot; pack de 5 sess&otilde;es &euro;85</b></div>'
        f'<div class="pline">Aulas particulares &nbsp;<b>sob marca&ccedil;&atilde;o</b></div>'
        f'</div></div>'
        f'<div class="drow"><span class="dlabel">Onde</span><div class="dvals">'
        f'<div class="pline">Pra&ccedil;a do Poder Local, Lote 14, Loja C &middot; 8600-524 Lagos</div>'
        f'</div></div>'
        f'</div>'
        f'<div class="qr"><img src="{QR}"><span class="qrlabel">L&ecirc; o c&oacute;digo para falares connosco</span></div>'
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
    render(build("schedule-sample-pt-1080x1620.html"))
    print("done")
