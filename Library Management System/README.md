# 📚 Library Management System - Python OOP Project

A clean, modular, and interactive console-based application to manage library books using Python's **Object-Oriented Programming (OOP)** principles.  
This project is built for **learning and demonstrating OOP concepts**, structured to reflect **real-world design patterns** and **best practices**.

---

## 🚀 Features

- 📖 Add books (EBook or Printed Book)
- 🔍 Search books by title
- 📚 View all available books
- 📥 Borrow a book
- 📤 Return a book
- 🧼 Menu-based interface for interaction

---

## 🧠 OOP Concepts Covered

| Concept               | How It's Demonstrated                                                                 |
|------------------------|--------------------------------------------------------------------------------------|
| **Class & Object**     | Classes like `Book`, `Borrower`, `LibraryManager`, etc.                             |
| **Encapsulation**      | Attributes are kept private or managed inside each class                            |
| **Inheritance**        | `EBook` and `PrintedBook` inherit from the abstract `Book` class                    |
| **Abstraction**        | `Book` is an abstract base class using `abc.ABC` with an abstract method `get_info()` |
| **Polymorphism**       | Different `Book` types implement `get_info()` differently                          |
| **Composition**        | `Borrower` class contains a reference to a `Book` object                            |
| **Separation of Concerns** | Files are modular: UI, logic, models, and utilities are separated                    |

---

## 🗂️ Project Structure

```

LibraryManagementSystem/
│
├── main.py               # 🚀 Entry point of the application
├── interface.py          # 🖥️ User interface layer (menu, options)
├── manager.py            # 🧠 Business logic (add/search/borrow/return books)
├── models.py             # 📦 Data models for books and borrowers
├── utility.py            # 🛠️ Input validation helper function
└── README.md             # 📘 Project documentation

````

---

## 🏗️ Module Breakdown

### 🔹 `main.py`
- Initializes and starts the application.
```python
from interface import LibraryInterface
...
interface = LibraryInterface()
interface.run()
````

### 🔹 `interface.py`

* Handles user interaction via console.
* Shows menu options and accepts input.
* Delegates tasks to `LibraryManager`.

### 🔹 `manager.py`

* Core logic layer.
* Maintains list of books and borrowers.
* Methods:

  * `add_book()`
  * `view_books()`
  * `search_by_title()`
  * `borrow_book()`
  * `return_book()`

### 🔹 `models.py`

* **Defines all classes and OOP relationships**.
* Uses:

  * `Book` (abstract class with `@abstractmethod`)
  * `EBook` and `PrintedBook` (concrete subclasses)
  * `Borrower` (has-a relationship with `Book`)
* Encapsulates all attributes and behaviors.
* Demonstrates polymorphism via `get_info()`.

### 🔹 `utility.py`

* Contains:

```python
def input_is_valid(msg, start, end)
```

* Ensures user selects valid menu choices.

---

## 💡 Sample Usage (Console)

```
Library Menu:
1) Add Book
2) View Books
3) Search Book by Title
4) Borrow Book
5) Return Book
6) Exit

Select an option: 1
Title: Python 101
Author: John Doe
Type (ebook/printed): ebook
File size in MB: 2.4
```

---

## 🛠 How to Run

```bash
python main.py
```

Make sure all files are in the same directory.

---

## 📌 Enhancement Ideas

* Save and load data from a file (e.g., JSON or CSV)
* Add return due date & fine system
* Add librarian/admin authentication
* Implement GUI using `tkinter` or `PyQt`
* Add search by author/genre

---

## ✅ Learning Outcomes

By completing and experimenting with this project, you'll deeply understand:

* How OOP models real-world problems
* How to organize code cleanly using classes and modular files
* Design patterns like composition and inheritance
* Practical use of abstraction and polymorphism

---

## 👨‍🏫 Ideal For

* Python beginners who just learned OOP
* Students preparing for interviews or coding assignments
* Teachers explaining OOP through real-world applications

---

## 📬 Feedback or Doubts?

Feel free to raise an issue or reach out for improvements or suggestions!

---

**Happy Coding & Learning! 🚀**

