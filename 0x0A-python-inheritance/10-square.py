#!/usr/bin/python3
"""This is a python script that inherits from rectangle 9"""


Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """ This is a class that defines a square"""

    def __init__(self, size):
        """Initialize the qaure"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
