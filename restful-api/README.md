# RESTful API

![Python](https://img.shields.io/badge/Python-3.12-blue) ![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Introduction to designing and consuming RESTful APIs. This project covers making HTTP requests with the `requests` library, building a raw HTTP server from scratch, creating a Flask-based REST API, and adding basic authentication for security.

---

## Tasks / Files

### 2. Consuming APIs with requests
**File:** `task_02_requests.py`

Use the `requests` library to perform GET, POST, PUT, and DELETE requests against a public REST API. Handle JSON responses and HTTP status codes.

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
```

### 3. Basic HTTP server
**File:** `task_03_http_server.py`

Build a basic HTTP server from scratch using Python's `http.server` module. Handle different HTTP methods and return appropriate status codes.

### 4. Flask REST API
**File:** `task_04_flask.py`

Develop a REST API using Flask with routes for CRUD operations and JSON responses.

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
```

### 5. Basic API security
**File:** `task_05_basic_security.py`

Add basic authentication (username/password or token-based) to protect API endpoints.

---

## Key Concepts

- REST architecture principles (stateless, resource-based, uniform interface)
- HTTP methods: GET, POST, PUT, DELETE, PATCH
- Flask route definition and JSON response formatting
- Request/response cycle and HTTP status codes (200, 201, 400, 401, 404, 500)
- API authentication basics (Basic Auth, token-based)
- `requests` library for consuming third-party APIs
- Testing APIs with `curl`

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: restful-api

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
