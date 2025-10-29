# -*- coding: utf-8 -*-
"""
Kata 6 - Banking Kata.
Implementación incremental siguiendo el manifiesto TDD.
Cada versión cumple con un requisito diferente.
"""


class Account:
    """Clase principal para manejar una cuenta bancaria."""

    def __init__(self):
        """Inicializa la cuenta con balance y lista de transacciones."""
        self.balance = 0
        self.transactions = []

    def deposit(self, amount: int, date: str):
        """Iteración 1: Depositar dinero en la cuenta."""
        self.balance += amount
        self.transactions.append((date, amount, self.balance))

    def withdraw(self, amount: int, date: str):
        """Iteración 2: Retirar dinero de la cuenta."""
        self.balance -= amount
        self.transactions.append((date, -amount, self.balance))

    def print_statement(self) -> str:
        """
        Iteración 3: Imprimir el estado de cuenta.
        Retorna un string en formato de columnas.
        """
        statement_lines = ["DATE       | AMOUNT  | BALANCE"]
        for date, amount, balance in reversed(self.transactions):
            statement_lines.append(f"{date} | {amount:.2f} | {balance:.2f}")
        statement = "\n".join(statement_lines)
        print(statement)
        return statement


def iteration1_deposit(account, amount, date):
    """Depósito básico."""
    account.deposit(amount, date)
    return account.balance


def iteration2_withdraw(account, amount, date):
    """Depósito y retiro básico."""
    account.withdraw(amount, date)
    return account.balance


def iteration3_print_statement(account):
    """Impresión del estado de cuenta."""
    return account.print_statement()
