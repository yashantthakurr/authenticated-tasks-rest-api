# 🔐 Authenticated Tasks API

A production-inspired RESTful API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** featuring JWT authentication, secure password hashing, database migrations with Alembic, and a clean layered architecture.

This project was built to practice modern backend development principles including authentication, dependency injection, database modeling, and API design.

---

## 🚀 Features

- 🔑 JWT Authentication
- 🔒 Secure password hashing using `pwdlib`
- 👤 User Registration & Login
- ✅ Complete CRUD operations for Tasks
- 🗄️ PostgreSQL database integration
- 🔄 Database migrations using Alembic
- 📦 Layered project architecture
- ✔️ Request and response validation using Pydantic
- 🛡️ Protected routes with authentication
- ⚡ FastAPI automatic OpenAPI documentation
- 🧩 Dependency Injection
- 📄 Environment variable configuration using Pydantic Settings

---

## 🛠️ Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic v2
- Pydantic Settings
- pwdlib
- JWT Authentication
- Uvicorn

---

## 📂 Project Structure

```
authenticated-tasks-api/
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── api/
│   ├── core/
│   ├── database/
│   ├── dependencies/
│   ├── exceptions/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── auth.py
│   └── config.py
│
├── main.py
├── .env
├── alembic.ini
├── pyproject.toml
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/authenticated-tasks-api.git

cd authenticated-tasks-api
```

### Create a virtual environment

Using uv

```bash
uv venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
uv sync
```

---

## 🗄️ Configure Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/database_name

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

DEBUG=True
```

---

## 🧱 Run Database Migrations

Generate migrations

```bash
alembic revision --autogenerate -m "Initial Migration"
```

Apply migrations

```bash
alembic upgrade head
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

Interactive Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 🔐 Authentication Flow

1. Register a new user
2. Login using email and password
3. Receive a JWT access token
4. Authorize using the Bearer Token
5. Access protected endpoints

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/users/register` | Register a new user |
| POST | `/users/login` | Login user |

### Tasks

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/tasks/` | Create Task |
| GET | `/tasks/` | Get All Tasks |
| GET | `/tasks/{id}` | Get Task by ID |
| PUT | `/tasks/{id}` | Update Task |
| DELETE | `/tasks/{id}` | Delete Task |

---

## 💡 Concepts Practiced

- REST API Development
- JWT Authentication
- Password Hashing
- Dependency Injection
- SQLAlchemy ORM
- Alembic Migrations
- PostgreSQL
- Pydantic Validation
- Environment Configuration
- Layered Architecture
- CRUD Operations
- Error Handling
- Type Hinting

---

## 🎯 Future Improvements

- Refresh Tokens
- Role-Based Authorization
- Docker & Docker Compose
- Unit & Integration Tests
- GitHub Actions CI/CD
- Pagination
- Filtering & Sorting
- Rate Limiting
- Email Verification
- Password Reset
- Async SQLAlchemy
- Redis Caching

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

Feel free to fork this repository and submit a pull request.


---

## 👨‍💻 Author

**Yashant Thakur**

If you found this project helpful, consider giving it a ⭐ on GitHub.
