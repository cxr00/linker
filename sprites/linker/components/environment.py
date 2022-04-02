from .base import LinkerSprite
from .assets import LINKER

import pygame


class Filler(LinkerSprite):
    """
    Filler contains tiles that can be used for either flooring or background
    """
    def __init__(self, tile_type=0, palette="pico-8"):
        super().__init__(LINKER["filler"], palette)
        self.tile_type = tile_type
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.tile_type]


class Tile(LinkerSprite):
    """
    Tile contains the variety of tiles which the player can walk on
    """
    def __init__(self, tile_type="smooth1", palette="pico-8"):
        super().__init__(LINKER["environment"]["tiles"], palette)
        self.tile_type = tile_type
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.tile_type]


class Accent(LinkerSprite):
    """
    Accents are impassible tiles. They may be pushable too
    """
    def __init__(self, accent_type="grey", palette="pico-8"):
        super().__init__(LINKER["accents"], palette)
        self.accent_type = accent_type
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.accent_type]


class Stairs(LinkerSprite):
    """
    Stairs are floor tiles which make the level look more dynamic
    """
    def __init__(self, stair_type=0, palette="pico-8"):
        super().__init__(LINKER["stairs"], palette)
        self.stair_type = stair_type
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.stair_type]


class Button(LinkerSprite):
    """
    Buttons can be stepped on to activate traps, doors, and more
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["button"], palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current


class Chest(LinkerSprite):
    """
    A (potentially locked and) openable treasure chest
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["chest"], palette)


class Pot(LinkerSprite):
    """
    A simple pot that can be full of liquid
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["pot"], palette)
        self.set_surface()

    def set_surface(self):
        self.surface = self._current


class Statue(LinkerSprite):
    """
    Statue contains the various statues which can be found in the temple
    """
    def __init__(self, statue_type="horns1", palette="pico-8"):
        super().__init__(LINKER["environment"]["statues"], palette)
        self.statue_type = statue_type
        self.set_surface()

    def set_surface(self):
        s = self[self.statue_type]
        height = s[0].get_height()
        output = pygame.Surface((s[0].get_width(), height * 2), pygame.SRCALPHA)
        output.blit(s[0], (0, 0))
        output.blit(s[1], (0, height))
        self.surface = output


class Vines(LinkerSprite):
    """
    Variable-size pot of growing vines
    """
    def __init__(self, height=0, palette="pico-8"):
        super().__init__(LINKER["vines"], palette)
        if height < 0:
            raise ValueError(f"Invalid height {height}, must be at least 0")
        self.height = height
        self.set_surface()

    def set_surface(self):
        dim = self["base"].get_size()
        output = pygame.Surface((dim[0], (self.height + 1) * dim[1]), pygame.SRCALPHA)

        # base
        output.blit(self["base"], (0, self.height * dim[1]))

        for i in range(self.height):
            output.blit(self[i % 2], (0, (self.height - i - 1) * dim[1]))

        self.surface = output
