#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    b = len(a_dictionary)
    j = 0
    for i in a_dictionary:
        j += 1
        a = i
        if a < a_dictionary[i] and j != b:
            continue
        else:
            a = i
    return a
