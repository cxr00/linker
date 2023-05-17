import json

from cxr import SMR, SM
from editor.components import Cursor, Player, Camera, Chunk
from editor import TICK, WIDTH, HEIGHT
from editor.utils import draw_meta
from linker import Filler
import pygame


def main():
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60
    screen = pygame.display.set_mode((672, 672))
    pygame.mouse.set_visible(False)


    SMR.initialize("editor")
    cursor = SM.generate("editor", Cursor)
    player = SM.generate("editor", Player, pos=(WIDTH//2, HEIGHT//2))
    camera = SM.generate("editor", Camera)
    player.attach_camera(camera)

    chunks = {
        (x, y): Chunk((x, y)) for x in range(-4, 5) for y in range(-4, 5)
    }

    run = True
    tiles = {}
    while run:
        clock.tick(FPS)
        pygame.event.post(pygame.event.Event(TICK, pos=player.character.pos, state=player.current_state()))

        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                cursor(event)
            elif event.type == pygame.QUIT:
                run = False
            elif event.type == TICK:
                player(event)
                camera(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    with open("chunks.json", "w+") as f:
                        json.dump([chunk.serialise() for chunk in chunks.values()], f)
                elif event.key == pygame.K_l:
                    try:
                        with open("chunks.json", "r") as f:
                            chunks = Chunk.deserialise(json.load(f))
                            chunks = {
                                (chunk.xy[0], chunk.xy[1]): chunk for chunk in chunks
                            }
                    except json.decoder.JSONDecodeError:
                        pass
        screen.fill((0, 0, 0))

        x = (cursor.pos[0] + camera.x - 336) // 48
        y = (cursor.pos[1] + camera.y - 336) // 48
        if cursor.create_tile:
            chunk_xy = (
                x // 14,
                y // 14
            )
            tile_x, tile_y = (
                x % 14, y % 14
            )
            if -4 <= chunk_xy[0] <= 4 and -4 <= chunk_xy[1] <= 4:
                chunks[chunk_xy][tile_x][tile_y] = Filler(tile_type=(x * 14 + y * 14) % 3)

        for tile_key in tiles:
            screen.blit(tiles[tile_key].surface, (tile_key[0] * 48 + 336-camera.x, tile_key[1] * 48 + 336-camera.y))

        for chunk in chunks.values():
            chunk.draw(screen, camera)
        player.draw(screen)
        draw_meta(screen, clock, camera, cursor, player, (x, y))
        if pygame.mouse.get_focused():
            cursor.draw(screen)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
