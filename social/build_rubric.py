#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Render the Level Check assessment guide (A4 PDF + PNG preview) for Sofia."""
import base64, os, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOCIAL = os.path.join(ROOT, "social")
IMG = os.path.join(ROOT, "assets", "img")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def b64(path, mime="image/png"):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

LOGO = b64(os.path.join(IMG, "Patio-Language-School-Logo-Color.png"))

FONTS = ('<meta charset="UTF-8">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">')

CSS = """
@page { size: A4; margin: 13mm 14mm; }
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Barlow',system-ui,sans-serif;color:#2B1F18;background:#fff;
  font-size:10.6pt;line-height:1.42;}
.head{display:flex;align-items:center;justify-content:space-between;
  border-bottom:2.5px solid #C19D5F;padding-bottom:12px;margin-bottom:16px;}
.head img{height:44px;}
.head .ttl{text-align:right;}
h1{font-family:'DM Serif Display',serif;font-size:24pt;color:#2B1F18;line-height:1;}
.subttl{color:#726651;font-weight:600;font-size:9.5pt;letter-spacing:.06em;
  text-transform:uppercase;margin-top:4px;}
.intro{color:#4a4038;font-size:10.6pt;margin-bottom:16px;max-width:64ch;}
.intro b{color:#B8593A;}
h2{font-family:'DM Serif Display',serif;font-size:14.5pt;color:#B8593A;
  margin:18px 0 9px;}
.flow{list-style:none;counter-reset:step;display:flex;flex-direction:column;gap:7px;}
.flow li{position:relative;padding-left:40px;counter-increment:step;}
.flow li::before{content:counter(step);position:absolute;left:0;top:-1px;
  width:26px;height:26px;border-radius:50%;background:#617C7B;color:#fff;
  font-weight:700;font-size:10pt;display:flex;align-items:center;justify-content:center;}
.flow b{color:#2B1F18;}
.flow .t{color:#726651;font-weight:600;font-size:9pt;}
table{width:100%;border-collapse:collapse;margin-top:4px;}
th,td{text-align:left;vertical-align:top;padding:8px 10px;font-size:9.9pt;}
thead th{background:#2B1F18;color:#FBF6EE;font-weight:700;font-size:8.6pt;
  letter-spacing:.05em;text-transform:uppercase;}
tbody tr{border-bottom:1px solid #ece3d3;}
.lvl{white-space:nowrap;font-weight:700;}
.chip{display:inline-block;color:#fff;font-weight:800;font-size:9pt;
  padding:3px 9px;border-radius:20px;margin-bottom:3px;}
.desc{color:#4a4038;font-weight:600;font-size:8.6pt;display:block;}
.ladder{display:flex;flex-direction:column;gap:8px;margin-top:2px;}
.rung{display:flex;gap:12px;align-items:baseline;}
.rung .n{flex:none;color:#C19D5F;font-family:'DM Serif Display',serif;font-size:13pt;width:20px;}
.rung .q{color:#2B1F18;}
.rung .q i{color:#617C7B;}
.rung .exp{color:#8a7d6c;font-weight:600;}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:4px;}
.box{background:#FBF6EE;border-left:4px solid #C19D5F;border-radius:8px;padding:12px 14px;}
.box.b{border-left-color:#B8593A;}
.box h3{font-size:10pt;color:#2B1F18;margin-bottom:6px;letter-spacing:.02em;}
.box ul{list-style:none;display:flex;flex-direction:column;gap:4px;}
.box li{position:relative;padding-left:16px;font-size:9.6pt;color:#4a4038;}
.box li::before{content:'';position:absolute;left:0;top:7px;width:6px;height:6px;
  border-radius:50%;background:#C19D5F;}
.box.b li::before{background:#B8593A;}
.rule{border-left:4px solid #617C7B;background:#eef2f1;border-radius:8px;
  padding:9px 14px;margin-top:10px;font-size:9.8pt;color:#2B1F18;}
.rule b{color:#617C7B;}
.foot{margin-top:16px;border-top:1px solid #ece3d3;padding-top:8px;
  color:#8a7d6c;font-size:8.4pt;display:flex;justify-content:space-between;}
"""

def build(fname):
    flow = [
        ("Welcome", "1&ndash;2 min &middot; English", "Put them at ease &mdash; a friendly chat, no test, no wrong answers. Ask what drew them to Portuguese."),
        ("Warm up in Portuguese", "2 min", "Simple greetings and introductions. See what they can produce on their own."),
        ("Work up the ladder", "5&ndash;6 min", "Climb the diagnostic prompts below; stop where they can no longer respond with ease."),
        ("Let them speak", "2&ndash;3 min", "A minute on a familiar topic, to gauge fluency and confidence."),
        ("Goals &amp; times", "2 min", "What they want from the course, and which days/times suit &mdash; mornings or evenings."),
        ("Close", "1 min", "Thank them; say you&rsquo;ll follow up with their level and the right class."),
    ]
    flow_html = "".join(
        f'<li><b>{t}</b> <span class="t">&middot; {tm}</span><br>{d}</li>'
        for t, tm, d in flow)

    rows = [
        ("#C19D5F", "A1", "Complete beginner", "Little to no Portuguese.",
         "Falls back to English straight away; a few isolated words at most."),
        ("#B8593A", "A1.2", "Continuing beginner", "Greet, introduce themselves, give basic personal info, use the present tense of common verbs, ask simple questions.",
         "Comfortable with &ldquo;Como se chama? De onde &eacute;?&rdquo; Struggles with the past tense."),
        ("#617C7B", "A2", "Post-A1 / Elementary", "Handle everyday exchanges &mdash; routine, family, work, ordering &mdash; using past and near-future tenses.",
         "Uses the pret&eacute;rito perfeito, links ideas, communicates despite errors."),
        ("#726651", "B1+", "Conversation", "Hold a conversation, give opinions, tell stories, cope with unexpected topics.",
         "Speaks at length; wants fluency and practice, not grammar basics &rarr; Conversation class."),
    ]
    trows = "".join(
        f'<tr><td class="lvl"><span class="chip" style="background:{c}">{lv}</span>'
        f'<span class="desc">{nm}</span></td><td>{can}</td><td>{hear}</td></tr>'
        for c, lv, nm, can, hear in rows)

    ladder = [
        ("1", "Ol&aacute;! Como se chama? De onde &eacute;? Onde mora?", "A1.2 can answer."),
        ("2", "O que gosta de fazer? A que horas se levanta?", "A2 answers with ease."),
        ("3", "O que fez no fim de semana passado?", "A2+ reaches for the past tense."),
        ("4", "Porque quer aprender portugu&ecirc;s? O que acha de viver em Lagos?", "B1+ elaborates."),
    ]
    lad = "".join(
        f'<div class="rung"><span class="n">{n}</span><span class="q"><i>&ldquo;{q}&rdquo;</i> '
        f'<span class="exp">&mdash; {e}</span></span></div>' for n, q, e in ladder)

    html = f"""<!DOCTYPE html><html lang="en"><head>{FONTS}<style>{CSS}</style></head><body>
<div class="head">
  <img src="{LOGO}" alt="Patio Language School">
  <div class="ttl"><h1>Level Check &mdash; Assessment Guide</h1>
    <div class="subttl">A quick, warm placement chat &middot; for Sofia</div></div>
</div>
<p class="intro">A short, consistent, low-pressure conversation to place each student in the right class
&mdash; <b>A1, A1.2, A2, or B1+ Conversation</b> &mdash; and to note their availability so we can form
groups. There is no pass or fail; the goal is simply to find where they are and what suits them.</p>

<h2>How the 15-minute check flows</h2>
<ol class="flow">{flow_html}</ol>

<h2>Level rubric</h2>
<table><thead><tr><th style="width:26%">Level</th><th style="width:40%">Can typically&hellip;</th>
<th style="width:34%">You&rsquo;ll hear</th></tr></thead><tbody>{trows}</tbody></table>

<h2>Diagnostic ladder</h2>
<p class="intro" style="margin-bottom:8px">Ask in Portuguese; drop into English only to reassure, then return.
Climb until they can no longer keep up.</p>
<div class="ladder">{lad}</div>
<div class="rule"><b>Rule of thumb:</b> place them at the highest rung they handle with reasonable ease.
If they stall at a rung, drop one.</div>

<h2>After the chat</h2>
<div class="cols">
  <div class="box"><h3>Note for each student</h3><ul>
    <li>Name &amp; contact</li>
    <li>Prior experience (self-reported)</li>
    <li>Observed level &rarr; recommended class</li>
    <li>Availability: mornings / evenings, which days</li>
    <li>Goals &amp; motivation</li>
    <li>Anything else (confidence, specific needs)</li>
  </ul></div>
  <div class="box b"><h3>Keep it warm</h3><ul>
    <li>Reassure often &mdash; &ldquo;n&atilde;o h&aacute; certo nem errado.&rdquo;</li>
    <li>Stay in Portuguese as far as they can go; switch to English to comfort.</li>
    <li>Availability matters as much as level &mdash; it decides the groups.</li>
    <li>End with a clear next step: their level, the class, and how to reserve a September spot.</li>
  </ul></div>
</div>

<div class="foot"><span>Patio Language School &middot; Lagos, Portugal</span>
<span>patiolanguage.pt &middot; Internal use</span></div>
</body></html>"""
    with open(os.path.join(SOCIAL, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname

def render_pdf(fname):
    pdf = fname.replace(".html", ".pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=4000",
        f"--print-to-pdf={os.path.join(SOCIAL, pdf)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", pdf)

def render_png(fname):
    png = fname.replace(".html", ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2", "--window-size=794,1123",
        f"--screenshot={os.path.join(SOCIAL, png)}", os.path.join(SOCIAL, fname)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("rendered", png)

if __name__ == "__main__":
    f = build("level-check-assessment-guide.html")
    render_pdf(f)
    render_png(f)
    print("done")
