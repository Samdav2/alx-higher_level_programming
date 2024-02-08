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
    def area(self):
        a = self.__size ** 2
    def size(self, vlaue):
        return self.value = a
    def size(self):
        return self.size
