#!/usr/bin/python3
"""This module defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a str to a text file and returns the number char written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
