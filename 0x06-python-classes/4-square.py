#!/usr/bin/python3
""" This is a python script that get and set value in a class"""


class Square:
    """ This is a class that get the value and set the value in a class"""
    def __init__(self, size=0):
        """ This is a automatic initializer in this class"""
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ Getting the data"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Settting the data"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Retunr the area"""
        return self.__size**2
