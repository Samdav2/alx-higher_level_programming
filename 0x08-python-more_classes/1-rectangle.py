#!/usr/bin/python3
""" This python file with a class
    that represent a rectangle
    """


class Rectangle:
    """ A class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width
    def width(self, value):
        if value is not int:
            raise TypeError("width must be an integer"):
        elif value < 0:
            raise ValueError("width must be >= 0"):
        else:
            self.__width = value
    def height(self):
        return self.__height
    def height(self, value):
        if value is not int:
            raise TypeError("height must be an integer"):
        elif value < 0:
            raise TypeError("height must be >= 0"):
        else:
            self.__height = value
