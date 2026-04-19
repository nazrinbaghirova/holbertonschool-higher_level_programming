#!/usr/bin/env python3
"""Module for Dragon class using mixins."""


class SwimMixin:
    """Mixin for swimming."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swim and fly abilities."""

    def roar(self):
        """Print roaring action."""
        print("The dragon roars!")
