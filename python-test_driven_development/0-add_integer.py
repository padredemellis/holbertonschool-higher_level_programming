#!/usr/bin/python3
"""
This module provides a function to add two integers.
It ensures inputs are integers or floats, and raises errors if not.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if needed.

    Args:
        a: First number, must be an int or float.
        b: Second number, must be an int or float. Defaults to 98.

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If a or b are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
