import pygame
import random
import itertools
import time

from linker import *
from tilemap import Chunk, Map, chunk_size
del sprites, Spritesheet

# pygame
pygame.init()
WIDTH, HEIGHT = 672, 672
FPS = 60
scroll_speed = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()


class Camera:
    """
    The Camera stores the current relative location on the screen
    """
    def __init__(self):
        self.x = 0
        self.y = 0

    def offset(self):
        return self.x, self.y

    def negative(self):
        return -self.x, -self.y

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.left()
        if keys_pressed[pygame.K_RIGHT]:
            self.right()

        if keys_pressed[pygame.K_UP]:
            self.up()
        if keys_pressed[pygame.K_DOWN]:
            self.down()

    def up(self):
        self.y += scroll_speed

    def down(self):
        self.y -= scroll_speed

    def left(self):
        self.x += scroll_speed

    def right(self):
        self.x -= scroll_speed


camera = Camera()


# The player is special
player = Player()
player.change_state("walk")

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
pot = Pot()

# The range of x and y values for the game map.
map_dim = 5
map_range1, map_range2 = range(-map_dim+1, map_dim), range(-map_dim+1, map_dim)

# Track the time it takes to construct the map
start_time = time.time()

# Generate a test game map
game_map = Map()
for x, y in itertools.product(map_range1, map_range2):
    chunk = Chunk()
    for i, j in itertools.product(range(chunk_size[0]), range(chunk_size[1])):
        chunk[j][i] = Filler(tile_type=(i + x*chunk_size[1] + j + y*chunk_size[0]) % 3)
    game_map[x, y] = chunk
print(f"Map of {game_map.get_size()} tiles generated in {time.time() - start_time}")

game_map.update_range()


def lotto():
    """
    Determine if a palette or color shift event occurs
    """
    return random.randint(0, 50) == 0


def sample_draw():
    """
    Test the various linker linker
    """
    screen.fill((0, 0, 0))

    # The corners are used to determine whether a chunk is drawn
    corner_size = WIDTH // 2, HEIGHT // 2
    corners = (
        pygame.Rect(camera.negative(), corner_size),
        pygame.Rect((-camera.x, HEIGHT // 2 - camera.y), corner_size),
        pygame.Rect((WIDTH // 2 - camera.x, -camera.y), corner_size),
        pygame.Rect((WIDTH // 2 - camera.x, HEIGHT // 2 - camera.y), corner_size)
    )

    r = pygame.Surface((250, 250), pygame.SRCALPHA)
    pygame.draw.line(r, (100, 100, 100), (0, 0), (0, 249))
    pygame.draw.line(r, (100, 100, 100), (0, 249), (249, 249))
    pygame.draw.line(r, (100, 100, 100), (249, 249), (249, 0))
    pygame.draw.line(r, (100, 100, 100), (249, 0), (0, 0))
    # r.fill((100, 100, 100))

    rect = r.get_rect(topleft=(200, 200))
    # game_map.draw(screen, corners, camera.offset(), rect=rect)

    # Draw game map
    game_map.draw(screen, corners, camera.offset())

    # Scrolls
    for s in scrolls:
        if lotto():
            s.shift_palette()
    scrolls[0].pos = (100 + camera.x, 100 + camera.y)
    scrolls[0].draw(screen)
    scrolls[1].pos = (200 + camera.x, 250 + camera.y)
    scrolls[1].draw(screen)

    # Vines
    for v in vines:
        if lotto():
            v.shift_palette()
    vines[0].pos = (400 + camera.x, 400 + camera.y)
    vines[0].draw(screen)
    vines[1].pos = (150 + camera.x, 220 + camera.y)
    vines[1].draw(screen)

    # Bangs
    for b in bangs:
        if lotto():
            b.shift_palette()
    bangs[0].pos = (500 + camera.x, camera.y)
    bangs[0].draw(screen)
    bangs[1].pos = (camera.x, 100 + camera.y)
    bangs[1].draw(screen)

    # Ink
    if lotto():
        ink.shift_palette()
    if lotto():
        ink.set_level((ink.level - 1) % 7)
    if lotto():
        ink.change_color()
    ink.pos = (400 + camera.x, 200 + camera.y)
    ink.draw(screen)

    # Pencil
    for p in pencils:
        if lotto():
            p.shift_palette()
        if lotto():
            p.change_color()
    pencils[0].pos = (400 + camera.x, 100 + camera.y)
    pencils[0].draw(screen)
    pencils[1].pos = (250 + camera.x, 150 + camera.y)
    pencils[1].draw(screen)

    # Statue
    if lotto():
        statue.shift_palette()
    statue.pos = (500 + camera.x, 500 + camera.y)
    statue.draw(screen)

    # Plinth
    if lotto():
        plinth.shift_palette()
    plinth.pos = (500 + camera.x, 610 + camera.y)
    plinth.draw(screen)

    # Dust
    dust.pos = (500 + camera.x, 300 + camera.y)
    dust.draw(screen)
    dust.update()
    if lotto():
        dust.shift_palette()

    # Fairies
    for d in demons:
        if lotto():
            d.shift_palette()
        d.update()
    demons[0].pos = (camera.x, 500 + camera.y)
    demons[0].draw(screen)
    demons[1].pos = (camera.x, 550 + camera.y)
    demons[1].draw(screen)

    # Player
    player.pos = (500 + camera.x, 200 + camera.y)
    player.draw(screen)
    player.update()
    if lotto():
        player.shift_palette()
    if lotto():
        player.turn_left()
    elif lotto():
        player.turn_right()

    # Pot
    pot.pos = (100, 10)
    pot.draw(screen)
    if lotto():
        if pot.state == "empty":
            pot.fill()
        else:
            pot.empty()

    text = font.render(f"{camera.negative()}", True, (255, 255, 255))
    screen.blit(text, (0, 0))
    text = font.render(f"{int(clock.get_fps())}", True, (255, 255, 255))
    screen.blit(text, (0, 100))

    screen.blit(r, rect)


run = True
while run:
    clock.tick(FPS)
    pygame.event.post(pygame.event.Event(pygame.USEREVENT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass

    pressed = pygame.key.get_pressed()
    camera.update(pressed)

    sample_draw()
    pygame.display.update()
