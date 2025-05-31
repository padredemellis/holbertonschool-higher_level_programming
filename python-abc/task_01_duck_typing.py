#!/usr/bin/python3
'''
Make an abstract method
'''
from abc import ABC, abstractmethod


class Shape(ABC):
    '''Class Base'''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Make a circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    '''Make a Rectangle'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


# Testing
circulo = Circle(5)
rectangulo = Rectangle(5, 3)

shape_info(circulo)
shape_info(rectangulo)
