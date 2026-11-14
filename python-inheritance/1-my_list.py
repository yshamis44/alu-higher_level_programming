#!/usr/bin/python3
"""Module that defines a MyList class that can print itself sorted."""


class MyList(list):
    """A list that can print its items in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
