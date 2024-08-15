#!/usr/bin/python3
""" This is a python function that returns python keys"""


class Student:
    """ This is a class that defines public variables"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and not None:
            return self.__dict__[attrs]
        else:
            return self.__dict__
