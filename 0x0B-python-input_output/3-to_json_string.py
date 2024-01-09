#!/usr/bin/python3
"""Defines the function to_json_string"""

import json

def to_json_string(my_obj):
    """gets the JSON representation of an object.


    Args:
        my_obj (type): object to be converted to JSON.

    Returns:
        str: JSON representation of object.
    """
    x = json.dumps(my_obj)

    return x
