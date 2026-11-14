#!/usr/bin/python3
"""Module that defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append text to the end of a file (UTF8), return the characters added.

    The file is created if it does not exist.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
