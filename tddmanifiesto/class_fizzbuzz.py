# -*- coding: utf-8 -*-

"""
FizzBuzz implementations - TDD iterations.
Cada función representa una iteración del ciclo Red-Green-Refactor.
"""


def iteration1_fizzbuzz(n):
    """
    Iteración 3: Agregamos la regla de múltiplos de 3.
    """
    if n % 3 == 0:
        return "Fizz"
    return str(n)


def iteration2_fizzbuzz(n):
    """
    Iteración 4: Agregamos la regla de múltiplos de 5.
    """
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def iteration3_fizzbuzz(n):
    """
    Iteración 5: Agregamos la regla de múltiplos de 3 Y 5.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizz_buzz(n):
    """
    Versión final refactorizada de FizzBuzz.
    """
    result = ""

    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"

    return result or str(n)
