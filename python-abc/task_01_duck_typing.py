#!/usr/bin/env python3
"""Module for Shape, Circle, Rectangle and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class Shape."""

    @abstractmethod
    def area(self):
        """Return area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Return area of circle."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Return perimeter of circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (abs(self.width) + abs(self.height))

def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
