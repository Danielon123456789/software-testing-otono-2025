# -*- coding: utf-8 -*-

"""
Test-Driven Development solution for FizzBuzz.
Siguiendo el manifiesto TDD con iteraciones incrementales.
"""

import unittest

from tddmanifiesto.class_fizzbuzz import (
    fizz_buzz,
    iteration1_fizzbuzz,
    iteration2_fizzbuzz,
    iteration3_fizzbuzz,
)


class TestIteration1(unittest.TestCase):
    """
    Iteración 1: Regla de múltiplos de 3.

    """

    def test_retorna_fizz_cuando_recibe_3(self):
        """
        Check if returns 'Fizz' for 3.
        """
        self.assertEqual(iteration1_fizzbuzz(3), "Fizz")


class TestIteration2(unittest.TestCase):
    """
    Iteración 2: Regla de múltiplos de 5.

    """

    def test_retorna_buzz_cuando_recibe_5(self):
        """
        Check if returns 'Buzz' for 5.
        """
        self.assertEqual(iteration2_fizzbuzz(5), "Buzz")


class TestIteration3(unittest.TestCase):
    """
    Iteración 3: Regla de múltiplos de 3 Y 5.

    """

    def test_retorna_fizzbuzz_cuando_recibe_15(self):
        """
        Check if returns 'FizzBuzz' for 15.
        """
        self.assertEqual(iteration3_fizzbuzz(15), "FizzBuzz")


class TestFizzBuzzFinal(unittest.TestCase):
    """
    Versión final refactorizada.
    """

    def test_numeros_normales(self):
        """
        Check if normal numbers are returned as strings.
        """
        self.assertEqual(fizz_buzz(1), "1")

    def test_multiplos_de_3_retornan_fizz(self):
        """
        Check if multiples of 3 return 'Fizz'.
        """
        self.assertEqual(fizz_buzz(3), "Fizz")

    def test_multiplos_de_5_retornan_buzz(self):
        """
        Check if multiples of 5 return 'Buzz'.
        """
        self.assertEqual(fizz_buzz(5), "Buzz")

    def test_multiplos_de_3_y_5_retornan_fizzbuzz(self):
        """
        Check if multiples of both 3 and 5 return 'FizzBuzz'.
        """
        self.assertEqual(fizz_buzz(15), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
