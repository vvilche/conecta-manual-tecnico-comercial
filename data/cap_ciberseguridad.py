# -*- coding: utf-8 -*-
"""Capitulo 5 — Ciberseguridad: que es y que pide el estandar del sistema electrico."""

CAP_CIBER = {
    "id": "ciberseguridad",
    "titulo": "Ciberseguridad",
    "subtitulo": "Que es en un sistema electrico, que exige la ley chilena, y que se puede vender de verdad.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "que-es-ciber",
            "titulo": "Que es ciberseguridad en un sistema electrico",
            "tipo": "idea",
            "html": """
<p class="lead">En una oficina, un incidente de ciberseguridad se paga con datos o con plata. En una
subestacion se paga con <b>consecuencia fisica</b>: un interruptor que se abre cuando no debe, una
proteccion que no dispara, un transformador que se daña. Esa es la diferencia y es lo que hay que
entender antes de vender.</p>

<p>Por eso no se aplican los mismos criterios que en TI. En una red industrial el objetivo principal no es
la confidencialidad: es la <b>disponibilidad</b> y la <b>integridad</b>. Un dato que no llega a tiempo es
un dato inutil, aunque nadie lo haya visto.</p>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Criterio de ingenieria OT, consistente con las fuentes de este capitulo.</cite>

<h4>Las cuatro cosas que se protegen</h4>
<table class="tabla">
<thead><tr><th>Se protege</th><th>Contra que</th><th>Ejemplo en subestacion</th></tr></thead>
<tbody>
<tr><td><b>Acceso</b></td><td>Quien puede entrar a un equipo y con que derechos</td><td>Un tecnico de otro proveedor con clave compartida de la RTU</td></tr>
<tr><td><b>Flujo</b></td><td>Que trafico cruza de una zona a otra</td><td>La red corporativa del cliente conectada directo al bus de proceso</td></tr>
<tr><td><b>Integridad</b></td><td>Que el dato llegue como salio</td><td>Un mando de TRIP falso</td></tr>
<tr><td><b>Registro</b></td><td>Quien hizo que y cuando</td><td>Nadie sabe quien cambio una configuracion de proteccion</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>

<div class="callout">
  <b>La verdad incomoda.</b> Los protocolos industriales historicos no se diseñaron para ser seguros.
  Modbus, por ejemplo, no tiene autenticacion ni cifrado: cualquier equipo que alcance el puerto puede
  leer los registros. Por eso la proteccion no se resuelve en el protocolo: se resuelve en la
  <b>arquitectura</b> (segmentacion, firewalls, control de acceso) y en el <b>equipo</b> (cuando soporta
  autenticacion y registro).
  <a href="#f-MODBUS-V1.1b3">MODBUS-V1.1b3</a> define solo el intercambio de bits y registros; no incluye
  mecanismos de seguridad en el protocolo.
</div>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-MODBUS-V1.1b3">MODBUS-V1.1b3</a> — el spec define el PDU de datos y las funciones; no define autenticacion ni cifrado.</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "ley-chile",
            "titulo": "Que exige la normativa chilena",
            "tipo": "detalle",
            "html": """
<p class="lead">En Chile la referencia es la <b>Ley 21.663, Ley Marco de Ciberseguridad</b>, publicada en
abril de 2024. No es una recomendacion: define quien esta obligado y quien fiscaliza.</p>

<h4>Quien esta dentro del alcance</h4>
<p>La ley aplica a los servicios calificados como esenciales y a los operadores de importancia vital. Son
<b>servicios esenciales</b>, entre otros, los provistos por los organismos del Estado <b>y por el
Coordinador Electrico Nacional</b>, los prestados bajo concesion de servicio publico, y los proveidos por
instituciones privadas que realicen <b>generacion, transmision o distribucion electrica</b>,
telecomunicaciones, agua potable, combustibles, e infraestructura digital.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-LEY21663">LEY21663</a>, Articulo 4 (ambito de aplicacion)</cite>

<div class="callout">
  <b>Traduccion comercial.</b> Practicamente todos los clientes de CONECTA en el sector electrico estan
  dentro del alcance de la ley. Eso cambia la conversacion: la ciberseguridad deja de ser un "seria bueno
  tenerlo" y pasa a ser una obligacion legal del cliente.
</div>

<h4>Los operadores de importancia vital</h4>
<p>La Agencia Nacional de Ciberseguridad (ANCI) califica a los operadores de importancia vital. Los
requisitos son dos: que la provision del servicio <b>dependa de redes y sistemas informaticos</b>, y que su
afectacion, interceptacion, interrupcion o destruccion tenga un <b>impacto significativo</b> en la seguridad
y el orden publico o en la provision continua de servicios esenciales. La calificacion se revisa al menos
cada tres años.</p>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-LEY21663">LEY21663</a>, Articulos 5 y 6</cite>

<div class="callout supuesto">
  <b>SUPUESTO — pregunta de calificacion.</b> No se debe afirmar en una reunion que un cliente "es" o "no
  es" operador de importancia vital: eso lo determina la ANCI. Lo que si se puede preguntar es si ya
  recibio la comunicacion. Si la respuesta es "no se", ese cliente tiene un problema mas grande que el
  proyecto que esta cotizando.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "iec62443",
            "titulo": "El estandar tecnico: IEC 62443",
            "tipo": "detalle",
            "html": """
<p class="lead">La ley dice que hay que proteger. El estandar tecnico dice <b>como</b>. La referencia
internacional para seguridad de sistemas de automatizacion y control industrial es la serie
<b>IEC 62443</b>, porque es la que entiende el mundo OT y no el mundo de oficina.</p>

<h4>Las cuatro ideas que hacen todo el trabajo</h4>
<table class="tabla">
<thead><tr><th>Idea</th><th>Que significa</th><th>Como se ve en un proyecto</th></tr></thead>
<tbody>
<tr><td><b>Zonas y conductos</b></td><td>Agrupar activos con requisitos de seguridad comunes en zonas, y controlar <b>todo</b> camino de comunicacion entre zonas como un conducto</td><td>Bus de proceso, red de subestacion, red corporativa: tres zonas, con firewall entre ellas</td></tr>
<tr><td><b>Nivel de seguridad (SL 1-4)</b></td><td>Cada zona recibe un SL objetivo segun el riesgo que debe soportar: SL1 mal uso casual, hasta SL4 atacante de nivel estado-nacion</td><td>La diferencia entre el SL objetivo y el SL alcanzado es la hoja de ruta de remediacion</td></tr>
<tr><td><b>Siete requerimientos fundacionales</b></td><td>Identificacion y autenticacion, control de uso, integridad del sistema, confidencialidad de datos, flujo de datos restringido, respuesta oportuna a eventos, disponibilidad de recursos</td><td>Cada zona se evalua contra estos siete, no contra una lista suelta</td></tr>
<tr><td><b>Separacion de roles</b></td><td>Dueño del activo, integrador de sistemas y proveedor de producto, cada uno con obligaciones definidas</td><td>CONECTA es integrador: responde por como se integra, no por el firmware del fabricante</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-IEC62443-SEC">IEC62443-SEC</a> — <b>fuente secundaria</b>: guia sobre la serie IEC 62443, no el texto de la norma (que es de pago). Para precision normativa hay que consultar la norma.</cite>

<div class="callout">
  <b>Por que "zonas y conductos" es lo primero.</b> La mayoria de los sistemas industriales tienen la red
  plana: todo ve a todo. La segmentacion es lo que impide que un notebook infectado en la oficina llegue al
  bus de proceso. Si el cliente no tiene segmentado, ese es el hallazgo, y es vendible como proyecto.
</div>

<h4>La separacion de roles, explicada para una propuesta</h4>
<p>Este punto es el que mas problemas evita en el cierre. Cuando un cliente exige ciberseguridad, hay que
dejar escrito <b>quien responde por que</b>:</p>
<ul class="lista">
  <li><b>Proveedor de producto:</b> responde por las capacidades de seguridad del equipo (autenticacion, registro, cifrado si lo soporta).</li>
  <li><b>Integrador (CONECTA):</b> responde por el diseño de zonas, la configuracion de firewalls, el endurecimiento y la puesta en servicio.</li>
  <li><b>Dueño del activo (el cliente):</b> responde por las politicas, las claves, los accesos y el monitoreo continuo.</li>
</ul>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Aplicacion propia de la separacion de roles descrita en IEC62443-SEC. La asignacion concreta se negocia en el contrato.</cite>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "que-pide-sector",
            "titulo": "Que pide el sector electrico en concreto",
            "tipo": "detalle",
            "html": """
<p class="lead">Bajando a lo que un proyecto tiene que entregar, estas son las exigencias que aparecen
efectivamente en los proyectos del sector electrico chileno.</p>

<table class="tabla">
<thead><tr><th>Exigencia</th><th>De donde viene</th><th>Que significa para la propuesta</th></tr></thead>
<tbody>
<tr><td><b>Segmentacion de red</b></td><td>IEC 62443 (zonas y conductos)</td><td>Firewall OT entre red corporativa y red de subestacion. No es opcional si el cliente esta bajo la ley.</td></tr>
<tr><td><b>Control de acceso</b></td><td>IEC 62443 (identificacion y autenticacion)</td><td>Sin claves compartidas, con roles. Los equipos deben soportar autenticacion.</td></tr>
<tr><td><b>Registro y trazabilidad</b></td><td>IEC 62443 (respuesta oportuna a eventos)</td><td>Que quede registro de quien cambio que. Se convierte en requerimiento del equipo.</td></tr>
<tr><td><b>Cumplimiento de estandares de ciberseguridad de la normativa sectorial</b></td><td>Coordinador Electrico, puesta en servicio de PMU</td><td>Se verifica expresamente antes de integrar una PMU: no es un anexo, es requisito de puesta en servicio.</td></tr>
<tr><td><b>Clasificacion y obligaciones legales</b></td><td>Ley 21.663</td><td>El cliente puede tener deberes de reporte de incidentes y de gestion de riesgo.</td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>
<cite><a href="#f-CEN-MMF2026">CEN-MMF2026</a> (pagina 102, verificacion de puesta en servicio: "Cumplimiento de los Estándares de Ciberseguridad requeridos en la normativa sectorial eléctrica") · <a href="#f-IEC62443-SEC">IEC62443-SEC</a> · <a href="#f-LEY21663">LEY21663</a></cite>

<div class="callout">
  <b>El detalle que sirve en una propuesta.</b> En la puesta en servicio de una PMU, el Coordinador exige
  verificar el cumplimiento de los estandares de ciberseguridad de la normativa sectorial. Si la propuesta
  no incluye ese trabajo, el cliente descubre el faltante cuando ya esta en la etapa de integracion.
</div>

<h4>Que se puede vender de ciberseguridad, sin inventar</h4>
<div class="callout supuesto">
  <b>SUPUESTO — oferta realista.</b> Los BOMs historicos de CONECTA no traen equipos de ciberseguridad en
  la planilla de "Equi. Mat. Arr. Sub.": son servicios y estudios (<a href="#f-CONECTA-BOM">CONECTA-BOM</a>).
  Por eso la ciberseguridad se vende como <b>servicio de ingenieria</b>: levantamiento, diseño de zonas,
  configuracion de firewalls, endurecimiento, y acompañamiento en puesta en servicio. Cuando hay hardware,
  entra como firewall OT o como capacidad del propio equipo (Orion soporta NERC CIP, por ejemplo).
</div>
""",
        },
    ],
}
