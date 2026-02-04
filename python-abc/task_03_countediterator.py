#!/usr/bin/python3
"""Module defining CountedIterator that tracks iteration count."""


class CountedIterator:
    """An iterator wrapper that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Fetch the next item and increment the counter."""
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return self._count
