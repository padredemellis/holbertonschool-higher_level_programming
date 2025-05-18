#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for k, value in a_dictionary.items():
        new_dict[k] = value * 2
    return new_dict
