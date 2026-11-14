#!/usr/bin/python3
"""Module that defines a function checking the kind of an object."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is a kind of a_class, else False."""
    return isinstance(obj, a_class)
