#!/usr/bin/python3
def common_elements(set_1, set_2):
    len1 = len(set_1)
    len2 = len(set_2)
    total = len1 + len2
    for i in set_1:
        for w in set_2:
            if i == w:
                equal.append(w)
    return equal
