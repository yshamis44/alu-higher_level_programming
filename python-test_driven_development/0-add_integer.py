#!/usr/bin/python3
"""
This module has one function, add_integer.
It adds two numbers after casting them to integers.
Floats are cast to int first, anything else raises a TypeError.
"""


def add_integer(a, b=98):
    """Return the sum of a and b as an integer, casting floats to int.
    Raise a TypeError if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
