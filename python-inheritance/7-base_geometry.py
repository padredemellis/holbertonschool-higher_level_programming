#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    Aquí se edificará algo
    """
    def area(self):
        """Raise an exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value as a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
