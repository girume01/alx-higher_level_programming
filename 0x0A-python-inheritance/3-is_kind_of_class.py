#!/usr/bin/python3
"""Define the class and inherited class checking function."""

def is_kind_of_class(obj, a_class):
    """
    check if the object is an instance or inherited instance class.

    Args:
    obj (any): object to check.
    a_class (type): the class to match the type of obj to.
    Returns:
    if obj is instance or inherited instance of a_class - True.
    otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
