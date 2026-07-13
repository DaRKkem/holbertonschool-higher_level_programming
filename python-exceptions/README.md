# Python Exceptions

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Error handling in Python: using try/except blocks, raising exceptions, and writing robust code.

---

## Tasks / Files

- **0-safe_print_list.py** - Safely prints a list using try/except.
- **1-safe_print_integer.py** - Safely prints an integer with type checking.
- **2-safe_print_list_integers.py** - Prints only integers from a list.
- **3-safe_print_division.py** - Performs division with try/except/else/finally.
- **4-list_division.py** - Divides two lists element-wise with error handling.
- **5-raise_exception.py** - Raises a custom exception.
- **6-raise_exception_msg.py** - Raises an exception with a custom message.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## Key Concepts

- try/except
- else/finally
- raising exceptions
- exception types (TypeError, ValueError, ZeroDivisionError)
- exception messages

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-exceptions

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
