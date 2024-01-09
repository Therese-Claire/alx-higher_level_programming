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
    totalChar = 0
    with open(filename, 'w', encoding="utf-8") as f:
        totalChar = f.write(text)

        return totalChar
