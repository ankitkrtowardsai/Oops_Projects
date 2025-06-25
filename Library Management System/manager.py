from models import Book, EBook, PrintedBook, Borrower
from utility import input_is_valid

class LibraryManager:
    """Handles business logic of managing books - BLL layer"""
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self):
        print("Add Book:")
        title = input("Title: ")
        author = input("Author: ")
        book_type = input("Type (ebook/printed): ").strip().lower()

        if book_type == 'ebook':
            size = float(input("File size in MB: "))
            book = EBook(title, author, size)
        else:
            weight = float(input("Weight in grams: "))
            book = PrintedBook(title, author, weight)

        self.books.append(book)
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book.get_info())

    def search_by_title(self):
        title = input("Enter title to search: ")
        found = [book for book in self.books if book.title.lower() == title.lower()]
        if not found:
            print("Book not found.")
        else:
            for book in found:
                print(book.get_info())

    def borrow_book(self):
        name = input("Your name: ")
        title = input("Enter book title to borrow: ")
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.borrow()
                borrower = Borrower(name, book)
                self.borrowers.append(borrower)
                print(f"{name} successfully borrowed '{book.title}'.")
                return
        print("Book is either unavailable or already borrowed.")

    def return_book(self):
        name = input("Your name: ")
        title = input("Enter book title to return: ")
        for borrower in self.borrowers:
            if borrower.name == name and borrower.book.title.lower() == title.lower():
                borrower.book.return_book()
                self.borrowers.remove(borrower)
                print(f"{name} returned '{title}'.")
                return
        print("No matching borrowed record found.")