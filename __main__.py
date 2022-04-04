import pygame
import random
import itertools
import time

from sprites import *
from tilemap import Chunk, Map
del linker, spritesheet

pygame.init()
WIDTH, HEIGHT = 672, 672
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# The player is special
player = Player()
player.change_state("fall")

# Various LinkerSprites
scrolls = Scroll(5, 7, palette="nes"), Scroll(4, 3)
vines = Vine(3), Vine(7, palette="nes")
bangs = Bang(2, 3), Bang(5, 3, palette="nes")
ink = Ink(level=2)
pencils = Pencil(), Pencil("red", palette="nes")
statue = Statue("horns1")
dust = Dust()
plinth = Plinth(1)
demons = Demon(), Demon()

# Chunks in a map must be the same size
chunk_dim = 14, 14

# The range of x and y values for the game map.
map_dim = 40
map_range1, map_range2 = range(-map_dim+1, map_dim), range(-map_dim+1, map_dim)

# Track the time it takes to construct the map
start_time = time.time()

# Generate the game map
game_map = Map(chunk_dim)
for x, y in itertools.product(map_range1, map_range2):
    chunk = Chunk(chunk_dim)
    for i, j in itertools.product(range(chunk_dim[0]), range(chunk_dim[1])):
        chunk[j][i] = Filler(tile_type=(i + x*chunk_dim[1] + j + y*chunk_dim[0]) % 3)
    game_map[x, y] = chunk
print(f"Map of {game_map.get_size()} tiles generated in {time.time() - start_time}")


# The offset determines the region of the map which will be drawn
offset = [0, 0]


def lotto():
    """
    Determine if a palette or color shift event occurs
    """
    return random.randint(0, 50) == 0


def sample_draw():
    """
    Test the various linker components
    """
    screen.fill((0, 0, 0))

    # The corners are used to determine whether a chunk is drawn
    corners = (
        pygame.Rect((-offset[0], -offset[1]), (WIDTH // 2, HEIGHT // 2)),
        pygame.Rect((-offset[0], HEIGHT // 2 - offset[1]), (WIDTH // 2, HEIGHT // 2)),
        pygame.Rect((WIDTH // 2 - offset[0], -offset[1]), (WIDTH // 2, HEIGHT // 2)),
        pygame.Rect((WIDTH // 2 - offset[0], HEIGHT // 2 - offset[1]), (WIDTH // 2, HEIGHT // 2))
    )

    # Draw game map
    game_map.draw(screen, corners, offset)

    # Scrolls
    for s in scrolls:
        if lotto():
            s.shift_palette()
    scrolls[0].draw(screen, (100 + offset[0], 100 + offset[1]))
    scrolls[1].draw(screen, (200 + offset[0], 250 + offset[1]))

    # Vines
    for v in vines:
        if lotto():
            v.shift_palette()
    vines[0].draw(screen, (400 + offset[0], 400 + offset[1]))
    vines[1].draw(screen, (150 + offset[0], 220 + offset[1]))

    # Bangs
    for b in bangs:
        if lotto():
            b.shift_palette()
    bangs[0].draw(screen, (500 + offset[0], offset[1]))
    bangs[1].draw(screen, (offset[0], 100 + offset[1]))

    # Ink
    if lotto():
        ink.shift_palette()
    if lotto():
        ink.set_level((ink.level - 1) % 7)
    if lotto():
        ink.change_color()
    ink.draw(screen, (400 + offset[0], 200 + offset[1]))

    # Pencil
    for p in pencils:
        if lotto():
            p.shift_palette()
        if lotto():
            p.change_color()
    pencils[0].draw(screen, (400 + offset[0], 100 + offset[1]))
    pencils[1].draw(screen, (250 + offset[0], 150 + offset[1]))

    # Statue
    if lotto():
        statue.shift_palette()
    statue.draw(screen, (500 + offset[0], 500 + offset[1]))

    # Plinth
    if lotto():
        plinth.shift_palette()
    plinth.draw(screen, (500 + offset[0], 610 + offset[1]))

    # Dust
    dust.draw(screen, (500 + offset[0], 300 + offset[1]))
    dust.tick()
    if lotto():
        dust.shift_palette()

    # Fairies
    for d in demons:
        if lotto():
            d.shift_palette()
        d.tick()
    demons[0].draw(screen, (offset[0], 500 + offset[1]))
    demons[1].draw(screen, (offset[0], 550 + offset[1]))

    # Player
    player.draw(screen, (500 + offset[0], 200 + offset[1]))
    player.tick()
    if lotto():
        player.shift_palette()
    if lotto():
        player.turn_left()
    elif lotto():
        player.turn_right()

    text = pygame.font.Font(None, 32).render(f"{-offset[0]},{-offset[1]}", True, (255, 255, 255))
    screen.blit(text, (0, 0))


run = True
FPS = 60
clock = pygame.time.Clock()
scroll_speed = 10
while run:
    clock.tick(FPS)
    pygame.event.post(pygame.event.Event(pygame.USEREVENT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            offset[0] += scroll_speed
        if pressed[pygame.K_RIGHT]:
            offset[0] -= scroll_speed

        if pressed[pygame.K_UP]:
            offset[1] += scroll_speed
        if pressed[pygame.K_DOWN]:
            offset[1] -= scroll_speed

    sample_draw()
    pygame.display.update()
