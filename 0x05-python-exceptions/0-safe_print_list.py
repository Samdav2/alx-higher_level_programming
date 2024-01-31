#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    new_list = []
    try:
        for i in range(x):
            j += 1
            new_list.append(my_list[i])
        return my_list[i]
    except IndexError:
        x = j
        for k in range(x):
            new_list.append(my_list[k])
        return my_list[k]
