#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0

    for i in range(len(roman_string)):
        current_value = roman_dict[roman_string[i]]
        previous_value = roman_dict[roman_string[i - 1]] if i > 0 else 0

        if i > 0 and current_value > previous_value:
            result += current_value - 2 * previous_value
        else:
            result += current_value

    return result
