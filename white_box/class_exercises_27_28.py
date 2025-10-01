# -*- coding: utf-8 -*-
"""
White-box unit testing solution 27 y 28.
"""

import unittest
from unittest.mock import patch

from white_box.class_exercises import BankAccount, BankingSystem, Product, ShoppingCart


class TestwhiteBoxExercises27(unittest.TestCase):
    """
    Class created for test exercise 27.
    """

    def test_initialization(self):
        """
        Initialization's test.
        """
        account = BankAccount("12345", 1000)
        self.assertEqual(account.account_number, "12345")
        self.assertEqual(account.balance, 1000)

    def test_view_account(self):
        """
        view account's test.
        """
        account = BankAccount("12345", 1000)

        with patch("white_box.class_exercises.print") as mock_print:
            account.view_account()
            mock_print.assert_called_once_with(
                "The account 12345 has a balance of 1000"
            )


class TestWhiteBoxBankingSystems(unittest.TestCase):
    """
    Class created for test bankingSystems:
    """

    def test_initialization(self):
        """
        Initialization's test.
        """
        system = BankingSystem()
        self.assertEqual(system.users, {"user123": "pass123"})
        self.assertEqual(system.logged_in_users, set())

    def test_authenticate_success(self):
        """
        Successful login with correct credentials.
        """
        system = BankingSystem()
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.authenticate("user123", "pass123")
            self.assertIn("user123", system.logged_in_users)
            mock_print.assert_called_once_with(
                "User user123 authenticated successfully."
            )
            self.assertTrue(result)

    def test_authenticate_fail_wrong_password(self):
        """
        Fail login with wrong password.
        """
        system = BankingSystem()
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.authenticate("user123", "wrong")
            self.assertFalse(result)
            mock_print.assert_called_once_with("Authentication failed.")

    def test_authenticate_fail_unknown_user(self):
        """
        Fail login with unknown user.
        """
        system = BankingSystem()
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.authenticate("unknown", "pass")
            self.assertFalse(result)
            mock_print.assert_called_once_with("Authentication failed.")

    def test_authenticate_already_logged_in(self):
        """
        Same user tries to log in again.
        """
        system = BankingSystem()
        system.authenticate("user123", "pass123")
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.authenticate("user123", "pass123")
            self.assertFalse(result)
            mock_print.assert_called_once_with("User already logged in.")

    def test_transfer_success_regular(self):
        """
        Successful transfer with regular fee.
        """
        system = BankingSystem()
        system.authenticate("user123", "pass123")
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.transfer_money("user123", "receiver", 100, "regular")
            self.assertTrue(result)
            mock_print.assert_called_once_with(
                "Money transfer of $100 (regular transfer) from user123 "
                + "to receiver processed successfully."
            )

    def test_transfer_fail_not_authenticated(self):
        """
        Transfer attempt without login.
        """
        system = BankingSystem()
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.transfer_money("user123", "receiver", 100, "regular")
            self.assertFalse(result)
            mock_print.assert_called_once_with("Sender not authenticated.")

    def test_transfer_fail_invalid_type(self):
        """
        Transfer attempt with invalid type.
        """
        system = BankingSystem()
        system.authenticate("user123", "pass123")
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.transfer_money("user123", "receiver", 100, "fast")
            self.assertFalse(result)
            mock_print.assert_called_once_with("Invalid transaction type.")

    def test_transfer_fail_insufficient_funds(self):
        """
        Transfer attempt with insufficient funds.
        """
        system = BankingSystem()
        system.authenticate("user123", "pass123")
        with patch("white_box.class_exercises.print") as mock_print:
            result = system.transfer_money("user123", "receiver", 2000, "regular")
            self.assertFalse(result)
            mock_print.assert_called_once_with("Insufficient funds.")


class TestWhiteBoxProduct(unittest.TestCase):
    """
    Class created for test Product.
    """

    def test_initialization(self):
        """
        Initialization's test.
        """
        product = Product("Laptop", 1500)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1500)

    def test_view_product(self):
        """
        View product's test.
        """
        product = Product("Phone", 800)
        with patch("white_box.class_exercises.print") as mock_print:
            result = product.view_product()
            mock_print.assert_called_once_with("The product Phone has a price of 800")
            self.assertEqual(result, "The product Phone has a price of 800")


class TestWhiteBoxShoppingCart(unittest.TestCase):
    """
    Class created for test ShoppingCart.
    """

    def test_initialization(self):
        """
        Initialization's test.
        """
        cart = ShoppingCart()
        self.assertEqual(cart.items, [])

    def test_add_product_new(self):
        """
        Add a new product to the cart.
        """
        cart = ShoppingCart()
        product = Product("Book", 20)
        cart.add_product(product, 2)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product)
        self.assertEqual(cart.items[0]["quantity"], 2)

    def test_add_product_existing(self):
        """
        Add more quantity to an existing product.
        """
        cart = ShoppingCart()
        product = Product("Pen", 5)
        cart.add_product(product, 1)
        cart.add_product(product, 3)  # increase quantity
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["quantity"], 4)

    def test_remove_product_partial(self):
        """
        Remove part of the quantity of a product.
        """
        cart = ShoppingCart()
        product = Product("Notebook", 50)
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        self.assertEqual(cart.items[0]["quantity"], 3)

    def test_remove_product_all(self):
        """
        Remove all quantity of a product.
        """
        cart = ShoppingCart()
        product = Product("Tablet", 300)
        cart.add_product(product, 2)
        cart.remove_product(product, 2)
        self.assertEqual(cart.items, [])

    def test_view_cart(self):
        """
        View cart's test.
        """
        cart = ShoppingCart()
        product = Product("Mouse", 25)
        cart.add_product(product, 2)
        with patch("white_box.class_exercises.print") as mock_print:
            cart.view_cart()
            mock_print.assert_called_once_with("2 x Mouse - $50")

    def test_checkout(self):
        """
        Checkout's test.
        """
        cart = ShoppingCart()
        product1 = Product("Keyboard", 100)
        product2 = Product("Monitor", 300)
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)

        with patch("white_box.class_exercises.print") as mock_print:
            cart.checkout()
            mock_print.assert_any_call("Total: $700")
            mock_print.assert_any_call("Checkout completed. Thank you for shopping!")
