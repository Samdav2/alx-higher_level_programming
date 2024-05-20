#!/usr/bin/python3
""" This is a function inherit from a class"""


class MyList(list):
    """ This is a child class that inherit from the parent"""

    def print_sorted(self):
        """ This print a sorted list"""

        list_cp = self.copy()
        list_cp.sort()
        print("{}" .format(list_cp))
