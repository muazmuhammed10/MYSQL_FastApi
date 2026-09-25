# FastAPI MySQL Learning Project

A beginner-friendly backend project built with FastAPI, MySQL, SQLAlchemy, PyMySQL, and Pydantic.

This project demonstrates how to build a REST API and connect it to a real MySQL database.

## 🚀 Features

- FastAPI REST API
- MySQL database integration
- SQLAlchemy database connection
- Pydantic request validation
- User CRUD operations
- Duplicate email checking
- Swagger API documentation

## 🛠️ Technologies

- Python
- FastAPI
- Uvicorn
- MySQL
- SQLAlchemy
- PyMySQL
- Pydantic
- Git & GitHub

## 📁 Project Structure

    FastAPI-MySQL-Learning/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── create_tables.py
    ├── requirements.txt
    └── .gitignore

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Test API |
| GET | /users | Get all users |
| GET | /users/{id} | Get one user |
| POST | /users | Create user |
| PUT | /users/{id} | Update user |
| DELETE | /users/{id} | Delete user |

## 🗄️ Database

Database: fastapi_learning

Table: users

The users table contains:

- id
- name
- email

Email addresses are unique.

## ⚙️ Run the Project

### 1. Create virtual environment

    py -m venv venv

### 2. Activate it

    venv\Scripts\Activate.ps1

### 3. Install dependencies

    py -m pip install -r requirements.txt

### 4. Start MySQL using XAMPP

Create the database:

    fastapi_learning

### 5. Create tables

    py create_tables.py

### 6. Start FastAPI

    py -m uvicorn main:app --reload

Open Swagger:

    http://127.0.0.1:8000/docs

## 🧠 Learning Goals

This project was created to practice:

- REST API development
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic validation
- CRUD operations
- Database sessions
- Git and GitHub

## 🚧 Future Improvements

- SQLAlchemy ORM
- JWT authentication
- Password hashing
- User roles
- Automated testing
- API security
- Docker
- Deployment

## 👨‍💻 Author

Muaz Mohammed

Software Engineering Student | Full-Stack Developer | AI/ML & Cybersecurity Enthusiast

Project Status: Learning / In Development