#!/usr/bin/python3
"""
Defines the python class to json function.
"""

def class_to_json(obj):
    """
    Return the dictionary representation of simple data structure.
    """
    return obj.__dict__
