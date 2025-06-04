
# 📚 Book Library API

## 1. Introduction

This project provides a simple RESTful API to manage a collection of books. It supports CRUD operations — Create, Read, Update, and Delete — on book records. Built with FastAPI and backed by a lightweight SQLite database, it's ideal for learning API development or quick prototyping. 🚀

## 2. Technologies

- 🐍 Python 3.13+
- ⚡ FastAPI framework
- 🗄️ SQLite for data storage
- 🚀 Uvicorn as ASGI server

## 3. Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/remas-anwar/MY-BOOK-API-.git
cd MY-BOOK-API-
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

4. Run the server:

```bash
uvicorn main:app --reload
```

5. Access the API docs in your browser:

```
http://127.0.0.1:8000/docs
```

## 4. API Endpoints

| Method | Endpoint           | Description                             | Request Body                         | Response                  |
|--------|--------------------|---------------------------------------|------------------------------------|---------------------------|
| GET    | /api/books         | Get list of books (supports pagination) | None                               | List of books             |
| POST   | /api/books         | Add a new book (requires Basic Auth)    | JSON with book details             | Created book info         |
| GET    | /api/books/{id}    | Get details of a specific book (Auth)   | None                              | Book details              |
| PUT    | /api/books/{id}    | Update a book by ID (Auth)               | JSON with fields to update        | Updated book info         |
| DELETE | /api/books/{id}    | Delete a book by ID (Auth)               | None                              | Deletion confirmation     |

## 5. Features

- 🔐 Basic Authentication for securing endpoints (username/password)
- 📄 Pagination with `skip` and `limit` query parameters
- 🗃️ Automatic creation of the SQLite database on first run
- 🛠️ FastAPI's interactive Swagger UI for easy testing


## 6. Repository

Source code available at:

[https://github.com/remas-anwar/MY-BOOK-API-.git](https://github.com/remas-anwar/MY-BOOK-API-.git)

---
