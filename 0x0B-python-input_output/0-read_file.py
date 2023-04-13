#!/usr/bin/python3
"""This module contains a function that reads a file"""


def read_file(filename=""):
    """This fuction opens a file and reads it"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
