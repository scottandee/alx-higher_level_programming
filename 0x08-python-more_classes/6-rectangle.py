#!/usr/bin/python3
"""
This module creates two private instance attributes
called width and height
"""


class Rectangle:
    """This is the rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This function runs when a new instance is created"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This returns the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width property"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This returns the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height property"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This finds the area of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """This finds the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            if i != self.__height - 1:
                print("")
        return ""

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", "\
             + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
