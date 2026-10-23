# -*- coding: utf-8 -*-
"""Capitulo 3 — Protocolos. La tabla que evita el error mas caro."""

CAP_PROTOCOLOS = {
    "id": "protocolos",
    "titulo": "Protocolos",
    "subtitulo": "Que transporta cada uno, y cual lleva la hora. Esta tabla evita el error mas caro.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "tabla-madre",
            "titulo": "La tabla madre: quien lleva estampa de tiempo",
            "tipo": "tabla",
            "html": """
<p class="lead">Si te llevas una sola hoja de este manual, que sea esta. La columna que importa no es
"que protocolo es mejor" sino <b>"quien pone la hora, y cuando"</b>.</p>

<div class="tabla-scroll">
<table class="tabla madre">
<thead>
<tr>
  <th>Protocolo</th>
  <th>Que transporta</th>
  <th>Lleva tiempo?</th>
  <th>Resolucion del tiempo</th>
  <th>Quien pone la hora</th>
  <th>El error tipico</th>
</tr>
</thead>
<tbody>

<tr class="r-no">
  <td><b>Modbus</b><br><span class="mini">RTU / TCP</span></td>
  <td>Bits y registros crudos de 16 bits en cuatro tablas: Discrete Input, Coils, Input Registers, Holding Registers <a href="#f-MODBUS-V1.1b3">[MODBUS-V1.1b3]</a></td>
  <td class="no"><b>NO</b></td>
  <td>—</td>
  <td>Nadie. El maestro pregunta y recibe un valor sin contexto temporal.</td>
  <td>Creer que el registro "trae hora". No la trae: si necesitas tiempo, lo pones tu al leer, y entonces mides el momento de la lectura, no el del evento.</td>
</tr>

<tr class="r-si">
  <td><b>DNP3</b><br><span class="mini">IEEE 1815</span></td>
  <td>Valor, calidad y tiempo, reportado por eventos (change-of-state) <a href="#f-IEEE1815-TUT">[IEEE1815-TUT]</a></td>
  <td class="si"><b>SI, opcional</b></td>
  <td>milisegundos</td>
  <td>La estacion remota, cuando arma el evento. En UTC desde 2008 <a href="#f-IEEE1815-TUT">[IEEE1815-TUT]</a></td>
  <td>Asumir que todo punto viene con hora. En DNP3 el timestamp es <b>opcional y solo para eventos y objetos congelados</b>, no para datos estaticos <a href="#f-IEEE1815-TUT">[IEEE1815-TUT]</a>.</td>
</tr>

<tr class="r-cond">
  <td><b>IEC 60870-5-101/104</b></td>
  <td>Telecontrol: medidas, estados, mandos, con marca de tiempo en el ASDU</td>
  <td class="cond"><b>SI, segun tipo</b></td>
  <td>CP56Time2a: milisegundos. Tambien existen CP24Time2a y CP32Time2a con menos alcance</td>
  <td>El equipo que origina el evento</td>
  <td>Elegir el tipo de dato sin hora y perder la secuencia. La marca de tiempo no es del protocolo, es del <i>tipo de dato</i> que se configure.</td>
</tr>

<tr class="r-si">
  <td><b>IEC 61850</b><br><span class="mini">MMS, GOOSE, SV</span></td>
  <td>Modelo de datos del equipo completo: medidas, estados, calidad y tiempo, con nombre semantico</td>
  <td class="si"><b>SI</b></td>
  <td>Estructura de tiempo de 80 bits (segundos + fraccion + calidad de tiempo)</td>
  <td>El IED que publica, sincronizado por PTP o IRIG-B</td>
  <td>Suponer que el nombre del punto dice cuando ocurrio. El tiempo viaja como atributo aparte del valor, y hay que leerlo.</td>
</tr>

<tr class="r-si">
  <td><b>IEC 61850-9-2</b><br><span class="mini">Sampled Values</span></td>
  <td>Valores muestreados del bus de proceso (corrientes y tensiones digitalizadas)</td>
  <td class="si"><b>SI, y sincronizado</b></td>
  <td>Muestras por ciclo; en el perfil 9-2LE tipicamente 80 muestras por ciclo</td>
  <td>La merging unit, con un flag de sincronizacion que dice si esta enganchada al reloj</td>
  <td>No verificar el flag de sincronizacion: si la MU perdio el reloj, sigue mandando muestras y parecen validas.</td>
</tr>

<tr class="r-si">
  <td><b>IEEE C37.118</b><br><span class="mini">Sincrofasores / PMU</span></td>
  <td>Fasores de tension y corriente, frecuencia y ROCOF, con time stamp de la muestra</td>
  <td class="si"><b>SI, es el nucleo</b></td>
  <td>Requiere 1 µs de precision de sincronizacion <a href="#f-CEN-MMF2026">[CEN-MMF2026]</a></td>
  <td>La PMU, sincronizada por GPS/IRIG-B</td>
  <td>Instalar la PMU sin resolver el reloj. Con el reloj malo la PMU entrega datos que parecen buenos y no lo son.</td>
</tr>

<tr class="r-cond">
  <td><b>OPC UA</b></td>
  <td>Valor + calidad + <b>dos</b> tiempos: sourceTimestamp y serverTimestamp <a href="#f-OPCUA-SRC-TS">[OPCUA-SRC-TS]</a></td>
  <td class="cond"><b>SI, y separa cual</b></td>
  <td>Resolucion del reloj del equipo; el estandar no fija una resolucion unica</td>
  <td>La fuente pone el sourceTimestamp; el servidor pone el serverTimestamp</td>
  <td>Usar el serverTimestamp como si fuera el momento del evento. Ese es el momento en que el servidor supo del valor, y se refresca aunque el valor no cambie.</td>
</tr>

<tr class="r-no">
  <td><b>SNMP</b></td>
  <td>Estado y contadores de la red: puertos, trafico, alarmas de equipos</td>
  <td class="no"><b>NO como evento</b></td>
  <td>—</td>
  <td>El colector, al hacer la consulta</td>
  <td>Usarlo como si fuera un registro de eventos de proceso. SNMP sirve para saber como esta la red, no cuando ocurrio un fenomeno electrico.</td>
</tr>

</tbody>
</table>
</div>
<span class="sello s-extraido">EXTRAIDO</span> Modbus, DNP3, OPC UA y CEN: fuente primaria con link.
<span class="sello s-supuesto">SUPUESTO</span> 60870-5-104, 61850 MMS/GOOSE, 9-2 y SNMP: clasificacion segun el uso habitual en el rubro; no se cito el texto de la norma.
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "modbus-detalle",
            "titulo": "Modbus: por que no tiene hora, y como se disfraza",
            "tipo": "detalle",
            "html": """
<p class="lead">El spec oficial de Modbus define cuatro tablas de datos: Discrete Input (bits, solo
lectura), Coils (bits, lectura/escritura), Input Registers (palabras de 16 bits, solo lectura) y Holding
Registers (palabras de 16 bits, lectura/escritura). <b>Ninguna de las cuatro tiene una columna de
tiempo</b>.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-MODBUS-V1.1b3">MODBUS-V1.1b3</a>, seccion 4.3 (pagina del spec, 50 paginas)</cite>

<h4>Lo que si existe, y no es lo mismo</h4>
<p>Como el protocolo no lleva hora, algunos fabricantes la mandan <b>como datos</b>: reservan dos o mas
registros para escribir una fecha y una hora, o implementan una extension tipo Enron Modbus. Eso no es
estampa de tiempo del protocolo; es un acuerdo entre el equipo y quien lo lee.</p>

<div class="callout">
  <b>La pregunta que desarma el problema.</b> "El registro de hora que me estas mostrando, lo escribe el
  equipo cuando ocurre el evento, o lo escribe el SCADA cuando hace la consulta?"
  Si la respuesta es la segunda, el dato no tiene tiempo del evento: tiene tiempo de cuando alguien lo miro.
</div>

<p>Consecuencia practica: en una instalacion Modbus, la secuencia de eventos se reconstruye con el reloj
del maestro, y la resolucion real es <b>el periodo de polling</b>, no menos. Si el maestro pregunta cada 5
segundos, dos eventos que ocurrieron con 100 ms de diferencia aparecen simultaneos o en orden arbitrario.</p>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Consecuencia de ingenieria, no una frase del spec. El spec solo define que no hay campo de tiempo.</cite>

<p>Esto no significa que Modbus sea malo. Significa que hay que saber <b>para que se usa</b>: leer un
estado actual, integrar un equipo de terceros, operar una valvula. Para reconstruir una perturbacion se
necesita otra cosa.</p>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "dnp3-detalle",
            "titulo": "DNP3: el tiempo es opcional y cambia el uso",
            "tipo": "detalle",
            "html": """
<p class="lead">DNP3 se diseno para no preguntar todo el tiempo: la estacion remota reporta los cambios
como eventos. El tutorial del comite de subestaciones del IEEE lo dice directo: los datos reportados son
<b>{Value, Quality, Timestamp}</b>, y los cambios se reportan como eventos <i>con o sin</b> timestamps</i>.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-IEEE1815-TUT">IEEE1815-TUT</a>, paginas 35-36</cite>

<h4>La distincion que hay que saber de memoria</h4>
<table class="tabla">
<thead><tr><th>Tipo de dato DNP3</th><th>Trae timestamp?</th><th>Para que sirve</th></tr></thead>
<tbody>
<tr><td>Datos <b>estaticos</b> (el valor actual)</td><td>Normalmente no</td><td>Saber como esta ahora. Se lee al arrancar o despues de una perdida de datos.</td></tr>
<tr><td><b>Eventos</b> (cambios, clase 1/2/3)</td><td><b>Opcional, por variacion del objeto</b></td><td>Reconstruir que paso y en que orden. Es la base de la secuencia de eventos.</td></tr>
<tr><td><b>Objetos congelados</b></td><td><b>Opcional</b></td><td>Capturar un valor con su hora para facturar o auditar.</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-IEEE1815-TUT">IEEE1815-TUT</a>, pagina 55: "Timestamp (optional: events &amp; frozen objects only)"</cite>

<div class="callout">
  <b>Regla de compra.</b> Al especificar un RTU o un equipo DNP3, pedir explicitamente que los eventos
  se transmitan <b>con timestamp</b> y que el equipo tenga reloj propio sincronizado. Si no se pide, la
  variacion por defecto puede no incluirlo, y despues no hay forma de recuperar ese tiempo.
</div>

<p>Detalle fino que sirve para cerrar bien una propuesta: los timestamps de DNP3 estan definidos en
<b>UTC desde 2008</b>, lo que evita el desorden del horario de verano. Pero el tutorial advierte que
algunos sistemas siguen usando hora local y que manejarlo "es un tema del proveedor". Si el cliente tiene
equipos de marcas distintas, ese es un punto de friccion real y conviene sacarlo en la reunion tecnica.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-IEEE1815-TUT">IEEE1815-TUT</a>, pagina 137</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "relojes-protocolos",
            "titulo": "Protocolos de sincronizacion: cual ofrecer",
            "tipo": "detalle",
            "html": """
<p class="lead">Los protocolos de tiempo no compiten entre si por "ser mejores": resuelven necesidades
distintas. Elegir mal se paga en datos que no cuadran.</p>

<table class="tabla">
<thead><tr><th>Protocolo</th><th>Precision</th><th>Como viaja</th><th>Cuando es la respuesta</th></tr></thead>
<tbody>
<tr><td><b>NTP / SNTP</b></td><td>decenas de µs en LAN moderna <a href="#f-RFC5905">[RFC5905]</a>; ~10 ms basta para secuencia de eventos clasica <a href="#f-PTP-PUP-NIST">[PTP-PUP-NIST]</a></td><td>Por la red, sin cable dedicado</td><td>Cuando no se necesita comparar angulos entre equipos. Monitoreo general, logs, servidores.</td></tr>
<tr><td><b>IRIG-B</b></td><td>Depende del reloj maestro; el Kronos declara 60 ns (99%) <a href="#f-KRONOS">[KRONOS]</a></td><td>Par trenzado, coaxil o fibra; modulada o no modulada</td><td>Cuando el equipo tiene puerto IRIG-B y se necesita tiempo robusto y probado. Es lo que pide el Coordinador para PMU <a href="#f-CEN-MMF2026">[CEN-MMF2026]</a>.</td></tr>
<tr><td><b>PTP (IEEE 1588)</b></td><td>submicrosegundo con el perfil de utility <a href="#f-PTP-PUP-NIST">[PTP-PUP-NIST]</a></td><td>Ethernet, con soporte de redundancia PRP/HSR</td><td>Subestacion digital, bus de proceso, cuando el tiempo viaja por la misma red que los datos.</td></tr>
<tr><td><b>PPS / PPM</b></td><td>pulso por segundo, sin informacion de fecha</td><td>Par dedicado</td><td>Sincronizar muestreo de proteccion. Necesita otro canal para saber que segundo es.</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>

<h4>Lo que exige el Coordinador para una PMU</h4>
<p>Esto es normativa chilena y conviene tenerlo a mano: la Tabla 7.1-1 del estudio del Modulo de Medicion
Fasorial pide, entre otras cosas, <b>precison de sincronizacion dentro de 1 µs</b> con base de tiempo
sincronizada por GPS, y <b>codigo de tiempo IRIG-B no modulada</b> (con PTP aceptado en casos de
indisponibilidad de antena). La sincronizacion por reloj externo debe entrar por <b>puerto IRIG-B</b>.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CEN-MMF2026">CEN-MMF2026</a>, Tabla 7.1-1, pagina 105 del PDF</cite>

<div class="callout">
  <b>Consecuencia comercial concreta.</b> Si el cliente esta obligado a instalar una PMU, el reloj no es
  opcional ni "se ve despues": es parte del requerimiento. Cotizar la PMU sin el reloj es entregar un
  proyecto que no va a pasar la puesta en servicio.
</div>

<div class="callout supuesto">
  <b>SUPUESTO.</b> Cuando el cliente ya tiene un reloj GPS de otra marca y funciona, no proponer
  reemplazarlo de entrada. Verificar primero si admite IRIG-B y PTP, y ofrecer solo lo que falta.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "preguntas-protocolo",
            "titulo": "Las cuatro preguntas que resuelven cualquier discusion de protocolo",
            "tipo": "idea",
            "html": """
<p class="lead">No hace falta memorizar todos los protocolos. Hace falta saber preguntar. Estas cuatro
preguntas ordenan cualquier conversacion tecnica y, de paso, muestran dominio del tema.</p>

<ol class="pasos">
  <li><b>Para que se usa este dato?</b> — Mirar una pantalla, facturar, o reconstruir una falla son tres
  necesidades distintas. La tercera es la que exige tiempo.</li>
  <li><b>Quien pone la hora?</b> — El equipo que origina el evento, o el sistema que lo recibe. Si es el
  segundo, la latencia de la red esta dentro del dato.</li>
  <li><b>Con que reloj esta sincronizado ese equipo?</b> — GPS, IRIG-B, PTP, NTP, o ninguno. Si es
  "ninguno", la estampa existe pero no significa nada entre equipos.</li>
  <li><b>Que pasa si el enlace se cae?</b> — El equipo guarda el evento y lo entrega despues con su hora
  original, o el evento se pierde. La diferencia define si el sistema sirve para post-operacion.</li>
</ol>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Guion de conversacion de CONECTA, armado sobre las fuentes citadas arriba.</cite>

<div class="callout">
  <b>Por que estas preguntas venden.</b> El cliente rara vez tiene las respuestas. Cuando descubre que su
  sistema actual no las cumple, la conversacion deja de ser sobre precio y pasa a ser sobre riesgo. Eso es
  la Mina de Oro aplicada a lo tecnico.
</div>
""",
        },
    ],
}
