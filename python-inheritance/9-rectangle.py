#!/usr/bin/python3
"""Module that defines a Rectangle class with an area and a description."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle that can compute its area and describe itself."""

    def __init__(self, width, height):
        """Create a rectangle after checking its width and height.

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
