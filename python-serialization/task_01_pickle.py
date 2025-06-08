#!/usr/bin/python3
"""
Learn how to serialize and deserialize
 custom Python objects using the pickle module.
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Muestra los atributos del objeto."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializa el objeto y lo guarda en un archivo.
        
        Args:
            filename (str): Nombre del archivo de salida.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializa un objeto desde un archivo.

        Args:
            filename (str): Nombre del archivo de entrada.

        Returns:
            CustomObject: Instancia deserializada o None en caso de error.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
