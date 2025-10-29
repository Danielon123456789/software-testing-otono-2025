# -*- coding: utf-8 -*-
"""
Pytest Data-Driven para la Kata - Barcode Scanner.
Implementación con @pytest.mark.parametrize.
Estructura de nombres Given-When-Then.
"""
# pylint: disable=import-error
import pytest

from tddmanifiesto.class_puntodeventa import (
    iteration1_scan,
    iteration2_scan,
    iteration3_scan,
    iteration4_scan,
    iteration5_scan_total,
)


@pytest.mark.parametrize(
    "barcode, expected",
    [
        ("12345", "$7.25"),
    ],
)
def test_given_barcode_when_iteration1_scan_called_then_returns_expected_price(
    barcode, expected
):
    """Iteración 1: Solo el código 12345 es válido."""
    assert iteration1_scan(barcode) == expected


@pytest.mark.parametrize(
    "barcode, expected",
    [
        ("12345", "$7.25"),
        ("23456", "$12.50"),
    ],
)
def test_given_known_barcodes_when_iteration2_then_returns_correct_prices(
    barcode, expected
):
    """Iteración 2: Se agrega el producto 23456."""
    assert iteration2_scan(barcode) == expected


@pytest.mark.parametrize(
    "barcode, expected",
    [
        ("12345", "$7.25"),
        ("23456", "$12.50"),
        ("99999", "Error: código de barras no encontrado"),
    ],
)
def test_given_empty_or_valid_when_iteration3_scan_then_return_message(
    barcode, expected
):
    """Iteración 3: Maneja código vacío."""
    assert iteration3_scan(barcode) == expected


@pytest.mark.parametrize(
    "barcode, expected",
    [
        ("12345", "$7.25"),
        ("23456", "$12.50"),
        ("99999", "Error: código de barras no encontrado"),
        ("", "Error: código de barras vacío"),
    ],
)
def test_given_barcode_when_iteration4_scan_called_then_returns_msg(barcode, expected):
    """Iteración 4: Usa base de datos simulada de productos."""
    result = iteration4_scan(barcode)
    assert result == expected


@pytest.mark.parametrize(
    "barcodes, expected",
    [
        (["12345", "23456"], "Total: $19.75"),
        (["12345", "99999"], "Error: código de barras no encontrado"),
        (["", "23456"], "Error: código de barras vacío"),
    ],
)
def test_given_multiple_when_iteration5_scan_total_called_then_returns_total(
    barcodes, expected
):
    """Iteración 5: Escaneo múltiple de productos."""
    result = iteration5_scan_total(barcodes)
    assert result == expected
