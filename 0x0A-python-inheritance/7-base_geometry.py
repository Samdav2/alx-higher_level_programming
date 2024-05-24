#!/usr/bin/python3
""" This is python script that raise exeption"""


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
