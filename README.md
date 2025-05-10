```markdown
# 📡 DataPeace Backend Assignment - User Management REST API

This project is a Django-based REST API that manages user data with full CRUD functionality, search, sorting, and pagination.  
It fulfills all the requirements given in the DataPeace Backend Assignment.

---

## 🚀 Features

- **Get Users** with support for:
  - Pagination (`page`, `limit`)
  - Search by name (substring match in `first_name` or `last_name`)
  - Sorting by any field (e.g., `sort=age`, `sort=-age`)
- **Create**, **Update**, **Delete**, and **Get Single User** endpoints
- Initial user data imported from a JSON file
- Clean and modular Django project using Django REST Framework

---

## 📁 Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite (default DB)

---

## 📂 Folder Structure

```
datapeace_api/
├── config/                 # Main Django settings and routing
├── users/                  # App for handling user-related logic
│   ├── migrations/
│   ├── management/commands/import_users.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── users.json              # Sample user data
├── requirements.txt        # Python dependencies
└── manage.py
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```
git clone 
cd datapeace_api
```

### 2. Set Up Virtual Environment

```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
# source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Import Initial Users from JSON

```
python manage.py import_users users.json
```

---

## ▶️ Running the Server

```
python manage.py runserver
```

Server will be running at:  
`http://127.0.0.1:8000/`

---

## 🔌 API Endpoints

### 📥 `GET /api/users`

List users with filters:

- `page` (default: 1)
- `limit` (default: 5)
- `name` (substring filter)
- `sort` (field to sort by, use `-` for descending)

**Example:**

```
GET /api/users?page=1&limit=10&name=James&sort=-age
```

---

### ➕ `POST /api/users`

Create a new user.

```
{
  "id": 999,
  "first_name": "Test",
  "last_name": "User",
  "company_name": "Test Inc",
  "city": "Testville",
  "state": "TS",
  "zip": 12345,
  "email": "test.user@test.com",
  "web": "http://test.com",
  "age": 30
}
```

Returns: `201 Created`

---

### 🔍 `GET /api/users/`

Get a single user by ID.

---

### 📝 `PUT /api/users/`

Update fields (only: `first_name`, `last_name`, `age`):

```
{
  "first_name": "Updated",
  "last_name": "User",
  "age": 35
}
```

---

### ❌ `DELETE /api/users/`

Deletes the user with the given ID.

---

## 🧪 Testing (Manual)

You can test endpoints using:

- [Postman](https://www.postman.com/)
- cURL
- Browser for GET requests

---

## 📌 Assignment Specs Covered ✅

| Feature                             | Status   |
| ----------------------------------- | -------- |
| Django + REST API                   | ✅ Done  |
| SQLite database                     | ✅ Done  |
| Load data from users.json           | ✅ Done  |
| GET / POST / PUT / DELETE endpoints | ✅ Done  |
| Pagination, Search, Sorting         | ✅ Done  |
| Status codes: 200, 201, 404, 400    | ✅ Done  |
| Modular code, clean structure       | ✅ Done  |

---

## 📬 Submission

To submit:

1. Push this project to a public GitHub/GitLab repo.
2. Share the repo URL + deployed link (if hosted) to: `careers@datapeace.in`

---

## 📄 License

This project is for educational/demo purposes as part of the DataPeace assignment.

---
```


