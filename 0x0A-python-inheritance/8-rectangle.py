#!/usr/bin/python3
""" Python that inherits from the upper parent"""


class BaseGeometry:
    """This is an empty class"""

    def area(self):
        """ This a method that returns a function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ The integer validator"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ A child class that inherits from the parent"""

    def __init__(self, width, height):
        """ Initialize the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
