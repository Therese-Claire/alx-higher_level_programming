#!/usr/bin/python3
"""Defines a function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file.


    Args:
        filename (str, optional): name of the file. Default ""
        text (str): string to write into text file

    Returns:
            int: number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        totalChars = f.write(text)
        return totalChars
