# Python Classes

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Introduction to object-oriented programming in Python through the design and implementation of Square classes. This project covers class creation, attribute encapsulation, property decorators, getters/setters, and instance methods.

---

## Tasks / Files

### 0. My first square
**File:** `0-square.py`

Define an empty Square class.

```python
class Square:
    pass
```

### 1. Square with private size
**File:** `1-square.py`

Define a Square class with a private instance attribute `size`.

```python
class Square:
    def __init__(self, size):
        self.__size = size
```

### 2. Square with size validation
**File:** `2-square.py`

Add validation to ensure `size` is an integer and >= 0.

### 3. Square with area method
**File:** `3-square.py`

Add a public `area()` method that returns the current square area.

### 4. Square with getter/setter
**File:** `4-square.py`

Use the `@property` decorator for a getter and `@size.setter` for a setter.

```python
class Square:
    def __init__(self, size=0):
        self.size = size  # uses setter

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
```

### 5. Square with print method
**File:** `5-square.py`

Add a `my_print()` method that prints the square using `#`.

```python
def my_print(self):
    for _ in range(self.size):
        print("#" * self.size)
```

### 6. Square with coordinates
**File:** `6-square.py`

Add a `position` attribute (tuple of 2 positive integers) to shift the printed square.

---

## Key Concepts

- Class definition (`class ClassName:`)
- `__init__` constructor method
- Private attributes (`__attribute`)
- Property decorators (`@property`, `@setter`)
- Getters and setters for encapsulation
- Instance methods (`area()`, `my_print()`)
- Type and value validation
- String repetition in Python

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-classes

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
