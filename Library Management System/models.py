from abc import ABC, abstractmethod

class Book(ABC):
    """Abstract base class to demonstrate Abstraction & Polymorphism"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    @abstractmethod
    def get_info(self):
        pass

class EBook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

    def get_info(self):
        return f"[EBook] '{self.title}' by {self.author}, Size: {self.size}MB, Borrowed: {self.is_borrowed}"

class PrintedBook(Book):
    def __init__(self, title, author, weight):
        super().__init__(title, author)
        self.weight = weight

    def get_info(self):
        return f"[PrintedBook] '{self.title}' by {self.author}, Weight: {self.weight}g, Borrowed: {self.is_borrowed}"

class Borrower:
    """Demonstrates composition: Borrower has a Book"""
    def __init__(self, name, book):
        self.name = name
        self.book = book
