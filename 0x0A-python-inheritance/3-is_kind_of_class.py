#!/usr/bin/python3
""" This is a class that cheekc the instnace of an object"""


def is_kind_of_class(obj, a_class):
    """ A method for checking instance parent"""

    if type(obj) is a_class:
        return True
    return False
