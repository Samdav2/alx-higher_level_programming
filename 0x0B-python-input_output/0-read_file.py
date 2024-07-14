#!/usr/bin/python3
""" Python script that reads text files and print it"""


def read_file(filename=""):
    """ This method read file (UTF8) and prints to stdout"""
    with open(filename, mode='r') as file:
        print(file.read(), end='')
