# Python Mini Projects

A collection of Python projects built from scratch to learn core concepts.

## 1. Number Guessing Game
A CLI game where the computer picks a random number 
and the user guesses it with high/low hints.

**Concepts used:** loops, conditionals, random library, user input

## 2. Budget Tracker
A CLI app where user enters monthly income and expenses, 
then gets a complete financial summary with remaining balance.

**Concepts used:** dictionaries, loops, f-strings, float input, file handling, JSON

### 3. Currency Converter
A lightweight command-line utility built in Python that fetches real-time global exchange rates to convert Indian Rupees (INR) into any target currency instantly. This project demonstrates network programming, API integration, and dynamic JSON data parsing.

---

## 🚀 Key Features

* **Real-time Data:** Connects directly to a live exchange rate API over the internet.
* **No Hardcoded Rates:** Dynamically fetches up-to-the-minute global values every single time it executes.
* **User-Input Sanitization:** Automatically handles case-insensitive inputs (e.g., handles `usd` or `USD` seamlessly).
* **Robust Logic:** Validates currency codes before performing calculations to prevent runtime errors.

---

## 🛠️ Tech Stack & Concepts Explored

* **Language:** Python 3
* **Networking Library:** `requests` (HTTP client)
* **Data Format:** JSON (JavaScript Object Notation) parsed directly into a Python Dictionary.
* **Core Logic:** Conditional blocks (`if/else`), type-casting (`string` to `float`), and string formatting.

---

## 📦 How to Install and Run

### 1. Prerequisites
Make sure you have Python 3 installed on your machine.

### 2. Install Dependencies
This project utilizes the external third-party library `requests` to communicate with the web. Install it via your terminal:
```bash
pip install requests
