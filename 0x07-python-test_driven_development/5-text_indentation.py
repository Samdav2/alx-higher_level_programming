#!/usr/bin/python3
""" This is a python script that reformat a test"""


def text_indentation(text):
    """ This is a function that split a sentence"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == "?" or i == "." or i == "," or i == ":":
            print("{}".format(i), end="")
            print()
            print()
        else:
            print("{}".format(i), end="")
