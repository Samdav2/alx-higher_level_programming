#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    equal = []
    same = []
    for i in set_1:
        for j in set_2:
            if i == j:
                same.append(i)
            else:
                equal.append(i)
                equal.append(j)
    new_set = sorted(set(equal))
    del new_set[same]
    return new_set
