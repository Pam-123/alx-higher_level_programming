#!/usr/bin/python3.8
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize the maximum value with the first element of the list
    max_value = my_list[0]

    # Iterate through the rest of the elements to find the maximum
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
