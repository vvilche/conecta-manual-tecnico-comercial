# -*- coding: utf-8 -*-
"""Capitulo 7 — Metodologia comercial: la Escalera, la Mina de Oro, las objeciones."""

CAP_METODOLOGIA = {
    "id": "metodologia",
    "titulo": "Metodologia comercial",
    "subtitulo": "Como se califica, como se conversa y que se responde. La parte que no es tecnica y decide la venta.",
    "bloques": [

        # ------------------------------------------------------------------
        {
            "id": "escalera",
            "titulo": "La Escalera al Exito: cuatro escalones, sin saltarse ninguno",
            "tipo": "idea",
            "html": """
<p class="lead">La metodologia de CONECTA ordena el trabajo comercial en cuatro escalones. La regla de
hierro es una sola: <b>no se sube un escalon si el anterior no esta cerrado</b>. En particular, si la
capacidad de respuesta (R) no esta al 100%, esta prohibido pasar al Escalon 2.</p>

<table class="tabla">
<thead><tr><th>Escalon</th><th>Formula</th><th>Pregunta</th></tr></thead>
<tbody>
<tr><td><b>1</b></td><td>P x M x R</td><td>Podemos cumplir?</td></tr>
<tr><td><b>2</b></td><td>N x Pv x Map</td><td>Donde esta el dinero?</td></tr>
<tr><td><b>3</b></td><td>F x Mt x E</td><td>Donde ponemos el foco?</td></tr>
<tr><td><b>4</b></td><td>Pv x Mt x Pc</td><td>Cuál es el plan?</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Metodologia de ventas de CONECTA (framework de trabajo, no una norma). Detalle en la skill escalera-al-exito.</cite>

<h4>Escalon 1 — P x M x R</h4>
<ul class="lista">
  <li><b>P (Producto):</b> que vendemos exactamente. Vector de diferenciacion, defendibilidad, el 10% de innovacion.</li>
  <li><b>M (Mercado):</b> quien compra. Es obligatorio o discrecional. El mercado crece.</li>
  <li><b>R (Respuesta):</b> tenemos HW y SW, equipo certificado, proveedor competitivo, tiempo de respuesta. Semaforo: verde subir, amarillo subir con condiciones, <b>rojo no subir</b>.</li>
</ul>
<div class="callout">
  <b>Los tres caminos cuando R falla.</b> A) cambiar el componente debil · B) redefinir el producto para
  un nicho donde si alcanza · C) diferenciar por servicio, no por hardware. Este ultimo es el mas usado en
  CONECTA, porque permite vender con el equipo que hay.
</div>

<h4>Escalon 2 — N x Pv x Map: donde esta el dinero</h4>
<p>Numero de clientes potenciales, potencial de venta por nicho, y mapeo de esfuerzo. El resultado es una
matriz de priorizacion: el foco esta en alto potencial con bajo esfuerzo.</p>
<table class="tabla">
<thead><tr><th></th><th>Alto Pv</th><th>Medio Pv</th><th>Bajo Pv</th></tr></thead>
<tbody>
<tr><td><b>Bajo esfuerzo</b></td><td>Foco primario</td><td>Volumen</td><td>Mantenimiento</td></tr>
<tr><td><b>Medio esfuerzo</b></td><td>Foco primario</td><td>Evaluar</td><td>Descartar</td></tr>
<tr><td><b>Alto esfuerzo</b></td><td>Evaluar ROI</td><td>Solo estrategico</td><td>Descartar</td></tr>
</tbody>
</table>

<h4>Escalon 3 — F x Mt x E: donde ponemos el foco</h4>
<p><b>F</b> es el foco (producto core, servicio incluido, recurrente, upsell). <b>Mt</b> es el Trivector:
las tres ventajas unicas que ningun competidor puede copiar rapido, y que deben aparecer tanto en las bases
tecnicas como en el resumen ejecutivo. <b>E</b> es la ecuacion de posicionamiento: precio x valor x
posicionamiento.</p>

<h4>Escalon 4 — Pv x Mt x Pc: el plan</h4>
<p>Plan de cuenta en cinco fases: <b>Inteligencia, Contacto, Demo, Propuesta, Expansion</b>. Sin plan de
cuenta no hay pipeline real.</p>

<div class="callout">
  <b>La regla del TAE.</b> Si no esta en la tabla de acciones estrategicas, no existe. Y una cuenta sin
  Campeon interno es una cuenta huerfana: muere en el primer recorte de presupuesto.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "mina-de-oro",
            "titulo": "La Mina de Oro: vender al miedo, no al dolor",
            "tipo": "idea",
            "html": """
<p class="lead">El gerente de mantenimiento no compra "mejorar la eficiencia". Teme que una falla pare la
planta y que lo despidan. Ese es el dolor oculto, y es el que decide.</p>

<h4>Antes de la reunion, cinco verificaciones</h4>
<ol class="pasos">
  <li>Quien es el comprador: nombre, cargo, antiguedad.</li>
  <li>Que paso en esa planta en los ultimos doce meses.</li>
  <li>Quien es su jefe y que le pide.</li>
  <li>Que pasaria si esta persona falla en su trabajo.</li>
  <li>Hay un competidor que ya los visito.</li>
</ol>

<h4>Las preguntas que abren la conversacion</h4>
<p><b>Para gerente de planta:</b></p>
<ul class="lista">
  <li>Cuál fue el peor dia en esta planta en el ultimo año.</li>
  <li>Si un equipo critico falla un viernes a las 8 de la noche, quien recibe la llamada.</li>
  <li>Que KPI le quita el sueño.</li>
  <li>Cuanto cuesta una hora de parada no planificada.</li>
</ul>
<p><b>Para gerente de mantenimiento:</b></p>
<ul class="lista">
  <li>Cuál es el equipo que mas veces han reparado este año.</li>
  <li>Se han quedado sin repuesto critico en el peor momento.</li>
  <li>Como saben que un equipo va a fallar, o se enteran cuando ya fallo.</li>
  <li>Si tuviera que defender su presupuesto mañana, que dato le falta.</li>
</ul>
<p><b>Para innovacion o TI:</b></p>
<ul class="lista">
  <li>Que dato de la planta le llega tarde.</li>
  <li>Si pudiera ver una sola cosa en tiempo real que hoy no ve, cual seria.</li>
  <li>Hay alguien que se resiste a digitalizar, y por que.</li>
  <li>Que proyecto de digitalizacion no salio como esperaban.</li>
</ul>
<p><b>Para CFO o finanzas:</b></p>
<ul class="lista">
  <li>Como evaluan el retorno de una inversion en tecnologia.</li>
  <li>Que proveedor actual les gustaria tener de respaldo.</li>
  <li>Si este proyecto sale mal, quien asume el costo politico interno.</li>
</ul>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Guion de ventas de CONECTA. No es una fuente externa.</cite>

<h4>Las señales de que se toco la Mina de Oro</h4>
<p>Cuando el cliente dice alguna de estas frases, <b>hay que dejar de vender</b> y escuchar:</p>
<ul class="lista">
  <li>"Si esto falla, me cortan la cabeza."</li>
  <li>"No puedo dormir pensando en eso."</li>
  <li>"Ya intentamos arreglarlo y no funciono."</li>
  <li>"Mi jefe me pregunta todas las semanas por este numero."</li>
  <li>"Prefiero no pensar en lo que costaria que esto salga mal."</li>
</ul>

<div class="callout">
  <b>Como se conecta con lo tecnico.</b> La estampa de tiempo y la sincronizacion son la respuesta tecnica
  a "no se que paso primero". Ese es el puente entre el capitulo Protocolos y este. Cuando el cliente dice
  "cuando tenemos un evento, discutimos dos dias que paso", la respuesta ya no es precio: es trazabilidad.
</div>
""",
        },

        # ------------------------------------------------------------------
        {
            "id": "objeciones",
            "titulo": "Objeciones: que responder sin inventar",
            "tipo": "tabla",
            "html": """
<p class="lead">Cada objecion tiene un ancla (la pregunta que la reencuadra), un dato y un rebote. La regla
de oro: <b>atacar el contenido con hechos, proteger el contexto con respeto</b>.</p>

<table class="tabla">
<thead><tr><th>Objecion</th><th>Ancla</th><th>Rebote</th></tr></thead>
<tbody>
<tr><td>"Es muy caro"</td><td>"Comparado con que referencia?"</td><td>"Y si el proyecto se paga solo en menos de doce meses?"</td></tr>
<tr><td>"Quien mas lo usa en Chile"</td><td>Nombrar referencias reales y verificables</td><td>"En su rubro serian pioneros. Ventaja o riesgo?"</td></tr>
<tr><td>"Ya tengo proveedor"</td><td>"No venimos a reemplazar. Agregamos inteligencia."</td><td>"Que es lo que su proveedor actual no les esta dando?"</td></tr>
<tr><td>"Mandame info por correo"</td><td>"Prefiero mostrarte en 20 minutos. Jueves?"</td><td>"Para enviarte algo util: que te preocupa mas de tu operacion hoy?"</td></tr>
<tr><td>"Sin presupuesto este año"</td><td>"El proyecto se cae por CAPEX o por prioridad?"</td><td>"Si se paga solo en menos de un año, cambia la conversacion?"</td></tr>
<tr><td>"Y si no funciona"</td><td>"Por eso acotamos el alcance a una fase verificable."</td><td>"Que necesitaria ver en 30 dias para sentirse seguro?"</td></tr>
<tr><td>"No tengo el dato tecnico"</td><td>"Entonces el primer entregable es levantarlo. Se cotiza."</td><td>"Quien en su equipo puede confirmar protocolos y reloj?"</td></tr>
</tbody>
</table>
<span class="sello s-supuesto">SUPUESTO</span>
<cite>Matriz de objeciones de CONECTA. Detalle por cliente en la skill conecta-objeciones.</cite>

<div class="callout">
  <b>Prohibido.</b> Ofrecer piloto sin costo, demo gratuita o prueba sin compromiso. Si el cliente pide
  probar, la respuesta es un <b>alcance acotado cotizado</b>, no un regalo. Regalar la prueba destruye el
  precio del proyecto completo.
</div>

<h4>Datos que se pueden citar con fuente</h4>
<table class="tabla">
<thead><tr><th>Si el cliente pregunta por...</th><th>Lo que se puede decir (con fuente)</th></tr></thead>
<tbody>
<tr><td>Precision de medicion Bitronics</td><td>0,2s, calibrada individualmente, MTBF 40 años, garantia 10 años <a href="#f-BITRONICS">[BITRONICS]</a></td></tr>
<tr><td>Precision de reloj</td><td>Kronos: 60 ns (99%), IRIG-B con extensiones C37.118, perfiles PTP <a href="#f-KRONOS">[KRONOS]</a></td></tr>
<tr><td>Retrofit sin recablear</td><td>Tarjetas adaptadoras para D20, SNW, Telegyr, Telvent, ACS; mismo espacio 3RU <a href="#f-ORION-RETROFIT">[ORION-RETROFIT]</a></td></tr>
<tr><td>Que exige el Coordinador a una PMU</td><td>Clase M, 50 muestras/s, 1 µs, IRIG-B, 8 horas de respaldo, 120 kbps <a href="#f-CEN-MMF2026">[CEN-MMF2026]</a></td></tr>
</tbody>
</table>
<span class="sello s-extraido">EXTRAIDO</span>

<div class="callout supuesto">
  <b>SUPUESTO — lo que NO se dice.</b> No afirmar que un competidor es "peor" sin evidencia. No prometer
  plazos que el fabricante no confirmo. No dar precios de memoria. Y no afirmar que un cliente esta o no
  obligado por la Ley 21.663: eso lo determina la ANCI.
</div>
""",
        },
    ],
}
