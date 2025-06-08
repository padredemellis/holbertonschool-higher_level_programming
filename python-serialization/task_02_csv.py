#!/usr/bin/python3
"""
Conocemos los archivos csv
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convierte un archivo CSV a formato JSON.

    Args:
        csv_filename (str): Nombre del archivo CSV.

    Returns:
        bool: True si la conversión fue exitosa, False en caso contrario.
    """
    try:
        # Leer datos CSV
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Escribir archivo JSON
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
