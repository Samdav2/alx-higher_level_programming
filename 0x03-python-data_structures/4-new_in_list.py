#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    if idx < 0 or > a:
        return my_list
    else:
        new_list = my_list
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list
