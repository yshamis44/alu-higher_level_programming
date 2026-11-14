#!/usr/bin/python3
"""Module that defines a BaseGeometry class that validates integers."""


class BaseGeometry:
    """A class for geometry shapes that can validate integers."""

    def area(self):
        """Raise an exception because the area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0.

        Args:
            name: the name of the value, used in the error message.
            value: the value to check.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
