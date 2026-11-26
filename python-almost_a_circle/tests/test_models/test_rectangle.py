#!/usr/bin/python3
"""Unittests for the Rectangle class in models/rectangle.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def output(self, func):
        """Return what func prints to stdout."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            func()
        return buf.getvalue()

    def test_is_base(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        """Ids come from Base."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """All values are stored and readable."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private(self):
        """The attributes are private."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def test_missing_args(self):
        """width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """More than 5 arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_type_errors(self):
        """Values that are not integers raise a TypeError."""
        cases = [("width", ("1", 2)), ("height", (1, "2")),
                 ("x", (1, 2, "3")), ("y", (1, 2, 3, "4")),
                 ("width", (1.5, 2)), ("height", (1, None)),
                 ("x", (1, 2, [3])), ("y", (1, 2, 3, {})),
                 ("width", (True, 2))]
        for name, args in cases:
            with self.assertRaises(TypeError) as e:
                Rectangle(*args)
            self.assertEqual(str(e.exception),
                             "{} must be an integer".format(name))

    def test_value_errors(self):
        """Values out of range raise a ValueError."""
        cases = [("width must be > 0", (0, 2)),
                 ("width must be > 0", (-1, 2)),
                 ("height must be > 0", (1, 0)),
                 ("height must be > 0", (1, -2)),
                 ("x must be >= 0", (1, 2, -3)),
                 ("y must be >= 0", (1, 2, 3, -1))]
        for msg, args in cases:
            with self.assertRaises(ValueError) as e:
                Rectangle(*args)
            self.assertEqual(str(e.exception), msg)

    def test_setters_validate(self):
        """The setters check values too."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}
        r.width = 5
        r.y = 0
        self.assertEqual((r.width, r.y), (5, 0))

    def test_area(self):
        """area returns width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_args(self):
        """area takes no arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display(self):
        """display prints the rectangle with #."""
        out = self.output(Rectangle(2, 2).display)
        self.assertEqual(out, "##\n##\n")

    def test_display_x_y(self):
        """display moves the rectangle by x and y."""
        out = self.output(Rectangle(2, 3, 2, 2).display)
        self.assertEqual(out, "\n\n  ##\n  ##\n  ##\n")
        out = self.output(Rectangle(3, 2, 1, 0).display)
        self.assertEqual(out, " ###\n ###\n")

    def test_str(self):
        """str gives the right format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """update sets values in order from args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update sets values from kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args_skip_kwargs(self):
        """kwargs are skipped when args are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(5, width=3)
        self.assertEqual(str(r), "[Rectangle] (5) 10/10 - 10/10")

    def test_update_nothing(self):
        """update with nothing changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_validates(self):
        """update uses the setters, so bad values raise errors."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.update(1, "2")
        with self.assertRaises(ValueError):
            r.update(width=0)

    def test_to_dictionary(self):
        """to_dictionary returns all attributes."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})
        self.assertEqual(type(d), dict)

    def test_to_dictionary_update(self):
        """A dictionary can update another rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
