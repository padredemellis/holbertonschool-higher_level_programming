#!/usr/bin/python3
'''
Write a class Student that defines a student by:
'''


class Student():
    '''Student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Retrieves dictionary representation'''
        return self.__dict__
