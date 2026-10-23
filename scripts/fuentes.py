#!/usr/bin/env python3
"""
Genera el bloque de fuentes y los helpers de cita del Manual Tecnico Comercial CONECTA.

REGLA 6 DEL ARNES: una cifra, un solo origen.
Las fuentes viven en data/fuentes.json. Este script las valida y emite el HTML de la
tabla de fuentes + el JSON que usa el manual para resolver las citas [N].

Uso:
    python scripts/fuentes.py            # valida y reporta
    python scripts/fuentes.py --html     # imprime el bloque HTML de la tabla
    python scripts/fuentes.py --verificar-urls   # HTTP real contra cada URL (lento)
"""
import json
import sys
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "data" / "fuentes.json"

# Los unicos tipos admitidos. El tipo define el color del sello en el manual.
TIPOS = {
    "regulador":        "Regulador",
    "regulador-citado": "Regulador (citado indirecto)",
    "estandar":         "Estandar",
    "paper":            "Paper",
    "fabricante":       "Fabricante",
    "interno-medido":   "Medido interno",
    "secundaria":       "Fuente secundaria",
}


def cargar():
    d = json.loads(FUENTES.read_text(encoding="utf-8"))
    fuentes = d["fuentes"]
    errores = []
    for k, v in fuentes.items():
        for campo in ("titulo", "autor", "url", "tipo", "nota"):
            if not v.get(campo):
                errores.append(f"{k}: falta '{campo}'")
        if v.get("tipo") not in TIPOS:
            errores.append(f"{k}: tipo '{v.get('tipo')}' no admitido")
        if not (v.get("url", "").startswith(("http://", "https://", "file:", "repo://"))):
            errores.append(f"{k}: url no valida")
    return fuentes, errores


def verificar_urls(fuentes):
    """Codigo HTTP real de cada fuente. 200 = ok. Se reporta lo que devuelve, no lo que uno espera."""
    filas = []
    for k, v in fuentes.items():
        u = v["url"]
        if u.startswith("file:"):
            p = Path(u.replace("file://", ""))
            filas.append((k, "LOCAL", "existe" if p.exists() else "FALTA", u))
            continue
        try:
            r = subprocess.run(
                ["curl", "-sSL", "-o", "/dev/null", "-w", "%{http_code}",
                 "-A", "Mozilla/5.0", "--max-time", "60", u],
                capture_output=True, text=True, timeout=90,
            )
            filas.append((k, r.stdout.strip() or "000", "ok" if r.stdout.strip() == "200" else "REVISAR", u))
        except Exception as e:  # noqa: BLE001
            filas.append((k, "ERR", str(e)[:40], u))
    return filas


def bloque_html(fuentes):
    """Tabla HTML de fuentes, ordenada por id. La usa el manual al pie."""
    partes = []
    for k in sorted(fuentes):
        v = fuentes[k]
        tipo = TIPOS.get(v["tipo"], v["tipo"])
        partes.append(
            f'<tr id="f-{k}">'
            f'<td class="fid">{k}</td>'
            f'<td><a href="{v["url"]}" target="_blank" rel="noopener">{v["titulo"]}</a>'
            f'<div class="fautor">{v["autor"]}</div></td>'
            f'<td><span class="tipo tipo-{v["tipo"]}">{tipo}</span></td>'
            f'<td class="fnota">{v["nota"]}</td>'
            f"</tr>"
        )
    return "\n".join(partes)


def main():
    fuentes, errores = cargar()
    if "--html" in sys.argv:
        print(bloque_html(fuentes))
        return 0
    if "--verificar-urls" in sys.argv:
        for k, code, estado, u in verificar_urls(fuentes):
            print(f"{k:18s} {code:6s} {estado:8s} {u[:78]}")
        return 0
    print(f"Fuentes registradas: {len(fuentes)}")
    for k, v in fuentes.items():
        print(f"  {k:18s} {v['tipo']:18s} {v['titulo'][:60]}")
    if errores:
        print("\nERRORES:")
        for e in errores:
            print("  -", e)
        return 1
    print("\nSin errores de estructura.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
