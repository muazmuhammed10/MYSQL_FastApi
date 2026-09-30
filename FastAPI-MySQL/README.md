FastAPI MySQL Learning Project

A beginner-friendly REST API built with **FastAPI, MySQL, SQLAlchemy ORM, PyMySQL, and Pydantic**.

The project demonstrates how to build a CRUD API connected to a real MySQL database using SQLAlchemy ORM.

 Features

 FastAPI REST API
 MySQL database integration
 SQLAlchemy ORM
 Pydantic request validation
 User CRUD operations
 Duplicate email validation
 Swagger API documentation

 Technologies

 Python FastAPI Uvicorn MySQL SQLAlchemy PyMySQL Pydantic

📁 Project Structure

    FastAPI-MySQL/
    ├── main.py
    ├── database.py
    ├── model.py
    ├── schemas.py
    ├── create_tables.py
    ├── requirements.txt
    └── .gitignore

 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Test API |
| GET | `/users` | Get all users |
| GET | `/users/{id}` | Get one user |
| POST | `/users` | Create user |
| PUT | `/users/{id}` | Update user |
| DELETE | `/users/{id}` | Delete user |

 Database

Database: `fastapi_learning`
Table: `users`
Columns:
- `id`
- `name`
- `email`
Email addresses are unique.
 Locally
 1. Create and activate virtual environment

    py -m venv venv
    venv\Scripts\Activate.ps1

 2. Install dependencies

    python -m pip install -r requirements.txt

 3. Start MySQL

Start MySQL from **XAMPP** and create:

    fastapi_learning

 4. Create the table

    python create_tables.py

 5. Start FastAPI

    python -m uvicorn main:app --reload

Open Swagger:

    http://127.0.0.1:8000/docs

 What I Learned

 Building REST APIs with FastAPI
 Connecting FastAPI to MySQL
 SQLAlchemy ORM
 Database sessions and dependencies
 Pydantic validation
 CRUD operations
 Git and GitHub



**Muaz Mohammed**

Software Engineering Student | Full-Stack Developer | AI/ML & Cybersecurity Enthusiast
