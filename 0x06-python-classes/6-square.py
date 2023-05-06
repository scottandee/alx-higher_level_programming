#!/usr/bin/python3
"""
This module initialises a private object variable
with an optional size
"""


class Square:
    """This is a class that creates a square"""

    def __init__(self, size=0, position=(0, 0)):
        """this initialises a private object variable"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2:
            raise TypeError("position must be a tuple\
 of 2 positive integers")
        for i in range(len(position)):
            if type(position[i]) != int:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
            if position[i] < 0 or i > 3:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
        self.__position = position
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

    @property
    def position(self):
        """This gets the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This sets the position
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple\
 of 2 positive integers")
        for i in range(len(value)):
            if type(value[i]) != int:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
            if value[i] < 0:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
        self.__position = value

    def area(self):
        """This returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """This prints the square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
