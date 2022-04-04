import pygame
import itertools
import random

from typing import Optional
from sprites import LinkerSprite, sprite_size


class Chunk:

    def __init__(self, width, height):
        self._chunk: list[list[Optional[LinkerSprite]]] = [[None for __ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

    def __getitem__(self, item):
        return self._chunk[item]

    def get_size(self):
        return self.width, self.height

    def get_surface_size(self):
        chunk_size = self.get_size()
        return chunk_size[0] * sprite_size[0], chunk_size[1] * sprite_size[1]

    def get_rect(self, pos):
        return pygame.Rect(pos, self.get_surface_size())


class Map:

    def __init__(self):
        self._map = {}

    def __getitem__(self, item: tuple[int, int]):
        return self._map[item]

    def __setitem__(self, key: tuple[int, int], value: Chunk):
        self._map[key] = value

    def keys(self):
        return self._map.keys()

    def values(self):
        return self._map.values()

    def get_range(self):
        if not self._map:
            return (0, 0), (0, 0)
        o = sorted(self.keys())
        map_range = o[0], o[-1]
        return map_range

    def draw(self, screen, corners, offset):
        map_range = self.get_range()
        for i, j in itertools.product(range(map_range[0][0], map_range[1][0] + 1), range(map_range[0][1], map_range[1][1] + 1)):
            chunk = self[i, j]
            chunk_size = chunk.get_size()
            surface_size = chunk.get_surface_size()
            rel_loc = (surface_size[0] * i, surface_size[1] * j)
            rect = chunk.get_rect(rel_loc)
            for corner in corners:
                if rect.collidepoint(corner):
                    for k, l in itertools.product(range(chunk_size[0]), range(chunk_size[1])):
                        if chunk[k][l]:
                            chunk_rect = chunk[k][l].get_rect((k * sprite_size[0] + rel_loc[0] + offset[0], l * sprite_size[1] + rel_loc[1] + offset[1]))

                            screen.blit(chunk[k][l].surface, chunk_rect)
                            if random.randint(0, 10) == 0:
                                chunk[k][l].shift_palette()
                    break
