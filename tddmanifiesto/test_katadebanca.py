# -*- coding: utf-8 -*-
"""
Pytest Data-Driven para la Kata 6 - Banking Kata.
Implementación con @pytest.mark.parametrize.
Estructura Given-When-Then.
"""
# pylint: disable=import-error
import pytest

from tddmanifiesto.class_katadebanca import (
    Account,
    iteration1_deposit,
    iteration2_withdraw,
    iteration3_print_statement,
)


@pytest.mark.parametrize(
    "amount, date, expected_balance",
    [
        (1000, "01/04/2014", 1000),
        (500, "10/04/2014", 500),
    ],
)
def test_given_deposit_when_iteration1_deposit_called_then_increase(
    amount, date, expected_balance
):
    """Iteración 1: Depósito incrementa el balance."""
    account = Account()
    iteration1_deposit(account, amount, date)
    assert account.balance == expected_balance


@pytest.mark.parametrize(
    "actions, expected_balance",
    [
        ([("deposit", 1000, "01/04/2014"), ("withdraw", 100, "02/04/2014")], 900),
        ([("deposit", 500, "10/04/2014"), ("withdraw", 200, "11/04/2014")], 300),
    ],
)
def test_given_deposits_and_withdrawa_when_iteration2_called_then_update(
    actions, expected_balance
):
    """Iteración 2: Retiros y depósitos actualizan el balance."""
    account = Account()
    for action, amount, date in actions:
        if action == "deposit":
            iteration1_deposit(account, amount, date)
        elif action == "withdraw":
            iteration2_withdraw(account, amount, date)
    assert account.balance == expected_balance


@pytest.mark.parametrize(
    "actions, expected_statement",
    [
        (
            [
                ("deposit", 1000, "01/04/2014"),
                ("withdraw", 100, "02/04/2014"),
                ("deposit", 500, "10/04/2014"),
            ],
            (
                "DATE       | AMOUNT  | BALANCE\n"
                "10/04/2014 | 500.00 | 1400.00\n"
                "02/04/2014 | -100.00 | 900.00\n"
                "01/04/2014 | 1000.00 | 1000.00"
            ),
        ),
    ],
)
def test_given_trans_when_iteration3_print_called_then_returns_format(
    actions, expected_statement
):
    """Iteración 3: Imprime el estado de cuenta con formato correcto."""
    account = Account()
    for action, amount, date in actions:
        if action == "deposit":
            iteration1_deposit(account, amount, date)
        elif action == "withdraw":
            iteration2_withdraw(account, amount, date)

    statement = iteration3_print_statement(account)
    assert statement == expected_statement


@pytest.mark.parametrize(
    "actions, expected_balance",
    [
        (
            [
                ("deposit", 1000, "01/04/2014"),
                ("withdraw", 100, "02/04/2014"),
                ("deposit", 500, "10/04/2014"),
            ],
            1400,
        ),
    ],
)
def test_given_full_sequence_when_final_account_used_then_balance(
    actions, expected_balance
):
    """Versión final: flujo completo de operaciones bancarias."""
    account = Account()
    for action, amount, date in actions:
        if action == "deposit":
            account.deposit(amount, date)
        elif action == "withdraw":
            account.withdraw(amount, date)

    assert account.balance == expected_balance
    statement = account.print_statement()
    assert "DATE       | AMOUNT  | BALANCE" in statement
