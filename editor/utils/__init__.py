import pygame
pygame.init()

TICK = pygame.event.custom_type()
PLAYER_MOVE = pygame.event.custom_type()
screen_size = 672, 672
font = pygame.font.Font(None, 32)

def draw_fps(surface, clock):
    text = font.render(str(clock.get_fps()), True, (255, 255, 255))
    text_rect = text.get_rect()
    surface.blit(text, text_rect)

def draw_meta(surface, clock, camera, cursor, player):
    fps_text = font.render(str(clock.get_fps()), True, (255, 255, 255))
    fps_rect = fps_text.get_rect()
    camera_text = font.render(str((camera.x, camera.y, camera.move_debt)), True, (255, 255, 255))
    camera_rect = camera_text.get_rect(topleft=(0, 48))
    player_text = font.render(str(player.character.pos), True, (255, 255, 255))
    player_rect = camera_text.get_rect(topleft=(0, 96))
    cursor_text = font.render(str(cursor.pos), True, (255, 255, 255))
    cursor_rect = camera_text.get_rect(topleft=(0, 144))
    surface.blit(fps_text, fps_rect)
    surface.blit(camera_text, camera_rect)
    surface.blit(player_text, player_rect)
    surface.blit(cursor_text, cursor_rect)


def draw_highlight_box(surface, x, y, camera_pos):
    scaled_x = (x * 48 - camera_pos[0] % 48)
    scaled_y = (y * 48 - camera_pos[1] % 48)
    pygame.draw.line(surface, "white", (scaled_x, scaled_y), (scaled_x + 48, scaled_y))
    pygame.draw.line(surface, "white", (scaled_x + 48, scaled_y), (scaled_x + 48, scaled_y + 48))
    pygame.draw.line(surface, "white", (scaled_x + 48, scaled_y + 48), (scaled_x, scaled_y + 48))
    pygame.draw.line(surface, "white", (scaled_x, scaled_y + 48), (scaled_x, scaled_y))
