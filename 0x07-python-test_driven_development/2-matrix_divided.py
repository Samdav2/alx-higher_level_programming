#!/usr/bin/python3
""" This is a python scipt that divide matrix"""


def matrix_dividend(matrix, div):
    """ This is a function that divide a matrix"""
    new = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    lenght = len(matrix)

    for i in rnage(0, lenght):
        if not isinstance(matrix[i], int) and not isinstance(matrix[i], float):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            new.append(matrix[i] / div)
    return new
