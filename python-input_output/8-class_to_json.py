#!/usr/bin/python3
"""Module to convert class instance to dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
