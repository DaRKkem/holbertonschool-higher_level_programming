#!/usr/bin/env python3
"""Module for pickling custom classes."""
import pickle


class CustomObject:
    """CustomObject class with serialization capabilities."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a file into a CustomObject instance."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
