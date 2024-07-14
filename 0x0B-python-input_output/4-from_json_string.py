#!/usr/bin/python3
"""returns the object representation"""


def from_json_string(my_str):
    """ This returns the object representation of a JSON"""
    return json.loads(my_str)
