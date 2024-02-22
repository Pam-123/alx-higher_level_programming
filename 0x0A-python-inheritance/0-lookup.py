#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: Object to look up attributes and methods for.
    :return: List of attribute and method names.
    """
    return dir(obj)

