
<p align="center">
  <img width="180px" src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">
</p>

<h1 align="center">Python File Handling & OOP</h1>

<p align="center">
Introduction simple à la lecture et écriture de fichiers en Python.
</p>

------------------------------------------------------------------------

## 📌 Description

Ce projet explique les bases de la **sérialisation en Python** :\
comment convertir des objets Python en formats stockables (JSON),\
et comment reconstruire ces objets à partir de données sauvegardées.

Objectifs :

-   Comprendre la sérialisation
-   Comprendre la désérialisation
-   Convertir un objet Python en chaîne JSON
-   Sauvegarder des données sérialisées dans un fichier
-   Charger et reconstruire des objets Python depuis un fichier JSON
-   Sérialiser des objets personnalisés (classes)
-   Utiliser `sys.argv` avec des données JSON
-   Appliquer les bonnes pratiques (DRY, modularité)

------------------------------------------------------------------------

## 📚 Concepts abordés

-   Sérialisation vs Désérialisation
-   Format JSON
-   `json.dumps()` vs `json.dump()`
-   `json.loads()` vs `json.load()`
-   Conversion d'objets en dictionnaires (`__dict__`)
-   Gestion d'erreurs lors du chargement JSON
-   Stockage persistant des données
-   Paramètres de ligne de commande (`sys.argv`)
-   Encapsulation des opérations JSON dans des fonctions/classes

------------------------------------------------------------------------

## 🔄 Qu'est-ce que la Sérialisation ?

La sérialisation est le processus qui consiste à transformer un objet
Python en un format qui peut être :

-   sauvegardé dans un fichier
-   envoyé sur un réseau
-   stocké dans une base de données

Schéma :

Objet Python ➜ JSON (string ou fichier)

### Exemple :

``` python
import json

data = {"name": "Alice", "age": 30}

json_string = json.dumps(data)
print(json_string)
```

------------------------------------------------------------------------

## 🔁 Qu'est-ce que la Désérialisation ?

La désérialisation est le processus inverse :\
elle permet de reconstruire un objet Python à partir de données JSON.

Schéma :

JSON (string ou fichier) ➜ Objet Python

### Exemple :

``` python
import json

json_string = '{"name": "Alice", "age": 30}'

data = json.loads(json_string)
print(data)
print(type(data))
```

------------------------------------------------------------------------

## ▶️ Exemples pratiques

### 🔹 Écriture JSON dans un fichier

``` python
import json

data = {"language": "Python", "level": "Intermediate"}

with open("data.json", "w") as f:
    json.dump(data, f)
```

### 🔹 Lecture JSON depuis un fichier

``` python
import json

with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)
```

------------------------------------------------------------------------

## 🏫 Sérialisation d'une classe personnalisée

``` python
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
```

### Utilisation :

``` python
import json

student = Student("Lina", "Smith", 20)

json_string = json.dumps(student.to_json())
print(json_string)
```

------------------------------------------------------------------------

## 🖥️ Arguments en ligne de commande + JSON

``` python
import sys
import json

filename = "items.json"

try:
    with open(filename, "r") as f:
        items = json.load(f)
except Exception:
    items = []

items.extend(sys.argv[1:])

with open(filename, "w") as f:
    json.dump(items, f)
```

Exécution :

python3 script.py apple banana

Résultat dans items.json :

\["apple", "banana"\]

------------------------------------------------------------------------

## 🚀 Lancer le projet

``` bash
git clone https://github.com/yourusername/serialization-project.git
cd serialization-project
python3 main.py
```

------------------------------------------------------------------------

## 🛠️ Technologies

-   Python 3
-   JSON (module standard)
-   Programmation Orientée Objet (OOP)
-   Gestion des fichiers

------------------------------------------------------------------------

## ✍️ Auteur

Rossi Damien
