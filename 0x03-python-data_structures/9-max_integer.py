#!/usr/bin/python3
def max_integer(my_list=[]):
    a = my_list[0]
    l = len(my_list)
    j = 0
    if not my_list:
        return None
    for i in my_list:
        j += 1
        if a > i and j != a:
            continue
        else:
            a = i
    return a
