#!/usr/bin/python3
"""
This module has one function, text_indentation.
It prints a text with 2 new lines after each '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after each of the characters . ? and :
    No printed line starts or ends with a space.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for c in text:
        result += c
        if c in ".?:":
            result += "\n\n"
    lines = [line.strip(" ") for line in result.split("\n")]
    print("\n".join(lines), end="")
