#!/usr/bin/python3
"""Defines a function for checking inheritance relationships."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a specific class.

    Args:
    obj (any): object to check.
    a_class (type): class to compare with obj type.

    Returns:
    True if obj is an inherited instance of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

