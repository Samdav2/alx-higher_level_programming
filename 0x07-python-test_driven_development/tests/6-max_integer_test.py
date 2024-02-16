#!/usr/bin/python3
"""
    This is a python script and text file
"""

def max_integer(list=[]):
    """ This is a function that find
        the number with the largest 
        value in a list
    """

    new = []

    new = sort(list)
    return new[-1]
