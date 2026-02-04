#!/usr/bin/python3
"""Defines a function that checks if an object"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclass."""

    return isinstance(obj, a_class)
