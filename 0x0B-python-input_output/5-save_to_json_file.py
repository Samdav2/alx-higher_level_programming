#!/usr/bin/python3
"""writes a object to a text file with JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ write a object with JSON representation"""

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
