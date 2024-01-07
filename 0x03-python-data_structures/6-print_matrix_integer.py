#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    if not matrix:
        print()
    else:
        for row in matrix:
            for i, item in enumerate(row):
                end_char = ' $' if i != len(row) - 1 else '$\n'
                print("{:d}".format(item), end=end_char)
                print()

