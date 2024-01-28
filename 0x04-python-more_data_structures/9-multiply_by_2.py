#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    clone = a_dictionary.copy()
    for i in clone:
        clone *= 2
    return clone
