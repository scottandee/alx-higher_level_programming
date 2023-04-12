#!/usr/bin/python3
"""
Module that contains function that checks
for class that inherits from
"""


def inherits_from(obj, a_class):
    """Checks if an object is only a subclass of"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
