#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = map(lambda x: x ** 2, matrix)
    listing = list(squared)
    return listing
