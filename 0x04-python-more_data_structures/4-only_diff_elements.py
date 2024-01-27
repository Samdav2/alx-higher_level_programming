#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    equal = []
    same = []
    new_set2 = []
    for i in set_1:
        for j in set_2:
            if i == j:
                same.append(i)
            else:
                equal.append(i)
                equal.append(j)
    new_set = sorted(set(equal))
    for k in new_set:
        for s in same:
            if s == k:
                continue
            else:
                new_set2.append(k)
    return new_set2
