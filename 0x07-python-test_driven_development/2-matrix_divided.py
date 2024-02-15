#!/usr/bin/python3
""" This is a python scipt that divide matrix"""


def matrix_divided(matrix, div):
    """ This is a function that divide a matrix"""
    new = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    lenght = len(matrix[0])

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != lenght:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for cell in row:
            if (not isinstance(cell, int) and not isinstance(cell, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(cell / div, 2))
        new.append(new_row)
    return new

