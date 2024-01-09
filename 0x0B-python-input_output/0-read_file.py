#!/usr/bin/python3
"""Defines a function read_file(filename="")"""


def read_file(filename=""):
    """function that reads a text file (UTF8),
    and prints it to stdout


    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, 'r',  encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end= '')
