# -*- coding: utf-8 -*-
"""Indice de contenido del manual. El orden de esta lista es el orden del manual."""

from contenido_base import INTRO, SELLOS
from cap_conceptos import CAP_CONCEPTOS
from cap_lineas import CAP_LINEAS
from cap_producto import CAP_PRODUCTO
from cap_protocolos import CAP_PROTOCOLOS
from cap_partners import CAP_PARTNERS
from cap_arquitectura import CAP_ARQUITECTURA
from cap_ciberseguridad import CAP_CIBER
from cap_cotizacion import CAP_COTIZACION
from cap_metodologia import CAP_METODOLOGIA

CAPITULOS = [
    CAP_CONCEPTOS,
    CAP_LINEAS,
    CAP_PRODUCTO,
    CAP_PROTOCOLOS,
    CAP_PARTNERS,
    CAP_ARQUITECTURA,
    CAP_CIBER,
    CAP_COTIZACION,
    CAP_METODOLOGIA,
]

__all__ = ["CAPITULOS", "INTRO", "SELLOS"]
