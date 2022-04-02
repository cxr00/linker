import sprites
from sprites.linker import Statue
from sprites.linker.components.assets import LINKER

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))

# Samples

# Scrolls
screen.blit(sprites.create_scroll(5, 7, palette="nes"), (100, 100))
screen.blit(sprites.create_scroll(4, 3, palette="pico-8"), (200, 250))

# Vines
screen.blit(sprites.create_vines(3), (400, 400))
screen.blit(sprites.create_vines(7, palette="nes"), (150, 220))

# Bangs
screen.blit(sprites.create_bang(), (500, 0))
screen.blit(sprites.create_bang(5, 3, palette="nes"), (0, 100))

# Potion
screen.blit(LINKER["item"]["ink"]["pico-8"]["blue"][2], (200, 200))
screen.blit(LINKER["item"]["ink"]["pico-8"]["vial"], (200, 200))

# Pencil
screen.blit(LINKER["item"]["pencil"]["nes"]["case"], (220, 150))
screen.blit(LINKER["item"]["pencil"]["nes"]["red"], (220, 150))

statue = Statue("eye2")
screen.blit(statue.surface, (500, 500))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass
    pygame.display.update()
