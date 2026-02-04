#!/usr/bin/python3
from abc import ABC, abstractmethod
""" This module defines an abstracted Animal
    class and its concrete subclasses. """


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method representing animal sound."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat."""

    def sound(self):
        """Return cat sound."""
        return "Meow"
