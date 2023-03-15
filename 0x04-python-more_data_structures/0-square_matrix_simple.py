#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Function to square all integers of a matrix

    """Using for loop"""
    """
    new_matrix = []
    sub_matrix = []
    for i in matrix:
        for j in i:
            sub_matrix.append(j * j)
        new_matrix.append(sub_matrix)
        sub_matrix = []
    return new_matrix
    """

    """Using list comprehension"""
    sub_matrix = []
    new_matrix = [[j * j for j in i] for i in matrix]
    return new_matrix
