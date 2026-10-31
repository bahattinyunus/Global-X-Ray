# -*- coding: utf-8 -*-
"""
scripts/data/__init__.py
Global X-Ray - Tüm Dünya Ülkeleri Entegre Veri Ambarı (205 Ülke ve Fiili Yönetim)
"""

from .middle_east import MIDDLE_EAST_COUNTRIES
from .europe import EUROPE_COUNTRIES
from .asia import ASIA_COUNTRIES
from .americas import AMERICAS_COUNTRIES
from .africa import AFRICA_COUNTRIES
from .oceania import OCEANIA_COUNTRIES

ALL_COUNTRIES = (
    MIDDLE_EAST_COUNTRIES +
    EUROPE_COUNTRIES +
    ASIA_COUNTRIES +
    AMERICAS_COUNTRIES +
    AFRICA_COUNTRIES +
    OCEANIA_COUNTRIES
)

__all__ = [
    "ALL_COUNTRIES",
    "MIDDLE_EAST_COUNTRIES",
    "EUROPE_COUNTRIES",
    "ASIA_COUNTRIES",
    "AMERICAS_COUNTRIES",
    "AFRICA_COUNTRIES",
    "OCEANIA_COUNTRIES"
]
