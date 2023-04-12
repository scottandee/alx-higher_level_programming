#!/usr/bin/python3
"""This module contains a function that appends to a file"""


def append_write(filename="", text=""):
    """This function opens and appends to a file"""

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
