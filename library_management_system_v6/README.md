# 📚 Library Management System — Version 0.6

A command-line Library Management System built using Python and SQLite.

## 🚀 What's New in Version 0.6?

Version 0.6 replaces the JSON-based storage from Version 0.5 with a SQLite database.

### Version 0.6 Features

- Add a book
- View all books
- Search for a book
- Remove a book
- Update a book
- Duplicate book checking
- Input validation
- SQLite database storage
- Automatic database and table creation

## 🗄️ Database

This version uses SQLite.

**Database file:**

`books.db`

**Table:**

`books`

The `books` table contains:

| Column | Type |
|---|---|
| id | INTEGER |
| title | TEXT |
| author | TEXT |
| edition | TEXT |
| publisher | TEXT |

## 🧠 SQL Concepts Used

During Version 0.6, I learned and implemented:

- `CREATE TABLE`
- `INSERT`
- `SELECT`
- `WHERE`
- `UPDATE`
- `DELETE`
- `fetchone()`
- `fetchall()`
- `commit()`
- `rowcount`
- Parameterized SQL queries

## 📂 Project Structure

```text
library_management_system_v6/
│
├── library.py
├── main.py
├── books.db
└── README.md
```

### `library.py`

Contains the main library logic and database operations.

### `main.py`

Contains the menu and user interaction.

## ▶️ How to Run

Make sure Python is installed.

Run:

```bash
python main.py
```

## 🛠️ Technologies Used

- Python
- SQLite
- SQL
- Git & GitHub

## 📌 Version History

- Version 0.5 — JSON-based storage
- Version 0.6 — SQLite database integration

---

### 🎯 Learning Goal

This project is being developed step-by-step to improve my Python, OOP, SQL, database, and backend development skills.