#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    equal = []
    equal = set_1 + set_2
    new_set = sorted(set(equal))
    return new_set
