#!/usr/bin/python3
"""This module defines a CustomObject class with serialization."""


class CustomObject:
    """Defines a custom object."""

    def __init__(self, name, age, is_student):
        if not isinstance(name, str):
            raise TypeError("Wrong type for name")
        if not isinstance(age, int):
            raise TypeError("Wrong type for age")
        if not isinstance(is_student, bool):
            raise TypeError("Wrong type for is_student")

        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Serialize the object using pickle."""
        import pickle
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def deserialize(filename):
        """Deserialize a file into a CustomObject."""
        import pickle
        with open(filename, "rb") as f:
            return pickle.load(f)
