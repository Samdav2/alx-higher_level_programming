#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 1000, 13, 34, 5, 100, -13, 3, 3000]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
