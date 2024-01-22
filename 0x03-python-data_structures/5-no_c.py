#!/usr/bin/python3.8
def no_c(my_string):
    # Create a new string without 'c' and 'C'
    new_string = ''
    for char in my_string:
        if char.lower() != 'c':
            new_string += char

    return new_string
