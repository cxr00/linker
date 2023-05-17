import pygame

from linker import LinkerSprite
from editor import font
from editor.utils import get_string_from_asset, get_asset_from_string


class Chunk:
    def __init__(self, xy, tiles=None, collectibles=None):
        self.xy = xy
        self.tiles = [
            ["x"] * 14 for _ in range(14)
        ] if tiles is None else tiles
        self.collectibles = [

        ] if collectibles is None else collectibles

    def __getitem__(self, item):
        return self.tiles[item]

    def __iter__(self):
        return iter(self.tiles)

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

    def shift_palette(self):
        for row in self:
            for tile in row:
                if tile != "x":
                    tile.shift_palette()


    def serialise(self):
        return dict(
            x=self.xy[0],
            y=self.xy[1],
            tiles=[[get_string_from_asset(self[x][y]) for x in range(14)] for y in range(14)],
            collectibles=self.collectibles
        )

    @staticmethod
    def deserialise(chunks, palette):
        return [
            Chunk(
                (chunk["x"], chunk["y"]),
                [[get_asset_from_string(chunk["tiles"][x][y], (x,y), palette) for x in range(14)] for y in range(14)],
                [
                    {
                        "item": get_asset_from_string(collectible["name"], (collectible["x"], collectible["y"])),
                        "x": collectible["x"],
                        "y": collectible["y"]
                    } for collectible in chunk["collectibles"]
                ]
            ) for chunk in chunks
        ]