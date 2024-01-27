#!/usr/bin/python3
def common_elements(set_1, set_2):
    equal = []
    for i in set_1:
        for w in set_2:
            if i == w:
                equal.append(w)
    return equal
