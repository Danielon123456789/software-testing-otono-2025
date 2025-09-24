# -*- coding: utf-8 -*-
"""
White-box unit testing solution.
"""
import unittest

from white_box.class_exercises import (
    calculate_total_discount,
    check_number_status,
    validate_password,
)


class TestWhiteBoxExercises(unittest.TestCase):
    """
    Exercises one, two and three.

    """

    # Answer check_number_status

    def test_check_number_status_negative_number(self):
        """
        Check if a number is negative.
        """
        self.assertEqual(check_number_status(-4), "Negative")

    def test_check_number_status_positive_number(self):
        """
        Check if a number is positive.
        """
        self.assertEqual(check_number_status(4), "Positive")

    def test_check_number_status_is_zero(self):
        """
        Check if a number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    # Tests adicionales para mejor cobertura
    def test_check_number_status_decimal_numbers(self):
        """
        Check with decimal numbers.
        """
        self.assertEqual(check_number_status(3.14), "Positive")
        self.assertEqual(check_number_status(-2.5), "Negative")
        self.assertEqual(check_number_status(0.0), "Zero")

    # Answer validate_password

    def test_validate_password_length(self):
        """
        Test password length validation.
        """

        self.assertFalse(validate_password("dani"))
        self.assertFalse(validate_password(""))
        self.assertFalse(validate_password("1234567"))

        self.assertTrue(validate_password("Daniel77@"))

    def test_validate_password_missing_uppercase(self):
        """
        Test password without uppercase letters.
        """
        self.assertFalse(validate_password("daniel77@"))
        self.assertFalse(validate_password("password123@"))

    def test_validate_password_missing_lowercase(self):
        """
        Test password without lowercase letters.
        """
        self.assertFalse(validate_password("DANIEL77@"))
        self.assertFalse(validate_password("PASSWORD123@"))

    def test_validate_password_missing_digit(self):
        """
        Test password without digits.
        """
        self.assertFalse(validate_password("Daniel@@"))
        self.assertFalse(validate_password("Password@"))

    def test_validate_password_missing_special_character(self):
        """
        Test password without special characters.
        """
        self.assertFalse(validate_password("Password123"))

    def test_validate_password_valid_passwords(self):
        """
        Test valid passwords that meet all requirements.
        """
        self.assertTrue(validate_password("Daniel77@"))

    def test_validate_password_not_valid_especial_character(self):
        """
        Test edge cases and boundary conditions.
        """

        self.assertFalse(
            validate_password("Test123*")
        )  # * no está en la lista de especiales válidos

    # Answer calculte_total_discount

    def test_calculate_total_discount_no_discount(self):
        """
        Test amounts below $100 should receive no discount.
        """
        self.assertEqual(calculate_total_discount(0), 0)
        self.assertEqual(calculate_total_discount(99.99), 0)

    def test_calculate_total_discount_10_percent(self):
        """
        Test amounts between $100-$500 should receive 10% discount.
        """
        self.assertEqual(calculate_total_discount(100), 10.0)
        self.assertEqual(calculate_total_discount(500), 50.0)

    def test_calculate_total_discount_20_percent(self):
        """
        Test amounts over $500 should receive 20% discount.
        """
        # Justo por encima del límite
        self.assertEqual(round(calculate_total_discount(500.01), 3), 100.002)
        self.assertEqual(round(calculate_total_discount(501), 1), 100.2)

    def test_calculate_total_discount_decimal_amounts(self):
        """
        Test with decimal amounts for precision.
        """
        # Sin descuento
        self.assertEqual(calculate_total_discount(0.01), 0)

        # 10% descuento
        self.assertEqual(round(calculate_total_discount(150.75), 3), 15.075)
        self.assertEqual(round(calculate_total_discount(250.25), 3), 25.025)

        # 20% descuento
        self.assertEqual(round(calculate_total_discount(750.50), 1), 150.1)
        self.assertEqual(round(calculate_total_discount(1250.75), 2), 250.15)
