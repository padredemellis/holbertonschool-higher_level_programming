#!/usr/bin/python3
"""
Write a function that creates
an Object from a “JSON file”:
"""


import json


def load_from_json_file(filename, encoding="utf-8"):
    '''Create an Objet from a 'Json file' '''
    with open(filename) as f:
        r = json.load(f)
    return r
