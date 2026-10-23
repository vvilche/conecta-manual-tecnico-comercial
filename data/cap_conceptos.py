# -*- coding: utf-8 -*-
"""Capitulo 1 — Conceptos. Las ideas que hay que tener claras antes de vender."""

CAP_CONCEPTOS = {
    "id": "conceptos",
    "titulo": "Conceptos",
    "subtitulo": "Lo que hay que entender antes de hablar con un cliente.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "dato-tiempo",
            "titulo": "El dato sin tiempo no sirve",
            "tipo": "idea",
            "html": """
<p class="lead">Este es el concepto que mas gente nueva confunde, y el que mas caro sale en terreno.
Un dato electrico tiene tres partes, y la tercera se olvida: <b>valor, calidad y tiempo</b>.
Sin el tiempo, el dato sirve para mirar una pantalla, pero no para reconstruir que paso.</p>

<div class="grid3">
  <div class="card"><div class="cta">VALOR</div><p>3,4 MW. El numero. Es lo unico que mira quien recien empieza.</p></div>
  <div class="card"><div class="cta">CALIDAD</div><p>Valido, invalido, cuestionable, sustituido. Un valor malo no es un valor.</p></div>
  <div class="card"><div class="cta">TIEMPO</div><p>Cuando ocurrio. Es lo que permite ordenar eventos y encontrar la causa.</p></div>
</div>

<div class="callout">
  <b>Por que importa comercialmente.</b> Cuando el Coordinador Electrico te pide reconstruir por que se
  cayo una zona, no le sirve saber que la tension bajo: necesita saber <i>que bajo primero</i>. Sin
  estampa de tiempo el evento no tiene secuencia, y sin secuencia no hay causa. Ahi es donde se pierden
  los reclamos y donde se ganan las ventas de sincronizacion y de medicion fasorial.
</div>

<p>La consecuencia practica es dura: <b>no todos los protocolos llevan estampa de tiempo</b>. Algunos
transportan valores crudos y el tiempo lo pone quien pregunta. Si el equipo que disenaste no guarda el
tiempo, cuando el operador lo mira ya es tarde y el dato perdio su origen. Esta es la diferencia entre
un sistema que <i>reporta</i> y un sistema que <i>registra</i>.</p>

<h4>Que significa exactamente "estampa de tiempo"</h4>
<p>Hay una trampa que conviene entender de entrada: no es lo mismo el tiempo <b>de la fuente</b> que el
tiempo <b>del servidor que lo recibio</b>. OPC UA los separa explicitamente y eso ayuda a pensar el resto
de los protocolos:</p>

<table class="tabla">
<thead><tr><th>Concepto OPC UA</th><th>Que significa</th><th>Fuente</th></tr></thead>
<tbody>
<tr><td><b>SourceTimestamp</b></td><td>El tiempo que le puso <i>la fuente del dato</i>. Una vez asignado no cambia nunca. Debe ir en UTC.</td><td><a href="#f-OPCUA-SRC-TS">OPCUA-SRC-TS</a></td></tr>
<tr><td><b>ServerTimestamp</b></td><td>El tiempo en que <i>el servidor recibio</i> el valor, o supo que era correcto. Puede refrescarse aunque el valor no cambie.</td><td><a href="#f-OPCUA-SRV-TS">OPCUA-SRV-TS</a></td></tr>
</tbody>
</table>

<p>Cuando alguien dice "ese dato viene con hora", la primera pregunta tecnica es <b>cual hora</b>. Si es la
del servidor, la latencia de la red se cuela dentro del dato y una comparacion entre dos subestaciones
queda corrida. Si es la de la fuente, el dato conserva su origen aunque llegue tarde. La especificacion de
OPC UA es explicita en que el <code>serverTimestamp</code> se actualiza periodicamente aunque el valor no
haya cambiado, justamente porque mide <i>cuando el servidor supo del valor</i>, no cuando ocurrio.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-OPCUA-SRC-TS">OPCUA-SRC-TS</a> · <a href="#f-OPCUA-SRV-TS">OPCUA-SRV-TS</a></cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "por-que-reloj",
            "titulo": "Por que el reloj es parte del sistema, no un accesorio",
            "tipo": "idea",
            "html": """
<p class="lead">Si dos equipos no comparten el mismo reloj, sus estampas de tiempo no se pueden comparar
entre si. Y comparar es exactamente para lo que sirve la estampa. Por eso la sincronizacion no es un
detalle de instalacion: es un requisito de la medicion.</p>

<p>La precision que exige cada aplicacion es distinta, y confundirlas hace que se pague de mas o se
entregue de menos. Estos numeros salen de fuente primaria:</p>

<table class="tabla">
<thead><tr><th>Necesidad</th><th>Precision de tiempo</th><th>Que la cumple</th><th>Fuente</th></tr></thead>
<tbody>
<tr><td>Secuencia de eventos clasica en la red</td><td>del orden de <b>~10 ms</b></td><td>SNTP</td><td><a href="#f-PTP-PUP-NIST">PTP-PUP-NIST</a></td></tr>
<tr><td>Comparacion de phase entre PMU</td><td><b>1 µs</b> se considera mas que suficiente</td><td>GPS / IRIG-B</td><td><a href="#f-PTP-PUP-NIST">PTP-PUP-NIST</a></td></tr>
<tr><td>Proteccion diferencial y bus de proceso digital</td><td>unos <b>microsegundos</b></td><td>PPS dedicado o PTP</td><td><a href="#f-PTP-PUP-NIST">PTP-PUP-NIST</a></td></tr>
<tr><td>Perfil PTP de utility (IEC/IEEE 61850-9-3)</td><td>garantiza <b>submicrosegundo</b> tras 15 TCs o 3 BC</td><td>PTP perfil 9-3</td><td><a href="#f-PTP-PUP-NIST">PTP-PUP-NIST</a></td></tr>
<tr><td>NTP en LAN moderna</td><td>decenas de <b>microsegundos</b></td><td>NTPv4</td><td><a href="#f-RFC5905">RFC5905</a></td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>

<div class="callout">
  <b>El dato que conviene memorizar.</b> Un error de fase de 0,1° equivale a un error de tiempo de 5 µs
  en el muestreo. Por eso la PMU exige microsegundos y no milisegundos: el error de tiempo se convierte
  directamente en error de angulo. <a href="#f-PTP-PUP-NIST">PTP-PUP-NIST</a>
</div>

<h4>Como se ve esto en un equipo real</h4>
<p>Un Kronos, por ejemplo, declara 60 ns de desviacion maxima de tiempo (99%), y admite como salidas
IRIG-B no modulada y modulada, PPS/PPM, NTP/SNTP y PTP con los perfiles UDP, 802.3, IEEE C37.238-2011,
IEEE C37.238-2016 e IEC 61850-9-3:2016. Ademas soporta PRP/HSR (IEC 62439-3) en la serie 3R, que es lo
que permite redundar la red sin perder paquetes.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-KRONOS">KRONOS</a> — pagina de producto NovaTech</cite>

<p>El punto comercial es este: el reloj define <b>cuanta verdad</b> tiene el sistema. Si el cliente va a
comparar eventos entre dos subestaciones y esta sincronizando con NTP por la red corporativa, sus
estampas van a estar corridas y el analisis posterior no va a cerrar. Ahi entra el reloj GPS como
producto, y no como accesorio del RTU.</p>

<div class="callout supuesto">
  <b>SUPUESTO — criterio CONECTA.</b> En una subestacion nueva, ofrecer la sincronizacion dedicada desde
  la primera conversacion. Es mas barato discutirla con el diseno abierto que justificarla despues,
  cuando el cliente ya descubrio que sus eventos no cuadran.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "capas",
            "titulo": "Las cinco capas que hay que saber nombrar",
            "tipo": "idea",
            "html": """
<p class="lead">Una planta o una subestacion se conversa en capas. Saber en que capa vive cada problema
permite responder sin marear al cliente, y permite armar el paquete sin vender tres veces lo mismo.</p>

<table class="tabla capa-tabla">
<thead><tr><th>Capa</th><th>Pregunta que responde</th><th>Que hay ahi</th></tr></thead>
<tbody>
<tr><td><b>1. Campo</b></td><td>Que esta pasando fisicamente</td><td>Instrumentos, sensores, valvulas, posicionadores, actitud de equipos</td></tr>
<tr><td><b>2. Control</b></td><td>Quien manda al proceso</td><td>DCS, PLC, SIS, reles de proteccion, controladores de planta</td></tr>
<tr><td><b>3. Adquisicion</b></td><td>Como el dato sale del equipo</td><td>RTU, gateway, IED, merging unit, PMU</td></tr>
<tr><td><b>4. Red</b></td><td>Como viaja sin perderse</td><td>Switches IEC 61850-3, PRP/HSR, firewalls OT, fibra</td></tr>
<tr><td><b>5. Aplicacion</b></td><td>Que se hace con el dato</td><td>SCADA, HMI, PDC, analitica, predictivo, UNS, reportes regulatorios</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Modelo de capas propio de CONECTA para conversar. No es un estandar publicado.</cite>

<h4>La regla que evita el error caro</h4>
<p>Antes de proponer hardware en la capa 3, verificar si el dato <b>ya existe</b> en la capa 2. Si la
senal vive en un rele o en un medidor, se lee por protocolo y no gasta una sola entrada digital. Es la
diferencia entre cotizar un gateway nuevo y no cotizarlo.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-ORION-IO-1MS">ORION-IO-1MS</a> — un Orion I/O entrega eventos discretos con resolucion de 1 ms; si el rele ya los publica, la I/O es redundante</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "lo-que-vendemos",
            "titulo": "Que vende CONECTA, en una frase por familia",
            "tipo": "idea",
            "html": """
<p class="lead">CONECTA no fabrica. Integra y responde tecnicamente por lo que instala. Esa es la
diferencia con un distribuidor puro, y es la razon por la que el cliente nos llama cuando algo no cuadra.</p>

<table class="tabla">
<thead><tr><th>Familia</th><th>En una frase</th><th>Cuando aparece</th></tr></thead>
<tbody>
<tr><td><b>Control y automatizacion</b></td><td>El cerebro de la planta: DCS, SIS, APC, predictivo</td><td>Planta nueva, o reemplazo de un control obsoleto</td></tr>
<tr><td><b>Adquisicion y RTU</b></td><td>El puente entre el equipo y el SCADA, sin recablear</td><td>RTU al final de su vida util, migracion a IEC 61850</td></tr>
<tr><td><b>Medicion de precision</b></td><td>El numero que se factura o se declara al Coordinador</td><td>Medicion de transferencias, monitoreo de red</td></tr>
<tr><td><b>Medicion fasorial</b></td><td>Lo que permite ver la dinamica de la red, no solo el estado</td><td>Exigencia del Coordinador, analisis de perturbaciones</td></tr>
<tr><td><b>Sincronizacion</b></td><td>Que todas las estampas de tiempo sean comparables</td><td>Cuando el cliente ya tiene datos y no cuadran</td></tr>
<tr><td><b>Red OT</b></td><td>Que el dato viaje aunque un enlace o un switch falle</td><td>Subestacion digital, bus de proceso, PRP/HSR</td></tr>
<tr><td><b>Conexion controlada</b></td><td>Energizar un transformador sin el golpe del inrush</td><td>Transformadores de poder, bancos de condensadores</td></tr>
<tr><td><b>Plataforma de datos</b></td><td>Poner el dato industrial donde la IA pueda usarlo</td><td>Digitalizacion, agentes, analitica</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Agrupacion comercial de CONECTA. Los productos concretos de cada familia estan en el capitulo Producto.</cite>

<div class="callout">
  <b>Lo que NO somos.</b> No somos un revendedor de partes con catalogo y precio en mano. Cuando un
  cliente pide "cotizame un switch", la respuesta correcta no es el switch: es preguntar que tiene que
  sobrevivir a que falla. Un switch IEC 61850-3 sin PRP no resuelve el problema que el cliente cree tener.
</div>
""",
        },
    ],
}
