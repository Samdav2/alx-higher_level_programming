#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    new_list = my_list[:]
    if idx < 0 or idx  >= a:
        return new_list
    else:
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list
