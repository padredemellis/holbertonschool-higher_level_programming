#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nueva_lista = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            try:
                resultado = a / b
            except ZeroDivisionError:
                print("division by 0")
                resultado = 0
            except (TypeError, ValueError):
                print("wrong type")
                resultado = 0
        except IndexError:
            print("out of range")
            resultado = 0
        finally:
            nueva_lista.append(resultado)
    return nueva_lista
