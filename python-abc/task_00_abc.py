#!/usr/bin/python3
from abc import ABC, abstractmethod
""" This module defines an abstracted Animal
    class and its concrete subclasses. """


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def speak(self):
        """Abstract method representing animal sound."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def speak(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat."""

    def speak(self):
        """Return cat sound."""
        return "Meow"
