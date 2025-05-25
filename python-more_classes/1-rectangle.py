#!/usr/bin/python3
"""
This module is my first Rectangle
"""


class Rectangle:
    """
    This class represents a rectangle.
    The class is currently empty but will be expanded in future exercises
    to include attributes and methods related to squares.
    """

    def __init__(self, width=0, heigth=0):
        self.width = width
        self.height = heigth

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
