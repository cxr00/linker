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
    palette = "pico-8"

    run = True
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
                            chunks = Chunk.deserialise(json.load(f), palette)
                            chunks = {
                                (chunk.xy[0], chunk.xy[1]): chunk for chunk in chunks
                            }
                    except json.decoder.JSONDecodeError:
                        pass
                elif event.key == pygame.K_p:
                    [chunk.shift_palette() for chunk in chunks.values()]
                    palette = "nes" if palette == "pico-8" else "pico-8"
        screen.fill((0, 0, 0))

        x = (cursor.pos[0] + camera.x_offset()) // 48
        y = (cursor.pos[1] + camera.y_offset()) // 48
        if cursor.create_tile:
            chunk_xy = (
                x // 14,
                y // 14
            )
            if -4 <= chunk_xy[0] <= 4 and -4 <= chunk_xy[1] <= 4:
                chunks[chunk_xy][x % 14][y % 14] = Filler(tile_type=(x * 14 + y * 14) % 3, palette=palette)

        for chunk in chunks.values():
            chunk.draw(screen, camera)
        player.draw(screen)
        # draw_meta(screen, clock, camera, cursor, player, (x, y))
        if pygame.mouse.get_focused():
            cursor.draw(screen)
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    main()
