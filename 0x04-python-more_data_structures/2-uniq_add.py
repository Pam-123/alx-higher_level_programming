#!/usr/bin/python3.8
def uniq_add(my_list=[]):
    # Use a set to store unique integers and then calculate the sum
    unique_set = set(my_list)
    result = sum(unique_set)
    return result
