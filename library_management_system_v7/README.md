# Library Management System V7

A full-stack library management web application built with **Python, Flask, SQLite, HTML, CSS, and Jinja2**.

The project started as a Python CLI-based library management system and was gradually developed into a web application with database integration, CRUD operations, user authentication, and deployment.

## 🚀 Live Demo

**Live Application:**
https://library-management-system-v7.onrender.com

> Note: The application is hosted on Render's free tier, so the service may take some time to wake up after a period of inactivity.

## 📌 Features

### Book Management

* Add new books
* View all books
* Search books by title
* Edit book details
* Delete books
* Prevent duplicate books
* Validate required fields

### Authentication

* User registration
* Secure password hashing using Werkzeug
* User login and logout
* Session-based authentication
* Protected routes
* Invalid login handling
* Duplicate username handling

### Database

The application uses **SQLite** for persistent application data during local development.

#### Books Table

* `id`
* `title`
* `author`
* `edition`
* `publisher`

#### Users Table

* `id`
* `username`
* `password_hash`

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **SQLite**
* **Jinja2**
* **HTML5**
* **CSS3**
* **Werkzeug**
* **python-dotenv**
* **Gunicorn**
* **Git & GitHub**
* **Render**

## 📂 Project Structure

```text
library_management_system_v7/
│
├── app.py
├── library.py
├── books.db
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── books.html
│   ├── login.html
│   ├── register.html
│   └── edit_book.html
│
└── static/
    └── style.css
```

> `books.db` and `.env` are excluded from Git using `.gitignore`.

## 🔐 Security

The application includes basic authentication and security practices:

* Passwords are stored as hashes rather than plain text.
* Flask sessions are used to maintain authentication state.
* Secret configuration is loaded through environment variables.
* `.env` and database files are excluded from version control.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ShristiAnjana-bit/python-mini-projects.git
```

### 2. Navigate to the project

```bash
cd python-mini-projects/library_management_system_v7
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

Add:

```text
SECRET_KEY=your-secret-key
```

Use your own secret key. Do not commit the `.env` file to GitHub.

### 7. Run the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## 🔄 Development Journey

The project was developed incrementally:

**V1 → Basic Python Library System**

**V2–V5 → Feature improvements and JSON-based storage**

**V6 → SQLite database integration**

**V7 → Flask web application**

V7 introduced:

* Web interface
* SQLite database
* CRUD operations
* Search
* User registration
* Password hashing
* Login/logout
* Session authentication
* Flash messages
* Environment variables
* Production server
* Deployment

## 🎯 What I Learned

Through this project, I practiced:

* Python application structure
* Object-oriented programming
* SQLite and SQL queries
* CRUD operations
* Flask routing
* GET and POST requests
* HTML forms
* Jinja2 templates
* Authentication and sessions
* Password hashing
* Environment variables
* Git and GitHub
* Deployment with Render
* Debugging real application errors

## 🔮 Future Improvements

Possible future improvements include:

* PostgreSQL for production database storage
* Role-based access control
* Pagination
* Better search and filtering
* Book cover images
* User-specific book management
* Improved UI/UX
* Automated tests
* CSRF protection
* Production-grade database management

## 👩‍💻 Author

**Shristi Anjana**

GitHub:
https://github.com/ShristiAnjana-bit

---

### Project Status

**V7 — Deployed and functional 🚀**
