# -*- coding: utf-8 -*-
"""Capitulo 2 — Producto. Que componente resuelve que problema. SIN cifras de costo."""

CAP_PRODUCTO = {
    "id": "producto",
    "titulo": "Producto",
    "subtitulo": "Que hay en el catalogo, que problema resuelve cada cosa, y con que no se confunde.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "mapa-portafolio",
            "titulo": "El portafolio en un mapa",
            "tipo": "tabla",
            "html": """
<p class="lead">CONECTA integra marcas de fabricante. Saber cual es cual evita el error de atribuir una
capacidad al producto equivocado, que es la forma mas rapida de perder credibilidad tecnica.</p>

<table class="tabla">
<thead><tr><th>Marca</th><th>Que hace</th><th>Productos que veras en propuestas</th></tr></thead>
<tbody>
<tr><td><b>SUPCON</b></td><td>Control y automatizacion de planta completa: DCS, SIS, instrumentacion, valvulas, software industrial, IA</td><td>ECS-700 (DCS), TCS-500 (SIS), PRIDE (predictivo), APC, supOS, transmisores CXT, valvulas y posicionador CVP2000</td></tr>
<tr><td><b>NovaTech</b></td><td>Automatizacion de subestacion, medicion de potencia y sincronizacion</td><td>Orion LX+/SX/MX/VX, Orion I/O, Bitronics, Kronos, switches Hermes</td></tr>
<tr><td><b>Vizimax</b></td><td>Conexion controlada (point-on-wave), PMU, merging unit</td><td>SynchroTeq MV/Plus/Lite, PMU, AMU, RightWON</td></tr>
<tr><td><b>Belden / Hirschmann</b></td><td>Red industrial endurecida para subestacion</td><td>Switches IEC 61850-3, PRP/HSR, firewalls OT</td></tr>
<tr><td><b>Elipse</b></td><td>SCADA e HMI, lectura de protecciones, drivers de protocolo</td><td>Elipse Power, driver IEC 61850, driver DNP3, COMTRADE</td></tr>
<tr><td><b>Tier0 (SUPCON)</b></td><td>Plataforma de datos industriales (UNS) para que la IA consuma el dato</td><td>Tier0 Cloud, Tier0 Edge</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Agrupacion comercial propia. Las capacidades concretas por equipo estan abajo, con su fuente.</cite>

<div class="callout">
  <b>Cuidado con esto.</b> Un producto puede ser de una marca y el servicio de otra. En una propuesta,
  el cliente compra una solucion, no seis marcas. La marca va en el anexo tecnico, no en el titulo.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "rtu",
            "titulo": "RTU y gateways: el reemplazo que no recablea",
            "tipo": "producto",
            "html": """
<p class="lead">El Orion es el caballo de batalla de la automatizacion de subestacion. Su argumento mas
fuerte no es la capacidad: es que permite reemplazar una RTU vieja <b>sin rehacer el cableado de campo</b>.</p>

<table class="tabla">
<thead><tr><th>Modelo</th><th>Posicionamiento</th></tr></thead>
<tbody>
<tr><td><b>OrionLX+</b></td><td>Subestaciones grandes y las aplicaciones mas complejas</td></tr>
<tr><td><b>OrionSX</b></td><td>Servidor de datos y HMI</td></tr>
<tr><td><b>OrionMX</b></td><td>Compacto, para espacios reducidos</td></tr>
<tr><td><b>OrionVX</b></td><td>Virtualizado, sobre servidor</td></tr>
<tr><td><b>Orion I/O</b></td><td>Retrofit de RTUs legacy; pin-compatible con GE D20</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-ORION-RETROFIT">ORION-RETROFIT</a> — pagina de solucion de retrofit de NovaTech</cite>

<h4>El argumento de venta, con la precision que corresponde</h4>
<p>NovaTech produce soluciones retrofit para RTU <b>D20, SNW, Telegyr, Telvent y ACS</b>. Las tarjetas
adaptadoras permiten que la mayoria de las actualizaciones se hagan <b>sin volver a cablear</b>, y el kit
reemplaza el espacio de <b>3RU</b>. Ademas, como hay emulacion de protocolo, el cambio de RTU puede ser
<b>transparente al SCADA</b>, sin modificar la base de datos del centro de control.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-ORION-RETROFIT">ORION-RETROFIT</a></cite>

<div class="callout">
  <b>No digas "cero recableado".</b> La fuente dice "sin necesidad de volver a cablear" para la mayoria de
  las actualizaciones, mediante tarjetas adaptadoras. Los conectores si se mueven a la adaptor board. Usar
  la frase exacta: <b>se reutiliza el cableado de campo existente</i></b>, no "no se toca un cable".
</div>

<h4>Que se gana en la practica</h4>
<p>El Orion I/O esta pensado para monitoreo y control de 12 Vdc a 125 Vdc en subestaciones, incluyendo
<b>registro de secuencia de eventos con resolucion de 1 ms</b>, mando TRIP/CLOSE de interruptor y
monitoreo de transductores analogicos. Una tarjeta de 16 entradas discretas se declara apta para
SOE de 1 ms, y con tarjetas discretas llenas entrega 64 I/O en 2 RU.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-ORION-IO-1MS">ORION-IO-1MS</a></cite>

<div class="callout supuesto">
  <b>SUPUESTO — pregunta obligatoria antes de cotizar.</b> "Cuantas de tus senales ya viven en un rele o
  en un medidor?" Si la senal ya esta en un IED, la RTU la lee por protocolo y no gasta una entrada. Cotizar
  I/O de mas es un error de dimensionamiento, y el cliente que sabe lo va a notar.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "medicion",
            "titulo": "Medicion de potencia: el numero que se audita",
            "tipo": "producto",
            "html": """
<p class="lead">Bitronics es la linea de medicion de precision de NovaTech. Lo que se vende aqui no es un
medidor mas: es un numero que resiste una auditoria y que no requiere cortar el servicio para instalarse.</p>

<ul class="lista">
  <li>Precision <b>0,2s</b> en todos los productos, calibrados individualmente, incluso con TC de nucleo partido externos.</li>
  <li><b>MTBF de 40 anos</b> y garantia de 10 anos.</li>
  <li>Se instala con TC externos opcionales <b>sin tomar una salida de servicio</b>.</li>
  <li>El <b>DGM</b> (Distribution Grid Monitor) es una solucion "primary in a box": medidor M661 + sensores Lindsey LEA + cableado, con OrionMX opcional para ciberseguridad, I/O y automatizacion.</li>
</ul>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-BITRONICS">BITRONICS</a> — pagina de producto de NovaTech</cite>

<div class="callout">
  <b>El argumento que gana la reunion.</b> "No hay que sacar de servicio la instalacion para medirla".
  En una planta que factura por disponibilidad, eso vale mas que cualquier decimal de precision.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "pmu-pdc",
            "titulo": "Medicion fasorial: PMU y PDC",
            "tipo": "producto",
            "html": """
<p class="lead">Una PMU no es un medidor mas rapido. Es un equipo que entrega fasores sincronizados en el
tiempo, y eso permite ver la dinamica de la red, no solo su estado.</p>

<h4>Lo que exige el Coordinador en Chile</h4>
<p>Las PMU que se integren al Modulo de Medicion Fasorial deben cumplir, a lo menos (Tabla 7.1-1):</p>

<table class="tabla">
<thead><tr><th>Requerimiento</th><th>Exigencia</th></tr></thead>
<tbody>
<tr><td>Clase de precision</td><td>IEEE 60255-118-1-2018 (o ultima version de IEEE C37.118), <b>M-Class</b></td></tr>
<tr><td>Tasa de muestreo</td><td><b>50 muestras por segundo</b></td></tr>
<tr><td>Protocolo de sincrofasores</td><td>Ultima version IEEE C37.118 o IEEE 60255-118-1-2018</td></tr>
<tr><td>Precision de sincronizacion</td><td><b>Dentro de 1 µs</b>, con base de tiempo GPS</td></tr>
<tr><td>Codigo de tiempo</td><td><b>IRIG-B no modulada</b> (PTP si no hay antena)</td></tr>
<tr><td>Alimentacion</td><td>Desde la red segura de la subestacion, con respaldo para medir al menos <b>8 horas</b></td></tr>
<tr><td>Ancho de banda</td><td><b>120 kbps</b> minimo por punto de monitoreo</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CEN-MMF2026">CEN-MMF2026</a>, Tabla 7.1-1 (pagina 105) y seccion 5.9 (ancho de banda, pagina 100)</cite>

<div class="callout">
  <b>Dato de lead directo.</b> El estudio de julio 2026 exige PMU en todas las instalaciones de generacion
  con potencia instalada <b>igual o superior a 9 MW</b>, y define 51 nuevos puntos de monitoreo. Donde va
  la PMU es distinto segun tecnologia: en bornes de cada unidad generadora sincronica; en el punto de
  control del PPC para parques renovables con inversores; y dos puntos cuando la central es hibrida
  (generacion + almacenamiento). <a href="#f-CEN-MMF2026">CEN-MMF2026</a>, seccion 5.1 y conclusiones.
</div>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CEN-MMF2026">CEN-MMF2026</a>, secciones 5.1 y 6</cite>

<h4>PDC: el concentrador</h4>
<p>La PMU no habla con el Coordinador de uno a uno: entrega sus datos a un <b>PDC Local</b>, y el PDC Local
los manda al PDC Corporativo del Coordinador. El estudio mantiene la arquitectura con un segundo data
center y un tercer PDC Corporativo, y establece que cada Coordinado puede implementar sus propios PDC
locales si lo necesita para cumplir la disponibilidad. Tambien exige que el PDC Local <b>almacene</b> la
informacion que no pudo transmitir y se sincronice al restablecerse la comunicacion.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CEN-MMF2026">CEN-MMF2026</a>, conclusiones y seccion 5.10.1</cite>

<div class="callout supuesto">
  <b>SUPUESTO.</b> La licencia del PDC es un punto de friccion recurrente: el Coordinador exige una licencia
  de integracion al PDC Local <b>adicional</b> a la del PDC Corporativo, y ese costo es del Coordinado
  (<a href="#f-CEN-MMF2026">CEN-MMF2026</a>, pagina 103). Preguntarlo temprano, no al final del proyecto.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "no-confundir",
            "titulo": "Cinco cosas que se confunden y cuestan una reunion",
            "tipo": "idea",
            "html": """
<p class="lead">Estos errores aparecen mucho en terreno. Cada uno se corrige en una frase, pero si no se
corrige a tiempo, el cliente deja de creer en el resto de la propuesta.</p>

<table class="tabla">
<thead><tr><th>Se confunde</th><th>Con</th><th>La diferencia que importa</th></tr></thead>
<tbody>
<tr><td><b>RTU</b></td><td>Controlador (PLC/DCS)</td><td>La RTU lleva datos al centro de control y puede ejecutar logica, pero no reemplaza al control del proceso. No vender una RTU como "el control de la planta".</td></tr>
<tr><td><b>Medidor de facturacion</b></td><td>Medidor de calidad de energia</td><td>Uno sirve para cobrar, el otro para diagnosticar. Pueden ser el mismo equipo, pero el argumento de venta es distinto.</td></tr>
<tr><td><b>PMU</b></td><td>SCADA mas rapido</td><td>La PMU entrega fasores con tiempo comun. Un SCADA rapido sigue siendo un SCADA.</td></tr>
<tr><td><b>Sincronizacion</b></td><td>Un servidor NTP en la red</td><td>NTP por red corporativa no alcanza para PMU ni para bus de proceso. Ver capitulo Protocolos.</td></tr>
<tr><td><b>Switch industrial</b></td><td>Switch IEC 61850-3 con PRP</td><td>Endurecido no es lo mismo que redundante sin perdida. Si el cliente necesita continuidad, el argumento es PRP/HSR.</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Distinciones de criterio propio, consistentes con las fuentes de cada capa.</cite>
""",
        },
    ],
}
