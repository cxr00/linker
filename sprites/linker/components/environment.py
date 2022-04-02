from sprites.linker.components import LinkerSprite
from sprites import LINKER


class Filler(LinkerSprite):
    """
    Filler contains tiles that can be used for either flooring or background
    """
    def __init__(self, palette="pico-8", tile_type=0):
        super().__init__(LINKER["filler"], palette)
        self.tile_type = tile_type


class Tile(LinkerSprite):
    """
    Tile contains the variety of tiles which the player can walk on
    """
    def __init__(self, palette="pico-8", tile_type="smooth1"):
        super().__init__(LINKER["environment"]["tiles"], palette)
        self.tile_type = tile_type


class Statue(LinkerSprite):
    """
    Statue contains the various statues which can be found in the temple
    """
    def __init__(self, palette="pico-8", statue_type="horns1"):
        super().__init__(LINKER["environment"]["statues"], palette)
        self.statue_type = statue_type


class Accent(LinkerSprite):
    """
    Accents are impassible tiles. They may be pushable too
    """
    def __init__(self, palette="pico-8", accent_type="grey"):
        super().__init__(LINKER["accents"], palette)
        self.accent_type = accent_type


class Stairs(LinkerSprite):
    """
    Stairs are floor tiles which make the level look more dynamic
    """
    def __init__(self, palette="pico-8", stair_type=0):
        super().__init__(LINKER["stairs"], palette)
        self.stair_type = stair_type


class Button(LinkerSprite):
    """
    Buttons can be stepped on to activate traps, doors, and more
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["button"], palette)


class Vines(LinkerSprite):
    """
    Variable-size pot of growing vines
    """
    def __init__(self, palette="pico-8", height=0):
        super().__init__(LINKER["vines"], palette)
        if height < 0:
            raise ValueError(f"Invalid height {height}, must be at least 0")
        self.height = height


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
