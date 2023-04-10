#!/usr/bin/python3
"""Script that contains say_my_name"""


def say_my_name(first_name, last_name=""):
    """This function says the name that is entered"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
