#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number and returns the value of the last digit.

    Args:
    - number: The input number.

    Returns:
    - The value of the last digit.
    """
    # Get the last digit using the modulo operator
    last_digit = abs(number) % 10

    # Print the last digit
    print(last_digit, end='')

    # Return the value of the last digit
    return last_digit
