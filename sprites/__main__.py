from sprites import *

import pygame
import random
import itertools

pygame.init()
WIDTH, HEIGHT = 672, 672
scroll_speed = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Player()
player.change_state("walk")

scrolls = Scroll(5, 7, palette="nes"), Scroll(4, 3)
vines = Vine(3), Vine(7, palette="nes")
bangs = Bang(), Bang(5, 3, palette="nes")
ink = Ink(level=2)
pencils = Pencil(), Pencil("red", palette="nes")
statue = Statue("horns1")
dust = Dust()
plinth = Plinth(1)
demons = Demon(), Demon()

chunk_width, chunk_height = 14, 14
map_size = 10

game_map = Map()
for x, y in itertools.product(range(-map_size+1, map_size), repeat=2):
    chunk = Chunk(chunk_width, chunk_height)
    for i, j in itertools.product(range(chunk_width), range(chunk_height)):
        chunk[i][j] = Filler(tile_type=random.randint(0, 2), palette=random.choice(["pico-8", "nes"]))
    game_map[x, y] = chunk

offset = [0, 0]


def sample_draw():
    screen.fill((0, 0, 0))

    corners = (-offset[0], -offset[1]), (WIDTH-offset[0], -offset[1]), (-offset[0], HEIGHT-offset[1]), (WIDTH-offset[0], HEIGHT-offset[1])
    game_map.draw(screen, corners, offset)

    # Scrolls
    for s in scrolls:
        if random.randint(0, 10) == 0:
            s.shift_palette()
    screen.blit(scrolls[0].surface, (100 + offset[0], 100 + offset[1]))
    screen.blit(scrolls[1].surface, (200 + offset[0], 250 + offset[1]))

    # Vines
    for v in vines:
        if random.randint(0, 10) == 0:
            v.shift_palette()
    screen.blit(vines[0].surface, (400 + offset[0], 400 + offset[1]))
    screen.blit(vines[1].surface, (150 + offset[0], 220 + offset[1]))

    # Bangs
    for b in bangs:
        if random.randint(0, 10) == 0:
            b.shift_palette()
    screen.blit(bangs[0].surface, (500 + offset[0], offset[1]))
    screen.blit(bangs[1].surface, (offset[0], 100 + offset[1]))

    # Ink
    if random.randint(0, 10) == 0:
        ink.shift_palette()
    if random.randint(0, 10) == 0:
        ink.set_level((ink.level - 1) % 7)
    if random.randint(0, 10) == 0:
        ink.change_color()
    screen.blit(ink.surface, (400 + offset[0], 200 + offset[1]))

    # Pencil
    for p in pencils:
        if random.randint(0, 10) == 0:
            p.shift_palette()
        if random.randint(0, 10) == 0:
            p.change_color()
    screen.blit(pencils[0].surface, (400 + offset[0], 100 + offset[1]))
    screen.blit(pencils[1].surface, (250 + offset[0], 150 + offset[1]))

    # Statue
    if random.randint(0, 10) == 0:
        statue.shift_palette()
    screen.blit(statue.surface, (500 + offset[0], 500 + offset[1]))

    # Plinth
    if random.randint(0, 10) == 0:
        plinth.shift_palette()
    screen.blit(plinth.surface, (500 + offset[0], 595 + offset[1]))

    # Dust
    screen.blit(dust.surface, (500 + offset[0], 300 + offset[1]))
    dust.tick()

    # Fairies
    for d in demons:
        if random.randint(0, 10) == 0:
            d.shift_palette()
        d.tick()
    screen.blit(demons[0].surface, (offset[0], 500 + offset[1]))
    screen.blit(demons[1].surface, (offset[0], 550 + offset[1]))

    # Player
    screen.blit(player.surface, (500 + offset[0], 200 + offset[1]))
    player.tick()

    text = pygame.font.Font(None, 32).render(f"{-offset[0]},{-offset[1]}", True, (255, 255, 255))
    screen.blit(text, (0, 0))


run = True
while run:
    pygame.event.post(pygame.event.Event(pygame.USEREVENT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass
        pos = pygame.mouse.get_pos()
        if pos[0] <= 30:
            offset[0] += scroll_speed
        elif pos[0] >= WIDTH - 30:
            offset[0] -= scroll_speed
        if pos[1] <= 30:
            offset[1] += scroll_speed
        elif pos[1] >= HEIGHT - 30:
            offset[1] -= scroll_speed
    sample_draw()
    pygame.display.update()
    pygame.time.wait(100)
