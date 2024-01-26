#!/usr/bin/python3.8
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = [replace if elem == search else elem for elem in my_list]
    return new_list
