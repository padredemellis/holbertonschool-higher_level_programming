#!/usr/bin/python3
'''
Write a class Student that defines a student by:
'''


class Student():
    '''Student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves dictionary representation'''
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        filtered_dict = {}
        for attr_name in attrs:
            if attr_name in self.__dict__:
                filtered_dict[attr_name] = getattr(self, attr_name)
        return filtered_dict

    def reload_from_json(self, json):
        '''Actualiza atributos desde diccionario (deserialización)'''
        for key, value in json.items():
            setattr(self, key, value)
