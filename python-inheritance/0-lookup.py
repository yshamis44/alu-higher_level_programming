#!/usr/bin/python3
"""Module that defines a function listing what an object has."""


def lookup(obj):
    """Return a list of the attributes and methods of an object."""
    return dir(obj)
