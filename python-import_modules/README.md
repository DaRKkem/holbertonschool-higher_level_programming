# Python Import & Modules

![Python](https://img.shields.io/badge/Python-3.12-blue) ![License](https://img.shields.io/badge/License-Holberton-yellow)

Organizing Python code into modules: importing functions, handling command-line arguments, and understanding namespaces.

---

## Tasks / Files

- **0-add.py** - Imports a function from a module and uses it.
- **1-calculation.py** - Imports multiple functions from a module.
- **2-args.py** - Prints the number of and list of command-line arguments using `sys.argv`.
- **3-infinite_add.py** - Infinite addition of variable arguments passed on the command line.
- **4-hidden_discovery.py** - Discovers all names defined in a compiled module using `dir()`.
- **5-variable_load.py** - Imports and prints a variable from a module.
- **add_0.py** - Helper module containing the `add` function.
- **calculator_1.py** - Helper module containing basic calculator functions.

```python
from add_0 import add

result = add(1, 2)
print(result)
```

---

## Key Concepts

- import statements
- from/import
- sys.argv
- dir()
- module namespace
- __name__
- variable arguments

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: python-import_modules

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
