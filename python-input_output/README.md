
<p align="center">
  <img width="180px" src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">
</p>

<h1 align="center">Python File Handling & OOP</h1>

<p align="center">
Introduction simple à la lecture et écriture de fichiers en Python.
</p>

---

## 📌 Description

Ce projet explique les bases de **la manipulation de fichiers en Python** et comment automatiser la lecture, l’écriture et le traitement des données.

Objectifs :

- ouvrir et fermer des fichiers
- lire le contenu complet d’un fichier
- lire un fichier ligne par ligne
- écrire du texte dans un fichier
- gérer les fichiers en toute sécurité avec `with`
- utiliser JSON pour la sérialisation et désérialisation
- accéder aux paramètres de la ligne de commande

Parfait pour comprendre la **gestion des fichiers et la sérialisation en Python**.

---

## 📚 Concepts abordés

- Lecture et écriture de fichiers (`open`, `read`, `write`)
- Gestion de fichiers avec `with`
- Curseur de fichier (`seek`, `tell`)
- Fermeture automatique de fichiers
- JSON (`json.dump`, `json.load`, `json.dumps`, `json.loads`)
- Sérialisation et désérialisation
- Paramètres de ligne de commande (`sys.argv`)
- Encapsulation des opérations de fichier dans des fonctions/classes
- Bonnes pratiques DRY

---

## ▶️ Exemples

### Écriture dans un fichier :

```python
with open("example.txt", "w") as file:
    file.write("Bonjour, ceci est un test !
")
    file.write("Python rend la gestion des fichiers simple.")
```

### Lecture complète d’un fichier :

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Lecture ligne par ligne :

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Déplacer le curseur :

```python
with open("example.txt", "r") as file:
    file.seek(0)  # Retour au début
    print(file.readline())
```

### Sérialisation JSON :

```python
import json

data = {"name": "Alice", "age": 30}

# Écrire JSON dans un fichier
with open("data.json", "w") as f:
    json.dump(data, f)

# Lire JSON depuis un fichier
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data)
```

### Paramètres de ligne de commande :

```python
import sys

# python3 script.py arg1 arg2
print("Arguments:", sys.argv)
```

---

🚀 Lancer le projet :
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
python3 main.py
```

🛠️ Technologies
Python 3

Lecture et écriture de fichiers

JSON & sérialisation

✍️ Auteur
Rossi Damien