#!/usr/bin/python3
"""Unittests for the Base class in models/base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the JSON files made by the tests."""
        for name in ["Base.json", "Rectangle.json", "Square.json"]:
            if os.path.exists(name):
                os.remove(name)

    def test_auto_id(self):
        """Ids go up by one when no id is given."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_given_id(self):
        """A given id is used and the counter does not move."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_none_id(self):
        """None counts as no id."""
        self.assertEqual(Base(None).id, 1)

    def test_other_id_types(self):
        """Any value that is not None is kept as the id."""
        self.assertEqual(Base("hi").id, "hi")
        self.assertEqual(Base(-5).id, -5)

    def test_nb_objects_private(self):
        """__nb_objects can't be read from outside the class."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_too_many_args(self):
        """More than one argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        """A list of dictionaries becomes a JSON string."""
        s = Base.to_json_string([{"id": 1}])
        self.assertEqual(s, '[{"id": 1}]')
        self.assertEqual(type(s), str)

    def test_to_json_string_empty(self):
        """None or an empty list gives "[]"."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_rectangle(self):
        """A rectangle dictionary becomes JSON with all its keys."""
        d = Rectangle(10, 7, 2, 8).to_dictionary()
        s = Base.to_json_string([d])
        self.assertEqual(Base.from_json_string(s), [d])

    def test_from_json_string(self):
        """A JSON string becomes a list of dictionaries."""
        out = Base.from_json_string('[{"id": 89, "width": 10}]')
        self.assertEqual(out, [{"id": 89, "width": 10}])
        self.assertEqual(type(out), list)

    def test_from_json_string_empty(self):
        """None or an empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_save_to_file_rectangle(self):
        """Rectangles are saved to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_to_file_square(self):
        """Squares are saved to Square.json."""
        s1 = Square(5, 1, 2, 3)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [s1.to_dictionary()])

    def test_save_to_file_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """An empty list saves an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_overwrite(self):
        """Saving again replaces the old file."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_create_rectangle(self):
        """create makes a new rectangle with the same values."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """create makes a new square with the same values."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_create_partial(self):
        """create works with only some keys."""
        r = Rectangle.create(id=89, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 4/1")

    def test_load_from_file_no_file(self):
        """No file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """Saved rectangles load back as new Rectangle objects."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in out], [str(r1), str(r2)])
        self.assertTrue(all(type(r) is Rectangle for r in out))

    def test_load_from_file_square(self):
        """Saved squares load back as new Square objects."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual([str(s) for s in out], [str(s1), str(s2)])
        self.assertTrue(all(type(s) is Square for s in out))


if __name__ == "__main__":
    unittest.main()
