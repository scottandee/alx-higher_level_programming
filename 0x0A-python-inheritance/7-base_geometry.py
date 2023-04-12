#!/usr/bin/python3
"""
Module in which contains the Base Geometry class
and instance methods: area and integer_validator
"""


class BaseGeometry:
    """This is a base geomety class with object method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater that zero".format(name))
