from .base import LinkerSprite
from .assets import LINKER


class Player(LinkerSprite):
    """
    Player is the player
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["player"], palette)
        self.fade = None
        self.idle = None
        self.walk = None
        self.fall = None
        self.set_sprites()

    def set_sprites(self):
        self.fade = self["fade"]
        self.idle = self["idle"]
        self.walk = self["walk"]
        self.fall = self["fall"]

    def shift_palette(self):
        super(Player, self).shift_palette()
        self.set_sprites()


class Fairy(LinkerSprite):
    """
    A cute little fairy
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["fairy"], palette)