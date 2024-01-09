#!/usr/bin/python3
"""Defines the function load_from_json_file."""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file.


    Args:
        filename (str, optional): name of the file


    Returns:
        object: The object created from the JSON data
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()

        return json.loads(read_data)
