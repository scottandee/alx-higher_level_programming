#!/usr/bin/python3
"""This module contains a function that checks if isinstance"""


def is_same_class(obj, a_class):
    if a_class == object:
         return False
    if isinstance(obj, a_class) is True:
        return True
    return False
