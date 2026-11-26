#!/usr/bin/python3
"""This module defines the Rectangle class, which inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle with a width, a height and an x/y position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create a rectangle and check every value through the setters."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def check_int(name, value, can_be_zero):
        """Raise an error if value is not a valid integer for name."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if can_be_zero and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        if not can_be_zero and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after checking it is an integer above 0."""
        self.check_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after checking it is an integer above 0."""
        self.check_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Return the x position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x after checking it is an integer of 0 or more."""
        self.check_int("x", value, True)
        self.__x = value

    @property
    def y(self):
        """Return the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y after checking it is an integer of 0 or more."""
        self.check_int("y", value, True)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with # characters, moved by x and y."""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Set id, width, height, x and y from args, or from kwargs."""
        names = ["id", "width", "height", "x", "y"]
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
