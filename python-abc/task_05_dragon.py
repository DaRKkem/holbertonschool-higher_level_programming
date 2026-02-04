#!/usr/bin/python3
"""This module defines SwimMixin, FlyMixin, and
   Dragon classes demonstrating mixin inheritance."""


class SwimMixin:
    """Mixin class that provides swimming ability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying ability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits swimming and flying abilities from mixins."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
