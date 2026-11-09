#!/usr/bin/python3
"""Module that defines a Square class with a private size."""


class Square:
    """A square defined by the length of one of its sides."""

    def __init__(self, size):
        """Create a new square.

        Args:
            size: the length of one side of the square.
        """
        self.__size = size
