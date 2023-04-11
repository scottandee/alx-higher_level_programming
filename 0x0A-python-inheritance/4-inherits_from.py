#!/usr/bin/python3
"""
Module that contains function that checks
for class that inherits from
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
