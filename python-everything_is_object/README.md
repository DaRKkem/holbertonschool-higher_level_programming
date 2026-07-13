# Python -- Everything is an Object

![Python](https://img.shields.io/badge/Python-3.12-blue)

```python
print(id([1, 2, 3]))  # memory address
```

A quiz-style project that explores Python's object model -- mutability, references, identity, and memory management. Inspired by the article "Everything is an Object" in Python, it consists of 29 short-answer questions plus one small coding task.

---

## Tasks

### Written answers (0-28)
**Files:** `0-answer.txt` through `28-answer.txt`

Each file contains a single-line answer to a question about Python object behaviour. Examples:

- `type()` -- function that returns the type of an object
- `id()` -- function that returns the identity of an object
- Answers covering mutable vs. immutable types, variable aliasing, reference behaviour, equality vs. identity, and integer caching

### Coding task
**File:** `19-copy_list.py`

A function that returns a copy of a list without referencing the original list object.

```python
def copy_list(l):
    return l[:]
```

Alternative approaches: `list(l)`, `l.copy()`, or `copy.deepcopy(l)`.

---

## Key Concepts

- `id()` and `type()` built-in functions
- Mutable vs. immutable types (list, dict, set vs. int, str, tuple)
- Variable references and aliasing
- Object identity (`is` operator) vs. equality (`==`)
- List copying techniques: slicing `[:]`, `list()`, `.copy()`, `copy` module
- Python's integer caching (small integers, string interning)
- Memory management and garbage collection basics

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-everything_is_object

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
