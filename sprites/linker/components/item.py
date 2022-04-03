"""
Contains everything that will appear in the inventory
"""
from .base import LinkerSprite
from .assets import LINKER

import pygame


class Item(LinkerSprite):
    """
    Items are special sprites which are contained in the Player's inventory
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["item"][type(self).__name__.lower()], palette)


class Pencil(Item):
    """
    A pencil has a case and a fill color, either blue or red
    """
    def __init__(self, color="blue", palette="pico-8"):
        super().__init__(palette)
        self.color = color
        self.set_surface()

    def set_surface(self):
        dim = self["case"].get_size()
        output = pygame.Surface(dim, pygame.SRCALPHA)
        output.blit(self[self.color], (0, 0))
        output.blit(self["case"], (0, 0))
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
        self.frame = 0
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.frame]

    def tick(self):
        self.frame = (self.frame + 1) % 4
        self.set_surface()


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
    def __init__(self, color="blue", level=6, palette="pico-8"):
        super().__init__(palette)
        self.color = color
        self.level = level
        self.set_surface()

    def set_surface(self):
        dim = self["vial"].get_size()
        if self.level > 0:
            fill = self[self.color][6 - self.level]
        else:
            fill = pygame.Surface(dim, pygame.SRCALPHA)
        output = pygame.Surface(dim, pygame.SRCALPHA)
        output.blit(fill, (0, 0))
        output.blit(self["vial"], (0, 0))
        self.surface = output

    def change_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"

    def set_level(self, level):
        if 0 <= level <= 6:
            self.level = level
        self.set_surface()
