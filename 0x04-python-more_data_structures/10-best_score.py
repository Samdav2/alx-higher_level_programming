#!/usr/bin/python3
def best_score(a_dictionary):
    b = len(a_dictionary)
    j = 0
    for i in a_dictionary:
        j += 1
        a = a_dictionary[i]
        if a < a_dictionary[i] and j != b:
            continue
        else:
            a = a_dictionary[i]
    return a
