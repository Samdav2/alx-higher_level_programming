#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    new_list = []
    p = 0
    y = 0
    try:
        for i in range(x + 1):
            j += 1
            new_list.append(my_list[i])
        return new_list
    except IndexError:
        if x > j:
            p = x - j
            y = x - p
            y += 1
        for k in range(y):
            new_list.append(my_list[k])
        return new_list
