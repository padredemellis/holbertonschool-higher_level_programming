#!/usr/bin/python3
'''
In this module we learn how to use the dir() method
'''


def lookup(obj):
    '''
    The lookup(obj) function returns a list of methods
    and attributes of an object.
    '''
    return [m for m in dir(obj)]
