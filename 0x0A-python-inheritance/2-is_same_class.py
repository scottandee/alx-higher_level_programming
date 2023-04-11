#!/usr/bin/python3
"""
This module contains a function that checks if isinstance
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """checks if Is the Same Class"""
    if a_class == object:
        return False
    if isinstance(obj, a_class) is True:
        return True
    return False
