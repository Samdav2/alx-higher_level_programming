#!/usr/bin/pyhton3
"""This is a function that inherits class checking"""


def inherits_from(obj, a_class):
    """This checks if an object is inherited in instance of a class"""
    if issubclass(type(obj), a_class) and (type(obj) != a_class):
        return True
    return False
