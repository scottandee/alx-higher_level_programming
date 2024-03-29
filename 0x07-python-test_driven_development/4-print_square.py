#!/usr/bin/python3
"""Module that contains the print square function"""


def print_square(size):
    """This function prints out a square of specified size"""
    if type(size) == float and size > 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        if i != size - 1:
            print("")
    print()
