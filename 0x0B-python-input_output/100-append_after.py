#!/usr/bin/python3
"""Defines the function append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): Specific string to search for in each line.
        new_string (str): Line of text to insert after each
        line containing the search string.
    """
    content = ""
    with open(filename) as f:
        for line in f:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, 'w') as new_f:
        new_f.write(content)
