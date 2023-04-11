#!/usr/bin/python3
"""
Module in which an empty class is created
"""


class BaseGeometry:
    """This is a base geomety class with object method"""
    def area(self):
        """This tells us that area is not implemented"""
        raise Exception(area() is not implemented)

    def integer_validator(self, name, value):
        """This makes sure that the integer is valid"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater that zero")
