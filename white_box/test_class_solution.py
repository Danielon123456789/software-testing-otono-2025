# -*- coding: utf-8 -*-
"""
White-box unit testing solution.
"""
import unittest

from white_box.class_exercises import (
    ElevatorSystem,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    validate_credit_card,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
)


class TestWhiteBoxExercises(unittest.TestCase):
    """
    Exercises one, two and three.

    """

    # Answer check_number_status (1)

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

    # Answer validate_password (2)

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

    # Answer calculte_total_discount (3)

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

        # 20% descuento
        self.assertEqual(round(calculate_total_discount(750.50), 1), 150.1)

    # Answer calculte_order_total (4)


class TestcalculateOrderTotal(unittest.TestCase):
    """
    class to test calculate_order_total
    """

    def test_no_discount_quantity_1_to_5(self):
        """
        Items with quantity between 1 and 5 should have no discount.
        """
        items = [
            {"quantity": 1, "price": 10},  # 10
            {"quantity": 5, "price": 20},  # 100
        ]
        expected_total = 10 + 100
        self.assertEqual(calculate_order_total(items), expected_total)

    def test_5_percent_discount_quantity_6_to_10(self):
        """
        Items with quantity between 6 and 10 should have a 5% discount.
        """
        items = [
            {"quantity": 6, "price": 10},  # 6*10*0.95 = 57
            {"quantity": 10, "price": 5},  # 10*5*0.95 = 47.5
        ]
        expected_total = 57 + 47.5
        self.assertEqual(calculate_order_total(items), expected_total)

    def test_10_percent_discount_quantity_above_10(self):
        """
        Items with quantity greater than 10 should have a 10% discount.
        """
        items = [
            {"quantity": 11, "price": 10},  # 11*10*0.9 = 99
            {"quantity": 20, "price": 5},  # 20*5*0.9 = 90
        ]
        expected_total = 99 + 90
        self.assertEqual(calculate_order_total(items), expected_total)

    def test_mixed_items_various_discounts(self):
        """
        Order with mixed quantities should correctly apply different discounts.
        """
        items = [
            {"quantity": 2, "price": 50},  # 2*50 = 100 (no discount)
            {"quantity": 7, "price": 10},  # 7*10*0.95 = 66.5
            {"quantity": 15, "price": 5},  # 15*5*0.9 = 67.5
        ]
        expected_total = 100 + 66.5 + 67.5
        self.assertEqual(calculate_order_total(items), expected_total)

    def test_empty_order(self):
        """
        An empty order should return 0.
        """
        self.assertEqual(calculate_order_total([]), 0)

    def test_decimal_prices(self):
        """
        Items with decimal prices should be calculated precisely.
        """
        items = [
            {"quantity": 3, "price": 19.99},  # 3*19.99 = 59.97
            {"quantity": 8, "price": 5.55},  # 8*5.55*0.95 = 42.18
            {"quantity": 12, "price": 2.75},  # 12*2.75*0.9 = 29.7
        ]
        expected_total = round(59.97 + 42.18 + 29.7, 2)
        self.assertEqual(round(calculate_order_total(items), 2), expected_total)

    # Answer calculate_item_shipping_cost (5):


class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    class to test CalculateItemsShippingCost
    """

    def test_standard_shipping(self):
        """Standard shipping should apply correct cost by weight."""
        items = [{"weight": 2}, {"weight": 3}]  # total = 5
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

        items = [{"weight": 6}]  # total = 6
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

        items = [{"weight": 11}]  # total = 11
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping(self):
        """Express shipping should apply correct cost by weight."""
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        """Invalid shipping method should raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 3}], "premium")


class TestValidateLogin(unittest.TestCase):
    """
    class to test validateLogin
    """

    def test_valid_login(self):
        """Login is successful if username and password lengths are valid."""
        self.assertEqual(
            validate_login("username123", "password123"), "Login Successful"
        )

    def test_invalid_username_length(self):
        """Usernames too short or too long should fail."""
        self.assertEqual(validate_login("usr", "password123"), "Login Failed")
        self.assertEqual(validate_login("u" * 21, "password123"), "Login Failed")

    def test_invalid_password_length(self):
        """Passwords too short or too long should fail."""
        self.assertEqual(validate_login("username123", "short"), "Login Failed")
        self.assertEqual(validate_login("username123", "p" * 16), "Login Failed")


class TestVerifyAge(unittest.TestCase):
    """
    class to test VerifyAge
    """

    def test_eligible_age_range(self):
        """Age between 18 and 65 is eligible."""
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")

    def test_not_eligible_age(self):
        """Ages outside range should not be eligible."""
        self.assertEqual(verify_age(17), "Not Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """
    class to test CategorizeProduct
    """

    def test_category_a(self):
        """Category A"""
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_category_b(self):
        """Category B"""
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_category_c(self):
        """Category C"""
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_category_d(self):
        """Category D"""
        self.assertEqual(categorize_product(9), "Category D")
        self.assertEqual(categorize_product(201), "Category D")


class TestValidateEmail(unittest.TestCase):
    """
    class to test ValidateEmail
    """

    def test_valid_email(self):
        """Valid email should contain @ and . and length 5–50."""
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_invalid_length(self):
        """Emails too short or too long should be invalid."""
        self.assertEqual(validate_email("a@b"), "Invalid Email")
        self.assertEqual(validate_email("a" * 45 + "@test.com"), "Invalid Email")

    def test_missing_symbols(self):
        """Emails missing @ or . should be invalid."""
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    class to test CelsiusToFahrenheit
    """

    def test_valid_range_conversion(self):
        """Valid Celsius should convert correctly."""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_invalid_temperature(self):
        """Temperatures outside -100 to 100 are invalid."""
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")
        self.assertEqual(celsius_to_fahrenheit(150), "Invalid Temperature")


class TestValidateCreditCard(unittest.TestCase):
    """
    class to test CreditCard
    """

    def test_valid_card(self):
        """Valid credit cards must be 13–16 digits long."""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_invalid_length(self):
        """Cards shorter than 13 or longer than 16 digits should be invalid."""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")
        self.assertEqual(validate_credit_card("1" * 17), "Invalid Card")

    def test_invalid_characters(self):
        """Cards must contain only digits."""
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")


class TestElevatorSystem(unittest.TestCase):
    """
    class to test ElevatorSystem
    """

    def test_initial_state(self):
        """Elevator should start in Idle state."""
        elevator = ElevatorSystem()
        self.assertEqual(elevator.state, "Idle")

    def test_move_up_from_idle(self):
        """Elevator should move up when Idle."""
        elevator = ElevatorSystem()
        result = elevator.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(elevator.state, "Moving Up")

    def test_move_down_from_idle(self):
        """Elevator should move down when Idle."""
        elevator = ElevatorSystem()
        result = elevator.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(elevator.state, "Moving Down")

    def test_invalid_move_up_when_moving(self):
        """Cannot move up if already moving."""
        elevator = ElevatorSystem()
        elevator.move_up()  # now Moving Up
        result = elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Moving Up")

    def test_invalid_move_down_when_moving(self):
        """Cannot move down if already moving."""
        elevator = ElevatorSystem()
        elevator.move_down()  # now Moving Down
        result = elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Moving Down")

    def test_stop_from_moving_up(self):
        """Should stop correctly when moving up."""
        elevator = ElevatorSystem()
        elevator.move_up()
        result = elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")

    def test_stop_from_moving_down(self):
        """Should stop correctly when moving down."""
        elevator = ElevatorSystem()
        elevator.move_down()
        result = elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")

    def test_invalid_stop_from_idle(self):
        """Cannot stop when already Idle."""
        elevator = ElevatorSystem()
        result = elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Idle")
