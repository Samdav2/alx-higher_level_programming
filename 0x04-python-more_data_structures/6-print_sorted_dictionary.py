#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary.key()):
        print("{}: {}" .format(keys, a_dictionary[key]))
