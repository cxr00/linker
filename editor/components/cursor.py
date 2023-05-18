
import pygame
from cxr import SM

from editor import WIDTH
from linker import Hand


class Cursor(SM):
    """
    Custom cursor. Accepts MOUSEMOTION, MOUSEBUTTONDOWN, and MOUSEBUTTONUP
    """

    def __init__(self, key, name):
        super().__init__(key, name)

        self._initialize()

    def _initialize(self):
        self.toggle_ser_priority(False)
        self["hand"] = Hand()
        self["pos"] = 100, 100
        self["create_tile"] = False

        @self.controller
        def controller(event):
            self["create_tile"] = False
            if event.type == pygame.MOUSEMOTION:
                self.hand.pos = self["pos"] = event.pos
                if not self.cmap.cmap_panel.collidepoint(event.pos):
                    if not self.cmap.in_map or not self.cmap.full_panel.collidepoint(event.pos):
                        self["create_tile"] = pygame.mouse.get_pressed()[0]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.hand.set_state("grab")
                    if not self.cmap.cmap_panel.collidepoint(event.pos):
                        if not self.cmap.in_map:
                            self["create_tile"] = True
                        elif not self.cmap.full_panel.collidepoint(event.pos):
                            self["create_tile"] = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.hand.set_state("point")

    def draw(self, surface):
        self.hand.draw(surface)

    def shift_palette(self):
        self.hand.shift_palette()

    def attach_cmap(self, cmap):
        self["cmap"] = cmap
