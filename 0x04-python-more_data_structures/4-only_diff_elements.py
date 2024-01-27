#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for i in set_1:
        for j in set_2:
            if j == i or i == j:
                continue
            else:
                new_set.append(i)
                new_set.append(j)
    return new_set
