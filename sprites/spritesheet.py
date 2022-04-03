import pygame


class Spritesheet:
    """
    Spritesheet handles the deconstruction of an image into component sprites.

    After a Spritesheet is constructed, you can access its members with __getitem__

    An entire Spritesheet can also be scaled by either width, height, or both

    :param image: the image you want to deconstruct
    :param width: the width of each sprite
    :param height: the height of each sprite
    """
    def __init__(self, image, width, height):
        self.sheet = image

        self.width = image.get_width() // width
        self.height = image.get_height() // height
        self.scale_width = 1
        self.scale_height = 1

        self.sprites: list[list[pygame.Surface]] = [[] for _ in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                s = pygame.Surface((width, height), pygame.SRCALPHA)
                s.blit(self.sheet, (0, 0), (x*width, y*height, width, height))
                self[y].append(s)

    def __getitem__(self, item):
        return self.sprites[item]

    def scale_sheet(self, width: int = 1, height: int = 1):
        """
        Increase the scale of the Spritesheet
        """
        if width > 0:
            self.scale_width *= width
        else:
            raise ValueError(f"Cannot scale width by a factor of zero or less")
        if height > 0:
            self.scale_height *= height
        else:
            raise ValueError(f"Cannot scale height by a factor of zero or less")
        for x in range(self.width):
            for y in range(self.height):
                self[y][x] = pygame.transform.scale(self[y][x], (self.width * self.scale_width, self.height * self.scale_height))

    def get_size(self):
        """
        Get the dimensions of each sprite according to scale
        """
        return self.width * self.scale_width, self.height * self.scale_height

    def get_width(self):
        """
        Get the width of each sprite according to scale
        """
        return self.width * self.scale_width

    def get_height(self):
        """
        Get the height of each sprite according to scale
        """
        return self.height * self.scale_height
