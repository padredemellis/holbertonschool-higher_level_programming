#!/usr/bin/python3
'''
Make a abstract method
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''Class Base'''
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Make a dog"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    '''Make a cat'''
    def sound(self):
        return "Meow"
