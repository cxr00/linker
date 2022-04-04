import pygame
import itertools

from typing import Optional
from sprites import LinkerSprite, sprite_size


class Chunk:

    def __init__(self, dim):
        self._chunk: list[list[Optional[LinkerSprite]]] = [[None for __ in range(dim[0])] for _ in range(dim[1])]
        self.width = dim[0]
        self.height = dim[1]

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

    def __init__(self, chunk_dim):
        self._map = {}
        self._chunk_width = chunk_dim[0]
        self._chunk_height = chunk_dim[1]

    def __getitem__(self, item: tuple[int, int]):
        return self._map[item]

    def __setitem__(self, key: tuple[int, int], value: Chunk):
        if value.get_size() != (self._chunk_width, self._chunk_height):
            raise ValueError(f"Invalid chunk dimensions {value.get_size()}, must be {self._chunk_width, self._chunk_height}")
        self._map[key] = value

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        return self._map.keys()

    def values(self):
        return self._map.values()

    def get_range(self):
        if not self._map:
            return range(0, 0), range(0, 0)
        o = sorted(self.keys())
        map_range = range(o[0][0], o[-1][0] + 1), range(o[0][1], o[-1][1] + 1)
        return map_range

    def get_size(self):
        if not self._map:
            return 0
        s = self[0, 0].get_size()
        return s[0] * s[1] * len(self.values())

    def draw(self, screen, corners, offset):
        range1, range2 = self.get_range()
        for i, j in itertools.product(range1, range2):
            chunk = self[i, j]
            surface_size = chunk.get_surface_size()
            rel_loc = (surface_size[0] * i, surface_size[1] * j)
            rect = chunk.get_rect(rel_loc)
            for corner in corners:
                if rect.colliderect(corner):
                    for k, l in itertools.product(range(self._chunk_width), range(self._chunk_height)):
                        if chunk[l][k]:
                            chunk_rect = chunk[l][k].get_rect((k * sprite_size[0] + rel_loc[0] + offset[0], l * sprite_size[1] + rel_loc[1] + offset[1]))
                            if chunk_rect.colliderect(screen.get_rect()):
                                screen.blit(chunk[l][k].surface, chunk_rect)
                    break
