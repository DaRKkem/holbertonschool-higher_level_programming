#!/usr/bin/python3
"""This module defines a VerboseList class that extends the built-in list."""


class VerboseList(list):
    """Within VerboseList, override the methods
    that modify the list: append, extend, remove, and pop."""

    def append(self, item):
        """Append an item to the list and print a message."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable and print a message."""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """Remove the first occurrence of an item from the list and print a message."""
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """Remove and return item at index (default last) and print a message."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
