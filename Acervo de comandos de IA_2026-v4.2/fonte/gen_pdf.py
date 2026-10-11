"""Gera o PDF (WeasyPrint) a partir de data.json, com capa, índice clicável, marcadores e paginação."""
import json, html
from weasyprint import HTML
data = json.load(open("data.json", encoding="utf-8"))
M = data["meta"]; e = html.escape
PL = {p["key"]: p["label"] for p in data["platforms"]}
SRC = {s["id"]: s for s in data["sources"]}
STY = {"oficial": "oficial, reaberta nesta revisão", "herdada": "oficial, citada em edição anterior e não reaberta",
       "busca": "oficial, localizada pela busca e não aberta", "nao-oficial": "não oficial"}

CSS = """
@page{size:A4;margin:20mm 17mm 20mm 17mm;
 @top-left{content:string(modtitle);font:8.5pt 'Inter',sans-serif;color:#6a716b}
 @top-right{content:"v%(v)s · %(d)s";font:8.5pt 'Inter',sans-serif;color:#6a716b}
 @bottom-left{content:"%(t)s";font:8pt 'Inter',sans-serif;color:#6a716b}
 @bottom-right{content:"Página " counter(page) " de " counter(pages);font:8.5pt 'Inter',sans-serif;color:#6a716b}}
@page cover{margin:0;@top-left{content:none}@top-right{content:none}@bottom-left{content:none}@bottom-right{content:none}}
@page toc{@top-left{content:"Índice"}}
body{font:10pt/1.5 'Inter',sans-serif;color:#1b1f23}
.cover{page:cover;height:297mm;background:#12463B;color:#fff;padding:40mm 22mm 0;position:relative;break-after:page}
.cover .ey{font-size:10pt;letter-spacing:.12em;text-transform:uppercase;opacity:.85}
.cover h1{font-size:30pt;line-height:1.15;margin:8mm 0 4mm;bookmark-level:none}
.cover .sub{font-size:15pt;opacity:.95}
.cover .box{margin-top:18mm;border-top:1px solid rgba(255,255,255,.4);padding-top:6mm;font-size:10.5pt;line-height:1.7}
.cover .foot{position:absolute;bottom:22mm;left:22mm;right:22mm;font-size:9pt;opacity:.85}
.toc{page:toc;break-after:page}
.toc h2{font-size:18pt;color:#12463B;margin:0 0 6mm;string-set:modtitle "Índice"}
.toc ol{list-style:none;padding:0;margin:0}
.toc li{margin:0;border-bottom:1px dotted #c9c6bb}
.toc li a{display:block;color:#1b1f23;text-decoration:none;padding:2.2mm 0}
.toc li a::after{content:target-counter(attr(href),page);float:right;color:#12463B;font-weight:600}
.toc li.sub a{padding-left:8mm;font-size:9.5pt;color:#444}
.howto{break-after:page}
h1.mod{font-size:17pt;color:#12463B;margin:0 0 2mm;string-set:modtitle content();bookmark-level:1;break-before:page}
.mdesc{color:#555d66;margin:0 0 5mm}
h2.sub{font-size:13pt;color:#12463B;bookmark-level:2;margin:7mm 0 3mm}
.item{border:0.6pt solid #d6d3c8;border-radius:2mm;padding:3.5mm 4mm;margin:0 0 4mm;break-inside:auto}
.item h3,.lbl,.tags{break-after:avoid}
.ih{break-inside:avoid;break-after:avoid}
.item p{orphans:3;widows:3}
.item h3{font-size:11pt;margin:0 0 1.5mm;bookmark-level:2}
.tags{margin:0 0 2mm}
.k,.p{display:inline-block;font-size:7.5pt;border-radius:1.2mm;padding:.3mm 1.6mm;margin:0 1mm 1mm 0}
.k{border:0.6pt solid currentColor;font-weight:700}
.k.cmd{color:#12463B}.k.ui{color:#2f6b5c}.k.prompt{color:#3d4f6b}.k.api{color:#8a6220}.k.unverified{color:#9E3B26}
.p{background:#efeee8;color:#4a5158}
.lbl{font-weight:700;font-size:8.5pt;color:#12463B;text-transform:uppercase;letter-spacing:.04em;margin:2mm 0 .5mm}
.pbox{break-inside:avoid;background:#f1f5f3;border-left:1.2mm solid #12463B;padding:2.5mm 3mm;border-radius:1mm;white-space:pre-wrap;font-size:9.5pt}
.pbox.code{font-family:'DejaVu Sans Mono',monospace}
.src{font-size:8.5pt;color:#444}
.src a{color:#12463B;word-break:break-all}
p{margin:.5mm 0}
.q{border:0.6pt solid #d6d3c8;border-radius:2mm;padding:2.5mm 3.5mm;margin:0 0 3mm;break-inside:avoid}
.q h3{font-size:10pt;margin:0 0 1mm;bookmark-level:none}
.srcl li{margin:0 0 2mm;font-size:9pt;break-inside:avoid}
.srcl a{color:#12463B;word-break:break-all}
.st{font-size:7.5pt;background:#efeee8;border-radius:1mm;padding:0 1.5mm}
.legend div{margin:1.5mm 0}
ul{padding-left:5mm}
""" % {"v": M["version"], "d": M["date"], "t": e(M["title"])}

def tags(x):
    return "".join(f'<span class="k {k}">{e(data["kinds"][k]["label"])}</span>' for k in x["kinds"]) + \
           "".join(f'<span class="p">{"Prompt portátil" if p=="portatil" else e(PL[p])}</span>' for p in x["platforms"])

def pbox(t):
    code = t.startswith("/") or t.startswith("$")
    return f'<div class="pbox{" code" if code else ""}">{e(t)}</div>'

def item(x):
    src = "; ".join(f'[{s}] <a href="{e(SRC[s]["url"])}">{e(SRC[s]["title"])}</a>' + (" (não reaberta nesta revisão)" if SRC[s]["type"] in ("herdada","busca") else "") for s in x["sources"])
    src = f"{src}. Verificado em {e(x['verified'])}." if src else "Prompt autoral; não depende de afirmação sobre produto."
    return f'''<div class="item" id="{x['id']}"><div class="ih"><h3>{e(x['title'])}</h3><div class="tags">{tags(x)}</div>
<div class="lbl">O que faz e quando usar</div><p>{e(x['what'])}</p></div>
<div class="lbl">Como usar</div><p>{e(x['how'])}</p>
<div class="lbl">Exemplo para copiar</div>{pbox(x['example'])}
<div class="lbl">Limitações e o que conferir</div><p>{e(x['limits'])}</p>
<div class="lbl">Fontes</div><p class="src">{src}</p></div>'''

parts = [f'''<section class="cover"><div class="ey">Consulta diária · pt-BR</div><h1>{e(M['title'])}</h1>
<div class="sub">{e(M['subtitle'])}</div>
<div class="box">Versão {M['version']} · pesquisa em {M['date']}<br>{len(data['items'])} itens em 17 módulos · {len(data['quick'])} exemplos de consulta rápida · {len(data['sources'])} fontes<br>
ChatGPT, Claude, Gemini, Microsoft Copilot, Perplexity, Grok, DeepSeek e Mistral Vibe, com Gemini Notebook, Midjourney, Google Flow, Runway, Kling, Luma, Adobe Firefly, Pika e Higgsfield.</div>
<div class="foot">{e(M['review'])} A seleção de plataformas não é ranking de mercado. Conteúdo equivalente à versão HTML, sem os controles interativos.</div></section>''']

toc = ['<section class="toc"><h2>Índice</h2><ol>', '<li><a href="#como-ler">Como ler este guia</a></li>']
for m in data["modules"]:
    toc.append(f'<li><a href="#mod-{m["n"]}">{m["n"]}. {e(m["title"])}</a></li>')
    if m["n"] == 17:
        for sid, st in (("historico", "Histórico de revisões"), ("consulta", "Consulta rápida"), ("fontes", "Fontes")):
            toc.append(f'<li class="sub"><a href="#{sid}">{st}</a></li>')
toc.append("</ol></section>")
parts.append("".join(toc))

legend = "".join(f'<div><span class="k {k}">{e(v["label"])}</span> {e(v["desc"])}</div>' for k, v in data["kinds"].items())
parts.append(f'''<section class="howto"><h1 class="mod" id="como-ler" style="break-before:auto">Como ler este guia</h1>
<p>Cada item traz classificação, plataformas, o que faz, como usar, exemplo pronto, limitações e fontes com data de verificação. Prompt portátil é uma instrução adaptável a diferentes modelos; não significa que todos pesquisem, executem ferramentas, exportem arquivos ou gerem mídia.</p>
<p>Modelo é o motor; aplicativo é o ambiente com menus, anexos, pesquisa e ferramentas. Capacidade documentada só na API não vale automaticamente para o aplicativo.</p>
<div class="lbl">Classificações</div><div class="legend">{legend}</div>
<p style="margin-top:4mm">Na versão HTML há busca, filtros, seleção e cópia. Neste PDF, use o índice e os marcadores do leitor.</p></section>''')

for m in data["modules"]:
    sec = [f'<h1 class="mod" id="mod-{m["n"]}">{m["n"]}. {e(m["title"])}</h1><p class="mdesc">{e(m["desc"])}</p>']
    if m["n"] == 17:
        sec.append('<h2 class="sub" id="historico">Histórico de revisões</h2>')
        for c in data["changelog"]:
            sec.append(f'<div class="lbl">Versão {e(c["version"])}{" · " + e(c["date"]) if c["date"] else ""}</div><ul>' + "".join(f"<li>{e(n)}</li>" for n in c["notes"]) + "</ul>")
        sec.append(f'<h2 class="sub" id="consulta">Consulta rápida · {len(data["quick"])} exemplos</h2><p>Itens iniciados com / são comandos documentados no ambiente indicado. Os demais são prompts.</p>')
        for q in data["quick"]:
            sec.append(f'<div class="q"><h3>{q["n"]:02d}. {e(q["title"])} <span style="font-weight:400;color:#666;font-size:8.5pt">· módulo {q["module"]}</span></h3><div class="tags">{tags(q)}</div>{pbox(q["example"])}</div>')
        sec.append(f'<h2 class="sub" id="fontes">Fontes e verificação · {len(data["sources"])}</h2><p>Pesquisa em {M["date"]}. Prompts são exemplos autorais; não houve teste de geração em todas as plataformas.</p><ol class="srcl" style="list-style:none;padding:0">')
        for s in data["sources"]:
            sec.append(f'<li id="src-{s["id"]}"><b>[{s["id"]}]</b> {e(s["title"])} <span class="st">{STY[s["type"]]}</span><br><a href="{e(s["url"])}">{e(s["url"])}</a></li>')
        sec.append("</ol>")
    else:
        G = {"": "Criação, edição e leitura de imagens", "Cena": "Construção de cena", "Estilo": "Estilos visuais", "Técnica": "Técnicas e parâmetros"}
        its = [x for x in data["items"] if x["module"] == m["n"]]
        grouped = any(x["title"].split(":")[0] in ("Cena", "Estilo", "Técnica") for x in its)
        last = None
        for x in its:
            g = x["title"].split(":")[0] if x["title"].split(":")[0] in ("Cena", "Estilo", "Técnica") else ""
            if grouped and g != last:
                n = sum(1 for y in its if (y["title"].split(":")[0] if y["title"].split(":")[0] in ("Cena", "Estilo", "Técnica") else "") == g)
                sec.append(f'<h2 class="sub">{G[g]} · {n}</h2>')
                last = g
            sec.append(item(x))
    parts.append("".join(sec))

doc = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{e(M["title"])}</title><meta name="author" content="Acervo Na Ponta do Lápis"><meta name="description" content="{e(M["subtitle"])}"><style>{CSS}</style></head><body>{"".join(parts)}</body></html>'
open("out/pdf_source.html", "w", encoding="utf-8").write(doc)
HTML(string=doc, base_url=".").write_pdf("out/guia-comandos-prompts-ia-2026.pdf")
print("pdf ok")
