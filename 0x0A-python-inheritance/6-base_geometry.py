#!/usr/bin/python3
"""
Module in which an empty class is created
"""


class BaseGeometry:
    """This is a base geomety class with object method"""
    def area(self):
        """This tells us that area is not implemented"""
        raise Exception("area() is not implemented")
