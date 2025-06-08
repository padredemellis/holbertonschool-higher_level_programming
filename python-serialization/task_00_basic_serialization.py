#!/usr/bin/python3
"""
Create a basic serialization module
 that adds the functionality to serialize a Python
 dictionary to a JSON file and deserialize
   the JSON file to recreate the Python Dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializa un diccionario en formato JSON y lo guarda en un archivo.

    Args:
        data (dict): Diccionario a serializar.
        filename (str): Nombre del archivo de salida.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Carga y deserializa datos JSON desde un archivo.

    Args:
        filename (str): Nombre del archivo de entrada.

    Returns:
        dict: Diccionario con los datos deserializados.
    """
    with open(filename, 'r') as file:
        return json.load(file)
