#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = len(my_list)
    if idx < 0:
        return my_list
    elif idx > a:
        return my_list
    else:
        return my_list[idx] = element
