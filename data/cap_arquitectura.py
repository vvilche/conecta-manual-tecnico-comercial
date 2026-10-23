# -*- coding: utf-8 -*-
"""Capitulo 4 — Arquitectura de comunicaciones."""

CAP_ARQUITECTURA = {
    "id": "arquitectura",
    "titulo": "Arquitectura de comunicaciones",
    "subtitulo": "Como se construye una, que elementos debe llevar, y que hay que dibujar para que no se caiga.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "que-es-arquitectura",
            "titulo": "Que es una arquitectura de comunicaciones",
            "tipo": "idea",
            "html": """
<p class="lead">Una arquitectura de comunicaciones no es un dibujo con cajitas y flechas. Es la
<b>decision sobre que pasa cuando algo falla</b>. Si el dibujo no responde esa pregunta, no es una
arquitectura: es un inventario.</p>

<p>Toda arquitectura de un sistema electrico industrial responde cinco preguntas. Si falta una, el
diseño esta incompleto:</p>

<table class="tabla">
<thead><tr><th>Pregunta</th><th>Que define</th><th>Si no se responde</th></tr></thead>
<tbody>
<tr><td><b>1. Que datos viajan</b></td><td>Señales de proceso, estados, alarms, mediciones, archivos de evento</td><td>Se dimensiona mal la red y falta ancho de banda</td></tr>
<tr><td><b>2. Con que protocolo</b></td><td>Como se lee cada equipo y quien pone el tiempo</td><td>Datos sin hora, o hora que no se puede comparar</td></tr>
<tr><td><b>3. Por donde</b></td><td>Medio fisico, segmentacion, rutas, redundancia</td><td>Un solo cable tumba todo el sistema</td></tr>
<tr><td><b>4. Que pasa si falla</b></td><td>Redundancia, buffers, retencion, modo degradado</td><td>Se pierden eventos justo cuando mas importan</td></tr>
<tr><td><b>5. Quien responde</b></td><td>Frontera entre CONECTA, el cliente y terceros</td><td>Nadie se hace cargo del problema en la reunion dificil</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Metodo propio de CONECTA para disenar y revisar arquitecturas. No es un estandar publicado.</cite>

<div class="callout">
  <b>La prueba del dibujo.</b> Si el cliente puede tapar cualquier caja del diagrama con el dedo y
  preguntar "y ahora que pasa?", y no hay respuesta, la arquitectura no esta terminada.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "elementos",
            "titulo": "Los elementos que toda arquitectura debe llevar",
            "tipo": "tabla",
            "html": """
<p class="lead">Estos son los elementos que hay que dibujar y rotular. Un esquema al que le falta la
sincronizacion o la frontera de responsabilidad no sirve para cotizar ni para discutir con el cliente.</p>

<table class="tabla">
<thead><tr><th>Elemento</th><th>Que debe mostrar</th><th>Por que es obligatorio</th></tr></thead>
<tbody>
<tr><td><b>Equipos de campo</b></td><td>Instrumentos, reles, medidores, transformadores de medida</td><td>Es donde nace el dato. Sin esto no se sabe que se esta midiendo.</td></tr>
<tr><td><b>Nivel de control</b></td><td>Controlador, DCS, PLC, SIS</td><td>Define quien manda y quien solo observa.</td></tr>
<tr><td><b>Nivel de adquisicion</b></td><td>RTU, gateway, merging unit, PMU</td><td>Define quien traduce y quien pone estampa de tiempo.</td></tr>
<tr><td><b>Red y segmentos</b></td><td>Switches, VLANs, zonas, conductos, enlaces</td><td>Define la contencion. Sin segmentos, cualquier falla es total.</td></tr>
<tr><td><b>Redundancia</b></td><td>PRP/HSR, hot standby, enlaces redundantes</td><td>Es la respuesta a "que pasa si falla".</td></tr>
<tr><td><b>Sincronizacion</b></td><td>Reloj GPS y como llega a cada equipo (IRIG-B, PTP, NTP)</td><td>Sin reloj comun, las estampas no se comparan.</td></tr>
<tr><td><b>Protocolos por enlace</b></td><td>Que protocolo va en cada flecha</td><td>Evita prometer una integracion que el equipo no soporta.</td></tr>
<tr><td><b>Frontera de responsabilidad</b></td><td>Que es de CONECTA, que del cliente, que de un tercero</td><td>Es el limite contractual. Sin linea, no hay discusion posible.</td></tr>
<tr><td><b>Nivel de aplicacion</b></td><td>SCADA, HMI, PDC, plataforma de datos, reportes</td><td>Es lo que el usuario ve y por lo que paga.</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Checklist propio de CONECTA. Los elementos tecnicos citados (IRIG-B, PTP, PRP/HSR) estan respaldados en el capitulo Protocolos.</cite>

<div class="callout">
  <b>El error frecuente.</b> Dibujar los equipos y olvidar el reloj. El reloj no es un accesorio del
  esquema: es una de las flechas, y si no esta dibujado, nadie lo cotiza.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "como-construir",
            "titulo": "Como se construye, paso a paso",
            "tipo": "detalle",
            "html": """
<p class="lead">El orden importa. Si se empieza por el equipo, la arquitectura termina justificando un
producto. Si se empieza por la pregunta, el producto aparece solo.</p>

<ol class="pasos">
  <li><b>Definir el objetivo del sistema.</b> Que decision tiene que poder tomar el cliente que hoy no
  puede. "Ver la planta" no es un objetivo; "saber que paso primero cuando se cayo" si lo es.</li>
  <li><b>Inventariar lo que ya existe.</b> Equipos, protocolos, reloj, red, cableado. Lo que existe
  condiciona mas que lo que se quiere comprar.</li>
  <li><b>Decidir que se lee por protocolo y que se cablea.</b> Es la decision que mas plata mueve. Si la
  señal ya esta en un IED, no se gasta una entrada.</li>
  <li><b>Fijar la sincronizacion.</b> Que reloj, con que precision, y como llega a cada equipo que
  necesita estampa. Ver capitulo Protocolos.</li>
  <li><b>Segmentar y definir la redundancia.</b> Zonas, conductos, que enlace es critico y que pasa si
  se cae.</li>
  <li><b>Dibujar y rotular.</b> Protocolo en cada enlace, reloj dibujado, frontera marcada.</li>
  <li><b>Recorrer las fallas.</b> Tapar cada caja y preguntar que pasa. Lo que no tiene respuesta vuelve
  al paso 5.</li>
</ol>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Procedimiento propio de CONECTA.</cite>

<div class="callout">
  <b>Regla de honestidad tecnica.</b> Si en el paso 2 el cliente dice "no se que protocolo usa ese
  equipo", no se asume: se pide la ficha o se manda a levantar. Un protocolo supuesto es la causa mas
  comun de un proyecto que no cierra en la puesta en servicio.
</div>

<h4>Que mirar cuando se revisa una arquitectura ajena</h4>
<p>Cuando se revisa un diseño de otro (un cliente, un competidor, un integrador), estas son las preguntas
que revelan rapido si el diseño piensa en fallas:</p>
<ul class="lista">
  <li>Hay un solo enlace entre dos zonas criticas?</li>
  <li>La PMU tiene su reloj, y ese reloj admite IRIG-B?</li>
  <li>El SCADA y el control comparten el mismo switch?</li>
  <li>Quien guarda los eventos si el centro de control no esta disponible?</li>
  <li>La frontera de responsabilidad esta escrita, o solo dibujada?</li>
</ul>
<span class="sello s-supuesto">SUPUESTO</span>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "arquitecturas-referencia",
            "titulo": "Tres arquitecturas de referencia",
            "tipo": "detalle",
            "html": """
<p class="lead">Estas tres se repiten en el negocio. Saberlas de memoria permite dibujar en una pizarra
en la primera reunion, que es donde se gana la confianza tecnica.</p>

<h4>A. Subestacion con PMU y PDC</h4>
<p>Del campo al Coordinador: los transformadores de medida entregan a la PMU; la PMU recibe el tiempo por
IRIG-B desde el reloj GPS; el dato va al PDC Local por la red de la subestacion; el PDC Local lo entrega
al PDC Corporativo del Coordinador, con almacenamiento si se corta el enlace.</p>
<p><b>Elementos obligatorios:</b> PMU, reloj GPS con salida IRIG-B, switch IEC 61850-3, PDC Local con
licencia, enlace de al menos 120 kbps por punto de monitoreo, respaldo de alimentacion 8 horas.
<a href="#f-CEN-MMF2026">CEN-MMF2026</a>, Tabla 7.1-1 y seccion 5.9.</p>
<span class="sello s-extraido">EXTRAIDO</span>

<h4>B. Reemplazo de RTU legacy</h4>
<p>Del campo existente al centro de control, sin rehacer el cableado: los cables de campo llegan a
tarjetas adaptadoras; el Orion I/O ocupa el mismo espacio de 3RU; la Orion emula el protocolo anterior y
el SCADA no cambia su base de datos.</p>
<p><b>Elementos obligatorios:</b> Orion I/O con tarjetas adaptadoras, Orion como RTU, switch, y el
levantamiento del protocolo que hoy habla el SCADA del cliente.
<a href="#f-ORION-RETROFIT">ORION-RETROFIT</a>.</p>
<span class="sello s-extraido">EXTRAIDO</span>

<h4>C. Bus de proceso digital (IEC 61850-9-2)</h4>
<p>Donde los transformadores de medida se digitalizan en la merging unit y viajan como valores muestreados
por la red. Aqui el tiempo no es un extra: es lo que permite que la proteccion diferencial compare muestras
tomadas en lugares distintos.</p>
<p><b>Elementos obligatorios:</b> merging unit sincronizada, red con PTP (perfil IEC/IEEE 61850-9-3) o
IRIG-B, y verificacion del flag de sincronizacion de cada MU. <a href="#f-PTP-PUP-NIST">PTP-PUP-NIST</a>.</p>
<span class="sello s-extraido">EXTRAIDO</span>

<div class="callout supuesto">
  <b>SUPUESTO.</b> En la mayoria de los proyectos chilenos de subestacion existente, la arquitectura que
  se vende es la B, no la C. El bus de proceso completo es atractivo tecnicamente pero cambia demasiado
  del sistema del cliente, y el riesgo de puesta en servicio se lo come el integrador.
</div>
""",
        },
    ],
}
