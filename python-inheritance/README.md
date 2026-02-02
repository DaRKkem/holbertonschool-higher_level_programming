<p align="center">
  <img width="180px" src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">
</p>

<h1 align="center">Python Inheritance & OOP</h1>

<p align="center">
Introduction simple à l’héritage (Inheritance) en Programmation Orientée Objet avec Python.
</p>

---

## 📌 Description

Ce projet explique les bases de **l’héritage en Python** et comment créer des classes qui réutilisent le code d’autres classes.

Objectifs :

- créer des classes parentes (superclasses)
- créer des classes enfants (subclasses)
- réutiliser du code existant
- redéfinir des méthodes
- comprendre `super()`
- appliquer la logique DRY (Don't Repeat Yourself)

Parfait pour comprendre la **POO avancée** en Python.

---

## 📚 Concepts abordés

- Héritage (Inheritance)
- Classes parentes / enfants
- Réutilisation de code
- `super()`
- Override (redéfinition de méthodes)
- Polymorphisme
- `isinstance()` / `issubclass()`
- Encapsulation
- Méthodes spéciales (`__str__`, `__repr__`)

---

## ▶️ Exemples

### Classe parente :

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
```

### Classe enfant (héritage) :
```python
class Dog(Animal):
    pass
```
Dog hérite automatiquement de name et speak().

### Override d’une méthode :
```python
class Dog(Animal):
    def speak(self):
        return "Woof!"
```
On redéfinit le comportement de la classe parente.

### Utilisation de super() :
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
super() permet d’appeler le constructeur de la classe parente.
```

### Utilisation :
```python
dog = Dog("Rex", "Labrador")

print(dog.name)
print(dog.speak())%
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

Inheritance & Polymorphism

✍️ Auteur
Rossi Damien
