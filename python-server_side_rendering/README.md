# Python Server-Side Rendering

![Python](https://img.shields.io/badge/Python-3.12-blue) ![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey)

```python
from flask import Flask, render_template
```

An introduction to generating dynamic HTML content on the server. The project moves from basic string template substitution through Jinja2 templating, conditionals and loops in templates, loading data from CSV/JSON files, and finally querying a SQLite database to render HTML pages.

---

## Tasks

### 0. Introduction to string templating
**Files:** `task_00_intro.py`, `main_00.py`, `template.txt` -- Substitutes placeholders in a text template with attendee data to generate personalised invitation files.

### 1. Jinja2 templating
**File:** `task_01_jinja.py` -- Introduces Jinja2 as the templating engine.

### 2. Logic in templates
**File:** `task_02_logic.py` -- Uses Jinja2 conditionals (`{% if %}`, `{% else %}`) and loops (`{% for %}`) in templates.

### 3. Loading data from files
**File:** `task_03_files.py` -- Parses `products.json` and `products.csv` to feed data into HTML templates.

### 4. Loading data from a database
**File:** `task_04_db.py` -- Queries a SQLite database (`products.db`) and passes the results to a Jinja2 template.

### Templates
**Directory:** `templates/`

| Template file              | Purpose                |
|----------------------------|------------------------|
| `index.html`               | Home page layout       |
| `about.html`               | About page             |
| `contact.html`             | Contact page           |
| `header.html`              | Reusable header        |
| `footer.html`              | Reusable footer        |
| `items.html`               | Item listing           |
| `product_display.html`     | Product cards display  |

---

## Key Concepts

- String templating with `str.format()` / `%` substitution
- Jinja2 engine setup and rendering
- Template inheritance (`{% extends %}`, `{% block %}`)
- Template logic: conditionals, loops, filters
- CSV file parsing with `csv.DictReader`
- JSON file parsing with `json.load()`
- SQLite database connectivity with `sqlite3`
- Server-side rendering (SSR) architecture

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-server_side_rendering

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
