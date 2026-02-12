#!/usr/bin/python3
"""This module defines a function to serialize an object to a file."""


from fileinput import filename


def serialize_and_save_to_file(data, filename):
    """Serialize an object to a file in JSON format."""
    import json
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Deserialize a JSON file to an object."""
    import json
    with open(filename, 'r')as f:
        return json.load(f)
