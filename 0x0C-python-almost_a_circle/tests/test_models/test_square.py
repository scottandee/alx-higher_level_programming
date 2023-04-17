#!/usr/bin/python3
"""This module contains unittests for the Square Class"""


import unittest
from models.square import Square


class TestSquareInitialization(unittest.TestCase):
    """This tests the initialization of the Square class"""

    def test_only_size(self):
        sq = Square(4)
        self.assertEqual(sq.width, 4)
        self.assertEqual(sq.height, 4)

    def test_sq_two_param(self):
        sq = Square(4, 5)
        self.assertEqual(sq.height, 4)
        self.assertEqual(sq.width, 4)
        self.assertEqual(sq.x, 5)

    def test_sq_three_param(self):
        sq = Square(5, 6, 7)
        self.assertEqual(sq.height, 5)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.x, 6)
        self.assertEqual(sq.y, 7)

    def test_sq_four_param(self):
        sq = Square(5, 6, 7, 50)
        self.assertEqual(sq.height, 5)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.x, 6)
        self.assertEqual(sq.y, 7)
        self.assertEqual(sq.id, 50)

class TestSqWidthValue(unittest.TestCase):
    """This tests the possible outcomes of values passed as width"""

    def test_sq_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("17")

    def test_sq_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.3)

    def test_sq_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_sq_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_sq_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10j)

    def test_sq_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

    def test_sq_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_sq_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 3])

class TestSqXValue(unittest.TestCase):
    """This tests the possible outcomes of values passed as x"""

    def test_sq_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "17")

    def test_sq_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 10.3)

    def test_sq_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(23, True)

    def test_sq_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(23, None)

    def test_sq_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 10j)

    def test_sq_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -2)

    def test_sq_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, [2, 3])

class TestSqYValue(unittest.TestCase):
    """This tests the possible outcomes of values passed as y"""

    def test_sq_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 10, "17")

    def test_sq_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 6, 10.3)

    def test_sq_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(23, 30, True)

    def test_sq_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(23, 7, None)

    def test_sq_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 4, 10j)

    def test_sq_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 3, -2)

    def test_sq_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 45, [2, 3])

class TestStrRepresentation(unittest.TestCase):
    """This tests the output of printing the string representation"""

    def test_sq_string_rep(self):
       sq = Square(23, 42, 4, 45)
       self.assertEqual(sq.__str__(), f"[Square] (45) 42/4 - 23")

class TestSizeGetterSetter(unittest.TestCase):
    """This tests the getter and setter for the size"""

    def test_size_getter(self):
        sq = Square(14)
        self.assertEqual(sq.size, 14)

    def test_size_setter(self):
        sq = Square(25)
        sq.size = 45
        self.assertEqual(sq.size, 45)

class TestSqUpdateArgs(unittest.TestCase):
    """This tests the update method when no keyword parameters are passed"""

    def setUp(self):
        self.sq = Square(10, 10, 10, 10)

    def test_sq_one_arg(self):
        self.sq.update(99)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 10/10 - 10")

    def test_sq_two_arg(self):
        self.sq.update(99, 30)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 10/10 - 30")

    def test_sq_three_arg(self):
        self.sq.update(99, 30, 3)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 3/10 - 30")

    def test_sq_three_arg(self):
        self.sq.update(99, 30, 3, 4)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 3/4 - 30")

class TestSqUpdateKwargsArgs(unittest.TestCase):
    """This tests the update method when keyworded parameters are passed"""

    def setUp(self):
        self.sq = Square(10, 10, 10, 10)

    def test_sq_one_kwarg(self):
        self.sq.update(id=99)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 10/10 - 10")

    def test_sq_two_kwarg(self):
        self.sq.update(size=30, id=99)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 10/10 - 30")

    def test_sq_three_kwarg(self):
        self.sq.update(id=99, x=3, size=30)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 3/10 - 30")

    def test_sq_three_kwarg(self):
        self.sq.update(size=30, id=99, y=4, x=3)
        self.assertEqual(self.sq.__str__(), "[Square] (99) 3/4 - 30")
    
    def test_sq_kwarg_arg(self):
        self.sq.update(43, 56, x=45, y=8)
        self.assertEqual(self.sq.__str__(), "[Square] (43) 10/10 - 56")

class TestSqToDict(unittest.TestCase):
    """
    This tests method that converts the 
    fields of the rectangle into a dictionary
    """

    def test_sq_to_dict(self):
        sq = Square(10, 2, 1, 10)
        expected = {'x': 2, 'y': 1, 'id': 10, 'size': 10}
        self.assertEqual(sq.to_dictionary(), expected)
        self.assertEqual(type(sq.to_dictionary()), dict)
