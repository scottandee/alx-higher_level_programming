#!/usr/bin/python3
"""This module contains the Base class"""


class Base:
    """This is the base class that monitors the id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This runs when a new instance is created"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
