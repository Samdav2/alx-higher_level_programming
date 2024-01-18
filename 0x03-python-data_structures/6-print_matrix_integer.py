#!/usr/bin/python2
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}" .format(row[i]), end="")
