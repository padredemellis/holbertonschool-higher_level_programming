#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    suma = 0

    if not my_list:
        return 0
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
            suma += element

    return suma
