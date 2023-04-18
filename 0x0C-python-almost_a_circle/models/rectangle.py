#!/usr/bin/python3
"""This module contains the rectangle class"""

from models.base import Base


class Rectangle(Base):
    """This is a subclass of the class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method runs after every new instantiation"""

        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def height(self):
        """This gets the value of instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """This gets the value of instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """This gets the value of instance x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This sets the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This gets the value of instance y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """This prints out the rectangle with a # symbol"""

        for i in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            if i != self.height - 1:
                print()
        print()

    def __str__(self):
        """This prints out the string representation of the rectangle"""

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """This updates the values of the instance attributes"""

        if not args and kwargs:
            for key in kwargs:
                if key == "height":
                    self.height = kwargs[key]
                if key == "id":
                    self.id = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "width":
                    self.width = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]

    def to_dictionary(self):
        """Returns the rectangle representation of a Rectangle instance"""

        dic = {'id': self.id, 'height': self.height, 'width': self.width,
               'x': self.x, 'y': self.y}
        return dic
