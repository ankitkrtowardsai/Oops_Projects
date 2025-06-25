from models import Account, SavingsAccount, CurrentAccount
from utility import input_is_valid

class BankManager:
    """Manages accounts and transactions"""
    def __init__(self):
        self.accounts = []

    def create_account(self):
        print("\n-- Create Account --")
        name = input("Enter account holder name: ")
        account_type = input("Type (savings/current): ").strip().lower()
        initial_deposit = float(input("Initial deposit: "))

        if account_type == 'savings':
            account = SavingsAccount(name, initial_deposit)
        else:
            account = CurrentAccount(name, initial_deposit)

        self.accounts.append(account)
        print(f"Account created successfully. Account Number: {account.account_number}")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def view_accounts(self):
        print("\n-- All Accounts --")
        if not self.accounts:
            print("No accounts to show.")
        for acc in self.accounts:
            print(acc.details())

    def deposit(self):
        acc_num = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        acc = self.find_account(acc_num)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self):
        acc_num = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        acc = self.find_account(acc_num)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self):
        from_acc_num = int(input("Enter sender's account number: "))
        to_acc_num = int(input("Enter recipient's account number: "))
        amount = float(input("Enter amount to transfer: "))

        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)

        if from_acc and to_acc:
            if from_acc.withdraw(amount):
                to_acc.deposit(amount)
                print("Transfer successful.")
        else:
            print("One or both accounts not found.")