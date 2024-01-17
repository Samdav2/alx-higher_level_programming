#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    if idx > a:
        return None
    elif idx < 0:
        return my_list
    else:
        return my_list[idx]

