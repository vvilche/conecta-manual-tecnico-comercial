# Manual Tecnico Comercial CONECTA

Manual para gente nueva y gente actual: que vende CONECTA, por que importa tecnicamente, y como
se conversa con un cliente sin inventar nada.

**Salida:** `manual.html` — un solo archivo autocontenido. Se abre con doble clic, no necesita servidor.

```bash
open -a "Google Chrome" ~/orca/projects/ConocimientoVentaConecta/manual.html
```

## Versionado

La version del documento vive en `VERSION` (unico origen). El build la lee y la inserta en el
encabezado y el pie del HTML, junto a la fecha de generacion. Para sacar una version nueva:

```bash
echo "1.1.0" > VERSION
$PY scripts/construir.py
git add -A && git commit -m "v1.1.0: <que cambio>"
git tag -a v1.1.0 -m "<que cambio>"
git push && git push --tags
```

El numero se ve en el sitio: encabezado arriba y pie abajo, con link al historial de cambios.

## Regla de construccion

Ninguna afirmacion tecnica del manual existe sin fuente. Cada una lleva uno de tres sellos:

| Sello | Significa | Verificacion |
|---|---|---|
| **MEDIDO** | Corrido sobre archivos reales | el detalle esta en el repo o en la fuente |
| **EXTRAIDO** | Lo dice una norma, fabricante o paper | link directo en la tabla de Fuentes |
| **SUPUESTO** | Criterio propio o convencion de industria | se declara como tal, no como hecho |

El build **falla** si una cita apunta a una fuente que no existe. No se emite un manual con
referencias rotas.

## Estructura

```
manual.html              <- el entregable (generado, no editar a mano)
index.html               <- copia identica, para que Pages sirva la raiz
VERSION                  <- version del documento (unico origen del numero)
data/
  fuentes.json           <- UNICO origen de las fuentes (link, autor, que respalda)
  contenido.py           <- indice de capitulos, en orden
  contenido_base.py      <- sellos e intro
  cap_conceptos.py       <- 01 Conceptos (dato sin tiempo, reloj, capas, lo que vendemos)
  cap_lineas.py          <- 02 Las seis lineas del cotizador
  cap_producto.py        <- 03 Producto (RTU, medicion, PMU/PDC)
  cap_protocolos.py      <- 04 Protocolos (la tabla madre)
  cap_arquitectura.py    <- 05 Arquitectura de comunicaciones
  cap_ciberseguridad.py  <- 06 Ciberseguridad (Ley 21.663, IEC 62443)
  cap_cotizacion.py      <- 07 Armar una cotizacion (10 elementos + ejemplo)
  cap_metodologia.py     <- 08 Metodologia comercial (Escalera, Mina de Oro, objeciones)
scripts/
  construir.py           <- genera manual.html + index.html y audita citas
  plantilla.py           <- HTML, CSS, buscador y comentarios
  fuentes.py             <- valida fuentes y verifica URLs por HTTP real
  verificar_manual.py    <- verificacion completa: version, guia, citas, fugas
```

## Uso

```bash
PY=~/.hermes/hermes-agent/venv/bin/python

$PY scripts/construir.py             # regenera manual.html + index.html
$PY scripts/construir.py --auditar   # solo audita citas, no escribe
$PY scripts/verificar_manual.py      # verificacion completa (16 chequeos)
$PY scripts/fuentes.py               # valida estructura del registro de fuentes
$PY scripts/fuentes.py --verificar-urls   # HTTP real contra cada URL
```

## Como agregar o corregir contenido

1. **Si es una fuente nueva:** agregarla a `data/fuentes.json` con `titulo`, `autor`, `url`, `tipo` y
   `nota` (que respalda exactamente). Verificar la URL antes con `curl`.
2. **Si es contenido:** editar el `cap_*.py` correspondiente. Cada bloque es un `article` con `id`,
   `titulo` y `html`.
3. **Regenerar:** `$PY scripts/construir.py`. Si falla, hay una cita que no resuelve: se corrige la
   cita, no se silencia el error.

## Decisiones que estan tomadas y no se reabren sin pedirlo

- **Sin cifras de costo.** El manual dice *que* compone cada linea, no *cuanto* vale. Los costos reales
  viven en el cotizador (`ConectaCotizador`). Un vendedor con precio de memoria es un pasivo.
- **Fuente secundaria se declara.** IEC 62443 esta explicado desde una guia, no desde la norma (que es de
  pago). La fila lo dice explicitamente.
- **El ATSM no tiene URL directa.** Se cita a traves del informe del Coordinador que lo transcribe, y la
  fila lo advierte.
- **Prohibido ofrecer pilotos gratis.** Coherente con la regla de hierro de ventas de CONECTA.
