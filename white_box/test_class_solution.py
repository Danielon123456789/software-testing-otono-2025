# -*- coding: utf-8 -*-
"""
White-box unit testing solution.
"""
import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    UserAuthentication,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
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
        """Valid credit cards must be 13-16 digits long."""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_invalid_length(self):
        """Cards shorter than 13 or longer than 16 digits should be invalid."""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")
        self.assertEqual(validate_credit_card("1" * 17), "Invalid Card")

    def test_invalid_characters(self):
        """Cards must contain only digits."""
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """
    Class to test validate_date
    """

    def test_valid_dates(self):
        """Valid years, months, and days should return 'Valid Date'."""
        self.assertEqual(validate_date(2000, 1, 1), "Valid Date")

    def test_invalid_years(self):
        """Years outside 1900-2100 should return 'Invalid Date'."""
        self.assertEqual(validate_date(1899, 6, 15), "Invalid Date")
        self.assertEqual(validate_date(2101, 6, 15), "Invalid Date")

    def test_invalid_months(self):
        """Months outside 1-12 should return 'Invalid Date'."""
        self.assertEqual(validate_date(2023, 0, 10), "Invalid Date")
        self.assertEqual(validate_date(2023, 13, 10), "Invalid Date")

    def test_invalid_days(self):
        """Days outside 1-31 should return 'Invalid Date'."""
        self.assertEqual(validate_date(2023, 5, 0), "Invalid Date")
        self.assertEqual(validate_date(2023, 5, 32), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """
    class to test check_flight_eligibility
    """

    def test_eligible_age(self):
        """Ages between 18-65 should be eligible."""
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_not_eligible_age(self):
        """Ages below 18 or above 65 should not be eligible."""
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

    def test_frequent_flyer_override(self):
        """Frequent flyers should always be eligible regardless of age."""
        self.assertEqual(check_flight_eligibility(15, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(80, True), "Eligible to Book")


class TestValidateURL(unittest.TestCase):
    """
    class to test validate_url
    """

    def test_valid_http_urls(self):
        """URLs starting with http:// or https:// and <=255 chars are valid."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")
        self.assertEqual(validate_url("https://example.org/page?id=1"), "Valid URL")

    def test_invalid_prefix(self):
        """URLs without valid prefix should be invalid."""
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")
        self.assertEqual(validate_url("www.example.com"), "Invalid URL")

    def test_invalid_length(self):
        """URLs longer than 255 characters should be invalid."""
        long_url = "http://" + "a" * 250
        self.assertEqual(validate_url(long_url), "Invalid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    class to test calculate_quantity_discount
    """

    def test_no_discount_boundary(self):
        """Quantities at or below 5 should return 'No Discount'."""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_5_percent_discount_boundary(self):
        """Quantities from 6 to 10 should return '5% Discount'."""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_10_percent_discount_boundary(self):
        """Quantities above 10 should return '10% Discount'."""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


class TestCheckFileSize(unittest.TestCase):
    """
    class to test check_file_size
    """

    def test_valid_file_size_boundary(self):
        """File sizes between 0 and 1MB (inclusive) should be valid."""
        self.assertEqual(check_file_size(0), "Valid File Size")
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_invalid_file_size_boundary(self):
        """File sizes below 0 or above 1MB should be invalid."""
        self.assertEqual(check_file_size(-1), "Invalid File Size")  # below lower limit
        self.assertEqual(
            check_file_size(1048577), "Invalid File Size"
        )  # above upper limit


class TestCheckLoanEligibility(unittest.TestCase):
    """
    class to test check_loan_eligibility
    """

    def test_not_eligible_low_income(self):
        """Income below 30000 should not be eligible."""
        self.assertEqual(check_loan_eligibility(25000, 800), "Not Eligible")

    def test_standard_or_secured_for_mid_income(self):
        """Income between 30000 and 60000: depends on credit score."""
        self.assertEqual(check_loan_eligibility(40000, 710), "Standard Loan")
        self.assertEqual(check_loan_eligibility(40000, 650), "Secured Loan")

    def test_high_income_premium_or_standard(self):
        """High income (>60000): premium if credit_score > 750, otherwise standard."""
        self.assertEqual(check_loan_eligibility(70000, 760), "Premium Loan")
        self.assertEqual(check_loan_eligibility(70000, 740), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """
    class to test calculate_shipping_cost
    """

    def test_small_package(self):
        """Small and light packages should cost 5."""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package(self):
        """Medium packages should cost 10."""
        self.assertEqual(calculate_shipping_cost(3, 15, 20, 25), 10)

    def test_large_package(self):
        """Large or heavy packages should cost 20."""
        self.assertEqual(calculate_shipping_cost(6, 40, 50, 60), 20)


class TestGradeQuiz(unittest.TestCase):
    """
    class to test grade_quiz
    """

    def test_pass(self):
        """At least 7 correct and at most 2 incorrect should pass."""
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_conditional_pass(self):
        """Between 5-6 correct and ≤3 incorrect should be conditional pass."""
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_fail(self):
        """Other cases should fail."""
        self.assertEqual(grade_quiz(4, 3), "Fail")


class TestAuthenticateUser(unittest.TestCase):
    """
    class to test authenticate_user
    """

    def test_admin_credentials(self):
        """Admin credentials should authenticate as Admin."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_valid_user_credentials(self):
        """Valid credentials (not admin) should authenticate as User."""
        self.assertEqual(authenticate_user("daniel", "mypassword"), "User")

    def test_invalid_credentials(self):
        """Short username or password should be invalid."""
        self.assertEqual(authenticate_user("usr", "12345678"), "Invalid")
        self.assertEqual(authenticate_user("daniel", "short"), "Invalid")


class TestGetWeatherAdvisory(unittest.TestCase):
    """
    class to test get_weather_advisory
    """

    def test_valid_temperature_humidity(self):
        """Valid temperature and humidity"""
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_invalid_temperature_humidity(self):
        """Invalid temperature and humidity"""
        self.assertEqual(get_weather_advisory(31, 70), "No Specific Advisory")

    def test_low_temperature(self):
        """Invalid temperature and humidity"""
        self.assertEqual(get_weather_advisory(-1, 71), "Low Temperature. Bundle Up!")


class TestUserAuthentication(unittest.TestCase):
    """
    class to test UserAuthentication
    """

    def setUp(self):
        """Initialize a new UserAuthentication object before each test."""
        self.auth = UserAuthentication()

    def test_initial_state(self):
        """Initial state should be 'Logged Out'."""
        self.assertEqual(self.auth.state, "Logged Out")

    def test_successful_login(self):
        """Login from 'Logged Out' should change state to 'Logged In'."""
        result = self.auth.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_invalid_login_when_logged_in(self):
        """Login when already 'Logged In' should be invalid."""
        self.auth.login()
        result = self.auth.login()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged In")

    def test_successful_logout(self):
        """Logout from 'Logged In' should change state to 'Logged Out'."""
        self.auth.login()
        result = self.auth.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_invalid_logout_when_logged_out(self):
        """Logout when already 'Logged Out' should be invalid."""
        result = self.auth.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged Out")


class TestDocumentEditingSystem(unittest.TestCase):
    """
    class to test DocumentEditingSystem
    """

    def setUp(self):
        """Initialize a new DocumentEditingSystem object before each test."""
        self.doc = DocumentEditingSystem()

    def test_initial_state(self):
        """Initial state should be 'Editing'."""
        self.assertEqual(self.doc.state, "Editing")

    def test_successful_save(self):
        """Saving from 'Editing' should change state to 'Saved'."""
        result = self.doc.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.doc.state, "Saved")

    def test_invalid_save_when_already_saved(self):
        """Saving when already 'Saved' should be invalid."""
        self.doc.save_document()
        result = self.doc.save_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Saved")

    def test_successful_edit_after_save(self):
        """Editing from 'Saved' should return to 'Editing'."""
        self.doc.save_document()
        result = self.doc.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.doc.state, "Editing")

    def test_invalid_edit_when_editing(self):
        """Editing when already 'Editing' should be invalid."""
        result = self.doc.edit_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Editing")


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
