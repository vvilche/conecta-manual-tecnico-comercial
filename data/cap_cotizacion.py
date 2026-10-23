# -*- coding: utf-8 -*-
"""Capitulo 6 — Como armar una cotizacion. Incluye ejemplo end-to-end con cifras ficticias."""

CAP_COTIZACION = {
    "id": "cotizacion",
    "titulo": "Armar una cotizacion",
    "subtitulo": "Los diez elementos que toda cotizacion debe llevar, en orden, con un ejemplo completo.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "los-diez",
            "titulo": "Los diez elementos, y por que cada uno existe",
            "tipo": "tabla",
            "html": """
<p class="lead">Una cotizacion no es un precio. Es un documento que define <b>que se vende, hasta donde, y
en que condiciones</b>. Si falta un elemento, alguien va a discutir despues. Estos son los diez, en el
orden en que aparecen.</p>

<table class="tabla">
<thead><tr><th>#</th><th>Elemento</th><th>Que debe contener</th><th>Que evita</th></tr></thead>
<tbody>
<tr><td>1</td><td><b>Resumen ejecutivo</b></td><td>Que problema resuelve, que se propone, cuanto cuesta y en cuanto tiempo. Media pagina, sin jerga.</td><td>Que el que firma no entienda la propuesta y la mande a "revisar despues"</td></tr>
<tr><td>2</td><td><b>Alcance</b></td><td>Que esta incluido, con limite claro: cantidad de equipos, cantidad de puntos, cantidad de subestaciones.</td><td>El "yo creia que estaba incluido"</td></tr>
<tr><td>3</td><td><b>Arquitectura</b></td><td>Diagrama con equipos, protocolos por enlace, sincronizacion y frontera de responsabilidad.</td><td>Prometer una integracion que el equipo no soporta</td></tr>
<tr><td>4</td><td><b>Suministros</b></td><td>Lista de equipos, uno por linea, con modelo y cantidad. Sin precio unitario si el cliente no lo pidio.</td><td>Que discutan el margen de un tornillo en vez del proyecto</td></tr>
<tr><td>5</td><td><b>Servicios</b></td><td>Ingenieria, programacion, montaje, puesta en servicio, capacitacion. Con horas o con entregables.</td><td>Regalar el trabajo que es donde esta el margen</td></tr>
<tr><td>6</td><td><b>Plazos de entrega</b></td><td>Plazo desde la OC, y plazos por hito. Distinguir entrega de suministro y termino de servicio.</td><td>Confundir "llega el equipo" con "queda operativo"</td></tr>
<tr><td>7</td><td><b>Lugar de entrega</b></td><td>Direccion, bodega o sitio. Quien recibe y con que documento.</td><td>Equipos perdidos en una bodega del cliente</td></tr>
<tr><td>8</td><td><b>Precio</b></td><td>Total, moneda, si incluye impuestos, y validez de la oferta.</td><td>Que la oferta "sirva" un año despues con otro tipo de cambio</td></tr>
<tr><td>9</td><td><b>Hitos de pago</b></td><td>Porcentajes y contra que documento se factura cada uno.</td><td>Financiar el proyecto con caja propia</td></tr>
<tr><td>10</td><td><b>Consideraciones y exclusiones</b></td><td>Que asume CONECTA y que hace el cliente. Todo lo que NO esta incluido.</td><td>El conflicto en terreno cuando falta el andamio</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Estructura propia de CONECTA, coherente con la plantilla de Valorizacion (Resumen, Ficha, Calculo HH, Equi. Mat. Arr. Sub., Expenses). Ver <a href="#f-CONECTA-BOM">CONECTA-BOM</a>.</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "resumen-ejecutivo",
            "titulo": "1. Resumen ejecutivo: lo que se lee y lo que se firma",
            "tipo": "detalle",
            "html": """
<p class="lead">Este es el unico elemento que el gerente va a leer completo. Si no convence en media
pagina, el resto del documento no se lee.</p>

<h4>Estructura en cuatro parrafos cortos</h4>
<ol class="pasos">
  <li><b>La situacion</b> — en una frase, el hecho tecnico o regulatorio que crea la necesidad. Con dato y fuente cuando exista.</li>
  <li><b>Lo que se propone</b> — en una frase, la solucion. Sin siglas sin explicar.</li>
  <li><b>Lo que el cliente obtiene</b> — el resultado verificable, no la caracteristica del equipo.</li>
  <li><b>Lo que cuesta y cuando</b> — monto, plazo y condicion de pago principal.</li>
</ol>
<span class="sello s-supuesto">SUPUESTO</span>

<div class="callout">
  <b>El error tipico del resumen ejecutivo.</b> Convertirlo en una lista de productos. Si el resumen
  empieza con "el Orion LX+ es una RTU...", el gerente dejo de leer. La RTU va en Suministros; el resumen
  habla de lo que le pasa al cliente.
</div>

<h4>Frases que no se usan</h4>
<p>Por definicion de CONECTA, no se usan estas expresiones en documentos comerciales:</p>
<ul class="lista">
  <li>"piloto gratuito", "sin costo", "demo gratuita", "sin compromiso"</li>
  <li>"revolucionario", "líder mundial", "unico en Chile", "la mejor solucion"</li>
  <li>"Calcular ROI" como boton o llamado a la accion</li>
  <li>Promesas de plazo que no estan respaldadas por el fabricante</li>
</ul>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Reglas de comunicacion de CONECTA. Se registran aqui porque son parte de la cotizacion, no solo del correo.</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "alcance-exclusiones",
            "titulo": "2 y 10. Alcance y exclusiones: las dos caras del mismo limite",
            "tipo": "detalle",
            "html": """
<p class="lead">El alcance y las exclusiones son el mismo documento visto de dos lados. Un alcance sin
exclusiones es una promesa abierta, y una promesa abierta se cobra en el margen.</p>

<h4>Como escribir el alcance para que no crezca</h4>
<p>Todo alcance se escribe con <b>unidades contables</b>. "Implementacion de SCADA" no es un alcance.
"Implementacion de SCADA para 1 subestacion, con 1.200 puntos, 3 pantallas y 1 base de eventos" si lo es.</p>

<table class="tabla">
<thead><tr><th>Dimensionar por</th><th>Porque</th><th>Ejemplo</th></tr></thead>
<tbody>
<tr><td>Cantidad de sitios</td><td>Cada sitio tiene traslado, montaje y puesta en servicio propios</td><td>"1 subestacion" vs "3 subestaciones"</td></tr>
<tr><td>Cantidad de puntos / señales</td><td>Es lo que consume programacion y bases de datos</td><td>"1.200 puntos DNP3"</td></tr>
<tr><td>Cantidad de equipos</td><td>Define el suministro y la importacion</td><td>"2 PMU, 1 PDC local"</td></tr>
<tr><td>Iteraciones de ingenieria</td><td>Cada revision del cliente son horas</td><td>"2 revisiones de ingenieria de detalle; adicionales se cotizan"</td></tr>
<tr><td>Dias de terreno</td><td>El montaje y la puesta en servicio se cobran por dia-persona</td><td>"5 dias de puesta en servicio, 2 especialistas"</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>

<h4>Las exclusiones que nunca pueden faltar</h4>
<div class="callout">
  <b>Checklist de exclusiones obligatorias.</b> Estas se repiten en todos los proyectos de CONECTA y
  olvidarlas es la causa mas comun de perdida de margen:
  <ul class="lista" style="margin-top:8px">
    <li><b>Obras civiles</b> — sala, fundaciones, canalizaciones, perforaciones.</li>
    <li><b>Cableado de campo</b> — tendido de cables entre equipos y tablero, cuando no esta en el alcance.</li>
    <li><b>Andamios, izaje y acceso</b> — si el equipo pesa o va en altura.</li>
    <li><b>Suministro electrico</b> — la alimentacion desde la red segura es del cliente salvo indicacion contraria.</li>
    <li><b>Configuracion de la red del cliente</b> — VLANs, firewall corporativo, apertura de puertos.</li>
    <li><b>Licencias del cliente</b> — lo que ya tiene y lo que debe comprar. La licencia PDC Local es adicional a la corporativa.</li>
    <li><b>Datos de entrada</b> — listado de puntos, planos, hojas de datos. Si el cliente no los entrega, se detiene el plazo.</li>
    <li><b>Aprobaciones de terceros</b> — permisos de la empresa dueña del PDC Local, validaciones del Coordinador.</li>
  </ul>
</div>
<span class="sello s-extraido">EXTRAIDO</span> (licencia adicional del PDC)
<cite><a href="#f-CEN-MMF2026">CEN-MMF2026</a>, pagina 103: "Costos asociados a la integración de los nuevos puntos, incluyendo licencia de integración al PDC Local (adicional a la licencia al PDC corporativo)"</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "servicios-precio",
            "titulo": "5, 8 y 9. Servicios, precio e hitos de pago",
            "tipo": "detalle",
            "html": """
<p class="lead">El suministro de equipos tiene poco margen y mucha competencia. Los servicios son donde
CONECTA aporta y donde se defiende el precio. Por eso se listan y se valorizan por separado.</p>

<h4>Los servicios que siempre hay que nombrar</h4>
<table class="tabla">
<thead><tr><th>Servicio</th><th>Que entrega</th><th>Como se dimensiona</th></tr></thead>
<tbody>
<tr><td><b>Ingenieria de detalle</b></td><td>Arquitectura, planos, listado de puntos, hojas de datos</td><td>Horas por documento, con numero de revisiones</td></tr>
<tr><td><b>Programacion y configuracion</b></td><td>RTU, HMI, base de datos, logica</td><td>Horas por punto o por equipo</td></tr>
<tr><td><b>Montaje y supervisión</b></td><td>Instalacion en terreno</td><td>Dias-persona por sitio</td></tr>
<tr><td><b>Puesta en servicio</b></td><td>Pruebas SAT, integracion, documentacion de cierre</td><td>Dias-persona, incluye traslados</td></tr>
<tr><td><b>Capacitacion</b></td><td>Transferencia al equipo del cliente</td><td>Horas o sesiones</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>

<h4>Precio: lo que no puede faltar</h4>
<ul class="lista">
  <li><b>Moneda</b> y si esta afecto a variacion. Si el equipo es importado, el precio no es fijo por dos años.</li>
  <li><b>Impuestos</b>: decir explicitamente si el monto es neto o incluye IVA.</li>
  <li><b>Validez de la oferta</b> con fecha de caducidad concreta.</li>
  <li><b>Si el precio es firme o estimado</b>. Un estimado presentado como firme es un problema futuro.</li>
</ul>
<span class="sello s-supuesto">SUPUESTO</span>

<div class="callout">
  <b>Regla dura.</b> Nunca poner un precio en un manual, en una ficha de producto ni en un catalogo. El
  precio sale del cotizador, con la composicion y el margen que corresponda. Un precio de memoria es la
  forma mas rapida de vender bajo el costo.
</div>

<h4>Hitos de pago: como se protege el flujo</h4>
<p>Un hito de pago no es solo un porcentaje: es un <b>documento contra el que se factura</b>. Si no se puede
nombrar el documento, el hito no existe.</p>
<table class="tabla">
<thead><tr><th>Hito</th><th>Contra que se factura</th></tr></thead>
<tbody>
<tr><td>Anticipo</td><td>Orden de compra aceptada y, si aplica, boleta de garantia</td></tr>
<tr><td>Hito de ingenieria</td><td>Entrega y aprobacion del paquete de ingenieria de detalle</td></tr>
<tr><td>Hito de suministro</td><td>Equipos entregados en el lugar acordado, con acta de recepcion</td></tr>
<tr><td>Hito de puesta en servicio</td><td>Protocolo de pruebas firmado y sistema operativo</td></tr>
<tr><td>Saldo / garantia</td><td>Termino del periodo de garantia o entrega de documentacion final</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "ejemplo",
            "titulo": "Ejemplo completo, de punta a punta",
            "tipo": "ejemplo",
            "html": """
<div class="callout ejemplo-aviso">
  <b>EJEMPLO DIDACTICO — TODAS LAS CIFRAS SON FICTICIAS.</b> Este ejemplo no es una oferta, no refleja
  costos reales de CONECTA ni precios de proveedor. Sirve para ver la <b>forma</b> del documento. Cualquier
  precio real sale del cotizador de CONECTA.
</div>

<p class="lead">Caso: un parque solar en operacion tiene que instalar PMU porque su capacidad supera el
umbral que fija el Coordinador. El cliente no tiene reloj GPS en la subestacion.</p>

<h4>1. Resumen ejecutivo</h4>
<div class="doc">
  <p>El Coordinador Electrico exige un punto de monitoreo fasorial en las instalaciones de generacion con
  potencia instalada igual o superior a 9 MW. El parque no cuenta hoy con medicion fasorial ni con una base
  de tiempo sincronizada que cumpla la precision requerida, por lo que no puede integrarse al Modulo de
  Medicion Fasorial en las condiciones que la normativa exige.</p>
  <p>Se propone el suministro e instalacion de una unidad de medicion fasorial sincronizada, junto con el
  reloj GPS y la integracion al concentrador, dejando el punto verificado y documentado para su puesta en
  servicio.</p>
  <p>Al termino, el parque cuenta con un punto de monitoreo fasorial operativo, con estampa de tiempo
  sincronizada a 1 µs, integrado a su PDC local y con la documentacion de puesta en servicio exigida.</p>
  <p>Plazo estimado de 14 semanas desde la orden de compra. El detalle economico y los hitos de pago se
  presentan en la seccion 8.</p>
</div>

<h4>2. Alcance</h4>
<div class="doc">
  <ul class="lista">
    <li>1 punto de monitoreo fasorial en la subestacion del parque, en el punto de control del PPC.</li>
    <li>1 unidad PMU clase M conforme IEEE 60255-118-1-2018, tasa de 50 muestras por segundo.</li>
    <li>1 reloj GPS con salida IRIG-B no modulada y capacidad PTP.</li>
    <li>1 gabinete de montaje en rack con borneras, protecciones y etiquetado.</li>
    <li>Integracion de la PMU al PDC local del cliente y verificacion de entrega al PDC corporativo.</li>
    <li>Configuracion de la PMU, pruebas de laboratorio y pruebas en terreno (SAT).</li>
    <li>Documentacion de puesta en servicio: planos de conexion, hojas de datos, ajustes y protocolo de pruebas.</li>
    <li>Capacitacion de 1 sesion de 4 horas al equipo de operacion.</li>
  </ul>
</div>

<h4>3. Arquitectura</h4>
<div class="doc">
  <p>El trazado de la solucion, con los elementos obligatorios del capitulo Arquitectura:</p>
  <pre class="diagrama">
  TTCC / TTPP (nucleos de medida)
        |
        v
  +-------------+   AC analogica    +----------------+
  | Bornes SE   |------------------>|  PMU (M-class) |
  +-------------+                   +--------+-------+
                                             |  C37.118
        +----------------+                   v
        |  Reloj GPS     |--IRIG-B-->  +-----------+
        |  (IRIG-B + PTP)|             |   Red     |
        +----------------+             |  61850-3  |
                                       +-----+-----+
                                             | >= 120 kbps
                                             v
                                     +---------------+
                                     |  PDC Local    |
                                     |  del cliente  |
                                     +-------+-------+
                                             |
                                             v
                                   PDC Corporativo CEN
  </pre>
  <p><b>Sincronizacion:</b> reloj GPS con salida IRIG-B no modulada hacia la PMU, con precision dentro de
  1 µs. <b>Respaldo:</b> PMU y comunicaciones alimentadas desde la red segura de la subestacion, con
  autonomia minima de 8 horas. <b>Redundancia:</b> enlace secundario al PDC local segun lo exija la
  arquitectura vigente del cliente.</p>
  <p><b>Frontera de responsabilidad:</b> CONECTA entrega hasta el puerto del PDC local del cliente,
  incluyendo la configuracion de la PMU. La configuracion del PDC local y su enlace al PDC corporativo son
  responsabilidad del cliente, con acompañamiento de CONECTA.</p>
</div>

<h4>4. Suministros</h4>
<div class="doc">
  <table class="tabla">
  <thead><tr><th>Item</th><th>Descripcion</th><th>Cant.</th></tr></thead>
  <tbody>
  <tr><td>1</td><td>Unidad de medicion fasorial clase M, IEEE 60255-118-1-2018, con entrada de tiempo IRIG-B</td><td>1</td></tr>
  <tr><td>2</td><td>Reloj satelital GPS con salida IRIG-B no modulada y soporte PTP, redundancia de alimentacion</td><td>1</td></tr>
  <tr><td>3</td><td>Antena GPS, cable y kit de montaje</td><td>1</td></tr>
  <tr><td>4</td><td>Gabinete rack con borneras, protecciones y etiquetado</td><td>1</td></tr>
  <tr><td>5</td><td>Switch industrial endurecido IEC 61850-3 para la red de la subestacion</td><td>1</td></tr>
  <tr><td>6</td><td>Fuente de alimentacion redundante para el conjunto</td><td>1</td></tr>
  </tbody>
  </table>
</div>

<h4>5. Servicios</h4>
<div class="doc">
  <table class="tabla">
  <thead><tr><th>Servicio</th><th>Entregable</th><th>Cantidad</th></tr></thead>
  <tbody>
  <tr><td>Ingenieria de detalle</td><td>Arquitectura, planos de conexion, listado de puntos, hojas de datos</td><td>2 revisiones incluidas</td></tr>
  <tr><td>Configuracion de PMU</td><td>Equipo configurado y respaldado</td><td>1 punto</td></tr>
  <tr><td>Pruebas de laboratorio</td><td>Informe de verificacion de medidas</td><td>1 juego</td></tr>
  <tr><td>Montaje y supervisión</td><td>Equipo instalado en gabinete y en sala</td><td>3 dias-persona</td></tr>
  <tr><td>Puesta en servicio (SAT)</td><td>Protocolo de pruebas firmado</td><td>3 dias-persona, 2 especialistas</td></tr>
  <tr><td>Integracion al PDC local</td><td>Datos visibles en el PDC del cliente</td><td>2 dias-persona</td></tr>
  <tr><td>Capacitacion</td><td>Sesion de transferencia</td><td>1 sesion de 4 horas</td></tr>
  </tbody>
  </table>
</div>

<h4>6. Plazos de entrega</h4>
<div class="doc">
  <ul class="lista">
    <li>Ingenieria de detalle: 4 semanas desde la OC.</li>
    <li>Suministro de equipos: 10 semanas desde la aprobacion de la ingenieria.</li>
    <li>Montaje: 1 semana desde la recepcion en sitio.</li>
    <li>Puesta en servicio: 1 semana desde el termino del montaje.</li>
    <li><b>Plazo total estimado: 14 semanas</b> desde la OC, sujeto a la entrega de datos de entrada por el cliente.</li>
  </ul>
</div>

<h4>7. Lugar de entrega</h4>
<div class="doc">
  <ul class="lista">
    <li>Equipos: subestacion del parque, direccion a confirmar, en horario coordinado con el cliente.</li>
    <li>Recepcion: contraparte tecnica designada por el cliente, con acta de recepcion y verificacion de embalaje.</li>
    <li>Documentacion digital: por correo al responsable designado.</li>
  </ul>
</div>

<h4>8. Precio</h4>
<div class="doc">
  <table class="tabla">
  <thead><tr><th>Concepto</th><th>Monto (USD, ficticio)</th></tr></thead>
  <tbody>
  <tr><td>Suministros</td><td>48.000</td></tr>
  <tr><td>Servicios de ingenieria y puesta en servicio</td><td>26.000</td></tr>
  <tr><td><b>Total neto</b></td><td><b>74.000</b></td></tr>
  </tbody>
  </table>
  <p>Monto neto, no incluye IVA. Moneda USD. Oferta valida por 30 dias desde la fecha de emision. Precio
  sujeto a variacion de tipo de cambio sobre el componente importado si la OC se emite despues de la
  validez.</p>
</div>

<h4>9. Hitos de pago</h4>
<div class="doc">
  <table class="tabla">
  <thead><tr><th>Hito</th><th>%</th><th>Contra</th></tr></thead>
  <tbody>
  <tr><td>Anticipo</td><td>30%</td><td>Orden de compra aceptada</td></tr>
  <tr><td>Ingenieria</td><td>20%</td><td>Aprobacion del paquete de ingenieria de detalle</td></tr>
  <tr><td>Suministro</td><td>30%</td><td>Acta de recepcion de equipos en sitio</td></tr>
  <tr><td>Puesta en servicio</td><td>20%</td><td>Protocolo de pruebas firmado</td></tr>
  </tbody>
  </table>
</div>

<h4>10. Consideraciones y exclusiones</h4>
<div class="doc">
  <p><b>Asume CONECTA:</b></p>
  <ul class="lista">
    <li>Dimensionamiento del punto de monitoreo y de la base de tiempo.</li>
    <li>Configuracion de la PMU y verificacion de entrega al PDC local del cliente.</li>
    <li>Documentacion de puesta en servicio de lo suministrado.</li>
    <li>Traslados y estadia del personal segun los dias-persona indicados.</li>
  </ul>
  <p><b>Asume el cliente:</b></p>
  <ul class="lista">
    <li>Punto de conexion a la red segura de la subestacion, con disponibilidad durante los trabajos.</li>
    <li>Acceso a la subestacion, permisos de trabajo y sala para el personal.</li>
    <li>Entrega del listado de puntos, planos de la subestacion y hojas de datos de los TTCC y TTPP al inicio.</li>
    <li>Licencia del PDC local y su enlace al PDC corporativo del Coordinador.</li>
    <li>Gestion y aprobacion ante el Coordinador de la puesta en servicio del punto de monitoreo.</li>
  </ul>
  <p><b>No incluido:</b></p>
  <ul class="lista">
    <li>Obras civiles, fundaciones, canalizaciones y perforaciones.</li>
    <li>Tendido de cables de fuerza o de señal desde los TTCC y TTPP hasta el gabinete.</li>
    <li>Andamios, izaje o trabajos en altura.</li>
    <li>Configuracion de la red corporativa del cliente (VLANs, firewall, apertura de puertos).</li>
    <li>Licencia del PDC corporativo y cualquier licencia no listada en Suministros.</li>
    <li>Estudios electricos, de coordinacion de protecciones o de modelacion.</li>
    <li>Revisiones de ingenieria adicionales a las dos incluidas.</li>
  </ul>
</div>

<div class="callout">
  <b>Por que este ejemplo sirve.</b> Cada seccion responde una pregunta que el cliente va a hacer, en el
  orden en que la va a hacer. Y las exclusiones no estan escondidas al final en letra chica: estan
  nombradas, porque cada una es una conversacion que se adelanta.
</div>
""",
        },
    ],
}
