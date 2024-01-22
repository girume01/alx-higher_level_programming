#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        double = 0
        for i in range(x):
            print(my_list[i], end='')
            double += 1
    except IndexError:
        pass
    finally:
        print()
        return double
