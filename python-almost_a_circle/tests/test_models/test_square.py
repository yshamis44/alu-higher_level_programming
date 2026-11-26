#!/usr/bin/python3
"""Unittests for the Square class in models/square.py."""
import io
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def output(self, func):
        """Return what func prints to stdout."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            func()
        return buf.getvalue()

    def test_is_rectangle(self):
        """Square inherits from Rectangle and Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_attributes(self):
        """size sets both width and height."""
        s = Square(3, 1, 2, 7)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (3, 3, 3, 1, 2, 7))

    def test_ids(self):
        """Ids come from Base."""
        self.assertEqual(Square(5).id, 1)
        self.assertEqual(Square(2, 2).id, 2)

    def test_missing_size(self):
        """size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_validation(self):
        """Square uses the Rectangle checks and messages."""
        with self.assertRaises(TypeError) as e:
            Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(TypeError) as e:
            Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_size_setter(self):
        """The size setter changes width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(ValueError):
            s.size = 0

    def test_area(self):
        """area is size times size."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)

    def test_str(self):
        """str gives the right format."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (2) 1/3 - 3")

    def test_display(self):
        """display uses x and y."""
        self.assertEqual(self.output(Square(2, 2).display), "  ##\n  ##\n")
        self.assertEqual(self.output(Square(1, 1, 1).display), "\n #\n")

    def test_update_args(self):
        """update sets id, size, x and y in order."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """update sets values from kwargs."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_skip_kwargs(self):
        """kwargs are skipped when args are given."""
        s = Square(5)
        s.update(3, size=9)
        self.assertEqual(str(s), "[Square] (3) 0/0 - 5")

    def test_update_validates(self):
        """update checks the values."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "2")
        with self.assertRaises(ValueError):
            s.update(size=-1)

    def test_to_dictionary(self):
        """to_dictionary returns id, size, x and y."""
        s = Square(10, 2, 1)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_update(self):
        """A dictionary can update another square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

    def test_square_y_string(self):
        """Square(1, 2, "3") raises a TypeError for y."""
        with self.assertRaises(TypeError) as e:
            Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_square_negative_size(self):
        """Square(-1) raises a ValueError for width."""
        with self.assertRaises(ValueError) as e:
            Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_square_negative_x(self):
        """Square(1, -2) raises a ValueError for x."""
        with self.assertRaises(ValueError) as e:
            Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_square_save_to_file_none(self):
        """Square.save_to_file(None) saves an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
