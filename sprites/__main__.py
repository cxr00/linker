from sprites import *

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 640))

player = Player()
player.change_state("walk")

scrolls = Scroll(5, 7, palette="nes"), Scroll(4, 3)
vines = Vine(3), Vine(7, palette="nes")
bangs = Bang(), Bang(5, 3, palette="nes")
ink = Ink(level=2)
pencils = Pencil(), Pencil("red", palette="nes")
statue = Statue("horns1")
dust = Dust()
plinth = Plinth(2)
demons = Demon(), Demon()


def sample_draw():
    screen.fill((0, 0, 0))

    # Scrolls
    for s in scrolls:
        if random.randint(0, 10) == 0:
            s.shift_palette()
    screen.blit(scrolls[0].surface, (100, 100))
    screen.blit(scrolls[1].surface, (200, 250))

    # Vines
    for v in vines:
        if random.randint(0, 10) == 0:
            v.shift_palette()
    screen.blit(vines[0].surface, (400, 400))
    screen.blit(vines[1].surface, (150, 220))

    # Bangs
    for b in bangs:
        if random.randint(0, 10) == 0:
            b.shift_palette()
    screen.blit(bangs[0].surface, (500, 0))
    screen.blit(bangs[1].surface, (0, 100))

    # Ink
    if random.randint(0, 10) == 0:
        ink.shift_palette()
    if random.randint(0, 10) == 0:
        ink.set_level((ink.level - 1) % 7)
    if random.randint(0, 10) == 0:
        ink.change_color()
    screen.blit(ink.surface, (400, 200))

    # Pencil
    for p in pencils:
        if random.randint(0, 10) == 0:
            p.shift_palette()
        if random.randint(0, 10) == 0:
            p.change_color()
    screen.blit(pencils[0].surface, (400, 100))
    screen.blit(pencils[1].surface, (250, 150))

    # Statue
    if random.randint(0, 10) == 0:
        statue.shift_palette()
    screen.blit(statue.surface, (500, 500))

    # Plinth
    if random.randint(0, 10) == 0:
        plinth.shift_palette()
    screen.blit(plinth.surface, (500, 595))

    # Dust
    screen.blit(dust.surface, (500, 300))
    dust.tick()

    # Fairies
    for d in demons:
        if random.randint(0, 10) == 0:
            d.shift_palette()
        d.tick()
    screen.blit(demons[0].surface, (0, 500))
    screen.blit(demons[1].surface, (0, 550))

    # Player
    screen.blit(player.surface, (500, 200))
    player.tick()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass
    sample_draw()
    pygame.display.update()
    pygame.time.wait(100)
