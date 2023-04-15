#!/usr/bin/python3
"""This module tests the Base class"""


from models.base import Base
import unittest


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
