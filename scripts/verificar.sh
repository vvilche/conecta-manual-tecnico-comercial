#!/usr/bin/env bash
# Verificación canónica del manual. Un solo exit code.
#   ./scripts/verificar.sh
# Corre: estructura de fuentes, citas (texto y enlaces), links locales, y que
# manual.html esté regenerado y sin montos de costo.
set -uo pipefail
cd "$(dirname "$0")/.."
PY="${PY:-$HOME/.hermes/hermes-agent/venv/bin/python}"
fail=0
run() { printf '%-42s' "$1"; shift; "$@" > /tmp/vf.log 2>&1 && echo "OK" || { echo "FALLA"; sed 's/^/    /' /tmp/vf.log | tail -15; fail=1; }; }

run "fuentes: estructura"        "$PY" scripts/fuentes.py
run "citas: texto y enlaces"     "$PY" scripts/construir.py --auditar
run "build: regenera manual.html" "$PY" scripts/construir.py

printf '%-42s' "links locales existen"
"$PY" - "$PWD" <<'EOF' && echo "OK" || { echo "FALLA"; fail=1; }
import json, pathlib, sys
fuentes = json.loads((pathlib.Path(sys.argv[1]) / "data/fuentes.json").read_text())["fuentes"]
malos = [v["url"] for v in fuentes.values()
         if v["url"].startswith("file://") and not pathlib.Path(v["url"][7:]).exists()]
if malos:
    print("no existen:", *malos, sep="\n  "); sys.exit(1)
EOF

printf '%-42s' "manual.html al día y sin montos"
"$PY" - "$PWD" <<'EOF' && echo "OK" || { echo "FALLA"; fail=1; }
import json, pathlib, re, sys
raiz = pathlib.Path(sys.argv[1])
n = len(json.loads((raiz / "data/fuentes.json").read_text())["fuentes"])
h = (raiz / "manual.html").read_text()
err = []
if h.count('<tr id="f-') != n: err.append(f"filas de fuente {h.count('<tr id=\"f-')} != {n}")
if re.search(r"\$\s?[\d.]{3,}", h): err.append("hay montos de costo en el manual")
if err: print(*err, sep="\n  "); sys.exit(1)
EOF

echo
[ $fail -eq 0 ] && echo "VERIFICADO" || echo "HAY FALLAS"
exit $fail
