#!/usr/bin/python3
""" This is a python script that adds integer"""


def add_integer(a, b=98):
    """ This  is a function that adds two integer"""
    if (isinstance(a, int or float) is False):
        raise TypeError("a must be an integer")
    elif (isinstance(a, int or float) is False):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
