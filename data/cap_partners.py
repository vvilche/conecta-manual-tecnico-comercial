# -*- coding: utf-8 -*-
"""Capitulo 9 — Casos de uso por partner: SATEC y SUPCON."""

CAP_PARTNERS = {
    "id": "partners",
    "titulo": "Casos de uso: SATEC y SUPCON",
    "subtitulo": "Los dos partners de mayor portafolio, con el caso de uso concreto de cada equipo y lo que no se debe prometer.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "por-que-casos",
            "titulo": "Por que un caso de uso vale mas que una ficha tecnica",
            "tipo": "idea",
            "html": """
<p class="lead">Un cliente no compra un PM180 ni un ECS-700. Compra que la planta deje de detenerse, o que el
Coordinador no lo observe. El caso de uso es el puente entre el equipo y esa frase. Sin el, la conversacion
termina en "mandame el datasheet y comparo precios".</p>

<table class="tabla">
<thead><tr><th>Nivel</th><th>Como suena</th><th>Que consigue</th></tr></thead>
<tbody>
<tr><td><b>Catalogo</b></td><td>"Tengo el PM180, es Clase A"</td><td>Que el cliente pida precio a tres proveedores</td></tr>
<tr><td><b>Funcion</b></td><td>"Registra fallas y calcula distancia a la falla"</td><td>Que el cliente pregunte como lo hace</td></tr>
<tr><td><b>Caso de uso</b></td><td>"Cuando dispare un alimentador, en vez de mandar una cuadrilla a recorrer 40 km, sabes en que tramo esta la falla"</td><td>Que el cliente cuente su propio problema</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Escalera de conversacion propia de CONECTA.</cite>

<div class="callout">
  <b>La regla.</b> Nunca presentar un equipo sin su caso de uso. Si no sabes cual es, la pregunta correcta
  no es "que modelo te ofrezco" sino "que te esta costando plata hoy".
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "satec-mapa",
            "titulo": "SATEC: que es y como se elige",
            "tipo": "producto",
            "html": """
<p class="lead">SATEC (Israel) fabrica medicion electrica de precision, calidad de energia (PQ) y
sincrofasores. Cubre desde medidores compactos DIN hasta analizadores Clase A y PMU de grado utilidad.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-SATEC">SATEC</a> — catalogo de producto del fabricante</cite>

<h4>El diferencial transversal, en una linea</h4>
<p>Tres cosas que SATEC hace y que hay que saber repetir:</p>
<ul class="lista">
  <li><b>Multi-protocolo nativo:</b> Modbus, DNP3, IEC 61850, IEC 60870-5-101/104, BACnet y C37.118.2.</li>
  <li><b>I/O embebido y PLC programable</b> en casi todos los equipos: el medidor tambien puede actuar.</li>
  <li><b>Entradas de corriente multiformato:</b> 5A/1A, 40mA HACS, pinzas Rogowski, LPIT, sensores ABB/GWP.</li>
</ul>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-SATEC">SATEC</a></cite>

<div class="callout">
  <b>Por que el multiformato importa comercialmente.</b> Si el cliente ya tiene TC de 5A o 1A, o sensores
  LPIT en celdas MT, el equipo entra sin instalar transformadores de medida nuevos. Eso abaraja la propuesta
  y hay que decirlo en la primera reunion, no en el anexo.
</div>

<h4>Logica de seleccion: seis preguntas, un equipo</h4>
<table class="tabla">
<thead><tr><th>Si el cliente necesita...</th><th>El equipo es</th></tr></thead>
<tbody>
<tr><td>Facturacion (revenue)</td><td>EM720, EM920, PM172E o EM133-MID</td></tr>
<tr><td>PQ certificada Clase A</td><td>PM180 o PM17x / PRO Series</td></tr>
<tr><td>PMU para WAMS</td><td>PMU PRO, o PM180 con modulo PMU</td></tr>
<tr><td>Muchos circuitos en un tablero</td><td>BFM-II o BFM136</td></tr>
<tr><td>Medicion DC (solar, BESS, data center)</td><td>PRO Series (Hall) o PM130 PLUS (shunt)</td></tr>
<tr><td>Registro de fallas</td><td>PM180 DFR o BFM-DFR</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-SATEC">SATEC</a> — logica de seleccion del catalogo</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "satec-casos",
            "titulo": "SATEC: los casos de uso, uno por uno",
            "tipo": "tabla",
            "html": """
<p class="lead">Este es el bloque que hay que saber de memoria. A la izquierda lo que el cliente dice; a la
derecha el equipo y la razon tecnica.</p>

<table class="tabla casos">
<thead><tr><th>Lo que el cliente dice</th><th>Equipo</th><th>Caso de uso y por que ese</th></tr></thead>
<tbody>

<tr>
<td>"Necesito demostrar que mi energia cumple, con respaldo legal"</td>
<td><b>PM180</b> / <b>PM17x PRO</b></td>
<td>PQ Clase A segun IEC 61000-4-30, que es el estandar exigido para monitoreo contractual y regulatorio. El PM180 esta certificado por NMI. Si el cliente esta en America (Chile incluido) la variante es <b>PM174 PRO</b> (IEEE 1159); si la casa matriz es europea, <b>PM175 PRO</b> (EN50160). Mismo equipo, distinto reporte.</td>
</tr>

<tr>
<td>"Cuando hay una falla, no se donde esta"</td>
<td><b>PM180 DFR</b> / <b>BFM-DFR</b></td>
<td>Registrador de fallas con calculo de distancia a falla. Reemplaza la cuadrilla que recorre la linea buscando el tramo quemado. El BFM-DFR ademas se monta sobre el secundario de TC de proteccion existente (HACS 100/200A), sin instalar TC nuevos.</td>
</tr>

<tr>
<td>"El Coordinador me pide fasores"</td>
<td><b>PMU PRO</b></td>
<td>PMU dedicada formato DIN, P/M-Class C37.118.1, 200/240 frames por segundo, TVE menor a 0,05%, con PTP e IRIG-B a 1 µs. Transmite C37.118.2 y habla IEC 61850-9-2. Es la respuesta cuando el requisito es cumplir, no monitorear.</td>
</tr>

<tr>
<td>"Tengo 18 clientes en un mismo tablero y no se cuanto consume cada uno"</td>
<td><b>BFM-II</b></td>
<td>Multicircuito 18 trifasicos o 54 monofasicos, con doble tension de dos fuentes distintas. Factura 18 clientes desde un solo equipo. Es el caso clasico de mall, edificio de oficinas o data center con submedicion.</td>
</tr>

<tr>
<td>"Quiero medir el BESS, carga y descarga, y la eficiencia del ciclo"</td>
<td><b>PRO Series</b> + <b>VRM</b></td>
<td>Medicion AC y DC en el mismo equipo. El VRM (modulo de razon de tension) permite medir DC sobre 820 V. Sin el, no se ve el lado DC del BESS.</td>
</tr>

<tr>
<td>"Mi medidor de facturacion no me dice nada de la calidad"</td>
<td><b>EM720</b> / <b>EM920</b></td>
<td>Hibrido revenue + PQ. Ademas trae <b>medicion virtual de perdidas</b> de transformador y linea, que permite eliminar un punto de medida fisico en alta tension.</td>
</tr>

<tr>
<td>"Tengo celdas MT y no puedo instalar TT/TC"</td>
<td><b>PM17x PRO</b> / <b>PRO Series</b></td>
<td>Interfaces para sensores ABB MV, LPIT o GWP 225 mV, que van en la celda sin transformadores convencionales. Es la ventaja mas fuerte en retrofit de media tension.</td>
</tr>

<tr>
<td>"Le estan cobrando de mas y no lo puede probar"</td>
<td><b>PM175</b> + <b>PM130EH</b></td>
<td>Caso documentado: un kibutz detecto sobrefacturacion de 13,5% y recupero USD 33.500. El argumento es la verificacion independiente, no el medidor.</td>
</tr>

<tr>
<td>"Necesito medicion DC en un data center o telecom"</td>
<td><b>PM130 PLUS</b></td>
<td>Unico de la linea compacta con medicion DC por shunt. Caso de uso: plantas de -48 V en telecom y data centers.</td>
</tr>

<tr>
<td>"Quiero que el medidor me avise sin que yo lo este preguntando"</td>
<td>Todos los SATEC</td>
<td>120 registros Modbus asignables (se leen en una sola peticion) y cliente de notificacion Modbus TCP, que hace push ante eventos en vez de polling. Baja trafico y latencia en el SCADA.</td>
</tr>

<tr>
<td>"Necesito resolver los servicios auxiliares de frecuencia"</td>
<td><b>PM180</b> / <b>PRO</b> / <b>PM17x</b></td>
<td>Resolucion de 0,0001 Hz (cuatro decimales) por ciclo. Es lo que exige medir respuesta en frecuencia.</td>
</tr>

<tr>
<td>"Tengo una fuga a tierra y no se en que circuito"</td>
<td><b>PRO Series</b> / <b>PM17x</b></td>
<td>Cuarta entrada de corriente dedicada a fuga. Aplicacion directa en seguridad electrica y tableros con aislamiento degradado.</td>
</tr>

</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-SATEC">SATEC</a> — casos de uso documentados en el catalogo del fabricante y en la matriz de conocimiento SATEC de CONECTA</cite>

<div class="callout">
  <b>El caso de uso que mas vende en Chile.</b> El registro de fallas con distancia a falla. Casi ningun
  cliente tiene respuesta a "donde esta la falla" sin mandar gente a terreno, y el costo de esa cuadrilla se
  calcula en una servilleta delante del jefe de operaciones.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "satec-warning",
            "titulo": "SATEC: cuatro cosas que no se pueden prometer",
            "tipo": "detalle",
            "html": """
<p class="lead">Estos errores no son tecnicos: son de credibilidad. Un cliente tecnico los detecta y despues
no cree en el resto de la propuesta.</p>

<div class="callout supuesto">
  <b>1. SATEC no tiene PDC.</b> El fabricante no hace concentrador de fasores. Su PMU PRO transmite
  C37.118.2 y se conecta a un PDC de terceros. Escribir "PDC SATEC" o "PDC incluido con el equipo" es un
  error que se paga. En la propuesta va como componente aparte, con tres rutas posibles: PDC de terceros
  suministrado por CONECTA, reutilizar el que el cliente ya opera, o el del Coordinador si hay que reportarle.
  <a href="#f-SATEC">SATEC</a>
</div>

<div class="callout supuesto">
  <b>2. El catalogo no trae precio de lista.</b> No existe tarifa publica. Cotizar SATEC requiere tarifa del
  distribuidor. Los costos que viven en disco son de BOMs de otras marcas y sirven como magnitud, no como
  precio.
</div>

<div class="callout supuesto">
  <b>3. PAS es solo Windows.</b> El software de configuracion no corre en macOS nativo ni en Linux. Si el
  cliente opera en Mac, hay que decirlo antes de vender, no despues.
</div>

<div class="callout supuesto">
  <b>4. La variante 17x se elige por pais, no por gusto.</b> PM175 PRO es EN50160 (Europa) y PM174 PRO es
  IEEE 1159 (America, Chile incluido). Equivocarse no cambia la arquitectura ni la cantidad, pero si la
  variante que se le promete al cliente, y es de lo primero que revisa.
</div>

<div class="callout">
  <b>Y un cuidado de conteo.</b> Los totales de una propuesta se calculan desde las filas, nunca se escriben a
  mano. Si el texto dice "17 equipos" y la tabla lista 6 filas, el documento se contradice a si mismo y el
  cliente lo ve en la primera lectura.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "supcon-mapa",
            "titulo": "SUPCON: el portafolio en cuatro bloques",
            "tipo": "producto",
            "html": """
<p class="lead">SUPCON es el partner de control y automatizacion de planta completa. Es el portafolio mas
grande de CONECTA y el que menos se conoce, porque se confunde con "un DCS chino".</p>

<table class="tabla">
<thead><tr><th>Bloque</th><th>Que resuelve</th><th>Productos</th></tr></thead>
<tbody>
<tr>
<td><b>Control</b></td>
<td>El cerebro del proceso: gobernar la planta</td>
<td>ECS-700 (DCS), TCS-500 (SIS, seguridad funcional)</td>
</tr>
<tr>
<td><b>Instrumentacion</b></td>
<td>Medir el proceso en terreno</td>
<td>Transmisores CXT y CJT, flujometros EMF/LUGB/SF20, nivel radar 80 GHz SL90, temperatura W, detectores DMD/DMC</td>
</tr>
<tr>
<td><b>Actuacion</b></td>
<td>Mover la planta</td>
<td>Valvulas de control (series LN/LM/SN/VN/CN/BN), posicionador CVP2000</td>
</tr>
<tr>
<td><b>Software e IA</b></td>
<td>Convertir el dato en decisiones</td>
<td>supOS (sistema operativo industrial), PRIDE (diagnostico predictivo), APC (control avanzado), TPT (modelo de IA)</td>
</tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-SUPCON">SUPCON</a> — catalogo de producto del fabricante</cite>

<div class="callout">
  <b>Dato de solidez que sirve para abrir puertas.</b> ECS-700 es el DCS numero uno en China, con 19,2% de
  participacion de mercado (dato ARC), CMMI nivel 5, certificaciones CE y G3 anticorrosion, y mas de 30.000
  bases instaladas. <a href="#f-SUPCON-ECS700">SUPCON-ECS700</a>
</div>
<span class="sello s-extraido">EXTRAIDO</span>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "supcon-casos",
            "titulo": "SUPCON: los casos de uso, uno por uno",
            "tipo": "tabla",
            "html": """
<p class="lead">Cada linea es una conversacion real. El equipo es la consecuencia, no el punto de partida.</p>

<table class="tabla casos">
<thead><tr><th>Lo que el cliente dice</th><th>Equipo</th><th>Caso de uso y por que ese</th></tr></thead>
<tbody>

<tr>
<td>"Mi DCS es un Yokogawa viejo y no consigo repuestos"</td>
<td><b>ECS-700</b></td>
<td>Reemplazo de DCS al final de la vida util. SUPCON tiene 60+ casos documentados de desplazamiento, 16 de ellos reemplazando Yokogawa CS3000/CENTUM-VP y 16 reemplazando Honeywell TPS/PKS. Ese historial es el argumento, no la ficha tecnica.</td>
</tr>

<tr>
<td>"Mi SIS tiene que ser SIL 3 o no paso la auditoria"</td>
<td><b>TCS-500</b></td>
<td>Sistema instrumentado de seguridad. No es un DCS con logica de enclavamiento: es un equipo certificado para funcion de seguridad. Mezclarlos es un error que aparece en la auditoria.</td>
</tr>

<tr>
<td>"Necesito que la planta avise antes de que un equipo falle"</td>
<td><b>PRIDE</b></td>
<td>Plataforma de diagnostico predictivo sobre supOS: 31.000+ estrategias de mantenimiento y 11.000+ casos de falla. Cubre valvulas, transmisores, flujometros, equipos rotativos, cabinas y fuga en ductos.</td>
</tr>

<tr>
<td>"Tengo valvulas pegandose y nadie sabe cuales"</td>
<td><b>PRIDE</b> (modulo valvulas)</td>
<td>Deteccion de stiction con cuatro metodos en valvulas inteligentes (estimacion de banda muerta, analisis de desviacion, modelo ML de presion de suministro, comparacion de curva offline) y tres en valvulas no inteligentes. Caso documentado: 2.800+ valvulas y transmisores monitoreados, 38 valvulas con excepcion de 454.</td>
</tr>

<tr>
<td>"Se me paran bombas y compresores sin aviso"</td>
<td><b>PRIDE</b> (equipos rotativos)</td>
<td>Monitoreo de vibracion con 1.566 tipos de falla cubiertos, 24/7. Referencias: CNOOC Huizhou (compresores), Jiangsu Oji Paper (bombas en linea), Hubei Sanning (proteccion de rotativos).</td>
</tr>

<tr>
<td>"Necesito medir presion con 0,035% de exactitud"</td>
<td><b>CXT</b></td>
<td>Transmisor de presion de silicio monocristalino: ±0,035%, rango 100 Pa a 40 MPa, estabilidad de ±0,1% en 10 años, IP67 y diafragma con baño de oro para inhibir la difusion de hidrogeno. Tiene WirelessHART y 5G RedCap como opcion de pedido — no decir que no las tiene.</td>
</tr>

<tr>
<td>"Necesito medir nivel en un silo con polvo"</td>
<td><b>SL90</b></td>
<td>Radar de 80 GHz sin contacto: antena pequena, haz angosto y alta relacion senal/ruido. Es la respuesta donde el ultrasonido falla por polvo o por espuma.</td>
</tr>

<tr>
<td>"Necesito medir caudal y el fluido no conduce"</td>
<td><b>LUGB</b> (vortex)</td>
<td>Vortex mide liquido, vapor y gas con baja perdida de carga. Si el fluido no conduce electricidad, el electromagnetico EMF no sirve — por eso la pregunta correcta es por la conductividad antes de ofrecer un EMF.</td>
</tr>

<tr>
<td>"Tengo una valvula critica y quiero control real, no solo abrir y cerrar"</td>
<td><b>CVP2000</b></td>
<td>Posicionador inteligente, ±0,5% FS, dos hilos 4-20 mA, con diagnostico. Es el accesorio que convierte una valvula en un equipo diagnosticable por PRIDE. Ojo: el CVP2000 es posicionador, no valvula.</td>
</tr>

<tr>
<td>"Quiero conectar la planta a la IA pero todo esta en silos"</td>
<td><b>supOS</b></td>
<td>Sistema operativo industrial: modelo unificado de datos sobre equipos de distintas marcas y generaciones. Es la capa que permite que PRIDE y APC funcionen sobre un DCS que no es SUPCON.</td>
</tr>

<tr>
<td>"Quiero mover la operacion sin cambiar los lazos"</td>
<td><b>APC</b></td>
<td>Control avanzado sobre el DCS existente. Segun el fabricante, 10-30% de reduccion de CAPEX, 3-8% de mejora de produccion y 3-5% de reduccion de energia. Son cifras del proveedor: citarlas como tales.</td>
</tr>

<tr>
<td>"Necesito la sala de control completa, no solo el DCS"</td>
<td><b>Consolas OP085</b></td>
<td>SUPCON tambien hace la sala: consolas de operacion y mobiliario tecnico. Se vende junto con el DCS en proyectos greenfield, y casi nadie lo sabe — es una venta adicional que se pierde por desconocimiento.</td>
</tr>

</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-SUPCON">SUPCON</a> · <a href="#f-SUPCON-ECS700">SUPCON-ECS700</a> · <a href="#f-SUPCON-PRIDE">SUPCON-PRIDE</a> — catalogo y documentacion del fabricante</cite>

<div class="callout supuesto">
  <b>SUPUESTO — el detalle de Chile.</b> Codelco adjudico el contrato marco "Tecnologia y Automatizacion de
  Procesos Plantas-Infraestructura" a un pool cerrado, y SUPCON no esta en el. Los OEM del pool no compran
  producto de un tercero; los integradores locales si son la via de entrada. Antes de invertir tiempo en un
  integrador, preguntar si el marco fija marcas homologadas: si las fija, no puede meter SUPCON aunque quiera.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "comparar",
            "titulo": "Cuando compiten entre si, y cuando no",
            "tipo": "tabla",
            "html": """
<p class="lead">SUPCON, SATEC, NovaTech y Vizimax se solapan menos de lo que parece. Confundirlos hace perder
la venta o, peor, prometer una capacidad que el equipo no tiene.</p>

<table class="tabla">
<thead><tr><th>Necesidad</th><th>El partner correcto</th><th>Por que no el otro</th></tr></thead>
<tbody>
<tr><td>Control de proceso de planta</td><td><b>SUPCON</b> (ECS-700)</td><td>SATEC mide; no gobierna el proceso.</td></tr>
<tr><td>Medicion de potencia y calidad</td><td><b>SATEC</b> (PM180, PM17x) o <b>NovaTech</b> (Bitronics)</td><td>SUPCON no es un fabricante de medicion de facturacion.</td></tr>
<tr><td>PMU para el Coordinador</td><td><b>SATEC</b> (PMU PRO), <b>Vizimax</b> o <b>NovaTech</b></td><td>SUPCON no es la via natural para C37.118.</td></tr>
<tr><td>Retrofit de RTU legacy</td><td><b>NovaTech</b> (Orion I/O)</td><td>SATEC no reemplaza una RTU de subestacion.</td></tr>
<tr><td>Predictivo de equipos de planta</td><td><b>SUPCON</b> (PRIDE)</td><td>SATEC no tiene plataforma de diagnostico de activos.</td></tr>
<tr><td>Conexion controlada de transformador</td><td><b>Vizimax</b> (SynchroTeq)</td><td>Ninguno de los otros tres lo hace.</td></tr>
<tr><td>Medicion DC de BESS</td><td><b>SATEC</b> (PRO + VRM)</td><td>Bitronics es AC de potencia.</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Asignacion comercial propia, consistente con las fuentes de cada partner.</cite>

<div class="callout">
  <b>El dato que zanja la discusion Bitronics vs SATEC.</b> Bitronics gana en confiabilidad declarada
  (MTBF 40 años, garantia 10 años, precision 0,2s). SATEC gana en cobertura: PQ Clase A, PMU, registro de
  fallas y medicion DC, que Bitronics no cubre. No es "cual es mejor": es cual necesita el caso de uso.
  <a href="#f-BITRONICS">BITRONICS</a> · <a href="#f-SATEC">SATEC</a>
</div>
<span class="sello s-extraido">EXTRAIDO</span>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "preguntas-partner",
            "titulo": "Las preguntas que definen que partner entra",
            "tipo": "idea",
            "html": """
<p class="lead">Antes de nombrar una marca, cinco preguntas. Con las respuestas, el portafolio se ordena solo.</p>

<ol class="pasos">
  <li><b>Que tiene que gobernar el sistema?</b> Si gobierna proceso, es SUPCON. Si solo mide, no.</li>
  <li><b>Que tiene que certificar?</b> PQ Clase A apunta a SATEC. Seguridad funcional SIL apunta a SUPCON TCS-500.</li>
  <li><b>Que equipos ya existen?</b> Si hay TC 5A/1A o sensores LPIT, SATEC entra sin transformadores nuevos. Si hay RTU D20, NovaTech.</li>
  <li><b>El dato tiene que viajar con hora?</b> Si la respuesta es si y va al Coordinador, es PMU y PDC, no un medidor.</li>
  <li><b>Quien hace la ingenieria?</b> Si la hace un integrador de un contrato marco con marcas homologadas, verificar antes de proponer.</li>
</ol>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Guion propio de CONECTA.</cite>

<div class="callout">
  <b>El error de novato.</b> Abrir con el portafolio completo de SUPCON en una reunion donde el problema era
  de medicion. El cliente concluye que no lo escuchamos, y la reunion siguiente la gana el competidor.
</div>
""",
        },
    ],
}
