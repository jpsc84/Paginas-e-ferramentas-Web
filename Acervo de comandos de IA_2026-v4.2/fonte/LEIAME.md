# Acervo de Comandos e Prompts de IA 2026 · base de geração

Base estruturada única para o HTML (../index.html) e o PDF (../guia-comandos-prompts-ia-2026.pdf).

- data_core.py: metadados, plataformas, módulos, fontes e histórico de revisões.
- data_items1/2/3/4.py: itens dos módulos 1 a 16 (o 4 traz a ampliação de imagens).
- data_quick.py: consulta rápida.
- build_data.py: valida e gera data.json.
- gen_html.py: gera out/index.html (e out/artifact.html para publicação no Claude).
- gen_pdf.py: gera o PDF com WeasyPrint.
- test_html.py: testes funcionais com Playwright.

Para regenerar: mkdir -p out && python3 build_data.py && python3 gen_html.py && python3 gen_pdf.py && python3 test_html.py

Ícone do app: fonte/pwa/ tem icon.svg, maskable.svg, manifest.json e gen_icons.py (gera icons/ a partir dos SVGs). manifest.json e icons/ ficam ao lado do index.html.
Modo offline: gen_html.py também gera out/sw.js (service worker), que fica ao lado do index.html. O nome do cache acompanha a versão em META; ao publicar nova versão, o app baixa a atualização na próxima abertura com internet.
