# -*- coding: utf-8 -*-
"""Capitulo 10 — Casos de uso: NovaTech, Vizimax y Belden."""

CAP_PARTNERS2 = {
    "id": "partners-2",
    "titulo": "Casos de uso: NovaTech, Vizimax y Belden",
    "subtitulo": "Los tres partners de subestacion. El retrofit de RTU es el negocio mas grande, y tiene una trampa que se paga caro.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "novatech-mapa",
            "titulo": "NovaTech: tres lineas, tres conversaciones distintas",
            "tipo": "producto",
            "html": """
<p class="lead">NovaTech (Bethlehem, PA, desde 1979) cubre automatizacion de subestacion, medicion de potencia
y sincronizacion satelital. Las tres lineas se venden a personas distintas y por razones distintas.</p>

<table class="tabla">
<thead><tr><th>Linea</th><th>Que resuelve</th><th>A quien se le vende</th></tr></thead>
<tbody>
<tr><td><b>Orion</b> (RTU y gateways)</td><td>Llevar las senales de la subestacion al centro de control, sin rehacer el cableado</td><td>Jefe de protecciones y control, jefe de subestaciones</td></tr>
<tr><td><b>Bitronics</b> (medicion)</td><td>El numero que se factura o se audita</td><td>Operaciones, facturacion, medidores</td></tr>
<tr><td><b>Kronos</b> (reloj satelital)</td><td>Que todas las estampas de tiempo sean comparables</td><td>Quien ya tiene el problema de datos que no cuadran</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-NOVATECH">NOVATECH</a> — catalogo de producto del fabricante</cite>

<div class="callout">
  <b>La venta mas facil de las tres.</b> El reloj. Cuando el cliente dice "tenemos dos eventos y no sabemos
  cual fue primero", ya reconocio el problema y no hay que convencerlo de nada. Se vende solo.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "retrofit-caso",
            "titulo": "El retrofit de RTU: el negocio mas grande y el mas mal entendido",
            "tipo": "detalle",
            "html": """
<p class="lead">Este es el caso de uso que mas plata mueve en NovaTech, y el que mas veces se cotiza mal.
El concepto que hay que entender, y repetir igual, es uno:</p>

<div class="callout">
  <b>El retrofit no reemplaza el campo. Reemplaza el procesador y los modulos, y conserva el cableado.</b>
  Los conectores de terreno se mueven a una <i>adaptor board</i>, y las interconexiones entre esa placa y el
  Orion I/O salen cableadas y probadas de fabrica.
</div>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-ORION-RETROFIT">ORION-RETROFIT</a> — "Many of our retrofit solutions do not require lifting of field wiring" (NovaTech)</cite>

<h4>Por que eso importa tanto</h4>
<p>Sin retrofit, cambiar una RTU es un proyecto de "intervenir la subestacion": retirar cables, probar punta
a punta, parada larga. Con retrofit, es un <b>cambio de modulo en la misma ventana de mantenimiento</b>. La
diferencia comercial no es el equipo: es que no hay parada extra.</p>

<h4>Los cinco legacy y que se necesita</h4>
<table class="tabla">
<thead><tr><th>RTU legacy</th><th>Como se hace el retrofit</th></tr></thead>
<tbody>
<tr><td><b>GE D20 / D200</b></td><td>El caso mas frecuente en Chile. Modulos de alta densidad con conectores estilo D20 de fabrica, en el mismo espacio de 3RU. Reemplaza D20A (32 AI), D20S (64 DI), D20K (32 DO) y D20C (16 DI + 16 DO + 16 AI).</td></tr>
<tr><td><b>Telvent</b></td><td>Tarjeta de interfaz NovaTech mas interconexion a Orion I/O. Las salidas usan tarjeta HPO (High Power Output).</td></tr>
<tr><td><b>Siemens Telegyr</b></td><td>Placa de interfaz de 8 puntos y "Top Hat" para el modulo de 32. Caso real: 96 DI + 32 DO en un solo Orion I/O.</td></tr>
<tr><td><b>Systems Northwest (SNW)</b></td><td>Placa que reemplaza los reles intermediarios. Se conservan las cuchillas de aislamiento.</td></tr>
<tr><td><b>ACS 7530</b></td><td>Dos placas adaptadoras y arneses precableados. Ejemplo: 32 DI, 16 DO, 8 AI.</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-NOVATECH-RETROFIT">NOVATECH-RETROFIT</a> — presentacion oficial "Legacy RTU Retrofit with Orion" (sept-2020)</cite>

<div class="callout">
  <b>La trampa que se paga caro.</b> En Chile, el "D20" muchas veces NO es una RTU: es el rele de proteccion
  GE D20/D25. Mismo prefijo, producto distinto. Si la funcion es proteccion, el reemplazo es un IED con
  pruebas de proteccion — no es un cambio de modulo. <b>Confirmar la funcion antes de cotizar.</b> En el
  inventario de Transelec hay un D25 marcado como "SUB RTU", que hace de RTU de respaldo: hay que leer la
  columna tipo, no el nombre del equipo.
</div>

<h4>El costo oculto que se olvida cotizar</h4>
<p>NovaTech convierte la configuracion D20 a NCD de OrionLX. Es una linea de servicio que va <b>aparte del
hardware</b>. Sin ella, el cliente queda con una RTU nueva y sin base de senales: el equipo llega y no
funciona. Vender solo hardware es vender medio proyecto.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-NOVATECH-RETROFIT">NOVATECH-RETROFIT</a></cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "novatech-casos",
            "titulo": "NovaTech: casos de uso por equipo",
            "tipo": "tabla",
            "html": """
<table class="tabla casos">
<thead><tr><th>Lo que el cliente dice</th><th>Equipo</th><th>Caso de uso y por que ese</th></tr></thead>
<tbody>

<tr>
<td>"Mi RTU D20 ya no tiene repuestos"</td>
<td><b>Orion I/O</b> + <b>OrionLX+</b></td>
<td>El caso central. Se conserva el cableado de campo, se cambia el procesador y los modulos. La RTU nueva emula el protocolo anterior, asi que el SCADA no cambia su base de datos y el cambio puede ser transparente al centro de control.</td>
</tr>

<tr>
<td>"No puedo botar 20 años de cableado"</td>
<td><b>Orion I/O</b> con adaptor board</td>
<td>Es la objecion mas comun y la mas facil de responder: el cableado no se levanta. Los conectores pasan a la placa adaptadora y las interconexiones vienen de fabrica.</td>
</tr>

<tr>
<td>"Tengo dos RTU y si una falla pierdo la subestacion"</td>
<td><b>OrionLX+</b> en hot standby</td>
<td>Redundancia del RTU. Ojo con el detalle: la redundancia va en el RTU, <b>no en el I/O</b>. El Orion I/O no soporta redundancia propia.</td>
</tr>

<tr>
<td>"Quiero ver la subestacion sin comprar un SCADA aparte"</td>
<td><b>Orion SCADA</b> (HMI local)</td>
<td>Unilineales, faceplates y alarmas en el propio Orion. Sirve para operacion local cuando el centro de control no esta disponible.</td>
</tr>

<tr>
<td>"Necesito medir potencia con precision de facturacion"</td>
<td><b>Bitronics 50/60</b></td>
<td>Precision 0,2s calibrada individualmente, MTBF de 40 años y garantia de 10 años. Se instala con TC de nucleo partido <b>sin tomar salida de servicio</b>.</td>
</tr>

<tr>
<td>"Quiero medir distribucion sin instalar TT/TC nuevos"</td>
<td><b>M661 DGM</b></td>
<td>Solucion "primary in a box": medidor M661 mas sensores Lindsey LEA, con OrionMX opcional para ciberseguridad e I/O. Llega lista para montar.</td>
</tr>

<tr>
<td>"Necesito sincronizar generadores"</td>
<td><b>PowerPlex II</b></td>
<td>Dos sets trifasicos con actualizacion de un ciclo. Es el equipo de sincronizacion de generadores, no un medidor de tablero.</td>
</tr>

<tr>
<td>"Mis eventos no cuadran entre dos subestaciones"</td>
<td><b>Kronos</b></td>
<td>El problema es el reloj, no el registro. Kronos declara 60 ns (99%) de desviacion maxima y soporta IRIG-B, NTP/SNTP y PTP con perfiles C37.238 e IEC 61850-9-3. Es la respuesta al dato sin tiempo comparable.</td>
</tr>

<tr>
<td>"Me piden IRIG-B para la PMU del Coordinador"</td>
<td><b>Kronos 3R</b></td>
<td>Trae IRIG-B con extensiones IEEE C37.118, PTP y PRP/HSR (IEC 62439-3). Es el que calza con la exigencia de 1 µs e IRIG-B no modulada que pide el Coordinador.</td>
</tr>

<tr>
<td>"Necesito que la red no pierda paquetes aunque falle un enlace"</td>
<td><b>Kronos 3R</b> + switch Hirschmann</td>
<td>PRP/HSR. El reloj y el switch tienen que soportarlo los dos: no basta con uno.</td>
</tr>

<tr>
<td>"Es una subestacion chica, no necesito tanto"</td>
<td><b>Kronos 2R</b> o <b>Kronos 1</b></td>
<td>2R con TCXO y NTP; 1 con IRIG-B y PPS. La precision es la misma familia; cambian las funciones avanzadas.</td>
</tr>

<tr>
<td>"Quiero migrar pero no tengo ventana de parada"</td>
<td><b>Orion I/O</b></td>
<td>El retrofit entra en la mantencion programada. Ese es el argumento de venta, no el precio: no requiere una parada adicional.</td>
</tr>

</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-NOVATECH">NOVATECH</a> · <a href="#f-ORION-RETROFIT">ORION-RETROFIT</a> · <a href="#f-ORION-IO-1MS">ORION-IO-1MS</a> · <a href="#f-KRONOS">KRONOS</a> · <a href="#f-BITRONICS">BITRONICS</a></cite>

<div class="callout">
  <b>Donde esta el margen, medido.</b> En un proyecto real de retrofit (S/E Atacama, Transelec) el margen
  de los equipos fue de un 11% y el de las horas hombre de un 77%. El retrofit <b>se vende como servicio de
  ingenieria con equipos</b>, no como venta de hardware. Cotizarlo como hardware es regalar el negocio.
  <a href="#f-NOVATECH-RETROFIT">NOVATECH-RETROFIT</a>
</div>
<span class="sello s-extraido">EXTRAIDO</span>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "vizimax",
            "titulo": "Vizimax: el caso de uso que nadie mas resuelve",
            "tipo": "producto",
            "html": """
<p class="lead">Vizimax hace una cosa que ninguno de los otros partners hace: <b>control de conexion
point-on-wave</b>. Ese es el caso de uso y hay que explicarlo bien, porque no es intuitivo.</p>

<h4>El problema en palabras simples</h4>
<p>Cuando energizas un transformador en el peor instante del ciclo de tension, aparece una corriente de
inrush enorme. Esa corriente no es una falla, pero estresa el transformador, mueve las protecciones
diferenciales y acorta la vida del equipo. El control point-on-wave <b>cierra el interruptor en el instante
correcto del ciclo</b> para que eso no ocurra.</p>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Explicacion divulgativa del fenomeno, no una cita textual del fabricante.</cite>

<table class="tabla casos">
<thead><tr><th>Lo que el cliente dice</th><th>Equipo</th><th>Caso de uso y por que ese</th></tr></thead>
<tbody>

<tr>
<td>"Cada vez que energizo el transformador salta la diferencial"</td>
<td><b>SynchroTeq Plus</b></td>
<td>Control de conexion point-on-wave en alta tension. Mitiga el inrush que dispara la proteccion diferencial. Es el caso mas claro y el mas caro de no resolver.</td>
</tr>

<tr>
<td>"Se me estan dañando los transformadores de poder"</td>
<td><b>SynchroTeq Plus</b></td>
<td>El inrush estresa termica y mecanicamente el transformador. El control de conexion extiende la vida util del activo, que es el argumento que habla con gerencia.</td>
</tr>

<tr>
<td>"Necesito conectar bancos de condensadores sin transitorios"</td>
<td><b>SynchroTeq MV</b></td>
<td>Hasta 69 kV. Aplica a bancos de capacitores, reactores shunt, cables de potencia y transformadores de media tension.</td>
</tr>

<tr>
<td>"Mi interruptor es de una marca que no es la suya"</td>
<td><b>SynchroTeq</b> (cualquier variante)</td>
<td>Es independiente del fabricante del interruptor: funciona con ABB, Siemens, SEL, GE y otros. Ese es el argumento fuerte en una subestacion heterogenea.</td>
</tr>

<tr>
<td>"Quiero migrar a IEC 61850 pero mis transformadores son analogos"</td>
<td><b>AMU</b></td>
<td>Merging unit que digitaliza las mediciones AC de transformadores instrumento convencionales. Es el puente entre lo analogo y el bus de proceso digital.</td>
</tr>

<tr>
<td>"Tengo interruptores viejos y no se como estan"</td>
<td><b>RightWON</b></td>
<td>Agrega inteligencia a equipos ya instalados: monitoreo de interruptores y transformadores, gestion de eventos. No requiere reemplazar nada.</td>
</tr>

<tr>
<td>"Necesito PMU y no quiero quedar amarrado a un solo proveedor"</td>
<td><b>PMU Vizimax</b></td>
<td>Cumple IEEE C37.118 y aplica al requisito del Coordinador para generadores. Compite de frente con la PMU de SUPCON y con la de SATEC: se ofrece la que mejor calce al proyecto.</td>
</tr>

</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-VIZIMAX">VIZIMAX</a> — catalogo de producto del fabricante</cite>

<div class="callout supuesto">
  <b>SUPUESTO — el detalle que hace perder la cotizacion.</b> Para cotizar SynchroTeq hay que conocer el
  <b>tipo de interruptor y su mecanismo</b>. Sin eso, el numero que se da es inventado. Es la primera pregunta
  de la reunion tecnica, no la ultima.
</div>

<h4>Donde Vizimax gana y donde no</h4>
<ul class="lista">
  <li><b>Gana</b> en point-on-wave: no tiene competidor directo fuerte. Su equivalente mas cercano es ABB Switchsync.</li>
  <li><b>Compite</b> en PMU con SUPCON y SATEC: ahi no hay ventaja estructural, se decide por proyecto.</li>
  <li><b>Pierde</b> si el cliente solo quiere medir: Vizimax no es un medidor de facturacion.</li>
</ul>
<span class="sello s-supuesto">SUPUESTO</span>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "belden",
            "titulo": "Belden / Hirschmann: la red que no se cae",
            "tipo": "producto",
            "html": """
<p class="lead">Hirschmann es la marca de switches industriales de Belden para entornos criticos. Se vende
por una razon sola: <b>que el dato llegue aunque falle un enlace</b>.</p>

<table class="tabla casos">
<thead><tr><th>Lo que el cliente dice</th><th>Equipo</th><th>Caso de uso y por que ese</th></tr></thead>
<tbody>

<tr>
<td>"Se me cae la comunicacion de la subestacion y no se por que"</td>
<td><b>MACH1000/4000</b></td>
<td>Backbone de subestacion con PRP/HSR. La red redunda sin perder paquetes, no solo sin perder el enlace: la diferencia importa en protecciones.</td>
</tr>

<tr>
<td>"Necesito un switch que aguante la subestacion"</td>
<td>Serie <b>RS20/RS30/RS40</b></td>
<td>Certificacion IEC 61850-3 e IEEE 1613, con rango de -40 a +85 grados. Es el requisito de ambiente, no una preferencia de marca.</td>
</tr>

<tr>
<td>"Tengo poco espacio en el gabinete"</td>
<td><b>BOBCAT</b></td>
<td>Switch compacto para gabinetes chicos. Es el que entra donde un rack no cabe.</td>
</tr>

<tr>
<td>"Me piden segmentar la red entre planta y oficina"</td>
<td><b>EAGLE</b></td>
<td>Firewall industrial OT para segmentacion. Es la respuesta tecnica a la Ley 21.663 y a IEC 62443, no un firewall de TI.</td>
</tr>

<tr>
<td>"Necesito todo por fibra, hay mucha distancia"</td>
<td><b>MACH4000</b> / <b>GREYHOUND</b></td>
<td>Backbone de fibra para planta completa. Caso real: en una subestacion donde no habia espacio para un armario nuevo, el proyecto termino con ~160 m de fibra por trinchera — la red define el costo real.</td>
</tr>

<tr>
<td>"Quiero certificar la subestacion digital"</td>
<td><b>MACH1000</b> + Orion + <b>Kronos</b></td>
<td>Red, RTU y reloj del mismo ecosistema. El paquete subestacion digital se vende junto, no por partes.</td>
</tr>

</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-BELDEN">BELDEN</a> — catalogo de producto del fabricante. El caso de los 160 m de fibra viene de <a href="#f-NOVATECH-RETROFIT">NOVATECH-RETROFIT</a> (S/E Atacama, Transelec)</cite>

<div class="callout">
  <b>Lo que hay que advertir siempre.</b> PRP/HSR <b>no es plug-and-play</b>: requiere configuracion
  especifica. Prometer "lo conectas y funciona" termina en una puesta en servicio que no cierra.
</div>

<h4>Contra quien compite</h4>
<table class="tabla">
<thead><tr><th>Competidor</th><th>Como se compite</th></tr></thead>
<tbody>
<tr><td>Siemens Ruggedcom</td><td>Relacion precio/prestaciones y facilidad de configuracion</td></tr>
<tr><td>Moxa</td><td>Certificacion IEC 61850-3 completa, no parcial</td></tr>
<tr><td>Cisco Industrial</td><td>Diseñado para OT desde el origen, no adaptado de TI</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Posicionamiento comercial propio, coherente con la ficha del fabricante.</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "paquete-subestacion",
            "titulo": "El paquete completo: cuando los tres partners se venden juntos",
            "tipo": "detalle",
            "html": """
<p class="lead">En una subestacion, los tres partners no compiten: se necesitan. Saber armar el paquete es
la diferencia entre vender un equipo y vender el proyecto.</p>

<table class="tabla">
<thead><tr><th>Capa</th><th>Producto</th><th>Partner</th></tr></thead>
<tbody>
<tr><td><b>Adquisicion</b></td><td>Orion LX+ / Orion I/O</td><td>NovaTech</td></tr>
<tr><td><b>Medicion</b></td><td>Bitronics 50/60 o M661 DGM</td><td>NovaTech</td></tr>
<tr><td><b>Sincronizacion</b></td><td>Kronos 3R (IRIG-B + PTP + PRP/HSR)</td><td>NovaTech</td></tr>
<tr><td><b>Conexion controlada</b></td><td>SynchroTeq Plus</td><td>Vizimax</td></tr>
<tr><td><b>Red OT</b></td><td>MACH1000 / RS40 con PRP/HSR</td><td>Belden</td></tr>
<tr><td><b>Segmentacion</b></td><td>Firewall EAGLE</td><td>Belden</td></tr>
<tr><td><b>Visualizacion local</b></td><td>Orion SCADA</td><td>NovaTech</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-NOVATECH">NOVATECH</a> · <a href="#f-VIZIMAX">VIZIMAX</a> · <a href="#f-BELDEN">BELDEN</a></cite>

<div class="callout">
  <b>La regla del paquete.</b> Si el cliente compra la red sin el reloj, tiene una red redundante con
  estampas que no se comparan. Si compra el reloj sin la red, tiene tiempo exacto que no llega. El paquete
  se defiende solo: cada pieza sin las otras es plata mal gastada.
</div>

<div class="callout supuesto">
  <b>SUPUESTO — el orden de venta.</b> No abrir con el paquete completo. Abrir con el problema mas urgente
  del cliente (casi siempre: la RTU sin repuestos), y despues mostrar las otras capas como consecuencia.
  Presentar siete capas en la primera reunion hace que el cliente no compre ninguna.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "trampas-partners",
            "titulo": "Las trampas de estos tres partners",
            "tipo": "detalle",
            "html": """
<div class="callout supuesto">
  <b>1. D20 no siempre es una RTU.</b> En Chile el D20/D25 muchas veces es rele de proteccion GE. Si la
  funcion es proteccion, no aplica el retrofit de I/O. Confirmar la funcion leyendo el inventario, no el
  nombre.
</div>

<div class="callout supuesto">
  <b>2. Orion I/O no soporta redundancia.</b> Si el cliente exige hot-standby, la redundancia va en el
  OrionLX, no en el I/O. Prometerlo al reves se descubre en la puesta en servicio.
</div>

<div class="callout supuesto">
  <b>3. "Cero recableado" esta mal dicho.</b> Lo correcto es "no requiere levantar el cableado de campo".
  Los conectores si se mueven a la placa adaptadora, y eso es trabajo de taller.
</div>

<div class="callout supuesto">
  <b>4. SynchroTeq necesita el tipo de interruptor.</b> Sin conocer el mecanismo, el numero es inventado.
</div>

<div class="callout supuesto">
  <b>5. PRP/HSR no es plug-and-play.</b> Requiere configuracion en el switch y en el reloj.
</div>

<div class="callout supuesto">
  <b>6. La conversion de configuracion va aparte.</b> Sin ella, el cliente recibe una RTU nueva y sin base
  de senales.
</div>

<div class="callout">
  <b>Y la trampa de la medicion de leads.</b> En InfoTecnica CEN hay panos llamados "ION" que parecen
  remotas y son medidores Schneider ION 8650. En un barrido sobre el padron completo eran la mayoria y
  triplicaban el universo real de remotas. Filtrar antes de contar, o la campana sale inflada.
</div>
""",
        },
    ],
}
