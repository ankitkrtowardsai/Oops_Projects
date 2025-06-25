# 💳 Banking System - Python OOP Project

A clean and modular **console-based banking application** built with Python, showcasing **Object-Oriented Programming (OOP)** concepts in action.

This project is crafted for **students and learners** who want to understand how OOP principles like inheritance, polymorphism, abstraction, and encapsulation are applied in a real-world context like a banking system.

---

## 🚀 Features

- 🧾 Create **Savings** or **Current** accounts
- 💰 Deposit funds
- 🏧 Withdraw funds (with overdraft in current accounts)
- 🔄 Transfer money between accounts
- 📋 View all accounts with details
- 🧼 Console-based menu for interaction

---

## 🧠 OOP Concepts Covered

| Concept           | Implementation Example                                                                 |
|------------------|------------------------------------------------------------------------------------------|
| **Class & Object**     | Classes like `Account`, `BankManager`, `SavingsAccount`, etc.                       |
| **Encapsulation**      | Sensitive data like balance is private and accessed via methods and properties     |
| **Inheritance**        | `SavingsAccount` and `CurrentAccount` inherit from `Account`                        |
| **Abstraction**        | `Account` is an abstract class using `abc.ABC` and `@abstractmethod`               |
| **Polymorphism**       | `withdraw()` behaves differently in `CurrentAccount` to allow overdraft            |
| **Composition**        | `BankManager` contains and manages multiple `Account` objects                      |
| **Separation of Concerns** | UI (interface), Logic (manager), Data Models (models), Utilities (input validation) |

---

## 📂 Project Structure

```

BankingSystem/
├── main.py            # 🚀 Application entry point
├── interface.py       # 🖥️ Menu interface logic
├── manager.py         # 🧠 Core banking logic (create, deposit, withdraw, transfer)
├── models.py          # 📦 Account classes and hierarchy
├── utility.py         # 🛠️ Input validation helper
└── README.md          # 📘 Project documentation

````

---

## 🔎 Module Breakdown

### 🔹 `main.py`
- Starts the app by invoking the `BankingInterface`.

### 🔹 `interface.py`
- Provides a user-friendly CLI (Command Line Interface).
- Receives menu choices and forwards them to `BankManager`.

### 🔹 `manager.py`
- Manages all business logic:
  - Create accounts
  - Deposit & withdraw
  - Transfer between accounts
  - Find account by number

### 🔹 `models.py`
- Uses **Abstract Base Class** `Account` with:
  - Common methods: `deposit()`, `withdraw()`, `details()`
  - Polymorphic behavior (e.g., `withdraw` overridden in `CurrentAccount`)
- Random account number generation for realism.

### 🔹 `utility.py`
- Provides a helper function:
```python
def input_is_valid(msg, start, end)
````

* Ensures valid menu input.

---

## 💡 Sample Console Interaction

```
Banking System Menu:
1) Create Account
2) View Accounts
3) Deposit Funds
4) Withdraw Funds
5) Transfer Funds
6) Exit

Choose an option: 1
Enter account holder name: Alice
Type (savings/current): savings
Initial deposit: 1000
Account created successfully. Account Number: 48213
```

---

## ✅ Learning Outcomes

By building and experimenting with this project, you’ll be able to:

* Understand **how OOP models real-world banking problems**
* Apply **inheritance and abstraction** to categorize account types
* Enforce **data integrity and encapsulation**
* Write clean and modular **Pythonic code**

---

## 📈 Possible Enhancements

* Store accounts in a file (CSV/JSON) for persistence
* Add user login system
* Add transaction history
* Add interest calculation in savings accounts
* Build a GUI with `tkinter` or `PyQt`

---

## 👨‍🎓 Perfect For

* Python beginners who’ve learned OOP and want to apply it
* B.Tech / CS / IT students preparing for interviews or internships
* Teachers & mentors explaining real-world use cases of OOP

---

## 📬 Feedback or Contributions?

Raise an issue or share your ideas to improve the project!
Pull requests are always welcome.

---

**Happy Coding & Learning Python! 🐍🚀**
