# -*- coding: utf-8 -*-
"""
Sellos de trazabilidad y textos de entrada del manual.

SELLO = de donde sale lo que se afirma. No es decoracion: es la regla 4 del arnes
("ninguna afirmacion sin fuente") hecha visible en pantalla.

  MEDIDO   -> lo corri un script sobre archivos reales y puedo mostrar el archivo.
  EXTRAIDO -> lo dice una fuente primaria (norma, fabricante, paper) y va con link.
  SUPUESTO -> es criterio de CONECTA o convencion de industria. NO es dato verificado.

Todo SUPUESTO debe leerse como opinion, no como hecho.
"""

SELLOS = {
    "medido": {
        "etiqueta": "MEDIDO",
        "titulo": "Corrido sobre archivos reales; el detalle esta en el repositorio",
        "clase": "s-medido",
    },
    "extraido": {
        "etiqueta": "EXTRAIDO",
        "titulo": "Fuente primaria con link verificable",
        "clase": "s-extraido",
    },
    "supuesto": {
        "etiqueta": "SUPUESTO",
        "titulo": "Criterio propio o convencion de industria. No es dato verificado",
        "clase": "s-supuesto",
    },
}

INTRO = {
    "titulo": "Manual Tecnico Comercial",
    "bajada": "Que vende CONECTA, por que importa tecnicamente, y como se conversa con un cliente sin inventar nada.",
    "para_quien": "Gente nueva que necesita entender el negocio, y gente actual que necesita una referencia unica para no improvisar en terreno.",
    "regla": (
        "Cada afirmacion tecnica de este manual lleva un sello y una fuente. "
        "<b>MEDIDO</b> = lo corri sobre archivos reales. "
        "<b>EXTRAIDO</b> = lo dice una norma o el fabricante, con link. "
        "<b>SUPUESTO</b> = es criterio de CONECTA o convencion de industria, y se declara como tal. "
        "Si una frase no tiene sello, es porque no afirma nada tecnico."
    ),
    "como_leer": [
        ("Conceptos", "Las ideas que hay que entender antes de vender. Empezando por la mas dificil: el dato sin tiempo no sirve."),
        ("Las seis lineas", "Lo que el cotizador trata como linea de negocio, y que se compone en cada una."),
        ("Producto", "Que componente resuelve que problema, y en que linea del catalogo cae."),
        ("Protocolos", "La tabla que evita el error mas caro: creer que todo protocolo trae estampa de tiempo."),
        ("Arquitectura", "Como se construye una, que elementos debe llevar, y que mirar cuando algo falla."),
        ("Ciberseguridad", "Que exige la ley chilena y el estandar tecnico, y que se puede vender de verdad."),
        ("Armar una cotizacion", "Los diez elementos que debe llevar, con un ejemplo completo."),
        ("Metodologia comercial", "La Escalera, la Mina de Oro, las objeciones. Como se califica y como se conversa."),
    ],
}
