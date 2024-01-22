#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        double = 0

        try:
            for i in range(x):
            value = int(my_list[i])

                print("{:d}".format(value), end=' ')
                double += 1

            except (IndexError, ValueError):
                pass

            finally:
                print()
                return double

