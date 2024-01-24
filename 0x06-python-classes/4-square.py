#!/usr/bin/python3
"""Define a class square"""
class Square:
    """represent python square"""

    def __init__(self, size=0):
        """initialize a new square.

        Args:
        size (int): size of new square.
        """

        self.size = size

        @property
        def size(self):
            """get the current size of square."""
            return (self._size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self._size = value

            def area(self):
                """return the currentarea of square."""
                return (self._size * self._size)
