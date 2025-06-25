from abc import ABC, abstractmethod
import random

class Account(ABC):
    """Abstract Account class for base functionality"""
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self.account_number = random.randint(10000, 99999)

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def details(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            print(f"Withdrawn: {amount}. Remaining balance: {self._balance}")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

class SavingsAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.interest_rate = 0.04  # example

    def details(self):
        return f"[Savings] {self.name} | Acct: {self.account_number} | Balance: {self._balance}"

class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.overdraft_limit = 500

    def withdraw(self, amount):
        if amount > 0 and self._balance + self.overdraft_limit >= amount:
            self._balance -= amount
            print(f"Withdrawn: {amount}. Remaining balance: {self._balance}")
            return True
        else:
            print("Overdraft limit exceeded or invalid amount.")
            return False

    def details(self):
        return f"[Current] {self.name} | Acct: {self.account_number} | Balance: {self._balance}"