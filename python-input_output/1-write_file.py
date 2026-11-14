#!/usr/bin/python3
"""Module that defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a file (UTF8) and return the number of characters.

    The file is created if it does not exist, and its content is
    replaced if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
