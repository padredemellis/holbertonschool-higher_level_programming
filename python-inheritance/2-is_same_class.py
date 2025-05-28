#!/usr/bin/python3
"""
True if object is an instance of a exactly class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""
    return type(obj) is a_class
