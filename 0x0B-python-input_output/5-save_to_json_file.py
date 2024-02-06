#!/usr/bin/python3
"""Defines the json file writing function."""
import json

def save_to_json_file(my_obj, filename):
    """
    write the object to the text file using JSON.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
