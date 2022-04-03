"""
Contains Player and Fairy
"""
from .base import LinkerSprite
from .assets import LINKER

import pygame


class Player(LinkerSprite):
    """
    Player is the player
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["player"], palette)
        self.state = "idle"
        self.frame = 0
        self.left = True
        self.sprites = {}
        self.set_sprites()
        self.set_surface()

    def set_sprites(self):
        self.sprites["fade"] = self["fade"]
        self.sprites["idle"] = self["idle"]
        self.sprites["walk"] = self["walk"]
        self.sprites["fall"] = self["fall"]

    def shift_palette(self):
        super(Player, self).shift_palette()
        self.set_sprites()
        self.set_surface()

    def change_state(self, state):
        if state not in ("fade", "idle", "walk", "fall"):
            raise ValueError("Invalid player state {state}")
        self.state = state
        self.frame = 0
        self.set_surface()

    def set_surface(self):
        self.surface = self.sprites[self.state][self.frame]
        if self.left:
            self.surface = pygame.transform.flip(self.surface, True, False)

    def tick(self):
        self.frame = (self.frame + 1) % len(self.sprites[self.state])
        self.set_surface()


class Fairy(LinkerSprite):
    """
    A cute little fairy
    """
    def __init__(self, palette="pico-8"):
        super().__init__(LINKER["fairy"], palette)
        self.frame = 0
        self.set_surface()

    def set_surface(self):
        self.surface = self[self.frame]

    def tick(self):
        self.frame = (self.frame + 1) % 2
        self.set_surface()
