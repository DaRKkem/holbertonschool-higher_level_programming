#!/usr/bin/python3
"""Add two integers."""


def add_integer(a, b=98):
    """Add two integers."""

    if type(a) not in (int, float) or type(a) is bool:
        raise TypeError("a must be an integer")

    if type(b) not in (int, float) or type(b) is bool:
        raise TypeError("b must be an integer")


    a = int(a)
    b = int(b)

    return a + b
