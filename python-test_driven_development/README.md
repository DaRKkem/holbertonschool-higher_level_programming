# Python Test-Driven Development

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Writing robust Python code using test-driven development with doctests and unit tests.

---

## Tasks / Files

- **0-add_integer.py** - Adds two integers with doctests for edge cases.
- **1-matrix_divided.py** - Divides all elements of a matrix with doctests.
- **2-say_my_name.py** - Prints a formatted name string.
- **3-print_square.py** - Prints a square using the `#` character.
- **4-text_indentation.py** - Prints text with proper indentation after `.`, `?`, and `:`.
- **5-max_integer.py** - Finds the maximum integer in a list (with unit tests).
- **6-max_integer_test.py** - Unit tests for the `max_integer` function.
- **tests/** - Directory containing doctest and unittest test files.

```python
def add_integer(a, b=98):
    """Returns a + b. Raises TypeError if not int/float."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    return int(a) + int(b)
```

---

## Key Concepts

- doctest
- unittest
- test-driven development
- TypeError handling
- edge case testing
- documentation strings

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-test_driven_development

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
