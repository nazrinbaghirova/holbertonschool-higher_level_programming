#!/usr/bin/env python3
"""Module for abstract Animal class and subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        """Return cat sound."""
        return "Meow"