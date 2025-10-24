# -*- coding: utf-8 -*-
"""
Unit tests for the String Calculator Kata.
Each test class corresponds to a version (requirement) of the add function.
Tests are named following the Given-When-Then convention (TDD Manifesto).
"""

import unittest

from tddmanifiesto.class_stringcalculator import add as add_version1
from tddmanifiesto.class_stringcalculator import add_v2 as add_version2
from tddmanifiesto.class_stringcalculator import add_v3 as add_version3
from tddmanifiesto.class_stringcalculator import add_v4 as add_version4
from tddmanifiesto.class_stringcalculator import add_v5 as add_version5
from tddmanifiesto.class_stringcalculator import add_v6 as add_version6
from tddmanifiesto.class_stringcalculator import add_v7 as add_version7
from tddmanifiesto.class_stringcalculator import add_v8 as add_version8


class TestVersion1(unittest.TestCase):
    """
    Version 1: Up to two numbers separated by commas, or empty string.
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version1(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version1("1,2"), 3)


class TestVersion2(unittest.TestCase):
    """
    Version 2: Handle unknown number of arguments.
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version2(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version2("1,2"), 3)

    def test_given_single_number_when_add_called_then_returns_number(self):
        """Should return the number itself when only one value is provided."""
        self.assertEqual(add_version2("5"), 5)

    def test_given_multiple_numbers_when_add_called_then_returns_total_sum(self):
        """Should correctly sum an arbitrary number of comma-separated values."""
        self.assertEqual(add_version2("1,2,3,4"), 10)
        self.assertEqual(add_version2("5,5,5,5"), 20)


class TestVersion3(unittest.TestCase):
    """
    Version 3: Handle newlines as separators.
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version3(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version3("1,2"), 3)

    def test_given_single_number_when_add_called_then_returns_number(self):
        """Should return the number itself when only one value is provided."""
        self.assertEqual(add_version3("5"), 5)

    def test_given_multiple_numbers_when_add_called_then_returns_total_sum(self):
        """Should correctly sum an arbitrary number of comma-separated values."""
        self.assertEqual(add_version3("1,2,3,4"), 10)
        self.assertEqual(add_version3("5,5,5,5"), 20)

    def test_given_newline_and_commas_when_add_called_then_returns_correct_sum(self):
        """Should support both commas and newlines as valid separators."""
        self.assertEqual(add_version3("1,2\n3"), 6)
        self.assertEqual(add_version3("4\n5\n6"), 15)


class TestVersion4(unittest.TestCase):
    """
    Version 4: Validation — no separator at the end.
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version4(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version4("1,2"), 3)

    def test_given_single_number_when_add_called_then_returns_number(self):
        """Should return the number itself when only one value is provided."""
        self.assertEqual(add_version4("5"), 5)

    def test_given_multiple_numbers_when_add_called_then_returns_total_sum(self):
        """Should correctly sum an arbitrary number of comma-separated values."""
        self.assertEqual(add_version4("1,2,3,4"), 10)
        self.assertEqual(add_version4("5,5,5,5"), 20)

    def test_given_newline_and_commas_when_add_called_then_returns_correct_sum(self):
        """Should support both commas and newlines as valid separators."""
        self.assertEqual(add_version4("1,2\n3"), 6)
        self.assertEqual(add_version4("4\n5\n6"), 15)

    def test_given_valid_input_when_add_called_then_returns_sum(self):
        """Should return correct sum when there is no trailing separator."""
        self.assertEqual(add_version4("1,2\n3"), 6)

    def test_given_trailing_separator_when_add_called_then_raises_valueerror(self):
        """Should raise ValueError when input ends with a separator (e.g., '1,2,')."""
        with self.assertRaises(ValueError):
            add_version4("1,2,")


class TestVersion5(unittest.TestCase):
    """
    Version 5: Handle different delimiters.
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version5(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version5("1,2"), 3)

    def test_given_single_number_when_add_called_then_returns_number(self):
        """Should return the number itself when only one value is provided."""
        self.assertEqual(add_version5("5"), 5)

    def test_given_multiple_numbers_when_add_called_then_returns_total_sum(self):
        """Should correctly sum an arbitrary number of comma-separated values."""
        self.assertEqual(add_version5("1,2,3,4"), 10)
        self.assertEqual(add_version5("5,5,5,5"), 20)

    def test_given_newline_and_commas_when_add_called_then_returns_correct_sum(self):
        """Should support both commas and newlines as valid separators."""
        self.assertEqual(add_version5("1,2\n3"), 6)
        self.assertEqual(add_version5("4\n5\n6"), 15)

    def test_given_valid_input_when_add_called_then_returns_sum(self):
        """Should return correct sum when there is no trailing separator."""
        self.assertEqual(add_version5("1,2\n3"), 6)

    def test_given_trailing_separator_when_add_called_then_raises_valueerror(self):
        """Should raise ValueError when input ends with a separator (e.g., '1,2,')."""
        with self.assertRaises(ValueError):
            add_version5("1,2,")

    def test_given_custom_delimiter_when_add_called_then_returns_sum(self):
        """Should use the specified custom delimiter to separate numbers."""
        self.assertEqual(add_version5("//;\n1;3"), 4)
        self.assertEqual(add_version5("//|\n1|2|3"), 6)
        self.assertEqual(add_version5("//sep\n2sep5"), 7)

    def test_given_input_ending_with_custom_delimiter_when_add_called_then_raises_valueerror(
        self,
    ):
        """Should raise ValueError if input ends with a custom delimiter."""
        with self.assertRaises(ValueError):
            add_version5("//;\n1;2;")


class TestVersion6(unittest.TestCase):
    """
    Version 6: Negative numbers are not allowed.
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version6(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version6("1,2"), 3)

    def test_given_single_number_when_add_called_then_returns_number(self):
        """Should return the number itself when only one value is provided."""
        self.assertEqual(add_version6("5"), 5)

    def test_given_multiple_numbers_when_add_called_then_returns_total_sum(self):
        """Should correctly sum an arbitrary number of comma-separated values."""
        self.assertEqual(add_version6("1,2,3,4"), 10)
        self.assertEqual(add_version6("5,5,5,5"), 20)

    def test_given_newline_and_commas_when_add_called_then_returns_correct_sum(self):
        """Should support both commas and newlines as valid separators."""
        self.assertEqual(add_version6("1,2\n3"), 6)
        self.assertEqual(add_version6("4\n5\n6"), 15)

    def test_given_valid_input_when_add_called_then_returns_sum(self):
        """Should return correct sum when there is no trailing separator."""
        self.assertEqual(add_version6("1,2\n3"), 6)

    def test_given_trailing_separator_when_add_called_then_raises_valueerror(self):
        """Should raise ValueError when input ends with a separator (e.g., '1,2,')."""
        with self.assertRaises(ValueError):
            add_version6("1,2,")

    def test_given_custom_delimiter_when_add_called_then_returns_sum(self):
        """Should use the specified custom delimiter to separate numbers."""
        self.assertEqual(add_version6("//;\n1;3"), 4)
        self.assertEqual(add_version6("//|\n1|2|3"), 6)
        self.assertEqual(add_version6("//sep\n2sep5"), 7)

    def test_given_input_ending_with_custom_delimiter_when_add_called_then_raises_valueerror(
        self,
    ):
        """Should raise ValueError if input ends with a custom delimiter."""
        with self.assertRaises(ValueError):
            add_version6("//;\n1;2;")

    def test_given_negative_numbers_when_add_called_then_raises_valueerror_with_listed_negatives(
        self,
    ):
        """Should raise ValueError and display message listing all negative numbers."""
        with self.assertRaises(ValueError) as ctx:
            add_version6("1,-2,3")
        self.assertIn("Negative numbers not allowed: -2", str(ctx.exception))


class TestVersion7(unittest.TestCase):
    """
    Version 7: Multiple errors are aggregated (negatives + mixed delimiter).
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version7(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version7("1,2"), 3)

    def test_given_single_number_when_add_called_then_returns_number(self):
        """Should return the number itself when only one value is provided."""
        self.assertEqual(add_version7("5"), 5)

    def test_given_multiple_numbers_when_add_called_then_returns_total_sum(self):
        """Should correctly sum an arbitrary number of comma-separated values."""
        self.assertEqual(add_version7("1,2,3,4"), 10)
        self.assertEqual(add_version7("5,5,5,5"), 20)

    def test_given_newline_and_commas_when_add_called_then_returns_correct_sum(self):
        """Should support both commas and newlines as valid separators."""
        self.assertEqual(add_version7("1,2\n3"), 6)
        self.assertEqual(add_version7("4\n5\n6"), 15)

    def test_given_valid_input_when_add_called_then_returns_sum(self):
        """Should return correct sum when there is no trailing separator."""
        self.assertEqual(add_version7("1,2\n3"), 6)

    def test_given_trailing_separator_when_add_called_then_raises_valueerror(self):
        """Should raise ValueError when input ends with a separator (e.g., '1,2,')."""
        with self.assertRaises(ValueError):
            add_version7("1,2,")

    def test_given_custom_delimiter_when_add_called_then_returns_sum(self):
        """Should use the specified custom delimiter to separate numbers."""
        self.assertEqual(add_version7("//;\n1;3"), 4)
        self.assertEqual(add_version7("//|\n1|2|3"), 6)
        self.assertEqual(add_version7("//sep\n2sep5"), 7)

    def test_given_input_ending_with_custom_delimiter_when_add_called_then_raises_valueerror(
        self,
    ):
        """Should raise ValueError if input ends with a custom delimiter."""
        with self.assertRaises(ValueError):
            add_version7("//;\n1;2;")

    def test_given_negative_numbers_when_add_called_then_raises_valueerror_with_listed_negatives(
        self,
    ):
        """Should raise ValueError and display message listing all negative numbers."""
        with self.assertRaises(ValueError) as ctx:
            add_version7("1,-2,3")
        self.assertIn("Negative number(s) not allowed: -2", str(ctx.exception))

    def test_given_negative_and_mixed_delimiter_when_add_called_then_returns_multiple_error_message(
        self,
    ):
        """
        Should detect multiple types of errors simultaneously.
        For example:
        “//|\n1|2,-3” should raise a ValueError with both messages:
        - Negative number(s) not allowed: -3
        - '|' expected but ',' found at position 3.
        """
        with self.assertRaises(ValueError) as ctx:
            add_version7("//|\n1|2,-3")

        self.assertEqual(
            str(ctx.exception),
            "Negative number(s) not allowed: -3\n'|' expected but ',' found at position 3.",
        )


class TestVersion8(unittest.TestCase):
    """
    Version 8: Combine all features — custom delimiter, negatives aggregated, and ignore >1000.
    """

    def test_given_empty_string_when_add_called_then_returns_zero(self):
        """Should return 0 when the input string is empty."""
        self.assertEqual(add_version8(""), 0)

    def test_given_two_numbers_when_add_called_then_returns_sum(self):
        """Should return the sum when input contains two comma-separated numbers."""
        self.assertEqual(add_version8("1,2"), 3)

    def test_given_single_number_when_add_called_then_returns_number(self):
        """Should return the number itself when only one value is provided."""
        self.assertEqual(add_version8("5"), 5)

    def test_given_multiple_numbers_when_add_called_then_returns_total_sum(self):
        """Should correctly sum an arbitrary number of comma-separated values."""
        self.assertEqual(add_version8("1,2,3,4"), 10)
        self.assertEqual(add_version8("5,5,5,5"), 20)

    def test_given_newline_and_commas_when_add_called_then_returns_correct_sum(self):
        """Should support both commas and newlines as valid separators."""
        self.assertEqual(add_version8("1,2\n3"), 6)
        self.assertEqual(add_version8("4\n5\n6"), 15)

    def test_given_valid_input_when_add_called_then_returns_sum(self):
        """Should return correct sum when there is no trailing separator."""
        self.assertEqual(add_version8("1,2\n3"), 6)

    def test_given_trailing_separator_when_add_called_then_raises_valueerror(self):
        """Should raise ValueError when input ends with a separator (e.g., '1,2,')."""
        with self.assertRaises(ValueError):
            add_version8("1,2,")

    def test_given_custom_delimiter_when_add_called_then_returns_sum(self):
        """Should use the specified custom delimiter to separate numbers."""
        self.assertEqual(add_version8("//;\n1;3"), 4)
        self.assertEqual(add_version8("//|\n1|2|3"), 6)
        self.assertEqual(add_version8("//sep\n2sep5"), 7)

    def test_given_input_ending_with_custom_delimiter_when_add_called_then_raises_valueerror(
        self,
    ):
        """Should raise ValueError if input ends with a custom delimiter."""
        with self.assertRaises(ValueError):
            add_version8("//;\n1;2;")

    def test_given_negative_numbers_when_add_called_then_raises_valueerror_with_listed_negatives(
        self,
    ):
        """Should raise ValueError and display message listing all negative numbers."""
        with self.assertRaises(ValueError) as ctx:
            add_version8("1,-2,3")
        self.assertIn("Negative number(s) not allowed: -2", str(ctx.exception))

    def test_given_negative_and_mixed_delimiter_when_add_called_then_returns_multiple_error_messag(
        self,
    ):
        """
        Should detect multiple types of errors simultaneously.
        For example:
        “//|\n1|2,-3” should raise a ValueError with both messages:
        - Negative number(s) not allowed: -3
        - '|' expected but ',' found at position 3.
        """
        with self.assertRaises(ValueError) as ctx:
            add_version8("//|\n1|2,-3")

        self.assertEqual(
            str(ctx.exception),
            "Negative number(s) not allowed: -3\n'|' expected but ',' found at position 3.",
        )

    def test_given_custom_delimiter_and_large_numbers_when_add_called_then_ignores_number_over_1000(
        self,
    ):
        """Should ignore numbers greater than 1000 when calculating the sum."""
        self.assertEqual(add_version8("//;\n1;2;1001"), 3)

    def test_given_negative_numbers_with_custom_delimiter_when_add_called_then_raises_valueerror(
        self,
    ):
        """Should raise ValueError and list all negative numbers, even with custom delimiters."""
        with self.assertRaises(ValueError) as ctx:
            add_version8("//|\n1|2|-3")
        self.assertIn("Negative number(s) not allowed: -3", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
