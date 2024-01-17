#!/usr/bin/python3
def uppercase(s):
    """
    Prints a string in uppercase followed by a new line.

    Args:
    - s: The input string.

    Returns:
    - None
    """
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase using ASCII values and print
            print("{:c}".format(ord(char) - ord('a') + ord('A')), end='')
        else:
            # Print non-letter characters as they are
            print(char, end='')

    # Print a new line at the end
    print("")
