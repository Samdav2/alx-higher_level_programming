#!/usr/bin/python3
"""function that print string to a text file"""


def write_file(filename="", text=""):
    """write string to a text"""

    with open(filename, mode='w') as file:
        nchar = file.write(text)
        return nchar
