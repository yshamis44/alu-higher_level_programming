#!/usr/bin/python3
"""
This module has one function, print_square.
It prints a square made of the # character.
"""


def print_square(size):
    """Print a square of # characters with sides of length size.
    Raise a TypeError if size is not an integer, ValueError if it is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
