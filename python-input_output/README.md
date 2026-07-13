# Python File I/O & JSON Serialization

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Working with file input/output operations and JSON serialization in Python. This project covers reading and writing files, working with JSON data (dump/load/dumps/loads), and implementing a Pascal's Triangle generator.

---

## Tasks / Files

### 0. Read file
**File:** `0-read_file.py`

Read a file and print its content to stdout.

```python
with open("file.txt", "r") as f:
    content = f.read()
```

### 1. Write to file
**File:** `1-write_file.py`

Write a string to a file (overwriting existing content).

### 2. Append to file
**File:** `2-append_write.py`

Append a string to the end of a file.

### 3. JSON to string
**File:** `3-to_json_string.py`

Convert a Python object to a JSON string using `json.dumps()`.

### 4. JSON from string
**File:** `4-from_json_string.py`

Convert a JSON string to a Python object using `json.loads()`.

### 5. Save object to JSON file
**File:** `5-save_to_json_file.py`

Write a Python object to a JSON file using `json.dump()`.

### 6. Load object from JSON file
**File:** `6-load_from_json_file.py`

Read a Python object from a JSON file using `json.load()`.

```python
import json

data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f)
```

### 7. Add items and save
**File:** `7-add_item.py`

Script that adds command-line arguments to a list and saves the list to a JSON file.

### 8. Class to JSON
**File:** `8-class_to_json.py`

Return a dictionary description of a class instance for JSON serialization.

### 9. Student class
**File:** `9-student.py`

Define a `Student` class with a `to_json()` method.

### 10. Student with filter
**File:** `10-student.py`

Extend `Student.to_json()` to accept an optional attribute filter.

### 11. Student reload from JSON
**File:** `11-student.py`

Add a `reload_from_json()` method to the `Student` class.

### 12. Pascal's Triangle
**File:** `12-pascal_triangle.py`

Generate Pascal's Triangle up to `n` rows.

```python
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
```

---

## Key Concepts

- `open()`, `read()`, `write()`, `append()` file operations
- `with` statement for automatic resource management
- JSON module: `dump`, `load`, `dumps`, `loads`
- File cursor positioning (`seek`, `tell`)
- Serialization of custom objects to dictionaries
- Pascal's Triangle algorithm (binomial coefficients)
- Scripting with `sys.argv`

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-input_output

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
