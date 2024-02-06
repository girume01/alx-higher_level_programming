#!/usr/bin/python3
"""Defines the json file reading function."""
import json

def load_from_json_file(filename):
    """
    create python object from a json file.
    """
    with open(filename) as f:
        return json.load(f)

