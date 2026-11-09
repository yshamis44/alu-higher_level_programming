#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """A square whose size is read and changed through a property."""

    def __init__(self, size=0):
        """Create a new square and set its size through the setter.

        Args:
            size: the length of one side of the square, 0 by default.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after checking the value.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
