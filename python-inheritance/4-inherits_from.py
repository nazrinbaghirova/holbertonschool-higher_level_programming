#!/usr/bin/python3
"""Module that defines a function to check inheritance only"""


def inherits_from(obj, a_class):
    """Return True if obj is subclass (not same class)"""
    return isinstance(obj, a_class) and type(obj) is not a_class
