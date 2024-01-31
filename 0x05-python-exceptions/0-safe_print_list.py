#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(x):
        j += 1
        try:
            return my_list[i]
    except IndexError:
        x = j
        for k in range x:
            return my_list[k]
