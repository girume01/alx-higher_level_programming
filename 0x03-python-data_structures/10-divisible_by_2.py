#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    #create new list to store true or false
    count_list = [num % 2 == 0 for num in my_list]

    return count_list
