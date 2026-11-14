#!/usr/bin/python3
"""Module that defines a function that turns an object into a dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON use."""
    return obj.__dict__
