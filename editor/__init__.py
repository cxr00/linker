import pygame

pygame.init()

TICK = pygame.event.custom_type()
PLAYER_MOVE = pygame.event.custom_type()
WIDTH, HEIGHT = 672, 672
font = pygame.font.Font(None, 32)
