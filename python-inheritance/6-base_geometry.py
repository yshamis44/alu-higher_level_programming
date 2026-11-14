#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """A class for geometry shapes that has an area method."""

    def area(self):
        """Raise an exception because the area is not implemented."""
        raise Exception("area() is not implemented")
