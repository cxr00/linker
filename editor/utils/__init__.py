import pygame

TICK = pygame.event.custom_type()
PLAYER_MOVE = pygame.event.custom_type()
screen_size = 672, 672

def draw_fps(surface, clock):
    text = pygame.font.Font(None, 32)
    text = text.render(str(clock.get_fps()), True, (255, 255, 255))
    text_rect = text.get_rect()
    surface.blit(text, text_rect)


def draw_highlight_box(surface, x, y):
    scaled_x, scaled_y = x * 48, y * 48
    pygame.draw.line(surface, "white", (scaled_x, scaled_y), (scaled_x + 48, scaled_y))
    pygame.draw.line(surface, "white", (scaled_x + 48, scaled_y), (scaled_x + 48, scaled_y + 48))
    pygame.draw.line(surface, "white", (scaled_x + 48, scaled_y + 48), (scaled_x, scaled_y + 48))
    pygame.draw.line(surface, "white", (scaled_x, scaled_y + 48), (scaled_x, scaled_y))
