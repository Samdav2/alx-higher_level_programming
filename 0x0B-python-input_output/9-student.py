#!/usr/bin/python3
""" This is a class of a studen """


class Student:
    """A class student with public class"""
    firs_name = NULL
    last_name = NULL
    age = NULL

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age  = age

    def to_json(self):
        return self.__dict__
