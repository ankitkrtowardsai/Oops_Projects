from manager import BankManager
from utility import input_is_valid

class BankingInterface:
    """Handles user interface interactions"""
    def __init__(self):
        self.manager = BankManager()

    def display_menu(self):
        print("\nBanking System Menu:")
        options = [
            "1) Create Account",
            "2) View Accounts",
            "3) Deposit Funds",
            "4) Withdraw Funds",
            "5) Transfer Funds",
            "6) Exit"
        ]
        print('\n'.join(options))
        return input_is_valid("Choose an option: ", 1, len(options))

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == 1:
                self.manager.create_account()
            elif choice == 2:
                self.manager.view_accounts()
            elif choice == 3:
                self.manager.deposit()
            elif choice == 4:
                self.manager.withdraw()
            elif choice == 5:
                self.manager.transfer()
            else:
                print("Thank you for using the Banking System. Goodbye!")
                break