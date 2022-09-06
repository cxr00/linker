"""
Classes for containing grids of tiles in any direction
"""
import pygame
import itertools

from typing import Optional
from sprites import LinkerSprite, sprite_size


def dot(a, b):
    """
    I'm lazy
    """
    return a[0]*b[0], a[1]*b[1]


# It just makes more sense to house chunk size here
chunk_size = 14, 14
surface_size = dot(sprite_size, chunk_size)


class Chunk:

    def __init__(self):
        self._chunk: list[list[Optional[LinkerSprite]]] = [
            [None for __ in range(chunk_size[0])] for _ in range(chunk_size[1])
        ]

    def __getitem__(self, item):
        return self._chunk[item]

    def get_rect(self, pos):
        return pygame.Rect(pos, surface_size)


class Map:

    def __init__(self):
        self._map = {}
        self._range = range(0, 0), range(0, 0)

    def __getitem__(self, item: tuple[int, int]):
        return self._map[item]

    def __setitem__(self, key: tuple[int, int], value: Chunk):
        self._map[key] = value

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        return self._map.keys()

    def values(self):
        return self._map.values()

    def update_range(self):
        o = sorted(self.keys())
        map_range = range(o[0][0], o[-1][0] + 1), range(o[0][1], o[-1][1] + 1)
        self._range = map_range

    def get_size(self):
        if not self._map:
            return 0
        return chunk_size[0] * chunk_size[1] * len(self.values())

    def draw(self, screen, corners, offset, rect=None):
        if rect is None:
            rect = screen.get_rect()
        for i, j in itertools.product(*self._range):
            chunk = self[i, j]
            rel_loc = dot(surface_size, (i, j))
            chunk_rect = chunk.get_rect(rel_loc)
            tile_offset = rel_loc[0] + offset[0], rel_loc[1] + offset[1]
            for corner in corners:
                if chunk_rect.colliderect(corner):
                    for k, l in itertools.product(range(chunk_size[0]), range(chunk_size[1])):
                        if chunk[l][k]:
                            chunk[l][k].pos = (k * sprite_size[0] + tile_offset[0], l * sprite_size[1] + tile_offset[1])
                            if chunk[l][k].colliderect(rect):
                                chunk[l][k].draw(screen)
                    break
