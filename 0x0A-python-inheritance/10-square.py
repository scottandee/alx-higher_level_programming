#!/usr/bin/python3
"""Module that contains a grandchild class"""\


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is a grandchild class that inherits the rectangle class"""

    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        return super().area()
