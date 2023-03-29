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

    @property
    def size(self):
        """This gets the size i.e getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the size i.e setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This returns the area of the square"""
        return self.__size ** 2
    def my_print(self):
        """This prints the square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
