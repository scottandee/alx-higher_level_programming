#!/usr/bin/python3
"""
Module containing function that divides all elements of a matrix 
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    m = [row[:] for row in matrix]
    len2 = 0
    length = 0

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    for i in range(len(m)):
        length = len(m[i])
        if i == 0:
            len2 = len(m[i])
        if i != 0 and len2 != len(m[i]):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(m[i]) == 1:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in range(length):
            if type(m[i][j]) != int and type(m[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            y = m[i][j] / div
            m[i][j] = round(y, 2)
    return m
