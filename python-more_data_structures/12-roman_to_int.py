#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    tab = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    length = len(roman_string)
    for i in range(length):
        value = tab[roman_string[i]]
        if i + 1 < length and tab[roman_string[i+1]] > value:
            result -= value
        else:
            result += value
    return result
