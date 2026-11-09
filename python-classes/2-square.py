#!/usr/bin/python3
"""Module that defines a Square class that validates its size."""


class Square:
    """A square defined by a size that must be a valid integer."""

    def __init__(self, size=0):
        """Create a new square and check the size that was given.

        Args:
            size: the length of one side of the square, 0 by default.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
