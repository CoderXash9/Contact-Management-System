<div align="center">

# 📇 Contact Management System API

### 🚀 A Production-Style RESTful Contact Management Backend built with Django REST Framework

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Django-5.x-darkgreen?style=for-the-badge&logo=django">
  <img src="https://img.shields.io/badge/Django%20REST%20Framework-REST-red?style=for-the-badge&logo=django">
  <img src="https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

### 💻 Built as part of the **CodSoft Backend Development Internship**

*A modern Contact Management REST API implementing CRUD operations, filtering, searching, ordering, pagination and validation.*

</div>

---

# 📑 Table of Contents

- 📖 About
- ✨ Features
- 🛠 Tech Stack
- 📂 Project Structure
- ⚙ Installation
- 🚀 Running the Project
- 📡 API Endpoints
- 🔍 Query Features
- 🧪 Validation
- 📷 Screenshots
- 📈 Future Improvements
- 👨‍💻 Author

---

# 📖 About

This project is a **RESTful Contact Management API** developed using **Django REST Framework**.

It allows users to:

- Create contacts
- View contacts
- Update contacts
- Delete contacts
- Search contacts
- Filter contacts
- Sort contacts
- Paginate large datasets
- Validate incoming data

The project demonstrates industry-standard backend development practices and follows REST architecture.

---

# ✨ Features

## ✅ CRUD Operations

- ➕ Create Contact
- 📖 Read Contacts
- ✏ Update Contact
- ❌ Delete Contact

---

## 🔎 Search

Search contacts by:

- Name
- Email
- Phone Number

Example:

```
GET /api/contacts/?search=Ashwini
```

---

## 🎯 Filtering

Filter contacts using company name.

Example:

```
GET /api/contacts/?company=GOOGLE
```

---

## 📊 Ordering

Sort contacts by any field.

Examples:

```
GET /api/contacts/?ordering=name

GET /api/contacts/?ordering=-created_at
```

---

## 📄 Pagination

Supports Page Number Pagination.

Example:

```
GET /api/contacts/?page=2
```

---

## 🛡 Validation

Implemented custom serializer validation for:

- Phone Number
- Name
- Company

Along with Django's built-in Email validation.

---

# 🛠 Tech Stack

| Technology | Usage |
|------------|------|
| 🐍 Python | Backend Language |
| 🌿 Django | Web Framework |
| ⚡ Django REST Framework | REST API Development |
| 🗄 SQLite | Database |
| 🔍 Django Filter | Filtering |
| 🧰 Git | Version Control |
| 🌐 GitHub | Repository Hosting |

---

# 📂 Project Structure

```
Contact-Management-System
│
├── contact_management/
│
├── contacts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│
├── db.sqlite3
├── requirements.txt
├── README.md
└── manage.py
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Contact-Management-System.git
```

Go inside the folder

```bash
cd Contact-Management-System
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Apply Migrations

```bash
python manage.py migrate
```

Run Server

```bash
python manage.py runserver
```

---

# 🚀 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/contacts/` | Retrieve All Contacts |
| POST | `/api/contacts/` | Create Contact |
| GET | `/api/contacts/<id>/` | Retrieve Single Contact |
| PUT | `/api/contacts/<id>/` | Update Entire Contact |
| PATCH | `/api/contacts/<id>/` | Partial Update |
| DELETE | `/api/contacts/<id>/` | Delete Contact |

---

# 🔍 Query Features

## Search

```
/api/contacts/?search=Ashwini
```

---

## Filter

```
/api/contacts/?company=GOOGLE
```

---

## Order

Ascending

```
/api/contacts/?ordering=name
```

Descending

```
/api/contacts/?ordering=-created_at
```

---

## Pagination

```
/api/contacts/?page=2
```

---

# 🧪 Validation

Implemented custom serializer validation.

✔ Name cannot be empty

✔ Minimum 3 characters

✔ Phone must contain only digits

✔ Phone must be exactly 10 digits

✔ Company name formatting

✔ Email validation using Django EmailField


# 📈 Future Improvements

- 🔐 JWT Authentication
- 👥 User Login System
- 🌍 PostgreSQL
- ☁ Deployment on Render
- 📖 Swagger Documentation
- 🧪 Unit Testing
- 📝 Logging
- 🐳 Docker Support

---

# 📊 Project Highlights

✔ RESTful API

✔ Clean Architecture

✔ CRUD Operations

✔ Filtering

✔ Searching

✔ Ordering

✔ Pagination

✔ Serializer Validation

✔ Django Admin Integration

✔ Production Ready Structure

---

<div align="center">

# ⭐ If you like this project, consider giving it a Star ⭐

</div>

---

# 👨‍💻 Author

## Ashwini Purohit

Backend Developer | Python Developer | Django Developer

🔗 GitHub

https://github.com/CoderXash9

🔗 LinkedIn

https://linkedin.com/in/ashwinicodes

---

<div align="center">

Made with ❤️ using Django REST Framework

</div>
