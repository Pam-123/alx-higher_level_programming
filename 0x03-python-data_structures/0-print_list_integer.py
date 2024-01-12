#!/usr/bin/python3.8

def print_list_integer(my_list=[]):
        """
        Print integers from a list,one per line.
        
        Args:

            my_list(list): The list of input containing integers.

            
        Returns:

           None

        """
        # Iterate through each elememnt in the list

        for num in my_list:

            # Print the integer using the specified format

            print("{:d}".format(num))
