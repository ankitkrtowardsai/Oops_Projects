from manager import LibraryManager
from utility import input_is_valid

class LibraryInterface:
    """Handles user interactions - UI layer"""
    def __init__(self):
        self.manager = LibraryManager()

    def display_menu(self):
        print("\nLibrary Menu:")
        options = [
            "1) Add Book",
            "2) View Books",
            "3) Search Book by Title",
            "4) Borrow Book",
            "5) Return Book",
            "6) Exit"
        ]
        print('\n'.join(options))
        return input_is_valid("Select an option: ", 1, len(options))

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == 1:
                self.manager.add_book()
            elif choice == 2:
                self.manager.view_books()
            elif choice == 3:
                self.manager.search_by_title()
            elif choice == 4:
                self.manager.borrow_book()
            elif choice == 5:
                self.manager.return_book()
            else:
                print("Exiting the system. Goodbye!")
                break
