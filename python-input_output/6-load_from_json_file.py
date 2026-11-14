#!/usr/bin/python3
"""Module that defines a function that loads an object out of a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object out of the JSON text stored in a file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
