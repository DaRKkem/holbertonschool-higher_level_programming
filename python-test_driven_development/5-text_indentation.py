#!/usr/bin/python3
"""Module for text indentation.

This module provides a function that prints a text,
adding 2 new lines after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with indentation after '.', '?' and ':'.

    Args:
        text: string to be printed.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = ".?:"
    i = 0
    length = len(text)

    while i < length:
        line = ""
        # Collect characters until a punctuation
        while i < length and text[i] not in end_chars:
            line += text[i]
            i += 1
        line = line.strip()
        if line:
            print(line)
        # Print punctuation if exists
        if i < length and text[i] in end_chars:
            # On imprime la ponctuation
            print(text[i], end="")
            i += 1
            # Ajoute 2 sauts de ligne seulement si ce n'est pas la fin du texte
            if i < length:
                print("\n")
        # Skip spaces after punctuation
        while i < length and text[i] == " ":
            i += 1
