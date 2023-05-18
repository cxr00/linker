from cxr import SM
from linker import *
del sprite_size, LinkerSprite, Bang, Player, Demon

import pygame


class SelectionPanel(SM):
    def __init__(self, key, name, screen=None, palette="nes"):
        super().__init__(key, name)
        self.toggle_ser_priority(False)
        self["palette"] = palette
        self._initialize()
        self.set_sp_position(screen)

    def _initialize(self):

        self["cmap_panel"] = Scroll(width=2, height=2, palette=self.palette)
        self["full_panel"] = Scroll(width=10, height=13, palette=self.palette, pos=(20, 20))
        self["in_map"] = False
        self["player"] = None
        self["assets"] = [
            Filler(palette=self.palette),
            Tile(palette=self.palette),
            Accent(palette=self.palette),
            Stairs(palette=self.palette),
            Hole(palette=self.palette),
            CrossTile(palette=self.palette),
            BrickTile(palette=self.palette),
            Button(palette=self.palette),
            Chest(palette=self.palette),
            Pot(palette=self.palette),
            Statue(palette=self.palette),
            Plinth(palette=self.palette),
            Vine(palette=self.palette),
            Pen(palette=self.palette),
            Bomb(palette=self.palette),
            Key(palette=self.palette),
            Sack(palette=self.palette),
            Gem(palette=self.palette),
            Pearl(palette=self.palette),
            Relic(palette=self.palette),
            Ink(palette=self.palette)
        ]
        self["current_selection"] = type(self.assets[0])
        self["asset_args"] = [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        ]
        self["current_selection_args"] = {}
        for i, asset in enumerate(self.assets):
            asset.pos =((i % 4) * 100 + 44, i // 4 * 100 + 44)

        @self.controller
        def controller(event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.cmap_panel.collidepoint(event.pos):
                self["in_map"] = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self["in_map"] = False
            elif self.in_map and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.check_for_selection()

    def associate_player(self, player):
        self["player"] = player

    def set_sp_position(self, screen):
        self["w"], self["h"] = screen.get_size()
        self["pos"] = self.w - 105, self.h
        self.cmap_panel.pos = (self.w-105, 10)

    def draw(self, screen):
        if self.in_map:
            self.full_panel.draw(screen)
            for i, asset in enumerate(self.assets):
                asset.draw(screen)
        else:
            self.cmap_panel.draw(screen)

    def shift_palette(self):
        self.cmap_panel.shift_palette()
        self.full_panel.shift_palette()
        for asset in self.assets:
            asset.shift_palette()

    def check_for_selection(self):
        pos = pygame.mouse.get_pos()
        for i, asset in enumerate(self.assets):
            if asset.collidepoint(pos):
                self["current_selection"] = type(asset)
                self["current_selection_args"] = self.asset_args[i]