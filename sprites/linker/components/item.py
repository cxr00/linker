from .base import LinkerSprite
from .assets import LINKER

import pygame


class Item(LinkerSprite):
    """
    Items are special sprites which are contained in some sort of inventory
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["item"][type(self).__name__.lower()], palette)


class Pencil(Item):
    """
    A pencil has a case and a fill color, either blue or red
    """
    def __init__(self, palette="pico-8", color="blue"):
        super().__init__(palette)
        self.color = color
        self.set_surface()

    def set_surface(self):
        dim = self["base"].get_size()
        output = pygame.Surface(dim, pygame.SRCALPHA)
        output.blit(self[self.color], (0, 0))
        output.blit(self["base"], (0, 0))
        self.surface = output

    def change_color(self):
        if self.color == "blue":
            self.color = "red"
        else:
            self.color = "blue"
        self.set_surface()


class Bomb(Item):
    """
    A bomb can be placed in order to destroy tiles. But be careful!
    """
    def __init__(self, palette="pico-8"):
        super().__init__(palette)


class Key(Item):
    """
    Keys can be used to unlock chests ... and maybe other things!
    """
    def __init__(self, palette="pico-8"):
        super().__init__(palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current


class Sack(Item):
    """
    Sacks contain items. This might be the inventory icon
    """
    def __init__(self, palette="pico-8"):
        super().__init__(palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current


class Gem(Item):
    """
    Gems are a valuable treasure. Collect them all!
    """
    def __init__(self, palette="pico-8"):
        super().__init__(palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current


class Pearl(Item):
    """
    Pearls are a valuable treasure. Collect them all!
    """
    def __init__(self, palette="pico-8"):
        super().__init__(palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current


class Relic(Item):
    """
    Relics are works of art from a long forgotten time
    """
    def __init__(self, palette="pico-8"):
        super().__init__(palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current


class Ink(Item):
    """
    Ink is used to write colored messages in important places
    """
    def __init__(self, palette="pico-8", color="red"):
        super().__init__(palette)
        self.color = color
        self.meter = self[self.color]

    def change_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"
        self.meter = self[self.color]

