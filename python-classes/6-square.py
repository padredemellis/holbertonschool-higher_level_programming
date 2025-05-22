#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    @property
    def position(self):
        return self._position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
            or not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
    
    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.size == 0:
            print()
            return
        
        for _ in range(self._position[1]):
            print()
        
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)