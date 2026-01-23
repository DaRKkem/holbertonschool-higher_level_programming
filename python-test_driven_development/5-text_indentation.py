#!/usr/bin/python3
"""Module for text indentation.

This module provides a function text_indentation(text) that
prints a text, adding 2 new lines after each of these characters:
'.', '?' and ':'.
"""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The string to be printed.

    Raises:
        TypeError: If text is not a string.
    """
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
