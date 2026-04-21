#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Student class with serialization helpers."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
