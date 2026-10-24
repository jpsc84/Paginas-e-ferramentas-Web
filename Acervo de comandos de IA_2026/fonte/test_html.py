"""Testes funcionais do HTML com Playwright (viewport de celular e desktop)."""
import json, sys
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "file:///home/claude/acervo/out/index.html"
data = json.load(open("/home/claude/acervo/data.json", encoding="utf-8"))
results = []
def check(name, cond, info=""):
    results.append((name, bool(cond), info)); print(("OK  " if cond else "FALHA ") + name, info)

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 375, "height": 760}, device_scale_factor=2, is_mobile=True, has_touch=True,
                        permissions=["clipboard-read", "clipboard-write"])
    pg = ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "ERR_TUNNEL" not in m.text and "fonts.g" not in m.text else None)
    pg.goto(URL); pg.wait_for_timeout(600)
    check("sem erros de JS", not errs, str(errs[:3]))
    check("17 módulos renderizados", pg.locator("section.mod").count() == 17)
    check("cards de itens = base", pg.locator("article.card").count() == len(data["items"]), pg.locator("article.card").count())
    check("consulta rápida >= 60", pg.locator(".q").count() >= 60, pg.locator(".q").count())
    check("módulos começam recolhidos", pg.locator(".mod-body:not([hidden])").count() == 0)
    sw = pg.evaluate("document.documentElement.scrollWidth"); check("sem rolagem horizontal 375px", sw <= 375, sw)
    pg.screenshot(path="/home/claude/acervo/review/m_inicio.png")
    # abrir módulo
    pg.click("#mod-3 .mod-head"); check("abrir módulo 3", pg.locator("#b-3").is_visible())
    pg.click("#mod-3 .mod-head"); check("recolher módulo 3", not pg.locator("#b-3").is_visible())
    # menu
    pg.click("#btnMenu"); check("menu abre", pg.locator("#menu").is_visible())
    pg.click("#menuList button[data-go='12']"); pg.wait_for_timeout(500)
    check("menu leva ao módulo 12 aberto", pg.locator("#b-12").is_visible() and not pg.locator("#menu").is_visible())
    pg.click("#collapse") if pg.locator("#collapse").is_visible() else None
    # busca
    pg.fill("#q", "speedshot"); pg.wait_for_timeout(400)
    vis = pg.locator("article.card:visible, .q:visible").count()
    check("busca 'speedshot' encontra itens", vis >= 2, vis)
    pg.screenshot(path="/home/claude/acervo/review/m_busca.png")
    pg.fill("#q", "orcamento previsto"); pg.wait_for_timeout(400)
    check("busca com dois termos e acento", pg.locator("article.card:visible, .q:visible").count() >= 1, pg.locator("article.card:visible, .q:visible").count())
    pg.fill("#q", "zzzxxyy"); pg.wait_for_timeout(400)
    check("busca sem resultado mostra aviso", pg.locator("#empty").is_visible())
    pg.click("#qclear"); pg.wait_for_timeout(300)
    check("limpar busca restaura", pg.locator("section.mod:visible").count() == 17)
    # filtros
    pg.click("#btnFilters"); check("painel de filtros abre", pg.locator("#filters").is_visible())
    pg.click("#fPlat [data-plat='claude']"); pg.uncheck("#tPortable"); pg.wait_for_timeout(300)
    exp = sum(1 for x in data["items"] if "claude" in x["platforms"]) + sum(1 for x in data["quick"] if "claude" in x["platforms"])
    got = pg.locator("article.card:not([hidden]), .q:not([hidden])").count()
    check("filtro Claude sem portáteis = base", got == exp, f"{got} vs {exp}")
    pg.check("#tPortable"); pg.wait_for_timeout(300)
    exp2 = sum(1 for x in data["items"] + data["quick"] if "claude" in x["platforms"] or "portatil" in x["platforms"])
    got2 = pg.locator("article.card:not([hidden]), .q:not([hidden])").count()
    check("filtro Claude com portáteis = base", got2 == exp2, f"{got2} vs {exp2}")
    pg.click("#reset"); pg.wait_for_timeout(200)
    pg.click("#fKind [data-kind='cmd']"); pg.wait_for_timeout(300)
    exp3 = sum(1 for x in data["items"] + data["quick"] if "cmd" in x["kinds"])
    got3 = pg.locator("article.card:not([hidden]), .q:not([hidden])").count()
    check("filtro classe comando = base", got3 == exp3, f"{got3} vs {exp3}")
    pg.click("#reset"); pg.select_option("#fMod", "7"); pg.wait_for_timeout(300)
    vis_mods = pg.eval_on_selector_all("section.mod:not([hidden])", "els=>els.map(e=>e.id)")
    check("filtro por tarefa mostra módulo 7 (e exemplos rápidos do 7)", set(vis_mods) <= {"mod-7","mod-17"} and "mod-7" in vis_mods, vis_mods)
    qv = pg.eval_on_selector_all(".q:not([hidden])", "els=>els.length")
    check("exemplos rápidos filtrados por tarefa", qv == sum(1 for q in data["quick"] if q["module"]==7), qv)
    pg.click("#reset"); pg.wait_for_timeout(200)
    # limitações
    pg.check("#tLim"); pg.wait_for_timeout(200)
    check("abrir limitações abre todos details", pg.locator("details.more[open]").count() == len(data["items"]))
    pg.uncheck("#tLim"); pg.click("#btnFilters")
    # seleção e cópia individual
    if pg.get_attribute("#mod-3 .mod-head","aria-expanded")!="true": pg.click("#mod-3 .mod-head")
    pg.locator("#b-3 [data-copy]").first.click(); pg.wait_for_timeout(300)
    clip = pg.evaluate("navigator.clipboard.readText()")
    check("copiar texto individual", clip == [x for x in data["items"] if x["module"] == 3][0]["example"])
    check("toast de cópia visível", pg.locator("#toast.on").count() == 1)
    boxes = pg.locator("#b-3 [data-sel]")
    boxes.nth(0).check(); boxes.nth(1).check()
    if pg.get_attribute("#mod-17 .mod-head","aria-expanded")!="true": pg.click("#mod-17 .mod-head")
    pg.locator(".q [data-sel]").nth(0).check()
    sw17 = pg.evaluate("document.documentElement.scrollWidth"); check("sem rolagem horizontal com módulo 17 aberto", sw17 <= 375, sw17)
    check("barra de lote mostra 3", "3 selecionados" in pg.inner_text("#bn"))
    pg.click("#bcopy"); pg.wait_for_timeout(300)
    clip = pg.evaluate("navigator.clipboard.readText()")
    check("copiar em lote contém 3 textos", clip.count("\n\n") == 2, repr(clip[:80]))
    pg.click("#bshow"); pg.wait_for_timeout(300)
    check("exibir só selecionados", pg.locator("article.card:not([hidden]), .q:not([hidden])").count() == 3)
    pg.screenshot(path="/home/claude/acervo/review/m_selecionados.png")
    pg.reload(); pg.wait_for_timeout(500)
    check("seleção persiste após recarregar", "3 selecionados" in pg.inner_text("#bn"))
    pg.click("#bclear"); check("limpar seleção esconde barra", not pg.locator("#batch").is_visible())
    # links de fonte internos
    ids = {s["id"] for s in data["sources"]}
    anchors = pg.eval_on_selector_all("a[href^='#src-']", "els=>els.map(e=>e.getAttribute('href').slice(5))")
    check("âncoras de fonte existem", all(a in ids for a in anchors) and pg.locator("li[id^='src-']").count() == len(ids), len(anchors))
    ext = pg.eval_on_selector_all("a[href^='http']", "els=>[...new Set(els.map(e=>e.href))]")
    check("links externos = fontes", set(ext) <= {s["url"] for s in data["sources"]} | {"https://fonts.googleapis.com/"}, len(ext))
    # alvo de toque
    small = pg.evaluate("""[...document.querySelectorAll('.btn,.chip,.mod-head')].filter(e=>e.offsetParent&&e.getBoundingClientRect().height<36).length""")
    check("controles com altura >= 36px", small == 0, small)
    if pg.get_attribute("#mod-2 .mod-head","aria-expanded")!="true": pg.click("#mod-2 .mod-head")
    pg.locator("#b-2 details.more").first.click()
    pg.locator("#mod-2").scroll_into_view_if_needed(); pg.screenshot(path="/home/claude/acervo/review/m_modulo2.png")
    sw = pg.evaluate("document.documentElement.scrollWidth"); check("sem rolagem horizontal com módulos abertos", sw <= 375, sw)
    # modo escuro
    ctx2 = b.new_context(viewport={"width": 1280, "height": 900}, color_scheme="dark")
    p2 = ctx2.new_page(); p2.goto(URL); p2.wait_for_timeout(500); p2.click("#mod-1 .mod-head"); p2.screenshot(path="/home/claude/acervo/review/d_dark.png")
    bg = p2.evaluate("getComputedStyle(document.body).backgroundColor"); check("tema escuro aplicado", bg != "rgb(246, 245, 241)", bg)
    b.close()
fails = [r for r in results if not r[1]]
print(f"\n{len(results)-len(fails)}/{len(results)} verificações OK")
sys.exit(1 if fails else 0)
