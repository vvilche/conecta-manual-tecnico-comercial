#!/usr/bin/env python3
"""Verificacion del manual. Uso: python3 scripts/verificar_manual.py

No es una suite de tests: son chequeos de comportamiento sobre el build real.
Cubre lo que puede fallar en silencio: version, guia vs capitulos, citas, fugas,
y que cada cifra del manual exista tambien en la nota de su fuente.
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

sys.path.insert(0, str(RAIZ / "data"))
from contenido import CAPITULOS  # noqa: E402
from contenido_base import INTRO  # noqa: E402


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
finally:
    shutil.rmtree(tmp, ignore_errors=True)

# ---------- B. la guia nombra los capitulos reales, con su titulo exacto ----------
reales = [c["titulo"] for c in CAPITULOS]
guia = [t for t, _ in INTRO["como_leer"]]
check("guia = titulos reales de los capitulos", guia == reales,
      f"{guia} vs {reales}" if guia != reales else f"{len(guia)} capitulos")
check("capitulos sin id duplicado", len({c["id"] for c in CAPITULOS}) == len(CAPITULOS))

# ---------- C. el repo real construye y queda consistente ----------
check("build del repo", build(RAIZ).returncode == 0)
manual, index = RAIZ / "manual.html", RAIZ / "index.html"
check("manual.html == index.html", manual.read_bytes() == index.read_bytes())

html = index.read_text(encoding="utf-8")
ver = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()
fuentes = json.loads((RAIZ / "data/fuentes.json").read_text(encoding="utf-8"))["fuentes"]

check("version vigente", f"Version {ver} · generado {HOY}" in html, ver)

# Los conteos se derivan de los capitulos reales, no se escriben a mano:
# un numero que se escribe dos veces se desfasa.
n_caps = len(CAPITULOS)
n_bloques = sum(len(c["bloques"]) for c in CAPITULOS)
check("un capitulo por bloque de contenido",
      html.count('class="capitulo"') == n_caps and html.count('class="bloque"') == n_bloques,
      f"{n_caps} capitulos, {n_bloques} bloques")
check("tabla de fuentes completa", html.count('<tr id="f-') == len(fuentes), f"{len(fuentes)} fuentes")
check("comentarios activos", html.count("utteranc.es/client.js") == 1)
check("link al historial", "github.com/vvilche/conecta-manual-tecnico-comercial" in html)
check("sin rutas del Mac", "/Users/victorvilche" not in html)
check("sin montos de costo", not re.search(r"\$\s?[\d.]{3,}", html))
check("audit de citas", subprocess.run([PY, "scripts/construir.py", "--auditar"],
                                       cwd=RAIZ, capture_output=True).returncode == 0)

# ---------- D. cada cifra del manual existe tambien en la nota de su fuente ----------
# Un link que abre no prueba que la fuente diga lo que el manual afirma. Estas se
# cruzan contra el texto que el registro declara: si una se desfasa, falla aqui.
CRUCES = [
    ("PM180", "SATEC"), ("PMU PRO", "SATEC"), ("BFM-II", "SATEC"),
    ("EM720", "SATEC"), ("PM130 PLUS", "SATEC"), ("C37.118.2", "SATEC"),
    ("31.000", "SUPCON-PRIDE"), ("1.566", "SUPCON-PRIDE"), ("2.800", "SUPCON-PRIDE"),
    ("19,2", "SUPCON-ECS700"), ("30.000", "SUPCON-ECS700"),
]
cap_partners = next((c for c in CAPITULOS if c["id"] == "partners"), None)
check("capitulo de partners existe", cap_partners is not None)
if cap_partners:
    texto = " ".join(b["html"] for b in cap_partners["bloques"])
    sin_respaldo = [k for k, f in CRUCES
                    if k not in texto or k.lower() not in fuentes.get(f, {}).get("nota", "").lower()]
    check("cifras de partners respaldadas por su fuente", not sin_respaldo, str(sin_respaldo))

# ---------- E. mismo cruce para el capitulo de subestacion ----------
CRUCES2 = [
    ("OrionLX+", "NOVATECH"), ("Bitronics", "NOVATECH"), ("Kronos", "NOVATECH"),
    ("adaptor board", "NOVATECH-RETROFIT"),
    ("SynchroTeq Plus", "VIZIMAX"), ("AMU", "VIZIMAX"), ("RightWON", "VIZIMAX"),
    ("MACH1000", "BELDEN"), ("BOBCAT", "BELDEN"), ("EAGLE", "BELDEN"),
]
cap2 = next((c for c in CAPITULOS if c["id"] == "partners-2"), None)
check("capitulo de subestacion existe", cap2 is not None)
if cap2:
    texto2 = " ".join(b["html"] for b in cap2["bloques"])
    sin2 = [k for k, f in CRUCES2
            if k.lower() not in texto2.lower() or k.lower() not in fuentes.get(f, {}).get("nota", "").lower()]
    check("cifras de subestacion respaldadas", not sin2, str(sin2))

# ---------- F. fuentes no verificables por HTTP quedan declaradas --------
# Belden devuelve 403 a peticiones automatizadas: la nota DEBE decirlo, para que nadie
# la cite como verificada al construir el manual.
nota_belden = fuentes.get("BELDEN", {}).get("nota", "")
check("aviso de Belden no verificable", "403" in nota_belden and "NO pudo verificarse" in nota_belden)

print()
print(f"FALLARON {len(fallos)}: {fallos}" if fallos else "Todo OK")
sys.exit(1 if fallos else 0)
