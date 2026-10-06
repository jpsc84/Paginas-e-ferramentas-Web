# Acervo de Comandos e Prompts de IA 2026 · base de geração

Base estruturada única para o HTML (../index.html) e o PDF (../guia-comandos-prompts-ia-2026.pdf).

- data_core.py: metadados, plataformas, módulos, fontes e histórico de revisões.
- data_items1/2/3.py: itens dos módulos 1 a 16.
- data_quick.py: consulta rápida.
- build_data.py: valida e gera data.json.
- gen_html.py: gera out/index.html (e out/artifact.html para publicação no Claude).
- gen_pdf.py: gera o PDF com WeasyPrint.
- test_html.py: testes funcionais com Playwright.

Para regenerar: mkdir -p out && python3 build_data.py && python3 gen_html.py && python3 gen_pdf.py && python3 test_html.py
