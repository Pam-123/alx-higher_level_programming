#!/usr/bin/python3.8
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, element in enumerate(row):
            if i == len(row) - 1:
                # Last element in the row, print without a space at the end
                print("{:d}".format(element), end="")
            else:
                # Regular element, print with a space at the end
                print("{:d}".format(element), end=" ")
        print()  # Move to the next line after printing each row
