#!/usr/bin/python3
'''
Clase VerboseList que extiende list y notifica las operaciones de adición y eliminación.
'''
class VerboseList(list):
    '''
    Extiende la clase list de Python para imprimir notificaciones
    cada vez que se añade o elimina un elemento.
    '''
    def append(self, item):
        super().append(item)
        print(f'Added [{item}] to the list.')
    def extend(self, iterable):
        count = len(iterable) 
        super().extend(iterable)
        print(f'Extended the list with [{count}] items.')

    def remove(self, item):
        print(f'Removed [{item}] from the list.')
        super().remove(item)

    def pop(self, index = -1):
        popped_item = self[index] 
        print(f'Popped [{popped_item}] from the list.')
        super().pop(index)

if __name__ == "__main__":
    lista = VerboseList([1,2,3,4])
    lista.append(5)
    lista_Dos = ["e","m","a"]
    lista.extend(lista_Dos)
    lista.remove(1)
    lista.pop(0)

