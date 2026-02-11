#!/usr/bin/python3
"""That module defines a function that
   returns the dictionary representation of
   a class object for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary representation of
       a class object for JSON serialization."""
    return obj.__dict__
