from sprites import *

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))

player = Player()
player.change_state("fall")

def sample_draw():
    # Scrolls
    screen.fill((0, 0, 0))
    screen.blit(Scroll(5, 7, palette="nes").surface, (100, 100))
    screen.blit(Scroll(4, 3, palette="pico-8").surface, (200, 250))

    # Vines
    screen.blit(Vines(3).surface, (400, 400))
    screen.blit(Vines(7, palette="nes").surface, (150, 220))

    # Bangs
    screen.blit(Bang().surface, (500, 0))
    screen.blit(Bang(5, 3, palette="nes").surface, (0, 100))

    # Ink
    screen.blit(Ink(level=2).surface, (400, 200))

    # Pencil
    screen.blit(Pencil().surface, (400, 100))
    screen.blit(Pencil("red", palette="nes").surface, (250, 150))

    # Statue
    screen.blit(Statue("eye2").surface, (500, 500))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass
    sample_draw()

    screen.blit(player.surface, (500, 200))
    player.tick()
    pygame.display.update()
    pygame.time.wait(100)
