#!/usr/bin/python3
""" python script that defines private instance and public Instance"""
class Square:
    """ Creating the class named squared with different instances"""
    def __init__(self, size):
        """ Automatic data assigning"""
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        self.area = size
