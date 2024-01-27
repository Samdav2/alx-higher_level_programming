#!/usr/bin/python3
def uniq_add(my_list=[]):
    index = 0
    new_list = []
    for i in my_list:
        temp = len(new_list)
        for j in range(temp):
            new_list.append(i)
            if i == new_list(j):
                continue
    add = 0
    for w in new_list:
        add += w
    return add
