#!/usr/bin/python3
""""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """This is a function that opens a file and writes to it"""

    with open(filename, mode="w", encoding="utf=8") as f:
        return f.write(text)
