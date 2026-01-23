#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = ".?:"
    i = 0
    length = len(text)

    while i < length:
        start = i
        while i < length and text[i] not in end_chars:
            i += 1
        line = text[start:i].strip()
        if line:
            print(line, end="")  # pas de saut de ligne automatique

        if i < length and text[i] in end_chars:
            print(text[i], end="")  # ponctuation collée
            i += 1
            # Vérifie s'il reste du texte après la ponctuation
            j = i
            while j < length and text[j] == " ":
                j += 1
            if j < length:
                print("\n")  # ajoute 2 sauts de ligne si plus de texte
        while i < length and text[i] == " ":
            i += 1
