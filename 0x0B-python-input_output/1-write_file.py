#!/usr/bin/python3
"""Defines a function write_file"""


def write_file(filename="", text=""):
    """writes string to a text file.


    Args:
        filename (string, optional): name of the file. Default ""
        text (string): string to write into text file

    Returns:
            int: number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
    """This method returns the number of characters written"""
        return f.write(text)
