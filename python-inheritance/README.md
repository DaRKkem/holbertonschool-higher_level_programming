# Python Inheritance

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Exploration of class inheritance in Python. The project builds a hierarchy from a `BaseGeometry` class down to `Rectangle` and `Square`, demonstrating method overriding, validation through base classes, and the use of `super()`, `isinstance()`, and `issubclass()`.

---

## Tasks / Files

### 0. Lookup
**File:** `0-lookup.py`

Returns a list of available attributes and methods of an object using `dir()`.

```python
def lookup(obj):
    return dir(obj)
```

### 1. `isinstance` / `issubclass` checks
**File:** `1-my_list.py`

Create a `MyList` class that inherits from `list` with a `print_sorted()` method.

### 2. BaseGeometry class
**File:** `2-base_geometry.py`

Create a `BaseGeometry` class with an `area()` method that raises an exception.

```python
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
```

### 3. Integer validator
**File:** `3-base_geometry.py`

Add `integer_validator(name, value)` to `BaseGeometry` that validates value is a positive integer.

### 4. Rectangle inherits from BaseGeometry
**File:** `4-rectangle.py`

Create a `Rectangle` class that inherits from `BaseGeometry`.

```python
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
```

### 5 - 8. Rectangle improvements
**Files:** `5-rectangle.py` through `8-rectangle.py`

Add `area()`, `__str__`, and `__repr__` to Rectangle.

### 9. Square inherits from Rectangle
**File:** `9-square.py`

Create a `Square` class that inherits from `Rectangle`.

### 10 - 11. Square improvements
**Files:** `10-square.py`, `11-square.py`

Add `__str__` to Square and ensure proper integration with the geometry hierarchy.

---

## Key Concepts

- Inheritance: `class Child(Parent)`
- `super()` to call parent class methods
- `isinstance(obj, class)` for type checking
- `issubclass(child, parent)` for subclass checking
- Method overriding in child classes
- Base class validation with `integer_validator`
- Exception raising for unimplemented methods
- Chained inheritance: `Square` -> `Rectangle` -> `BaseGeometry`

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-inheritance

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
