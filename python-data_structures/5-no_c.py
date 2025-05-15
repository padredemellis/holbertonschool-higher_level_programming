#!/usr/bin/python3

def no_c(my_string):
    characters = "'cC'"
    my_string= "".join(x for x in my_string if x not in characters)
    print(my_string)
