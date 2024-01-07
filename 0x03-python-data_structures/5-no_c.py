#!/usr/bin/python3

def no_c(my_string):
    #create a new string without 'c' and 'C'
    count_string = ''.join(char for char in my_string if char not in ('c', 'C'))
    return count_string
