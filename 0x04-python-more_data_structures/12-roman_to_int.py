#!/usr/bin/python3

def roman_to_int(roman_string: str = None):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data.get(x, 0) for x in roman_string]
    rep = 0

    for current, next_num in zip(numbers, numbers[1:] + [0]):
        if current >= next_num:
            rep += current
        else:
            rep -= current

            print(f"{roman_string} = {rep}")
            return rep
