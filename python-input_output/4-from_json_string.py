#!/usr/bin/python3
"""This module defines a function that returns
   the Python object represented by a JSON string"""


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string"""
    import json
    return json.loads(my_str)
