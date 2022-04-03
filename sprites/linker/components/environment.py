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
        # Note that this does not work for overriden for CrossTiles or BrickTiles
        self.surface = self[self.tile_type]


class CrossTile(LinkerSprite):
    """
    Tiles marked with an X
    """
    def __init__(self, tile_type=0, palette="pico-8"):
        if not 0 <= tile_type <= 3:
            raise ValueError(f"Invalid CrossTile type {tile_type}, must be between 0 and 3")
        super().__init__(LINKER["environment"]["tiles"], palette)
        self.tile_type = tile_type
        self.set_surface()

    def set_surface(self):
        self.surface = self["x"][self.tile_type]


class BrickTile(LinkerSprite):
    """
    Brick-pattern tiles
    """
    def __init__(self, size="small", shade="dark", palette="pico-8"):
        if size not in ("small", "big"):
            raise ValueError(f"Invalid BrickTile size {size}, must be big or small")
        elif shade not in ("dark", "light"):
            raise ValueError(f"Invalid BrickTile shade {shade}, must be dark or light")
        super().__init__(LINKER["environment"]["tiles"], palette)
        self.size = size
        self.shade = shade
        self.set_surface()

    def set_surface(self):
        self.surface = self[f"{self.size}brick"][self.shade]


class Accent(LinkerSprite):
    """
    Accents are impassible tiles that can also function as UI elements. They may be pushable too
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
        self.state = "closed"
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.state]

    def open(self):
        if self.state == "closed":
            self.state = "open"
            self.set_surface()
        else:
            raise AttributeError("Chest is already opened")

    def close(self):
        if self.state == "open":
            self.state = "closed"
            self.set_surface()
        else:
            raise AttributeError("Chest is already closed")


class Pot(LinkerSprite):
    """
    A simple pot that can be full of liquid
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["pot"], palette)
        self.state = "full"
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.state]

    def empty(self):
        if self.state == "full":
            self.state = "empty"
            self.set_surface()
        else:
            raise AttributeError("Pot is already empty")

    def fill(self):
        if self.state == "empty":
            self.state = "full"
            self.set_surface()
        else:
            raise AttributeError("Pot is already full")


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
            raise ValueError(f"Invalid Vines height {height}, must be at least 0")
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

    def grow(self):
        self.height += 1
        self.set_surface()

    def shrink(self):
        if self.height > 0:
            self.height -= 1
            self.set_surface()
        else:
            raise ValueError("Cannot shrink Vines below a height of zero")
