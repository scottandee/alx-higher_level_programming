#!/usr/bin/python3
"""This module tests the Rectangle class"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestInstantiation(unittest.TestCase):
    """Unittesting instantiation with different number of attributes"""

    def test_no_param(self):
        self.assertRaises(TypeError, Rectangle)

    def test_one_param(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_two_param(self):
        rect = Rectangle(10, 23)
        rect1 = Rectangle(14, 15)
        self.assertEqual(rect.id, rect1.id - 1)

    def test_three_param(self):
        rect = Rectangle(12, 10, 67)
        rect1 = Rectangle(14, 15, 30)
        self.assertEqual(rect.id, rect1.id - 1)

    def test_four_param(self):
        rect = Rectangle(3, 3, 2, 102)
        rect1 = Rectangle(14, 15, 30, 2)
        self.assertEqual(rect.id, rect1.id - 1)

    def test_five_param(self):
        rect = Rectangle(3, 4, 1, 1, 500)
        self.assertEqual(rect.id, 500)

    def test_over_five(self):
        self.assertRaises(TypeError, Rectangle, 3, 4, 6, 7, 102, 4)

class TestGetterSetter(unittest.TestCase):
    def setUp(self):
        self.rect_1 = Rectangle(10, 12)
        self.rect_2 = Rectangle(10, 62, 1, 2, 13)
    
    def test_get_height(self):
        self.assertEqual(self.rect_2.height, 62)
        self.assertEqual(self.rect_1.height, 12)

    def test_set_height(self):
        self.rect_1.height = 5
        self.rect_2.height = 20
        self.assertEqual(self.rect_1.height, 5)
        self.assertEqual(self.rect_2.height, 20)

    def test_get_width(self):
        self.assertEqual(self.rect_1.width, 10)
        self.assertEqual(self.rect_2.width, 10)

    def test_set_width(self):
        self.rect_1.width = 20
        self.rect_2.width = 15
        self.assertEqual(self.rect_1.width, 20)
        self.assertEqual(self.rect_2.width, 15)

    def test_get_x(self):
        self.assertEqual(self.rect_1.x, 0)
        self.assertEqual(self.rect_2.x, 1)

    def test_set_x(self):
        self.rect_1.x = 2
        self.rect_2.x = 2
        self.assertEqual(self.rect_1.x, 2)
        self.assertEqual(self.rect_2.x, 2)

    def test_get_y(self):
        self.assertEqual(self.rect_1.y, 0)
        self.assertEqual(self.rect_2.y, 2)

    def test_set_y(self):
        self.rect_1.y = 1
        self.rect_2.y = 1
        self.assertEqual(self.rect_1.y, 1)
        self.assertEqual(self.rect_2.y, 1)

class TestWidthValue(unittest.TestCase):
    """This tests the possible outcomes of values passed as width"""

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("17", 10)

    def test_bool_width(self):
        with self.assertRaisesRegex(typeerror, "width must be an integer"):
            Rectangle(True, 10)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.3, 10)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 10)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10j, 3)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 1)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 3], 10)

class TestHeightValue(unittest.TestCase):
    """This tests the possible outcomes of values passed as width"""

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, False)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 50j)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [2, 3])

class TestXValue(unittest.TestCase):
    """This tests the possible outcomes of values passed as width"""

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, "1", 45)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(11, 10, True, 34)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(34, 10, None, 67)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 34, 5j, 50)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(34, 49, -10, 2)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(45, 56, [2, 3], 10)

class TestYValue(unittest.TestCase):
    """This tests the possible outcomes of values passed as width"""

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 45, "1")

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(11, 10, 34, True)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(34, 10, 67, None)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 34, 50, 5j)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(34, 49, 2, -10)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(45, 56, 10, [2, 3])

class TestArea(unittest.TestCase):
    """This tests the the area method"""

    def test_small_area(self):
        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

    def test_big_area(self):
        rect = Rectangle(10000, 10000)
        self.assertEqual(rect.area(), 100000000)

    def test_changed_area(self):
        rect = Rectangle(50, 20)
        rect.height = 56
        rect.width = 60
        self.assertEqual(rect.area(), 3360)

class TestDispayStdOut(unittest.TestCase):
    """This method tests the display that is produced to stdout"""

    def test_display_rect_width_height(self):
       expected = "##\n##\n##\n"
       with patch('sys.stdout', new = StringIO()) as fake_out:
           rect = Rectangle(2, 3)
           rect.display()
           self.assertEqual(fake_out.getvalue(), expected)

    def test_display_rect_width_height_x(self):
       expected = " ##\n ##\n ##\n"
       with patch('sys.stdout', new = StringIO()) as fake_out:
           rect = Rectangle(2, 3, 1)
           rect.display()
           self.assertEqual(fake_out.getvalue(), expected)

    def test_display_rect_width_height_y(self):
       expected = "\n##\n##\n##\n"
       with patch('sys.stdout', new = StringIO()) as fake_out:
           rect = Rectangle(2, 3, 0, 1)
           rect.display()
           self.assertEqual(fake_out.getvalue(), expected)

    def test_display_rect_width_height_x_y(self):
       expected = "\n\n  ##\n  ##\n  ##\n"
       with patch('sys.stdout', new = StringIO()) as fake_out:
           rect = Rectangle(2, 3, 2, 2)
           rect.display()
           self.assertEqual(fake_out.getvalue(), expected)

    def test_str_height_width_display(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            rect = Rectangle(2, 3)
            self.assertEqual(rect.__str__(), "[Rectangle] ({}) 0/0 - \
2/3".format(rect.id))

    def test_str_height_width_x_display(self):
        rect = Rectangle(2, 3, 1, 15)
        self.assertEqual(rect.__str__(), "[Rectangle] ({}) 1/15 - \
2/3".format(rect.id))

    def test_str_height_width_y_display(self):
        rect = Rectangle(2, 3, 0, 2, 10)
        self.assertEqual(rect.__str__(), "[Rectangle] ({}) 0/2 - \
2/3".format(rect.id))

class TestArgUpdate(unittest.TestCase):
    """Testing the update function that assigns no keyword argument to attribute"""

    def setUp(self):
        self.rect = Rectangle(10, 10, 10, 10)

    def test_one_arg(self):
        self.rect.update(43)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 10/10 - \
10/10")

    def test_two_arg(self):
        self.rect.update(43, 23)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 10/10 - \
23/10")

    def test_three_arg(self):
        self.rect.update(43, 23, 40)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 10/10 - \
23/40")

    def test_four_arg(self):
        self.rect.update(43, 23, 40, 5)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 5/10 - \
23/40")

    def test_five_arg(self):
        self.rect.update(43, 23, 40, 5, 6)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 5/6 - \
23/40")

    def test_more_than_five_arg(self):
        self.rect.update(43, 23, 40, 5, 6, 7)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 5/6 - \
23/40")


class TestKwargUpdate(unittest.TestCase):
    """Testing the update function that assigns key-worded argument to attribute"""

    def setUp(self):
        self.rect = Rectangle(10, 10, 10, 10)

    def test_one_kwarg(self):
        self.rect.update(id=43)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 10/10 - \
10/10")

    def test_two_kwarg(self):
        self.rect.update(width=23, id=43)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 10/10 - \
23/10")

    def test_three_kwarg(self):
        self.rect.update(height=40, width=23, id=43)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 10/10 - \
23/40")

    def test_four_kwarg(self):
        self.rect.update(x=5, width=23, height=40, id=43)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 5/10 - \
23/40")

    def test_five_kwarg(self):
        self.rect.update(height=40, width=23, id=43, x=5, y=6)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 5/6 - \
23/40")

    def test_more_than_five_kwarg(self):
        self.rect.update(id=43, width=23, height=40, x=5, y=6, z=7)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (43) 5/6 - \
23/40")

    def test_arg_is_not_empty_kwarg(self):
        self.rect.update(54, 56, 7, y=3, x=3)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (54) 10/10 - \
56/7")


class TestRectToDict(unittest.TestCase):
    """
    This tests method that converts the 
    fields of the rectangle into a dictionary
    """

    def test_rect_to_dict(self):
        rect = Rectangle(10, 2, 1, 9, 77)
        expected = {'x': 1, 'y': 9, 'id': 77, 'height': 2, 'width': 10}
        self.assertEqual(rect.to_dictionary(), expected)
        self.assertEqual(type(rect.to_dictionary()), dict)
