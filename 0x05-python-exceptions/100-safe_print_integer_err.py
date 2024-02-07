#!/usr/bin/python3
def safe_print_integer_err(value):
    """Prints an integer if it's valid, otherwise prints an error message.

    Args:
        value: The value to attempt printing.

    Returns:
        True if the value is an integer and was printed successfully, False otherwise.
    """

    try:
        # Improved error handling to catch more potential exceptions
        if not isinstance(value, int):
            raise ValueError("Not an integer")
        print("{:d}".format(value))
        return True
    except (ValueError, KeyError) as e:  # Combine potential exceptions
        print("Exception:", e, file=sys.stderr)
        return False
