#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    equal = []
    for i in set_1:
        for j in set_2:
            equal.append(i)
            equal.append(j)
    new_set = sorted(set(equal))
    return new_set
