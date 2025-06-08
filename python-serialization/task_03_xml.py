#!/usr/bin/python3
"""
Serialización con XML
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializa un diccionario en formato XML.

    Args:
        dictionary (dict): Diccionario a serializar.
        filename (str): Nombre del archivo de salida.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = value
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserializa un archivo XML a un diccionario.

    Args:
        filename (str): Nombre del archivo XML.

    Returns:
        dict: Diccionario con los datos deserializados.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for element in root:
        result[element.tag] = element.text
    return result
