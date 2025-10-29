# -*- coding: utf-8 -*-
"""
Kata - Barcode Scanner.
Implementación incremental siguiendo el manifiesto TDD.
Cada versión cumple con un requisito diferente.
"""

# Base de datos simulada de productos con precios
PRODUCT_DB = {
    "12345": 7.25,
    "23456": 12.50,
}


def iteration1_scan(barcode: str) -> str:
    """
    Iteración 1: Si el código es '12345', retorna '$7.25'.
    """
    if barcode == "12345":
        return "$7.25"
    return "Error: código de barras no encontrado"


def iteration2_scan(barcode: str) -> str:
    """
    Iteración 2: Agrega el código '23456' con precio '$12.50'.
    """
    if barcode == "12345":
        return "$7.25"
    if barcode == "23456":
        return "$12.50"
    return "Error: código de barras no encontrado"


def iteration3_scan(barcode: str) -> str:
    """
    Iteración 3: Si el código está vacío, retorna error correspondiente.
    """
    if barcode == "":
        return "Error: código de barras vacío"
    if barcode == "12345":
        return "$7.25"
    if barcode == "23456":
        return "$12.50"
    return "Error: código de barras no encontrado"


def iteration4_scan(barcode: str) -> str:
    """
    Iteración 4: Implementa búsqueda basada en base de datos.
    """
    if not barcode:
        return "Error: código de barras vacío"

    if barcode in PRODUCT_DB:
        return f"${PRODUCT_DB[barcode]:.2f}"
    return "Error: código de barras no encontrado"


def iteration5_scan_total(barcodes: list[str]) -> str:
    """
    Iteración 5: Permite escanear varios productos y muestra el total.
    """
    total = 0.0

    for code in barcodes:
        if not code:
            return "Error: código de barras vacío"
        if code not in PRODUCT_DB:
            return "Error: código de barras no encontrado"
        total += PRODUCT_DB[code]

    return f"Total: ${total:.2f}"
