#!/usr/bin/python3
"""
This module contains a function that checks if isinstance
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """checks if Is the Same Class"""
    if type(obj) is a_class:
        return True
    return False
