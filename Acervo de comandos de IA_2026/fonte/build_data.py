"""Monta a base estruturada única (data.json) usada pelo HTML e pelo PDF."""
import json, re, sys
from data_core import META, KINDS, PLATFORMS, MODULES, SOURCES, CHANGELOG, VERIFIED
from data_items1 import ITEMS
import data_items2, data_items3  # noqa: registram itens em ITEMS
from data_quick import Q

src_ids = {s[0] for s in SOURCES}
errors = []
items = []
counters = {}
for x in ITEMS:
    m = x["module"]
    counters[m] = counters.get(m, 0) + 1
    x["id"] = f"m{m:02d}-{counters[m]:02d}"
    x["verified"] = VERIFIED if x["sources"] else ""
    for s in x["sources"]:
        if s not in src_ids:
            errors.append(f"fonte inexistente {s} em {x['title']}")
    for k in x["kinds"]:
        if k not in KINDS:
            errors.append(f"classe inválida {k} em {x['title']}")
    items.append(x)

quick = []
for i, (t, m, pl, k, txt, origin) in enumerate(Q, 1):
    quick.append(dict(id=f"q{i:02d}", n=i, title=t, module=m, platforms=pl, kinds=[k], example=txt, origin=origin))

pkeys = {p[0] for p in PLATFORMS}
for x in items + quick:
    for p in x["platforms"]:
        if p not in pkeys:
            errors.append(f"plataforma inválida {p} em {x['title']}")

data = dict(meta=META,
            kinds={k: {"label": v[0], "desc": v[1]} for k, v in KINDS.items()},
            platforms=[{"key": k, "label": l} for k, l in PLATFORMS],
            modules=[{"n": n, "title": t, "desc": d} for n, t, d in MODULES],
            items=items, quick=quick,
            sources=[{"id": a, "title": b, "url": c, "type": d} for a, b, c, d in SOURCES],
            changelog=[{"version": v, "date": d, "notes": n} for v, d, n in CHANGELOG])

blob = json.dumps(data, ensure_ascii=False)
if "—" in blob:
    errors.append("travessão (—) encontrado no conteúdo")
used = {s for x in items for s in x["sources"]}
unused = src_ids - used
if errors:
    print("\n".join(errors)); sys.exit(1)
json.dump(data, open("data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
per_mod = {m["n"]: sum(1 for x in items if x["module"] == m["n"]) for m in data["modules"]}
print("itens:", len(items), "| consulta rápida:", len(quick), "| fontes:", len(SOURCES))
print("por módulo:", per_mod)
print("origem v3/v4 itens:", sum(x['origin']=='v3' for x in items), sum(x['origin']=='v4' for x in items))
print("quick por módulo:", {m: sum(1 for q in quick if q['module']==m) for m in range(1,18)})
print("fontes não usadas em itens:", sorted(unused))
