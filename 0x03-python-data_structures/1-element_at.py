#!/usr/bin/python3.8
def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None

    # Check if idx is within the valid range
    if idx >= len(my_list):
        return None

    # Return the element at the specified index
    return my_list[idx]
