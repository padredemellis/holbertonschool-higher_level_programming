#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    contador = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            contador += 1
    except IndexError:
        pass
    print()
    return contador
