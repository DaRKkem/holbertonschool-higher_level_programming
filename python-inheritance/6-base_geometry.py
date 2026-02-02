#!/usr/bin/python3
"""This module defines an empty BaseGeometry class."""


class BaseGeometry:
    """Empty class."""
    def area(self):
        """Method that raises an exception indicating it's not implemented."""
        raise Exception("area() is not implemented")
