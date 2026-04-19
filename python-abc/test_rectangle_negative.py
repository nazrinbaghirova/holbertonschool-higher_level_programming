#!/usr/bin/env python3
from task_01_duck_typing import Rectangle

rectangle_negative = Rectangle(-1, -2)

assert rectangle_negative.area() == 2, "Incorrect area for negative dimensions"
assert rectangle_negative.perimeter() == 6, "Incorrect perimeter for negative dimensions"

print("OK")