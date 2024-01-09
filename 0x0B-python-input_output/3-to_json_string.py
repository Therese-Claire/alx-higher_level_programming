#!/usr/bin/python3
"""Defines the function to_json_string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj(object): The object to be serialized to JSON.

    """
    return json.dumps(my_obj)
