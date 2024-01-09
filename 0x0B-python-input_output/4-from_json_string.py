#!/usr/bin/python3
"""Defines the function from_json_string."""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object.

    Args:
        my_obj(object): The object to be deserialized from JSON.

    """
    return json.loads(my_str)
