# -*- coding: utf-8 -*-
"""Plantilla HTML del manual. Una sola vista: navegacion lateral por capas, buscador, autoevaluacion."""

CSS = """
:root{
  --bg:#0e1116; --bg2:#151a21; --bg3:#1c232c; --line:#2a323d;
  --txt:#e6eaf0; --txt2:#a8b3c1; --txt3:#6d7a8a;
  --acc:#38bdf8; --acc2:#0ea5e9;
  --medido:#22c55e; --extraido:#38bdf8; --supuesto:#f59e0b; --sec:#a855f7;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,system-ui,sans-serif;
  --mono:"SF Mono",ui-monospace,Menlo,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--txt);font-family:var(--sans);font-size:16px;line-height:1.65;-webkit-font-smoothing:antialiased}
.layout{display:flex;min-height:100vh}

/* ---------- SIDEBAR ---------- */
aside{width:300px;flex:0 0 300px;background:var(--bg2);border-right:1px solid var(--line);
  position:sticky;top:0;height:100vh;overflow-y:auto;padding:22px 0 40px}
.brand{padding:0 22px 18px;border-bottom:1px solid var(--line);margin-bottom:14px}
.brand h1{font-size:15px;letter-spacing:.5px;text-transform:uppercase;color:var(--acc);font-weight:700}
.brand p{font-size:12px;color:var(--txt3);margin-top:4px;line-height:1.4}
.search-wrap{padding:14px 18px}
#buscar{width:100%;background:var(--bg);border:1px solid var(--line);border-radius:8px;
  padding:9px 12px;color:var(--txt);font-size:13px;font-family:var(--sans);outline:none}
#buscar:focus{border-color:var(--acc)}
#buscar::placeholder{color:var(--txt3)}
#res-count{font-size:11px;color:var(--txt3);padding:0 18px 8px;font-family:var(--mono);min-height:16px}
nav{padding:0 10px}
nav .cap{margin-bottom:2px}
nav .cap>a{display:block;padding:9px 12px;color:var(--txt);text-decoration:none;font-size:14px;
  font-weight:600;border-radius:7px;border-left:3px solid transparent}
nav .cap>a:hover{background:var(--bg3);border-left-color:var(--acc)}
nav .cap>a .n{color:var(--txt3);font-family:var(--mono);font-size:12px;margin-right:8px}
nav ul{list-style:none;padding:2px 0 8px 0}
nav ul li a{display:block;padding:5px 12px 5px 34px;color:var(--txt2);text-decoration:none;
  font-size:13px;border-radius:6px;line-height:1.35}
nav ul li a:hover{background:var(--bg3);color:var(--txt)}
nav ul li a.active{color:var(--acc);background:#152430}

/* ---------- MAIN ---------- */
main{flex:1;min-width:0;max-width:1000px;padding:0 46px 120px}
header.hero{padding:60px 0 40px;border-bottom:1px solid var(--line)}
header.hero .kicker{color:var(--acc);font-family:var(--mono);font-size:12px;letter-spacing:1.5px;text-transform:uppercase}
header.hero h1{font-size:46px;line-height:1.1;margin:14px 0 16px;font-weight:800;letter-spacing:-1px}
header.hero .bajada{font-size:19px;color:var(--txt2);max-width:720px;line-height:1.55}
.para-quien{margin-top:22px;font-size:14px;color:var(--txt3);max-width:700px}
.regla{background:var(--bg2);border:1px solid var(--line);border-left:3px solid var(--acc);
  border-radius:8px;padding:18px 22px;margin-top:26px;font-size:14.5px;color:var(--txt2)}
.regla b{color:var(--txt)}

section.capitulo{padding:56px 0 10px;border-top:1px solid var(--line);margin-top:30px}
section.capitulo:first-of-type{border-top:none}
.cap-head{margin-bottom:26px}
.cap-num{font-family:var(--mono);font-size:12px;color:var(--acc);letter-spacing:2px}
.cap-head h2{font-size:34px;font-weight:800;letter-spacing:-.6px;margin:6px 0 8px}
.cap-head .sub{color:var(--txt2);font-size:16px;max-width:700px}

article.bloque{margin-bottom:52px;scroll-margin-top:24px}
article.bloque h3{font-size:23px;font-weight:700;letter-spacing:-.3px;margin-bottom:16px;
  padding-bottom:8px;border-bottom:1px solid var(--line)}
article.bloque h4{font-size:16.5px;font-weight:700;margin:26px 0 10px;color:var(--txt)}
article.bloque p{margin-bottom:14px;color:var(--txt2)}
article.bloque p.lead{font-size:17.5px;color:var(--txt);line-height:1.6}
article.bloque ul.lista,article.bloque ol.pasos{margin:0 0 16px 22px}
article.bloque ul.lista li,article.bloque ol.pasos li{margin-bottom:9px;color:var(--txt2)}
article.bloque code{background:var(--bg3);padding:2px 6px;border-radius:4px;font-family:var(--mono);font-size:.88em;color:var(--acc)}
article.bloque a{color:var(--acc);text-decoration:none;border-bottom:1px solid #1e4a63}
article.bloque a:hover{border-bottom-color:var(--acc)}
mark.resaltado{background:#3f3418;color:#ffd479;padding:1px 3px;border-radius:3px}

/* ---------- TABLAS ---------- */
.tabla-scroll{overflow-x:auto;margin-bottom:12px;border:1px solid var(--line);border-radius:10px}
table.tabla{width:100%;border-collapse:collapse;font-size:14px;margin-bottom:14px;background:var(--bg2);
  border:1px solid var(--line);border-radius:10px;overflow:hidden}
table.tabla thead th{background:var(--bg3);text-align:left;padding:12px 14px;font-size:12px;
  text-transform:uppercase;letter-spacing:.7px;color:var(--txt3);font-weight:700;border-bottom:1px solid var(--line)}
table.tabla td{padding:12px 14px;border-bottom:1px solid var(--line);color:var(--txt2);vertical-align:top}
table.tabla tbody tr:last-child td{border-bottom:none}
table.tabla tbody tr:hover{background:#181f27}
table.tabla td b{color:var(--txt)}
.mini{font-size:11.5px;color:var(--txt3);font-family:var(--mono)}
table.madre td{font-size:13.4px}
table.madre .no{color:#f87171;font-weight:700;white-space:nowrap}
table.madre .si{color:var(--medido);font-weight:700;white-space:nowrap}
table.madre .cond{color:var(--supuesto);font-weight:700;white-space:nowrap}
table.madre tr.r-no{background:rgba(248,113,113,.045)}
table.madre tr.r-si{background:rgba(34,197,94,.04)}
table.madre tr.r-cond{background:rgba(245,158,11,.045)}

/* ---------- SELLOS ---------- */
.sello{display:inline-block;font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:1px;
  padding:3px 8px;border-radius:4px;vertical-align:middle;margin-right:6px;text-transform:uppercase}
.s-medido{background:rgba(34,197,94,.15);color:var(--medido);border:1px solid rgba(34,197,94,.35)}
.s-extraido{background:rgba(56,189,248,.13);color:var(--extraido);border:1px solid rgba(56,189,248,.3)}
.s-supuesto{background:rgba(245,158,11,.13);color:var(--supuesto);border:1px solid rgba(245,158,11,.32)}
cite{display:block;font-size:12.5px;color:var(--txt3);font-style:normal;margin:-4px 0 18px;
  padding-left:12px;border-left:2px solid var(--line);line-height:1.5}
cite a{color:var(--txt2);border-bottom:1px dotted var(--line)}

/* ---------- CARDS / CALLOUTS ---------- */
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0 20px}
.card{background:var(--bg2);border:1px solid var(--line);border-radius:10px;padding:16px}
.card .cta{font-family:var(--mono);font-size:11px;letter-spacing:1.5px;color:var(--acc);font-weight:700;margin-bottom:8px}
.card p{font-size:13.5px;margin:0;color:var(--txt2)}
.callout{background:var(--bg2);border:1px solid var(--line);border-left:3px solid var(--acc);
  border-radius:8px;padding:16px 20px;margin:18px 0;font-size:14.5px;color:var(--txt2);line-height:1.6}
.callout b{color:var(--txt)}
.callout.supuesto{border-left-color:var(--supuesto);background:rgba(245,158,11,.045)}
.callout.ejemplo-aviso{border-left-color:#f43f5e;background:rgba(244,63,94,.08);color:#fecdd3}
.doc{background:var(--bg2);border:1px solid var(--line);border-radius:10px;padding:20px 24px;margin:14px 0 20px}
.doc p{color:var(--txt2);font-size:14.5px}
.doc ul.lista{margin-left:20px}
.doc h4{margin-top:0}
pre.diagrama{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:18px;
  font-family:var(--mono);font-size:11.5px;line-height:1.5;color:var(--txt2);overflow-x:auto;margin:14px 0}

/* ---------- FUENTES ---------- */
section.fuentes{padding:56px 0 40px;border-top:2px solid var(--line);margin-top:40px}
section.fuentes h2{font-size:30px;font-weight:800;margin-bottom:10px}
section.fuentes>p{color:var(--txt2);margin-bottom:24px;max-width:740px}
table.fuentes-tabla{width:100%;border-collapse:collapse;font-size:13px}
table.fuentes-tabla thead th{background:var(--bg3);text-align:left;padding:10px 12px;font-size:11px;
  text-transform:uppercase;letter-spacing:.7px;color:var(--txt3);border-bottom:1px solid var(--line)}
table.fuentes-tabla td{padding:12px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--txt2)}
.fid{font-family:var(--mono);font-size:11.5px;color:var(--acc);white-space:nowrap}
.fautor{font-size:11.5px;color:var(--txt3);margin-top:3px}
.frepo{font-family:var(--mono);font-size:10.5px;color:var(--txt3);margin-top:2px}
.fnota{font-size:12px;color:var(--txt3);max-width:420px}
.tipo{font-family:var(--mono);font-size:10px;padding:2px 6px;border-radius:3px;white-space:nowrap;font-weight:700}
.t-regulador{background:rgba(34,197,94,.15);color:#4ade80}
.t-regulador-citado{background:rgba(34,197,94,.1);color:#86efac}
.t-estandar{background:rgba(56,189,248,.15);color:#7dd3fc}
.t-paper{background:rgba(168,85,247,.15);color:#c084fc}
.t-fabricante{background:rgba(245,158,11,.15);color:#fbbf24}
.t-interno-medido{background:rgba(236,72,153,.15);color:#f472b6}
.t-secundaria{background:rgba(148,163,184,.15);color:#cbd5e1}

footer{padding:30px 0 60px;color:var(--txt3);font-size:12.5px;border-top:1px solid var(--line)}

/* ---------- COMENTARIOS ---------- */
section.comentarios{padding:50px 0 20px;border-top:2px solid var(--line);margin-top:30px}
section.comentarios h2{font-size:28px;font-weight:800;margin-bottom:10px}
section.comentarios>p{color:var(--txt2);margin-bottom:24px;max-width:700px;font-size:15px}
#utterances-hilo{min-height:180px;background:var(--bg2);border:1px solid var(--line);
  border-radius:10px;padding:8px}
#utterances-hilo .utterances{max-width:100%}

@media(max-width:1000px){
  aside{display:none}
  main{padding:0 20px 80px}
  header.hero h1{font-size:32px}
  .grid3{grid-template-columns:1fr}
}
"""

JS = """
document.addEventListener('DOMContentLoaded', function(){
  var input = document.getElementById('buscar');
  var count = document.getElementById('res-count');
  var bloques = Array.prototype.slice.call(document.querySelectorAll('article.bloque'));

  // --- Buscador sobre el contenido de cada bloque ---
  input.addEventListener('input', function(){
    var q = input.value.trim().toLowerCase();
    if(!q){
      bloques.forEach(function(b){ b.style.display=''; b.classList.remove('oculto'); });
      document.querySelectorAll('section.capitulo').forEach(function(s){ s.style.display=''; });
      count.textContent = '';
      return;
    }
    var hits = 0;
    bloques.forEach(function(b){
      var txt = b.textContent.toLowerCase();
      var ok = txt.indexOf(q) !== -1;
      b.style.display = ok ? '' : 'none';
      if(ok) hits++;
    });
    // ocultar capitulos sin resultados
    document.querySelectorAll('section.capitulo').forEach(function(s){
      var visibles = s.querySelectorAll('article.bloque:not([style*="display: none"])').length;
      s.style.display = visibles ? '' : 'none';
    });
    count.textContent = hits + ' bloque(s) encontrado(s)';
  });

  // --- Resaltar enlace activo al hacer scroll ---
  var links = Array.prototype.slice.call(document.querySelectorAll('nav ul li a'));
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        links.forEach(function(l){ l.classList.remove('active'); });
        var l = links.find(function(x){ return x.getAttribute('href') === '#' + e.target.id; });
        if(l) l.classList.add('active');
      }
    });
  }, {rootMargin:'-15% 0px -70% 0px'});
  bloques.forEach(function(b){ if(b.id) obs.observe(b); });

  // --- Autoevaluacion ---
  document.querySelectorAll('.quiz-item').forEach(function(item){
    var btns = item.querySelectorAll('.quiz-btn');
    btns.forEach(function(btn){
      btn.addEventListener('click', function(){
        var ok = btn.dataset.ok === '1';
        var fb = item.querySelector('.quiz-fb');
        item.querySelectorAll('.quiz-btn').forEach(function(b){ b.style.borderColor='var(--line)'; });
        btn.style.borderColor = ok ? 'var(--medido)' : '#f87171';
        fb.textContent = ok ? 'Correcto. ' + (fb.dataset.ok || '')
                            : 'No. ' + (fb.dataset.no || '');
        fb.style.color = ok ? 'var(--medido)' : '#f87171';
      });
    });
  });
});
"""


# Utterances: comentarios sobre GitHub Issues, sin backend propio.
# Va aparte del f-string porque las llaves de JavaScript chocan con el formateo.
UTTERANCES = """
<script>
(function(){
  var d = document.getElementById('utterances-hilo');
  if(!d) return;
  var s = document.createElement('script');
  s.src = 'https://utteranc.es/client.js';
  s.setAttribute('repo', 'vvilche/conecta-manual-tecnico-comercial');
  s.setAttribute('issue-term', 'pathname');
  s.setAttribute('label', 'comentario');
  s.setAttribute('theme', 'github-dark');
  s.setAttribute('crossorigin', 'anonymous');
  s.async = true;
  d.appendChild(s);
})();
</script>
"""


def _version_y_fecha():
    """Version del documento desde VERSION (unico origen) y fecha de build."""
    import datetime
    from pathlib import Path
    raiz = Path(__file__).resolve().parent.parent
    v = (raiz / "VERSION").read_text(encoding="utf-8").strip() if (raiz / "VERSION").exists() else "sin-version"
    f = datetime.date.today().strftime("%d-%m-%Y")
    return v, f


def pagina(capitulos, fuentes, sellos, intro, bloque_fuentes):
    nav, cuerpo, quiz = [], [], []
    VERSION, FECHA = _version_y_fecha()

    for i, cap in enumerate(capitulos, 1):
        cap_id = cap["id"]
        sub = "".join(
            f'<li><a href="#{b["id"]}">{b["titulo"]}</a></li>'
            for b in cap["bloques"] if b.get("id")
        )
        nav.append(
            f'<div class="cap"><a href="#{cap_id}"><span class="n">{i:02d}</span>{cap["titulo"]}</a>'
            f'<ul>{sub}</ul></div>'
        )

        bloques_html = []
        for b in cap["bloques"]:
            bloques_html.append(
                f'<article class="bloque" id="{b.get("id","")}">'
                f'<h3>{b["titulo"]}</h3>{b["html"]}</article>'
            )
        cuerpo.append(
            f'<section class="capitulo" id="{cap_id}">'
            f'<div class="cap-head"><div class="cap-num">CAPITULO {i:02d}</div>'
            f'<h2>{cap["titulo"]}</h2><div class="sub">{cap["subtitulo"]}</div></div>'
            + "".join(bloques_html) +
            "</section>"
        )

    como_leer = "".join(
        f'<li><b>{t}</b> — {d}</li>' for t, d in intro["como_leer"]
    )

    return f"""<!DOCTYPE html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{intro["titulo"]} — CONECTA Ingenieria</title>
<style>{CSS}</style>
</head>
<body>
<div class="layout">
<aside>
  <div class="brand">
    <h1>CONECTA</h1>
    <p>Manual tecnico comercial<br>Uso interno</p>
  </div>
  <div class="search-wrap">
    <input id="buscar" type="text" placeholder="Buscar en el manual..." autocomplete="off">
  </div>
  <div id="res-count"></div>
  <nav>{"".join(nav)}</nav>
</aside>

<main>
<header class="hero">
  <div class="kicker">CONECTA Ingenieria · Documento interno · {VERSION} · {FECHA}</div>
  <h1>{intro["titulo"]}</h1>
  <p class="bajada">{intro["bajada"]}</p>
  <p class="para-quien">{intro["para_quien"]}</p>
  <div class="regla">{intro["regla"]}</div>
  <div class="regla" style="border-left-color:var(--txt3)">
    <b>Como esta ordenado.</b>
    <ul class="lista" style="margin-top:10px">{como_leer}</ul>
  </div>
</header>

{"".join(cuerpo)}

<section class="fuentes" id="fuentes">
  <h2>Fuentes</h2>
  <p>Cada afirmacion tecnica del manual apunta a una de estas fuentes. Las que tienen link directo se
  pueden abrir desde aca. Las marcadas como fuente secundaria se declaran como tales. Ninguna cifra del
  manual sale de memoria.</p>
  <div class="tabla-scroll" style="border:none">
  <table class="fuentes-tabla">
    <thead><tr><th>ID</th><th>Documento</th><th>Tipo</th><th>Que respalda</th></tr></thead>
    <tbody>{bloque_fuentes}</tbody>
  </table>
  </div>
</section>

<section class="comentarios" id="comentarios">
  <h2>Comentarios y revisión</h2>
  <p>Deja tu observación acá. Se necesita una cuenta de GitHub; cada comentario queda registrado
  con autor y fecha, y no se puede editar el documento sin que quede rastro.</p>
  <div id="utterances-hilo"></div>
  <noscript>Para comentar, activa JavaScript. Los comentarios se guardan como Issues del repositorio.</noscript>
</section>

<footer>
  Manual tecnico comercial · CONECTA Ingenieria · Documento de uso interno.<br>
  Construido con fuentes verificables. Si una afirmacion no tiene sello, no afirma nada tecnico.<br>
  Version {VERSION} · generado {FECHA} ·
  <a href="https://github.com/vvilche/conecta-manual-tecnico-comercial">codigo y historial de cambios</a>.
</footer>
</main>
</div>
<script>{JS}</script>
{UTTERANCES}
</body>
</html>"""
