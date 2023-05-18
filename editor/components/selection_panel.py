from cxr import SM

from editor import WIDTH
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

        self["cmap_panel"] = Scroll(width=3, height=3, palette=self.palette)
        self["full_panel"] = Scroll(width=10, height=13, palette=self.palette, pos=(20, 20))
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
            [{}],
            [{"tile_type": "smooth1"}, {"tile_type": "smooth2"}, {"tile_type": "cracked1"}, {"tile_type": "cracked2"}, {"tile_type": "pillar1"}, {"tile_type": "pillar2"}],
            [{"accent_type": "grey"}, {"accent_type": "black"}, {"accent_type": "light"}, {"accent_type": "dark"},],
            [{"stair_type": 0}, {"stair_type": 1}],
            [{}],
            [{"tile_type": 0}, {"tile_type": 1}, {"tile_type": 2}, {"tile_type": 3}],
            [{"size": "small", "shade": "dark"}, {"size": "small", "shade": "light"}, {"size": "big", "shade": "dark"}, {"size": "big", "shade": "light"}],
            [{}],
            [{}],
            [{}],
            [{"statue_type": "horns1"}, {"statue_type": "horns2"}, {"statue_type": "eye1"}, {"statue_type": "eye2"}, {"statue_type": "a1"}, {"statue_type": "a2"}],
            [{"plinth_type": 1}, {"plinth_type": 2}],
            [{}],
            [{"color": "blue"}, {"color": "red"}],
            [{}],
            [{}],
            [{}],
            [{}],
            [{}],
            [{}],
            [{"color": "blue"}, {"color": "red"}]
        ]
        self["current_selection_args"] = [{}]
        self["current_selection_args_index"] = 0
        for i, asset in enumerate(self.assets):
            asset.pos =((i % 4) * 100 + 44, i // 4 * 100 + 44)
        self.set_mini_sprite()

        @self.controller
        def controller(event):
            pass

        @self.add_state("map_closed")
        def map_closed(event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.cmap_panel.collidepoint(event.pos):
                self.change_state("map_open")
            elif event.type == pygame.MOUSEWHEEL:
                self.change_selection_args(-event.y)

        @self.add_state("map_open")
        def map_open(event):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.change_state("map_closed")
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.check_for_selection()

    def attach_player(self, player):
        self["player"] = player

    def set_sp_position(self, screen):
        self["w"], self["h"] = screen.get_size()
        self["pos"] = self.w - 150, self.h
        self.cmap_panel.pos = (self.w-150, 10)

    def draw(self, screen):
        if self.current_state() == "map_open":
            self.full_panel.draw(screen)
            for i, asset in enumerate(self.assets):
                asset.draw(screen)
        else:
            self.cmap_panel.draw(screen)
            self.mini_sprite.draw(screen)

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
                self["current_selection_args_index"] = 0
                self.set_mini_sprite()
                self.change_state("map_closed")

    def change_selection_args(self, amt):
        if len(self.current_selection_args) == 0:
            pass
        elif amt == -1:
            if self.current_selection_args_index == 0:
                self["current_selection_args_index"] = len(self.current_selection_args) - 1
            else:
                self["current_selection_args_index"] -= 1
        elif amt == 1:
            if self.current_selection_args_index == len(self.current_selection_args) - 1:
                self["current_selection_args_index"] = 0
            else:
                self["current_selection_args_index"] += 1
        self.set_mini_sprite()

    def get_args(self):
        return self.current_selection_args[self.current_selection_args_index]

    def set_mini_sprite(self):
        self["mini_sprite"] = self.current_selection(palette=self.palette, **self.get_args())
        self.mini_sprite.pos = WIDTH - 120, 36
