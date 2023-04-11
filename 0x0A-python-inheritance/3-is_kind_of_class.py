#!/usr/bin/python3
"""
This module contains a function that checks if object is
instance of or if  if the object is an instance of a class
that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """checks if obj is kind of class"""
    if isinstance(obj, a_class) is True:
        return True
    return False
