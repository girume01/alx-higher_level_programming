#!/usr/bin/python3
"""Define a python class square."""

class Square:
    """represent a square."""

    def __init__(self, size=0):
        """initialize a new square.

        Args:
        size: The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def area(self):
            """Area of this square.

            Returns:
            The size squared.
            """
            return self.__size ** 2

        my_square_1 = Square(5)
        print("Area: {}".format(my_square_1.area()))

