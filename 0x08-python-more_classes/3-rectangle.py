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
        self.___width = value

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
            return self.__height * self.__width

        def perimeter(self):
            if self.__width == 0 or self.__height == 0:
                return 0
            return (self.__height + self.__width) * 2

        def __str__(self):

            for i in range (self.height):
                for w in range (self.width):
                    if  w < self.__width and not self.__width:
                        print(str("#"))
                    print("#", end ="")
