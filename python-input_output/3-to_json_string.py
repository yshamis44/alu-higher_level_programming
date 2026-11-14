#!/usr/bin/python3
"""Module that defines a function that converts an object to JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON representation (a string) of an object."""
    return json.dumps(my_obj)
