#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Render the Teste de Nível — Guia de Avaliação (A4 PDF + PNG) for Sofia, in European Portuguese."""
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
h1{font-family:'DM Serif Display',serif;font-size:23pt;color:#2B1F18;line-height:1;}
.subttl{color:#726651;font-weight:600;font-size:9.5pt;letter-spacing:.04em;
  margin-top:4px;}
.intro{color:#4a4038;font-size:10.6pt;margin-bottom:16px;max-width:66ch;}
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
        ("Acolhimento", "1&ndash;2 min &middot; em inglês", "Põe o aluno à vontade &mdash; uma conversa amigável, sem teste, sem respostas erradas. Pergunta o que o levou ao português."),
        ("Aquecimento em português", "2 min", "Cumprimentos e apresentações simples. Vê o que consegue produzir por si."),
        ("Sobe a escada de perguntas", "5&ndash;6 min", "Avança pelas perguntas de diagnóstico abaixo; para quando já não conseguir responder com à-vontade."),
        ("Deixa-o falar", "2&ndash;3 min", "Um minuto sobre um tema familiar, para avaliar a fluência e a confiança."),
        ("Objetivos &amp; horários", "2 min", "O que procura no curso e que dias/horas lhe convêm &mdash; manhãs ou noites."),
        ("Fecho", "1 min", "Agradece; diz que vais dar seguimento com o nível dele e a turma certa."),
    ]
    flow_html = "".join(
        f'<li><b>{t}</b> <span class="t">&middot; {tm}</span><br>{d}</li>'
        for t, tm, d in flow)

    rows = [
        ("#C19D5F", "A1", "Principiante total", "Pouco ou nenhum português.",
         "Recorre logo ao inglês; quando muito, algumas palavras soltas."),
        ("#B8593A", "A1.2", "Principiante em progressão", "Cumprimentar, apresentar-se, dar informação pessoal básica, usar o presente dos verbos comuns e fazer perguntas simples.",
         "À vontade com &ldquo;Como se chama? De onde é?&rdquo; Tem dificuldade com o passado."),
        ("#617C7B", "A2", "Pós-A1 / Elementar", "Lidar com trocas do dia a dia &mdash; rotina, família, trabalho, pedidos &mdash; usando o passado e o futuro próximo.",
         "Usa o pretérito perfeito, liga ideias e comunica apesar dos erros."),
        ("#726651", "Conversação B1+", "Conversação", "Manter uma conversa, dar opiniões, contar histórias e lidar com temas inesperados.",
         "Fala longamente; quer fluência e prática, não gramática básica &rarr; turma de Conversação."),
    ]
    trows = "".join(
        f'<tr><td class="lvl"><span class="chip" style="background:{c}">{lv}</span>'
        f'<span class="desc">{nm}</span></td><td>{can}</td><td>{hear}</td></tr>'
        for c, lv, nm, can, hear in rows)

    ladder = [
        ("1", "Olá! Como se chama? De onde é? Onde mora?", "o A1.2 consegue responder."),
        ("2", "O que gosta de fazer? A que horas se levanta?", "o A2 responde com à-vontade."),
        ("3", "O que fez no fim de semana passado?", "o A2+ recorre ao passado."),
        ("4", "Porque quer aprender português? O que acha de viver em Lagos?", "o B1+ desenvolve."),
    ]
    lad = "".join(
        f'<div class="rung"><span class="n">{n}</span><span class="q"><i>&ldquo;{q}&rdquo;</i> '
        f'<span class="exp">&mdash; {e}</span></span></div>' for n, q, e in ladder)

    html = f"""<!DOCTYPE html><html lang="pt-PT"><head>{FONTS}<style>{CSS}</style></head><body>
<div class="head">
  <img src="{LOGO}" alt="Patio Language School">
  <div class="ttl"><h1>Teste de Nível &mdash; Guia de Avaliação</h1>
    <div class="subttl">Uma conversa breve e acolhedora para apurar o nível &middot; para a Sofia</div></div>
</div>
<p class="intro">Uma conversa breve, consistente e sem pressão para colocar cada aluno na turma certa
&mdash; <b>A1, A1.2, A2 ou Conversação B1+</b> &mdash; e registar a sua disponibilidade, para podermos
formar os grupos. Não há aprovação nem reprovação; o objetivo é apenas perceber em que ponto está e o que lhe convém.</p>

<h2>Como decorre a conversa de 15 minutos</h2>
<ol class="flow">{flow_html}</ol>

<h2>Grelha de níveis</h2>
<table><thead><tr><th style="width:27%">Nível</th><th style="width:40%">Consegue normalmente&hellip;</th>
<th style="width:33%">Vais ouvir</th></tr></thead><tbody>{trows}</tbody></table>

<h2>Escada de diagnóstico</h2>
<p class="intro" style="margin-bottom:8px">Pergunta em português; passa ao inglês só para tranquilizar e depois volta.
Sobe até já não conseguir acompanhar.</p>
<div class="ladder">{lad}</div>
<div class="rule"><b>Regra prática:</b> coloca-o no nível mais alto que consegue com relativa facilidade.
Se travar num nível, desce um.</div>

<h2>Depois da conversa</h2>
<div class="cols">
  <div class="box"><h3>Regista de cada aluno</h3><ul>
    <li>Nome e contacto</li>
    <li>Experiência anterior (o que diz ter)</li>
    <li>Nível observado &rarr; turma recomendada</li>
    <li>Disponibilidade: manhãs / noites, que dias</li>
    <li>Objetivos e motivação</li>
    <li>Outras notas (confiança, necessidades específicas)</li>
  </ul></div>
  <div class="box b"><h3>Mantém o tom acolhedor</h3><ul>
    <li>Tranquiliza várias vezes &mdash; &ldquo;não há certo nem errado.&rdquo;</li>
    <li>Fica em português o mais possível; passa ao inglês para dar conforto.</li>
    <li>A disponibilidade conta tanto como o nível &mdash; é o que define os grupos.</li>
    <li>Termina com um passo seguinte claro: o nível, a turma e como reservar lugar para setembro.</li>
  </ul></div>
</div>

<div class="foot"><span>Patio Language School &middot; Lagos, Portugal</span>
<span>patiolanguage.pt &middot; Uso interno</span></div>
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
    f = build("teste-de-nivel-guia-avaliacao.html")
    render_pdf(f)
    render_png(f)
    print("done")
