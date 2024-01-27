#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        new_list.append(i)
        if i == new_list[i]:
            continue
    add = 0
    for w in new_list:
        add += w
    return add
