"""
Contains anything that doesn't fit into another category
"""
from .base import LinkerSprite
from .assets import LINKER


class Hand(LinkerSprite):
    """
    A simple UI element
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["hand"], palette)
        self.state = "point"
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.state]

    def set_state(self, state):
        if state not in ("point", "grab"):
            raise ValueError(f"Invalid Hand state {state}, must be point or grab")
        else:
            self.state = state
            self.set_surface()


class Dust(LinkerSprite):
    """
    A simple particle effect
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["dust"], palette)
        self.timer = 0
        self.frame = 0
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.frame]

    def tick(self):
        self.timer = (self.timer + 1) % 5
        if self.timer == 0:
            self.frame = (self.frame + 1) % 3
            self.set_surface()


class Shadow(LinkerSprite):
    """
    An undershadow for items which appear in the overworld
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["shadow"], palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current
