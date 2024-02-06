#!/usr/bin/python3
"""Defines a file appending function."""

def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file.

    Args:
    filename (str): the name of the file to append to.
    text (str): string to append to the file.
    Returns:
    the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)

