#!/usr/bin/python3
"""
Module in which contains the Base Geometry class
and instance methods: area and integer_validator
"""


class BaseGeometry:
    """This is a base geomety class with object method"""

    def area(self):
        """This finds the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This confirms if the integer is valid"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.__class__.__name__))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
