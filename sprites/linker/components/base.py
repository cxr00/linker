from sprites import LINKER


class LinkerSprite:
    """
    A LinkerSprite is the base class for palette-swappable tiles
    """
    def __init__(self, base, palette="pico-8"):
        self.base = base
        self.palette = palette
        self._current = self.base[self.palette]

    def __getitem__(self, item):
        return self._current[item]

    def shift_palette(self):
        if self.palette == "pico-8":
            self.palette = "nes"
        else:
            self.palette = "pico-8"
        self._current = self.base[self.palette]


class Dust(LinkerSprite):
    """
    A simple particle effect
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["dust"], palette)


class Scroll(LinkerSprite):
    """
    A variable-size UI element for displaying text, inventory, etc
    """
    def __init__(self, palette="pico-8", width=2, height=2):
        super().__init__(LINKER["scroll"], palette)
        if width < 2 or height < 2:
            raise ValueError(f"Invalid dimension {width}x{height}, must be at least 2x2")
        self.width = width
        self.height = height


class Bang(LinkerSprite):
    """
    A variable-size UI element and effect
    """
    def __init__(self, palette="pico-8", width=2, height=2):
        super().__init__(LINKER["bang"], palette)
        if width < 2 or height < 2:
            raise ValueError(f"Invalid dimension {width}x{height}, must be at least 2x2")
        self.width = width
        self.height = height


class Hand(LinkerSprite):
    """
    A simple UI element
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["hand"], palette)
