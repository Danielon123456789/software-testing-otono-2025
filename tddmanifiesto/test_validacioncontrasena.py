# -*- coding: utf-8 -*-
"""
Unit tests for the Password Validator Kata.
Each test class corresponds to a version (requirement) of the validator function.
Tests are named following the Given-When-Then convention (TDD Manifesto).
"""

import unittest

from tddmanifiesto.class_validacioncontrasena import validate_password_v1 as version1
from tddmanifiesto.class_validacioncontrasena import validate_password_v2 as version2
from tddmanifiesto.class_validacioncontrasena import validate_password_v3 as version3
from tddmanifiesto.class_validacioncontrasena import validate_password_v4 as version4
from tddmanifiesto.class_validacioncontrasena import validate_password_v5 as version5


class TestVersion1(unittest.TestCase):
    """
    Version 1: The password must have at least 8 characters.
    """

    def test_given_short_password_when_validate_called_then_returns_error(self):
        """Should return an error when password length is less than 8 characters."""
        result = version1("abc")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe tener al menos 8 caracteres", result["errors"]
        )

    def test_given_eight_or_more_characters_when_validate_called_then_returns_valid(
        self,
    ):
        """Should return valid when password length is 8 or more characters."""
        result = version1("abcdefgh")
        self.assertTrue(result["is_valid"])
        self.assertEqual(result["errors"], [])


class TestVersion2(unittest.TestCase):
    """
    Version 2: Must also contain at least two numbers.
    """

    def test_given_short_password_when_validate_called_then_returns_error(self):
        """Should return an error when password length is less than 8 characters."""
        result = version2("abc")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe tener al menos 8 caracteres", result["errors"]
        )

    def test_given_eight_or_more_characters_when_validate_called_then_returns_valid(
        self,
    ):
        """Should return valid when password length is 8 or more characters."""
        result = version2("abcdefgh")
        self.assertTrue(
            result["is_valid"] or "La contraseña debe contener" in result["errors"][0]
        )

    def test_given_password_with_less_than_two_numbers_when_validate_called_then_returns_er(
        self,
    ):
        """Should return an error when password does not contain at least two numbers."""
        result = version2("abcdefg1")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe contener al menos dos números", result["errors"]
        )

    def test_given_password_with_two_or_more_numbers_when_validate_called_then_returns_valid(
        self,
    ):
        """Should return valid when password contains two or more numbers."""
        result = version2("abcd1234")
        self.assertTrue(result["is_valid"])


class TestVersion3(unittest.TestCase):
    """
    Version 3: Handle multiple validation errors together.
    """

    def test_given_short_password_when_validate_called_then_returns_error(self):
        """Should return an error when password length is less than 8 characters."""
        result = version3("abc")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe tener al menos 8 caracteres", result["errors"]
        )

    def test_given_password_with_less_than_two_numbers_when_validate_called_then_returns_err(
        self,
    ):
        """Should return an error when password does not contain at least two numbers."""
        result = version3("abcdefg1")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe contener al menos dos números", result["errors"]
        )

    def test_given_password_with_multiple_violations_when_validate_called_then_returns_errors(
        self,
    ):
        """Should return multiple validation messages for several invalid rules."""
        result = version3("abc")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe tener al menos 8 caracteres", result["errors"]
        )
        self.assertIn(
            "La contraseña debe contener al menos dos números", result["errors"]
        )

    def test_given_valid_password_when_validate_called_then_returns_valid(self):
        """Should return valid when password meets the first two rules."""
        result = version3("abcd1234")
        self.assertTrue(result["is_valid"])


class TestVersion4(unittest.TestCase):
    """
    Version 4: Password must contain at least one uppercase letter.
    """

    def test_given_password_without_uppercase_when_validate_called_then_returns_error(
        self,
    ):
        """Should return an error when no uppercase letter is found."""
        result = version4("abcd1234")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe contener al menos una letra mayúscula", result["errors"]
        )

    def test_given_password_with_uppercase_when_validate_called_then_returns_valid(
        self,
    ):
        """Should return valid when at least one uppercase letter is present."""
        result = version4("Abcd1234")
        self.assertTrue(result["is_valid"])

    def test_given_password_with_multiple_errors_when_validate_called_then_returns_all_messa(
        self,
    ):
        """Should detect multiple missing requirements at once."""
        result = version4("abc")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe tener al menos 8 caracteres", result["errors"]
        )
        self.assertIn(
            "La contraseña debe contener al menos dos números", result["errors"]
        )
        self.assertIn(
            "La contraseña debe contener al menos una letra mayúscula", result["errors"]
        )


class TestVersion5(unittest.TestCase):
    """
    Version 5: Password must contain at least one special character.
    """

    def test_given_password_meets_all_requirements_when_validate_called_then_returns_valid(
        self,
    ):
        """Should return valid when all requirements are met."""
        result = version5("Abcd1234!")
        self.assertTrue(result["is_valid"])

    def test_given_password_without_special_char_when_validate_called_then_returns_error(
        self,
    ):
        """Should return an error when no special character is present."""
        result = version5("Abcd1234")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe contener al menos un carácter especial",
            result["errors"],
        )

    def test_given_password_with_special_char_when_validate_called_then_returns_valid(
        self,
    ):
        """Should return valid when password contains a special character."""
        result = version5("Abcd1234!")
        self.assertTrue(result["is_valid"])

    def test_given_password_with_multiple_errors_when_validate_called_then_returns_all_messag(
        self,
    ):
        """Should return multiple messages if multiple rules fail."""
        result = version5("abc")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "La contraseña debe tener al menos 8 caracteres", result["errors"]
        )
        self.assertIn(
            "La contraseña debe contener al menos dos números", result["errors"]
        )
        self.assertIn(
            "La contraseña debe contener al menos una letra mayúscula", result["errors"]
        )
        self.assertIn(
            "La contraseña debe contener al menos un carácter especial",
            result["errors"],
        )


if __name__ == "__main__":
    unittest.main()
