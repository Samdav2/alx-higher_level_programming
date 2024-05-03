#!/usr/bin/python3
"""python script that print the
perimeter of the rectangle
"""


class Rectangle:
    """ A class the defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        s = ''
        if sef.__height == 0 or self.__width == 0:
            return s
        for i in range(self.height):
            for j in range(self.width):
                s += '#'
            if i != self.height - 1:
                s += '\n'
        return s

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
