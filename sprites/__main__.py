from sprites import *

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))

# Samples

# Scrolls
screen.blit(Scroll(5, 7, palette="nes").surface, (100, 100))
screen.blit(Scroll(4, 3, palette="pico-8").surface, (200, 250))

# Vines
screen.blit(Vines(3).surface, (400, 400))
screen.blit(Vines(7, palette="nes").surface, (150, 220))

# Bangs
screen.blit(Bang().surface, (500, 0))
screen.blit(Bang(5, 3, palette="nes").surface, (0, 100))

# Potion
screen.blit(LINKER["item"]["ink"]["pico-8"]["blue"][2], (200, 200))
screen.blit(LINKER["item"]["ink"]["pico-8"]["vial"], (200, 200))

# Pencil
screen.blit(Pencil().surface, (400, 100))
screen.blit(Pencil("red", palette="nes").surface, (220, 150))
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
