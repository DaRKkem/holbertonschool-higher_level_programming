#!/usr/bin/python3
"""This module defines an empty BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry."""
    def area(self):
        """Method that raises an exception indicating it's not implemented."""
        raise Exception("area() is not implemented")
