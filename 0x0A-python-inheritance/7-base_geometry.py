#!/usr/bin/python3
""" This is python script that raise exeption"""


class BaseGeometry:
    """This is an empty class"""

    def area(self):
        """ This a method that returns a function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name

        if (isinstance(value, int) == False):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.value = value
