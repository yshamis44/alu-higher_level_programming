#!/usr/bin/python3
"""Module that defines a Square class with a size and a position."""


class Square:
    """A square that has a size and a position on the screen."""

    def __init__(self, size=0, position=(0, 0)):
        """Create a new square with a size and a position.

        Args:
            size: the length of one side of the square, 0 by default.
            position: a tuple of 2 positive integers, (0, 0) by default.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after checking the value.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        msg = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(msg)
        for n in value:
            if not isinstance(n, int) or n < 0:
                raise TypeError(msg)
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character, moved by its position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
