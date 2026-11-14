#!/usr/bin/python3
"""Module that defines a function that converts JSON to an object."""
import json


def from_json_string(my_str):
    """Return the object that a JSON string describes."""
    return json.loads(my_str)
