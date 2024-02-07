#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        # Attempt to convert the value to an integer
        integer_value = int(value)
        # Print the integer followed by a new line
        print("{:d}".format(integer_value))
        return True
    except ValueError:
        # Handle the case where the value is not an integer
        import sys
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return False
