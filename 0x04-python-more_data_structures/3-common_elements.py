#!/usr/bin/python3
def common_elements(set_1, set_2):
    len1 = len(set_1)
    len2 = len(set_2)
    total = len1 + len2
    for i in range(total):
        if set_1[i] == set_2[i]:
            equal = set_1
    return equal
