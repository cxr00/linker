from cxr import SMR, SM
from editor.components import Cursor, Player, Camera
from editor.utils import TICK, draw_fps, draw_highlight_box, screen_size
from linker import Filler
import pygame


def get_string_from_asset():
    # TODO: assign string values to each asset
    pass


def get_asset_from_string():
    # TODO: assign classes to each string
    pass


def main():
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60
    screen = pygame.display.set_mode((672, 672))
    pygame.mouse.set_visible(False)


    SMR.initialize("editor")
    c = SM.generate("editor", Cursor)
    player = SM.generate("editor", Player, pos=(screen_size[0]//2, screen_size[1]//2))
    camera = SM.generate("editor", Camera)
    player.attach_camera(camera)

    run = True
    tiles = {}
    while run:
        clock.tick(FPS)
        pygame.event.post(pygame.event.Event(TICK, pos=player.character.pos, state=player.current_state()))

        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                c(event)
            elif event.type == pygame.QUIT:
                run = False
            elif event.type == TICK:
                # camera(event)
                player(event)
        screen.fill((0, 0, 0))

        x, y = (c.pos[0]) // 48, (c.pos[1]) // 48
        if c.create_tile:
            tiles[(x, y)] = Filler(tile_type=(x * 14 + y * 14) % 3)

        for tile_key in tiles:
            screen.blit(tiles[tile_key].surface, (tile_key[0] * 48 + 336-camera.x, tile_key[1] * 48 + 336-camera.y))

        player.draw(screen)
        draw_highlight_box(screen, x, y)
        draw_fps(screen, clock)
        if pygame.mouse.get_focused():
            c.draw(screen)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
