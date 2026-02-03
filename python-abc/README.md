<p align="center">
  <img width="180px" src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">
</p>

<h1 align="center">Python Advanced OOP & Design Patterns</h1>

<p align="center">
Introduction simple aux concepts avancés de la Programmation Orientée Objet (OOP) en Python.
</p>

---

## 📌 Description

Ce projet explore des notions **plus avancées de la POO Python** :

- classes abstraites (ABC)
- héritage et polymorphisme
- duck typing
- extension de classes natives (list, iterator…)
- itérateurs personnalisés
- héritage multiple
- mixins

Parfait pour comprendre **comment Python structure les objets complexes** dans des projets réels.

---

## 📚 Concepts abordés

- Abstract Base Classes (`ABC`, `@abstractmethod`)
- Duck Typing
- Héritage simple & multiple
- Extension de classes natives
- Itérateurs personnalisés
- Mixins
- Polymorphisme
- Méthodes spéciales (`__iter__`, `__next__`, `__str__`, etc.)

---

## ▶️ Exemples

### Classe abstraite (ABC)

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```

### Implémentation concrète

```python
class Dog(Animal):
    def sound(self):
        return "Bark"
```

### Duck Typing
```python
class Bird:
    def fly(self):
        print("Flying")

class Plane:
    def fly(self):
        print("Also flying")

def make_it_fly(obj):
    obj.fly()
```

### Extending the Python List with Notifications
```python
class NotifyingList(list):
    def append(self, item):
        super().append(item)
        print("Item added:", item)
```

### CountedIterator — Keeping Track of Iteration
```python
class CountedIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
```

### The Enigmatic FlyingFish — Multiple ### Inheritance
```python
class Swimmer:
    def swim(self):
        return "Swimming"

class Flyer:
    def fly(self):
        return "Flying"

class FlyingFish(Swimmer, Flyer):
    pass
```

### The Mystical Dragon — Mixins
```python
class FireMixin:
    def breathe_fire(self):
        return "Fire breath!"

class Dragon(FireMixin):
    def roar(self):
        return "Roar!"
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

✍️ Auteur
DaRKkem
