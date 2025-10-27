# -*- coding: utf-8 -*-
"""
Kata 4 - Search Functionality.
Implementación incremental siguiendo el manifiesto TDD.
Cada versión cumple con un criterio diferente.
"""

CITY_DB = [
    "Paris",
    "Budapest",
    "Skopje",
    "Rotterdam",
    "Valencia",
    "Vancouver",
    "Amsterdam",
    "Vienna",
    "Sydney",
    "New York City",
    "London",
    "Bangkok",
    "Hong Kong",
    "Dubai",
    "Rome",
    "Istanbul",
]


def iteration1_search(search_text: str) -> list:
    """
    Iteración 1: Si el texto tiene menos de 2 caracteres, retorna lista vacía.
    """
    if len(search_text) < 2:
        return []
    return CITY_DB


def iteration2_search(search_text: str) -> list:
    """
    Iteración 2: Retorna ciudades que comienzan con el texto (sensible a mayúsculas).
    """
    if len(search_text) < 2:
        return []

    return [city for city in CITY_DB if city.startswith(search_text)]


def iteration3_search(search_text: str) -> list:
    """
    Iteración 3: Búsqueda insensible a mayúsculas/minúsculas.
    (Aquí se introduce la conversión a minúsculas.)
    """
    if len(search_text) < 2:
        return []

    search_text = search_text.lower()
    return [city for city in CITY_DB if city.lower().startswith(search_text)]


def iteration4_search(search_text: str) -> list:
    """
    Iteración 4: Si el texto es parte del nombre de una ciudad.
    """
    if len(search_text) < 2:
        return []

    search_text = search_text.lower()
    return [city for city in CITY_DB if search_text in city.lower()]


def iteration5_search(search_text: str) -> list:
    """
    Iteración 5: Si el texto es '*', retorna todas las ciudades.
    """
    if search_text == "*":
        return CITY_DB

    if len(search_text) < 2:
        return []

    search_text = search_text.lower()
    return [city for city in CITY_DB if search_text in city.lower()]


def search_cities(search_text: str) -> list:
    """
    Versión final: combina todas las reglas.
    """
    if search_text == "*":
        return CITY_DB

    if len(search_text) < 2:
        return []

    search_text = search_text.lower()
    return [city for city in CITY_DB if search_text in city.lower()]
