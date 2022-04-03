"""
The basis of all implementations of LINKER sprites
"""
from .assets import LINKER

import pygame


class LinkerSprite:
    """
    A LinkerSprite is the base class for LINKER sprites
    """
    def __init__(self, base, palette="pico-8"):
        self._base = base
        self.palette = palette
        self._current = self._base[self.palette]
        self.surface = None

    def __getitem__(self, item):
        return self._current[item]

    def shift_palette(self):
        """
        Change the sprite's current palette between pico-8 and nes
        """
        if self.palette == "pico-8":
            self.palette = "nes"
        else:
            self.palette = "pico-8"
        self._current = self._base[self.palette]
        self.set_surface()

    def set_palette(self, palette):
        """
        Explicitly set the current palette to pico-8 or nes
        """
        if palette not in ("pico-8", "nes"):
            raise ValueError(f"Invalid palette {palette}, must be pico-8 or nes")
        else:
            if palette != self.palette:
                self.shift_palette()

    def set_surface(self):
        """
        Each LinkerSprite overrides this method to create an appropriate Surface
        The Surface is then assigned to the self.surface attribute
        """
        self.surface = self.surface


class ScalableSprite(LinkerSprite):
    """
    Scrolls and Bangs can have varying dimension, so their set_surface is defined here
    """
    def __init__(self, base, width=2, height=2, palette="pico-8"):
        super().__init__(base, palette)
        if width < 2 or height < 2:
            raise ValueError(f"Invalid dimension {width}x{height}, must be at least 2x2")
        self.width = width
        self.height = height
        self.set_surface()

    def set_surface(self):
        dim = self["tl"].get_size()
        output = pygame.Surface((dim[0] * self.width, dim[1] * self.height), pygame.SRCALPHA)

        w_max = (self.width - 1) * dim[0]
        h_max = (self.height - 1) * dim[1]

        # top
        output.blit(self["tl"], (0, 0))
        for i in range(1, self.width - 1):
            output.blit(self["t"], (i * dim[0], 0))
        output.blit(self["tr"], (w_max, 0))

        # middle
        for i in range(1, self.height - 1):
            output.blit(self["ml"], (0, i * dim[1]))
            for j in range(1, self.width - 1):
                output.blit(self["m"], (j * dim[0], i * dim[1]))
            output.blit(self["mr"], (w_max, i * dim[1]))

        # bottom
        output.blit(self["bl"], (0, h_max))
        for i in range(1, self.width - 1):
            output.blit(self["b"], (i * dim[0], h_max))
        output.blit(self["br"], (w_max, h_max))

        self.surface = output


class Scroll(ScalableSprite):
    """
    A UI element for displaying text, inventory, etc
    """
    def __init__(self, width=2, height=2, palette="pico-8"):
        super().__init__(LINKER["scroll"], width, height, palette)


class Bang(ScalableSprite):
    """
    A UI element and effect
    """
    def __init__(self, width=2, height=2, palette="pico-8"):
        super().__init__(LINKER["bang"], width, height, palette)
