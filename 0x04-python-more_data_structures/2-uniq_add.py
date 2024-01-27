#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    new_list = sorted(set(my_list))
    add = 0
    for w in new_list:
        add += w
    return add
