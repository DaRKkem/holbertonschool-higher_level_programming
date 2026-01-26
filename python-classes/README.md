<p align="center">
  <img width="180px" src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">
</p>

<h1 align="center">Python Classes & Methods</h1>

<p align="center">
Introduction simple à la Programmation Orientée Objet (OOP) en Python.
</p>

---

## 📌 Description

Ce projet explique les bases des **classes Python** :

- créer des objets
- définir des attributs
- écrire des méthodes
- comprendre public / protected / private
- appliquer l’encapsulation

Parfait pour débuter avec la POO en Python.

---

## 📚 Concepts abordés

- Classes & objets
- `__init__` (constructeur)
- Attributs d’instance
- Méthodes
- Attributs publics / protégés / privés
- Encapsulation
- Méthodes spéciales (`__str__`, `__repr__`)

---

## ▶️ Exemples

### Classe simple :

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Méthode d’instance :

```python
class Person:
    def greet(self):
        return f"Hello, my name is {self.name}"
```

### Attribut privé (encapsulation) :

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

### Utilisation :

```python
account = BankAccount(100)
account.deposit(50)

print(account.get_balance())
```


🚀 Lancer le projet :
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
python3 main.py
```
🛠️ Technologies
Python 3


Programmation Orientée Objet (OOP)

✍️ Auteur :
DaRKkem