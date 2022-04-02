import pygame


class Spritesheet:
    """
    Spritesheet handles the deconstruction of an image into component sprites.

    After a Spritesheet is constructed, you can access its members with __getitem__

    An entire Spritesheet can also be scaled

    :param image: the image you want to deconstruct
    :param width: the width of each sprite
    :param height: the height of each sprite
    """
    def __init__(self, image, width, height):
        self.sheet = image

        self.width = image.get_width() // width
        self.height = image.get_height() // height
        self.scale = 1

        self.sprites = [[] for _ in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                s = pygame.Surface((width, height), pygame.SRCALPHA)
                s.blit(self.sheet, (0, 0), (x*width, y*height, width, height))
                self[y].append(s)

    def __getitem__(self, item):
        return self.sprites[item]

    def __setitem__(self, key, value):
        self.sprites[key] = value

    def scale_sheet(self, scale: int):
        """
        Increase or decrease the scale of the Spritesheet
        """
        if scale > 0:
            self.scale *= scale
        else:
            raise ValueError(f"Cannot scale with zero or less")
        for x in range(self.width):
            for y in range(self.height):
                self[y][x] = pygame.transform.scale(self[y][x], (self.width * self.scale, self.height * self.scale))

    def get_dim(self):
        return self.width * self.scale, self.height * self.scale

    def get_width(self):
        return self.width * self.scale

    def get_height(self):
        return self.height * self.scale
