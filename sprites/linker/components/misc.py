from .base import LinkerSprite
from .assets import LINKER


class Hand(LinkerSprite):
    """
    A simple UI element
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["hand"], palette)


class Dust(LinkerSprite):
    """
    A simple particle effect
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["dust"], palette)
