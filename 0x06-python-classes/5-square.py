#!/bin/usr/python3
""" This is a pyhon script class that defines instances and modifies it attribut"""


class Square:
    """ This is a class that defines other attributes and instances"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Function that retrieve the value of the data"""
        return self.__size

    @size.setter
    def size(self, value):
        """ function that set the value"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif size< 0:
            raise ValueError("Size must be >= 0")
        else:
            self.size = value

    def area(self):
        """instances that returns the square of size"""
        return self.__size**2

    def my_prinf(self):
        """ function that print # with the number of size"""
        for i in range(0, self.area):
            if i == self.size and i != self.area:
                print("#")
            else print("#", end="")
    print()
