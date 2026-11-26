#!/usr/bin/python3
"""This module defines the Base class used by every shape in the project."""
import json


class Base:
    """Base class that manages the id of every object created."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Set the id, or give the next free number if id is None."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of a list of objects to <Class name>.json."""
        dicts = []
        if list_objs is not None:
            dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries stored in a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances read from <Class name>.json."""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in dicts]
