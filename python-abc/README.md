# Python Abstract Base Classes & Design Patterns

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Study of abstract base classes (ABCs), duck typing, multiple inheritance, and mixins in Python. The project demonstrates how to enforce interface contracts, wrap iterators, subclass built-in types, and compose behavior through mixin classes.

---

## Tasks / Files

### 0. Abstract Base Class
**File:** `task_00_abc.py`

Define an abstract class using `ABC` and `abstractmethod`.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
```

### 1. Duck typing
**File:** `task_01_duck_typing.py`

Demonstrate duck typing by defining shapes (`Circle`, `Rectangle`) that implement a common interface without inheritance.

### 2. VerboseList
**File:** `task_02_verboselist.py`

Subclass the built-in `list` to print a message on every mutation (`append`, `extend`, `remove`, `pop`).

### 3. CountedIterator
**File:** `task_03_countediterator.py`

Wrap an iterable in an iterator class that counts how many items have been retrieved.

### 4. FlyingFish (multiple inheritance)
**File:** `task_04_flyingfish.py`

Create a `FlyingFish` class that inherits from both `Fish` and `Bird`, demonstrating the diamond problem and MRO (Method Resolution Order).

### 5. Dragon (mixins)
**File:** `task_05_dragon.py`

Create `SwimMixin` and `FlyMixin` classes with `swim()` and `fly()` methods, then compose them into a `Dragon` class.

---

## Key Concepts

- `ABC` (`from abc import ABC, abstractmethod`)
- `@abstractmethod` decorator for enforcing implementation
- Duck typing: "if it walks like a duck and quacks like a duck..."
- Multiple inheritance with `class Child(Parent1, Parent2):`
- Mixins for composing reusable behavior
- Iterator protocol (`__iter__`, `__next__`)
- Subclassing built-in types (e.g., `list`)
- `super()` resolution in diamond hierarchies (MRO)
- Design for interface contracts

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-abc

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
