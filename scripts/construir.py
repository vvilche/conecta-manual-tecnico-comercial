#!/usr/bin/env python3
"""
Construye el Manual Tecnico Comercial CONECTA (un solo HTML autocontenido).

REGLA 6 DEL ARNES: una cifra, un solo origen.
- Las fuentes viven SOLO en data/fuentes.json.
- El contenido del manual vive en data/contenido.py (texto + citas por id de fuente).
- Este script valida que TODA cita [FUENTE] exista y que ningun dato tecnico quede sin cita.
- Si una cita no resuelve, el build FALLA. No se emite un manual con referencias rotas.

Uso:
    python scripts/construir.py            # construye manual.html
    python scripts/construir.py --auditar  # solo audita citas, no escribe
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTES_F = RAIZ / "data" / "fuentes.json"
SALIDA = RAIZ / "manual.html"

sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "data"))


def cargar_fuentes():
    return json.loads(FUENTES_F.read_text(encoding="utf-8"))["fuentes"]


def auditar(capitulos, fuentes):
    """Toda cita [ID] y todo enlace #f-ID debe existir en fuentes.json.

    Dos formas de citar conviven: el texto [ID] y el enlace <a href="#f-ID">. La primera
    version de este auditor solo miraba la primera y dejaba pasar enlaces rotos.
    """
    usadas, errores = set(), []
    for cap in capitulos:
        for blq in cap["bloques"]:
            html = blq.get("html", "")
            for cita in re.findall(r"\[([A-Z0-9][A-Z0-9\-\.]*)\]", html):
                if cita in fuentes:
                    usadas.add(cita)
                else:
                    errores.append(f"capitulo '{cap['id']}' bloque '{blq.get('id','')}': cita [{cita}] no existe en fuentes.json")
            for ref in re.findall(r'#f-([A-Za-z0-9_.\-]+)', html):
                if ref in fuentes:
                    usadas.add(ref)
                else:
                    errores.append(f"capitulo '{cap['id']}' bloque '{blq.get('id','')}': enlace #f-{ref} no existe en fuentes.json")
    return usadas, errores


def construir():
    from contenido import CAPITULOS, SELLOS, INTRO  # noqa: PLC0415

    fuentes = cargar_fuentes()
    usadas, errores = auditar(CAPITULOS, fuentes)

    if "--auditar" in sys.argv:
        print(f"Fuentes registradas : {len(fuentes)}")
        print(f"Fuentes citadas     : {len(usadas)}")
        sin_usar = sorted(set(fuentes) - usadas)
        if sin_usar:
            print(f"Registradas sin citar: {', '.join(sin_usar)}")
        if errores:
            print("\nCITAS ROTAS:")
            for e in errores:
                print("  -", e)
            return 1
        print("\nSin citas rotas.")
        return 0

    if errores:
        print("BUILD ABORTADO — hay citas que no resuelven:")
        for e in errores:
            print("  -", e)
        return 1

    html = render(CAPITULOS, fuentes, SELLOS, INTRO)
    SALIDA.write_text(html, encoding="utf-8")
    # GitHub Pages sirve la raiz: index.html es el mismo contenido, generado en el mismo
    # paso para que no se desfase. No editar index.html a mano.
    (RAIZ / "index.html").write_text(html, encoding="utf-8")
    n_bloques = sum(len(c["bloques"]) for c in CAPITULOS)
    print(f"OK: {SALIDA} + index.html")
    print(f"   capitulos={len(CAPITULOS)} bloques={n_bloques} fuentes_citadas={len(usadas)} bytes={len(html)}")
    return 0


def render(capitulos, fuentes, sellos, intro):
    from plantilla import pagina  # noqa: PLC0415
    return pagina(capitulos, fuentes, sellos, intro, bloque_fuentes=bloque_fuentes(fuentes))


def bloque_fuentes(fuentes):
    """Tabla de fuentes al pie. Orden estable por id."""
    tipos = {
        "regulador": "Regulador",
        "regulador-citado": "Regulador (citado)",
        "estandar": "Estandar",
        "paper": "Paper",
        "fabricante": "Fabricante",
        "interno-medido": "Medido interno",
    }
    filas = []
    for k in sorted(fuentes):
        v = fuentes[k]
        filas.append(
            f'<tr id="f-{k}"><td class="fid">{k}</td>'
            f'<td><a href="{v["url"]}" target="_blank" rel="noopener">{v["titulo"]}</a>'
            f'<div class="fautor">{v["autor"]}</div></td>'
            f'<td><span class="tipo t-{v["tipo"]}">{tipos.get(v["tipo"], v["tipo"])}</span></td>'
            f'<td class="fnota">{v["nota"]}</td></tr>'
        )
    return "\n".join(filas)


if __name__ == "__main__":
    sys.exit(construir())
