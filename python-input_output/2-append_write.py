#!/usr/bin/python3
"""This module defines a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a str to a text file and returns the number of char added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
