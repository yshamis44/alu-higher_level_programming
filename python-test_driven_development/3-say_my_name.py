#!/usr/bin/python3
"""
This module has one function, say_my_name.
It prints a sentence with a first name and a last name.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is followed by the first name and the last name.
    Raise a TypeError if either name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
