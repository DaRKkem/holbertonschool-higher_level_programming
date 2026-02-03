#!/usr/bin/python3
from abc import ABC, abstractmethod
""" This module defines an abstracted Shape
    class and its concrete subclasses. """


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method representing shape area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method representing shape perimeter."""
        pass

class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return circle area."""
        from math import pi
        return self.radius ** 2 * pi

    def perimeter(self):
        """Return circle perimeter."""
        from math import pi
        return self.radius * 2 * pi

class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return self.width * 2 + self.height * 2
