#!/usr/bin/python3
"""Defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of the,
    specifies class ; otherwise False


    Args:
        obj (a_class): object to check type.
        a_class (type): type of type to check.

    Returns:
        boolean: True or False
    """
    return type(obj) is a_class
