#!/usr/bin/python3
def common_elements(set_1, set_2):
    len1 = len(set_1)
    len2 = len(set_2)
    total = len1 + len2
    for i, w in set_1, set_2:
        if i == w:
            equal = w
    return equal
