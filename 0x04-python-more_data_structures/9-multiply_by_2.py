#!/usr/bin/python3

def multiply_by_2(my_dict):
    return dict(map(lambda item: (item[0], item[1]*2), my_dict.items()))

