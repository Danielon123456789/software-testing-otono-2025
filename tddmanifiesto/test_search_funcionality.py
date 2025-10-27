# -*- coding: utf-8 -*-
"""
Pytest Data-Driven para la Kata 4 - Search Functionality.
Implementación con @pytest.mark.parametrize.
Estructura de nombres Given-When-Then.
"""
# pylint: disable=import-error
import pytest

from tddmanifiesto.class_search_funcionality import (
    CITY_DB,
    iteration1_search,
    iteration2_search,
    iteration3_search,
    iteration4_search,
    iteration5_search,
    search_cities,
)


@pytest.mark.parametrize(
    "search_text, expected",
    [
        ("", []),
        ("a", []),
        ("X", []),
    ],
)
def test_given_short_search_text_when_iteration1_called_then_returns_empty_list(
    search_text, expected
):
    """Iteración 1: Si el texto tiene menos de 2 caracteres, retorna lista vacía."""
    assert iteration1_search(search_text) == expected


@pytest.mark.parametrize(
    "search_text, expected",
    [
        ("Va", ["Valencia", "Vancouver"]),
        ("va", []),
        ("Ro", ["Rotterdam", "Rome"]),
        ("Am", ["Amsterdam"]),
    ],
)
def test_given_valid_search_prefix_when_iteration2_called_then_returns_cities_starting_with_text(
    search_text, expected
):
    """Iteración 2: Retorna ciudades que comienzan con el texto (sensible a mayúsculas)."""
    result = iteration2_search(search_text)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize(
    "search_text, expected",
    [
        ("va", ["Valencia", "Vancouver"]),
        ("vA", ["Valencia", "Vancouver"]),
        ("VA", ["Valencia", "Vancouver"]),
    ],
)
def test_given_mixed_case_search_text_when_iteration3_called_then_returns_case_insensitive_matches(
    search_text, expected
):
    """Iteración 3: Búsqueda insensible a mayúsculas/minúsculas."""
    result = iteration3_search(search_text)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize(
    "search_text, expected",
    [
        ("ape", ["Budapest"]),
        ("don", ["London"]),
    ],
)
def test_given_partial_text_when_iteration4_called_then_returns_matching_cities(
    search_text, expected
):
    """Iteración 4: Permite coincidencias parciales dentro del nombre."""
    result = iteration4_search(search_text)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize(
    "search_text, expected",
    [
        ("*", CITY_DB),
    ],
)
def test_given_asterisk_when_iteration5_called_then_returns_all_cities(
    search_text, expected
):
    """Iteración 5: Si el texto es '*', retorna todas las ciudades."""
    result = iteration5_search(search_text)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize(
    "search_text, expected",
    [
        ("a", []),
        ("Va", ["Valencia", "Vancouver"]),
        ("ape", ["Budapest"]),
        ("*", CITY_DB),
    ],
)
def test_given_various_search_inputs_when_final_search_called_then_returns_expected_results(
    search_text, expected
):
    """Versión final refactorizada: combina todas las reglas."""
    result = search_cities(search_text)
    assert sorted(result) == sorted(expected)
