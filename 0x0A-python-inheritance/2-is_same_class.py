#!/usr/bin/python3
""" This is a class checks if a child is a class"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
