#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


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

    def to_json(self, attrs=None):
        """Return the dictionary description of the student.

        If attrs is a list of strings, only the attributes named in it
        are returned. Otherwise, all the attributes are returned.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            result = {}
            for name in attrs:
                if name in self.__dict__:
                    result[name] = self.__dict__[name]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the student with the ones in json."""
        for key, value in json.items():
            setattr(self, key, value)
