#!/usr/bin/python3

def no_c(my_string):
    characters = {'c', 'C'}
    my_string= "".join(x for x in my_string if x not in characters)
    return (my_string)
