#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = sum({elem for elem in my_list})
    return unique_sum
