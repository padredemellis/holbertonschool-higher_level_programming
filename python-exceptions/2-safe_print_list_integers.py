#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    contador = 0
    try:
        for i in range(x):
            valor = my_list[i]
            try:
                print("{:d}".format(valor), end="")
                contador += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        raise
    print()
    return contador
