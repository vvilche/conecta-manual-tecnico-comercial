# -*- coding: utf-8 -*-
"""Capitulo 2.5 — Las seis lineas de negocio del cotizador CONECTA."""

CAP_LINEAS = {
    "id": "lineas",
    "titulo": "Las seis lineas",
    "subtitulo": "Lo que el cotizador trata como linea de negocio, que se compone en cada una, y que NO va en ella.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "que-es-linea",
            "titulo": "Que es una linea, y por que importa saberlo",
            "tipo": "idea",
            "html": """
<p class="lead">En CONECTA una <b>linea</b> no es un catalogo de productos: es una unidad de trabajo que
tiene su propio alcance, su propia composicion de equipos y sus propias horas de ingenieria. Cuando alguien
dice "eso es PMU" o "eso es Repro", esta diciendo como se cotiza, no que se vende.</p>

<p>El cotizador de CONECTA reconoce seis lineas. Son las que tienen cuestionario propio de "Datos Cliente"
y plantilla de cotizacion construida:</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CONECTA-BOM">CONECTA-BOM</a> — repo ConectaCotizador, README: "PMU, PDC, RTU, SCADA, EDAC y Repro usan el formato NUEVO (cuestionario) vía 23_cotizar_pmu.py --linea". Las lineas Medición, GPS y Licencias usan el formato viejo.</cite>

<div class="callout">
  <b>Por que una linea y no un producto.</b> El cliente compra un resultado: "que la planta deje de
  detenerse", "que el Coordinador no me observe", "que el transformador no se dañe". La linea es como
  CONECTA empaqueta ese resultado. Si se cotiza por producto suelto, se pierden las horas de ingenieria
  que son justamente donde esta el margen.
</div>

<h4>La regla de la linea</h4>
<p>Una linea tiene cuatro cosas, siempre las mismas:</p>
<ol class="pasos">
  <li><b>Un alcance tecnico</b> — que queda dentro y que queda fuera. Se escribe, no se sobreentiende.</li>
  <li><b>Una composicion de equipos</b> — que hardware entra, tipicamente en un gabinete o armario.</li>
  <li><b>Horas hombre por rol</b> — ingenieria, programacion, montaje, puesta en servicio, capacitacion.</li>
  <li><b>Una condicion de cierre</b> — el entregable que demuestra que la linea quedo terminada.</li>
</ol>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Estructura propia, derivada de la plantilla de Valorizacion historica de CONECTA.</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "las-seis",
            "titulo": "Las seis, una por una",
            "tipo": "tabla",
            "html": """
<p class="lead">Para cada linea: que resuelve, que se compone historicamente, y con que no se debe
confundir. La composicion es la que aparece en los BOMs reales, <b>sin cifras de costo</b>.</p>

<table class="tabla seis">
<thead><tr><th>Linea</th><th>Que resuelve</th><th>Composicion tipica (BOMs reales)</th><th>No confundir con</th></tr></thead>
<tbody>

<tr>
<td><b>1. PMU</b><br><span class="mini">Medicion fasorial</span></td>
<td>Entregar fasores sincronizados al Coordinador, con la precision que exige la norma.</td>
<td>PMU Vizimax, GPS Kronos, gabinete Rittal, licencia PDC, switch industrial, importacion.</td>
<td>No es "un medidor mejor". Si no hay reloj resuelto, la PMU no cumple.</td>
</tr>

<tr>
<td><b>2. PDC</b><br><span class="mini">Concentrador de datos fasoriales</span></td>
<td>Concentrar los datos de las PMU y entregarlos al PDC del Coordinador, con almacenamiento si se cae el enlace.</td>
<td>Licencia PDC corporativo o local, servidor, redundancia, dongle, capacitacion.</td>
<td>No es un servidor generico. La licencia PDC Local es adicional a la corporativa.</td>
</tr>

<tr>
<td><b>3. RTU</b><br><span class="mini">Adquisicion en subestacion</span></td>
<td>Llevar las señales de la subestacion al centro de control, reutilizando el cableado existente.</td>
<td>Orion SX, Orion I/O (DI, DO, AI), switch Hermes, HMI, gabinete, fuente, touch y teclado rack.</td>
<td>No es un PLC. No reemplaza el control del proceso.</td>
</tr>

<tr>
<td><b>4. SCADA</b><br><span class="mini">Supervision y control</span></td>
<td>Ver y operar la instalacion desde una sala de control, con HMI y base de datos de eventos.</td>
<td>Orion SX (servidores), exportacion, I/O de terceros, pantalla o workstation.</td>
<td>No es el sistema de proteccion. El SCADA mira, no dispara.</td>
</tr>

<tr>
<td><b>5. EDAC</b><br><span class="mini">Desconexion automatica de carga</span></td>
<td>Desconectar carga automaticamente ante una contingencia, segun lo que exige el Coordinador.</td>
<td>Orion I/O, Orion SX, licencias PCVue, despacho expedito.</td>
<td>No es un plan de defensa completo por si solo: el EDAC ejecuta, el plan define.</td>
</tr>

<tr>
<td><b>6. Repro</b><br><span class="mini">Reconfiguracion de protecciones</span></td>
<td>Ajustar y reconfigurar protecciones existentes para que coordinen y cumplan.</td>
<td>Reles de proteccion, proteccion diferencial de transformador, blocks de prueba, importacion.</td>
<td>No es venta de reles nuevos. Muchas veces es servicio sobre lo que ya esta instalado.</td>
</tr>

</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CONECTA-BOM">CONECTA-BOM</a> — composicion extraida de los BOMs historicos por ZIP+XML, cero LLM. Muestras por linea: RTU 23, SCADA 41, EDAC 50, Repro 57.</cite>

<div class="callout">
  <b>Aviso de lectura.</b> La composicion muestra <b>que</b> compone una linea, no <b>cuanto</b> vale.
  Los costos reales existen y estan medidos, pero no se publican en este manual: se consultan en el
  cotizador. Un vendedor que da un precio de memoria es un pasivo, no un activo.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "lineas-fuera",
            "titulo": "Lo que no es una de las seis, y aun asi se vende",
            "tipo": "detalle",
            "html": """
<p class="lead">Las seis lineas son las que tienen motor de cotizacion. Pero CONECTA vende mas cosas, y
conviene saber donde caen para no forzar un producto dentro de una linea donde no pertenece.</p>

<table class="tabla">
<thead><tr><th>Lo que el cliente pide</th><th>Donde cae</th><th>Nota</th></tr></thead>
<tbody>
<tr><td>Medicion de potencia (Bitronics)</td><td>Linea Medición (formato viejo)</td><td>El medidor de precision no es una PMU.</td></tr>
<tr><td>Solo el reloj GPS</td><td>Linea GPS (formato viejo)</td><td>Se puede vender solo, y muchas veces es la venta mas facil.</td></tr>
<tr><td>Licencias, drivers, upgrade de software</td><td>Linea Licencias (formato viejo)</td><td>Firewall, Modbus, OPC, redundancia basica, upgrade.</td></tr>
<tr><td>SynchroTeq (conexion controlada)</td><td>Linea propia en el catalogo</td><td>Se relaciona con Repro pero es otro producto y otras horas.</td></tr>
<tr><td>Ciberseguridad</td><td>Linea propia, sin BOM de hardware</td><td>Ver capitulo Ciberseguridad: es servicio, no equipos en la planilla historica.</td></tr>
<tr><td>Protecciones</td><td>Linea propia, sin BOM de hardware</td><td>Los BOMs reales no traen equipos en "Equi. Mat. Arr. Sub.": son servicios y estudios.</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CONECTA-BOM">CONECTA-BOM</a> — costos_hardware.json, campo _vacios: "Protecciones y Ciberseguridad: sus BOMs reales no traen equipos en 'Equi. Mat. Arr. Sub.' (son servicios/estudios). No se inventa hardware donde no lo hay."</cite>

<div class="callout supuesto">
  <b>SUPUESTO — reflejo que hay que tener.</b> Si el cliente pide algo que no cae en ninguna linea, la
  respuesta no es forzarlo: es preguntar que tiene que lograr y armar el alcance.
</div>

<div class="callout">
  <b>Seis no son todo el catalogo.</b> El catalogo de CONECTA tiene del orden de 86 lineas de producto
  agrupadas por categoria y partner; las seis de este capitulo son solo las que tienen motor de
  cotizacion construido. Confundir ambas cosas lleva a dos errores opuestos: creer que no vendemos algo
  que si esta en catalogo, o prometer una cotizacion automatica para una linea que hay que armar a mano.
  <a href="#f-CATALOGO-86">CATALOGO-86</a>
</div>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CATALOGO-86">CATALOGO-86</a> — referencia del catalogo consolidado: "Catalogo consolidado de 86 lineas por categoria y partner".</cite>
""",
        },
    ],
}
