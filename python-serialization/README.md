# Python Serialization

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Exploration of data serialization formats in Python. This project covers JSON, Pickle, CSV, and XML -- each serving different use cases for persisting and exchanging data between systems or across program runs.

---

## Tasks / Files

### 0. Basic JSON serialization
**File:** `task_00_basic_serialization.py`

Serialize a dictionary to a JSON file and deserialize it back.

```python
import json

data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)
```

### 1. Pickle serialization
**File:** `task_01_pickle.py`

Serialize and deserialize Python objects using the `pickle` module (binary format). Demonstrates handling of custom class instances.

### 2. CSV parsing and conversion
**File:** `task_02_csv.py`

Parse a CSV file, convert rows to dictionaries, and serialize the result to JSON.

### 3. XML serialization and parsing
**File:** `task_03_xml.py`

Generate XML from Python data and parse XML back into Python structures.

---

## Key Concepts

- **JSON**: Human-readable text format, language-independent, `json.dump` / `json.load`
- **Pickle**: Binary Python-specific format, preserves Python objects, `pickle.dump` / `pickle.load`
- **CSV**: Tabular data format, `csv.reader` / `csv.DictReader`, conversion to JSON
- **XML**: Hierarchical markup format, `xml.etree.ElementTree`, generation and parsing
- Serialization format comparison: readability, security, portability
- Data persistence patterns

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-serialization

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
