#!/usr/bin/python3
""" This is a python script tha prints square"""


def print_square(size):
    """ This is a function that print square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, False) is True and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(i):
            print("#", end="")
        print()
    print()
