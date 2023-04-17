#!/usr/bin/python3
"""This module tests the Base class"""

import json
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_init_value(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base(5)
        self.assertEqual(c.id, 5)
        d = Base()
        self.assertEqual(d.id, 3)

class TestDictToJsonClassMethod(unittest.TestCase):
    """This tests the class method that converts dict to JSON string"""

    def test_empty_dict_list(self):
        b = Base()
        list_dict = []
        self.assertEqual(b.to_json_string(list_dict), "[]")

    def test_type_dict_list(self):
        b = Base()
        list_dict = []
        self.assertEqual(type(b.to_json_string(list_dict)), type("[]"))

    def test_one_dict_list(self):

        b = Base()
        r1 = Rectangle(10, 7, 2, 8, 1)
        list_dict = []
        list_dict.append(r1.to_dictionary())
        self.assertEqual(json.loads(b.to_json_string(list_dict)), [{"x": 2, \
"width": 10, "id": 1, "height": 7, "y": 8}])

    def test_two_dict_list(self):
        b = Base()
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(1, 2, 3, 4, 5)
        list_dict = []
        list_dict.append(r1.to_dictionary())
        list_dict.append(r2.to_dictionary())
        self.assertEqual(json.loads(b.to_json_string(list_dict)), [{"x": 2, \
"width": 10, "id": 1, "height": 7, "y": 8}, {"x": 3, "width": 1, "id":\
5, "height": 2, "y": 4}])

    def test_none_dict_list(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")

class TestSaveToFile(unittest.TestCase):
    """This tests the save to file class method that was created"""

    def test_rect_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 3, 4, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            contents = file.read()

        expected = [{"y": 8, "x": 2, "id": 5, "width": 10, "height": 7}\
, {"y": 3, "x": 4, "id": 4, "width": 2, "height": 4}]
        self.assertEqual(json.loads(contents), expected)

    def test_sq_save_to_file(self):
        sq_1 = Square(10, 7, 2, 8)
        sq_2 = Square(2, 4, 5, 6)
        Square.save_to_file([sq_1, sq_2])

        with open("Square.json", "r") as file:
            contents = file.read()

        expected = [{"y": 2, "x": 7, "id": 8, "size": 10}\
, {"y": 5, "x": 4, "id": 6, "size": 2}]
        self.assertEqual(json.loads(contents), expected)


