#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """A student with a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Create a new student.

        Args:
            first_name: the first name of the student.
            last_name: the last name of the student.
            age: the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description of the student."""
        return self.__dict__
