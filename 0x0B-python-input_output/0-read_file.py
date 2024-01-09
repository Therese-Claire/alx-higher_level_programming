#!/usr/bin/python3
"""Defines the function read_file"""


def read_file(filename=""):
    """reads a text file and prints to stdout.


    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end= '')
