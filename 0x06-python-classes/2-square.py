#!/usr/bin/python3
"""
This module initialises a private object variable
with an optional size
"""


class Square:
    """This is a class that creates a square"""

    def __init__(self, size=0):
        """this initialises a private object variable"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
