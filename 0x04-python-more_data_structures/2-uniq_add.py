#!/usr/bin/python3
def uniq_add(my_list=[]):
    index = 0
    new_list = []
    index = 0
    for i in my_list:
        index += 1
        for j in range(index):
            new_list.append(i)
            if i == new_list(index):
                continue
    add = 0
    for w in new_list:
        add += w
    return add
