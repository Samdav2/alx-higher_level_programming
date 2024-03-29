#!/usr/bin/python3
""" This is a code that validates the size of a Class"""


class Square:
    """ The class name square that validate the size"""
    def __init__(self, size=0):
        """ This automatically Initialize the size and contetn"""
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
