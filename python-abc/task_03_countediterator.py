#!/usr/bin/python3
"""This module crea un contador de iterables"""
class CountedIterator:
    """
    Clase CountedIterator que envuelve un iterable
    y cuenta el número de elementos iterados.
    """

    def __init__(self, iterable):
        """
        Constructor de la clase CountedIterator.
        Inicializa el iterador interno y el contador de elementos.

        Args:
            iterable: El objeto iterable (por ejemplo, una lista)
                      que se va a iterar.
        """
        self.internal_iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Devuelve el siguiente elemento de la secuencia e incrementa el contador.
        Levanta StopIteration si no quedan más elementos.
        """
        try:
            item = next(self.internal_iterator)
            self.count += 1
            return item
        except StopIteration:

            raise StopIteration

    def __iter__(self):
        """
        Hace que una instancia de CountedIterator sea su propio iterador.
        Esto permite que se use directamente en bucles for.
        """
        return self

    def get_count(self):
        """
        Devuelve el número actual de elementos que han sido iterados.
        """
        return self.count
