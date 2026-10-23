#!/usr/bin/env python3
"""Verificacion del manual. Uso: python3 scripts/verificar_manual.py

No es una suite de tests: son chequeos de comportamiento sobre el build real.
Cubre lo que puede fallar en silencio: version, guia vs capitulos, citas, fugas.
Cada chequeo dice QUE comprueba; si algo falla, nombra el archivo culpable.
"""
import datetime
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PY = sys.executable
HOY = datetime.date.today().strftime("%d-%m-%Y")
fallos = []


def check(nombre, cond, detalle=""):
    print(f"[{'OK ' if cond else 'FAIL'}] {nombre}" + (f" — {detalle}" if detalle else ""))
    if not cond:
        fallos.append(nombre)


def build(cwd):
    return subprocess.run([PY, "scripts/construir.py"], cwd=cwd, capture_output=True, text=True)


# ---------- A. VERSION es el unico origen (en copia aislada) ----------
tmp = Path(tempfile.mkdtemp(prefix="hermes-verify-manual-"))
try:
    for d in ("data", "scripts"):
        shutil.copytree(RAIZ / d, tmp / d, ignore=shutil.ignore_patterns("__pycache__"))
    (tmp / "VERSION").write_text("9.9.9\n", encoding="utf-8")
    check("build aislado corre", build(tmp).returncode == 0)
    h = (tmp / "index.html").read_text(encoding="utf-8")
    check("VERSION manda en encabezado", f"Documento interno · 9.9.9 · {HOY}" in h)
    check("VERSION manda en pie", f"Version 9.9.9 · generado {HOY}" in h)

    (tmp / "VERSION").unlink()
    check("sin VERSION no explota", build(tmp).returncode == 0)
    check("sin VERSION dice sin-version", "sin-version" in (tmp / "index.html").read_text(encoding="utf-8"))

    # ---------- B. la guia nombra los capitulos reales, con su titulo exacto ----------
    sys.path.insert(0, str(tmp / "data"))
    from contenido import CAPITULOS
    from contenido_base import INTRO

    reales = [c["titulo"] for c in CAPITULOS]
    guia = [t for t, _ in INTRO["como_leer"]]
    check("guia = titulos reales de los capitulos", guia == reales, f"{guia} vs {reales}" if guia != reales else f"{len(guia)} capitulos")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# ---------- C. el repo real construye y queda consistente ----------
check("build del repo", build(RAIZ).returncode == 0)
manual, index = RAIZ / "manual.html", RAIZ / "index.html"
check("manual.html == index.html", manual.read_bytes() == index.read_bytes())

html = index.read_text(encoding="utf-8")
ver = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()
fuentes = json.loads((RAIZ / "data/fuentes.json").read_text(encoding="utf-8"))["fuentes"]

check("version vigente", f"Version {ver} · generado {HOY}" in html, ver)
check("8 capitulos / 33 bloques", html.count('class="capitulo"') == 8 and html.count('class="bloque"') == 33)
check("tabla de fuentes completa", html.count('<tr id="f-') == len(fuentes), f"{len(fuentes)} fuentes")
check("comentarios activos", html.count("utteranc.es/client.js") == 1)
check("link al historial", "github.com/vvilche/conecta-manual-tecnico-comercial" in html)
check("sin rutas del Mac", "/Users/victorvilche" not in html)
check("sin montos de costo", not re.search(r"\$\s?[\d.]{3,}", html))
check("audit de citas", subprocess.run([PY, "scripts/construir.py", "--auditar"],
                                       cwd=RAIZ, capture_output=True).returncode == 0)

print()
print(f"FALLARON {len(fallos)}: {fallos}" if fallos else "Todo OK")
sys.exit(1 if fallos else 0)
