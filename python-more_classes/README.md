# Python More Classes

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Advanced object-oriented programming in Python through the design of a Rectangle class. This project explores special methods (`__str__`, `__repr__`, `__del__`), class attributes, static methods, and class methods.

---

## Tasks / Files

### 0. Empty Rectangle class
**File:** `0-rectangle.py`

Define an empty Rectangle class.

```python
class Rectangle:
    pass
```

### 1. Rectangle with width and height
**File:** `1-rectangle.py`

Add private `width` and `height` attributes with validation.

### 2. Area and perimeter
**File:** `2-rectangle.py`

Add `area()` and `perimeter()` methods.

```python
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
```

### 3. String representation (`__str__`)
**File:** `3-rectangle.py`

Return a string representation of the rectangle using the `#` character.

### 4. Official representation (`__repr__`)
**File:** `4-rectangle.py`

Return a string representation that can recreate the rectangle with `eval()`.

### 5. Delete notification (`__del__`)
**File:** `5-rectangle.py`

Print a message when an instance is deleted.

```python
def __del__(self):
    print("Bye rectangle...")
```

### 6. Number of instances
**File:** `6-rectangle.py`

Track the number of Rectangle instances with a class attribute `number_of_instances`.

### 7. Print symbol
**File:** `7-rectangle.py`

Allow changing the print symbol via a class attribute `print_symbol`.

### 8. Static method `bigger_or_equal`
**File:** `8-rectangle.py`

Static method that returns the largest rectangle based on area.

### 9. Class method `square`
**File:** `9-rectangle.py`

Class method that creates a new Rectangle instance with equal width and height (a square).

---

## Key Concepts

- `__str__` for human-readable string representation
- `__repr__` for unambiguous / official representation
- `__del__` destructor method
- Class attributes vs instance attributes
- `@staticmethod` decorator
- `@classmethod` decorator
- Property validation with `@property` / `@setter`
- Rectangle geometry (area, perimeter)

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-more_classes

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
