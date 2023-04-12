#!/usr/bin/python3
"""
Module that contains function that checks
for class that inherits from
"""


def inherits_from(obj, a_class):
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
