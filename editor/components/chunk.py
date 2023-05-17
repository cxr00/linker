import pygame

from linker import LinkerSprite
from editor import font


class Chunk:
    def __init__(self, xy):
        self.xy = xy
        self.tiles = [
            ["x"] * 14 for _ in range(14)
        ]
        self.collectibles = {

        }

    def __getitem__(self, item):
        return self.tiles[item]

    def draw(self, surface, camera):
        tl = self.xy[0] * 672 - camera.x_offset(), self.xy[1] * 672 - camera.y_offset()
        tr = tl[0] + 672, tl[1]
        br = tr[0], tr[1] + 672
        bl = br[0] - 672, br[1]
        for x, row in enumerate(self.tiles):
            for y, element in enumerate(row):
                if isinstance(element, LinkerSprite):
                    surface.blit(element.surface, (self.xy[0]*672 + x*48 - camera.x_offset(), self.xy[1]*672 + y*48 - camera.y_offset()))

        coord = font.render(f"{self.xy}", True, (255, 255, 255))
        coord_rect = coord.get_rect(topleft=(tl[0] + 5, tl[1] + 5))
        surface.blit(coord, coord_rect)
        pygame.draw.line(surface, "white", tl, tr)
        pygame.draw.line(surface, "white", tr, br)
        pygame.draw.line(surface, "white", br, bl)
        pygame.draw.line(surface, "white", bl, tl)
