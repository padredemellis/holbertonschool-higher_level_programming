#!/usr/bin/python3
"""
Write a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """Retorna la descripción del diccionario
    para serialización JSON de un objeto.

    Args:
        obj: Instancia de una clase con atributos serializables.

    Returns:
        dict: Diccionario con los atributos del objeto.
    """
    return obj.__dict__
