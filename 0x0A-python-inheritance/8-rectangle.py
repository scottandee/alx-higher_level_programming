#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Module that contains class that inherits another class"""


class Rectangle(BaseGeometry):
    """Rectangle Inheritance of BaseGeometry class"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width
