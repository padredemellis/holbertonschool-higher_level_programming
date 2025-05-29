#!/usr/bin/python3
'''
Write a class Square that inherits from Rectangle (9-rectangle.py).
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with custom string representation."""

    def __init__(self, size):
        """Initialize a Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
