import pygame
from editor import font

from linker import *
del sprite_size, LinkerSprite, Scroll, Bang, Player, Demon


def draw_fps(surface, clock):
    text = font.render(str(clock.get_fps()), True, (255, 255, 255))
    text_rect = text.get_rect()
    surface.blit(text, text_rect)

def draw_meta(surface, clock, camera, cursor, player, xy):
    fps_text = font.render(str(clock.get_fps()), True, (255, 255, 255))
    fps_rect = fps_text.get_rect()
    surface.blit(fps_text, fps_rect)

    camera_text = font.render(str((camera.x, camera.y, camera.move_debt)), True, (255, 255, 255))
    camera_rect = camera_text.get_rect(topleft=(0, 48))
    surface.blit(camera_text, camera_rect)

    player_text = font.render(str(player.character.pos), True, (255, 255, 255))
    player_rect = camera_text.get_rect(topleft=(0, 96))
    surface.blit(player_text, player_rect)

    cursor_text = font.render(str(xy), True, (255, 255, 255))
    cursor_rect = camera_text.get_rect(topleft=(cursor.pos[0]+48, cursor.pos[1]+16))
    surface.blit(cursor_text, cursor_rect)

    xy_text = font.render(str(xy), True, (255, 255, 255))
    xy_rect = xy_text.get_rect(topleft=(0, 192))
    surface.blit(xy_text, xy_rect)


def draw_highlight_box(surface, x, y, camera_pos):
    # I never quite managed to get this to work
    scaled_x = (x * 48 - camera_pos[0] % 48)
    scaled_y = (y * 48 - camera_pos[1] % 48)
    pygame.draw.line(surface, "white", (scaled_x, scaled_y), (scaled_x + 48, scaled_y))
    pygame.draw.line(surface, "white", (scaled_x + 48, scaled_y), (scaled_x + 48, scaled_y + 48))
    pygame.draw.line(surface, "white", (scaled_x + 48, scaled_y + 48), (scaled_x, scaled_y + 48))
    pygame.draw.line(surface, "white", (scaled_x, scaled_y + 48), (scaled_x, scaled_y))



def get_string_from_asset(a):
    if a == "x":
        return "x"
    if isinstance(a, Filler):
        return f"filler,{a.tile_type}"
    if isinstance(a, Tile):
        return f"tile,{a.tile_type}"
    if isinstance(a, CrossTile):
        return f"crosstile,{a.tile_type}"
    if isinstance(a, BrickTile):
        return f"bricktile,{a.size},{a.shade}"
    if isinstance(a, Accent):
        return f"accent,{a.accent_type}"
    if isinstance(a, Stairs):
        return f"stairs,{a.stair_type}"
    if isinstance(a, Button):
        return f"button"
    if isinstance(a, Chest):
        return f"chest"
    if isinstance(a, Pot):
        return f"pot"
    if isinstance(a, Statue):
        return f"statue,{a.statue_type}"
    if isinstance(a, Plinth):
        return f"plinth,{a.plinth_type}"
    if isinstance(a, Vine):
        return f"vine,{a.height}"

    if isinstance(a, Pen):
        return f"pen,{a.color}"
    if isinstance(a, Bomb):
        return f"bomb"
    if isinstance(a, Key):
        return f"key"
    if isinstance(a, Sack):
        return f"sack"
    if isinstance(a, Gem):
        return f"gem"
    if isinstance(a, Pearl):
        return f"pearl"
    if isinstance(a, Relic):
        return f"relic"
    if isinstance(a, Ink):
        return f"ink,{a.color}"



def get_asset_from_string(s, pos):
    if s == "x":
        return "x"
    s = s.split(",")
    t = s[0]
    if t == "filler":
        return Filler(int(s[1]), pos=pos)
    if t == "tile":
        return Tile(s[1], pos=pos)
    if t == "crosstile":
        return CrossTile(int(s[1]), pos=pos)
    if t == "bricktile":
        return BrickTile(s[1], s[2], pos=pos)
    if t == "accent":
        return Accent(s[1], pos=pos)
    if t == "stairs":
        return Stairs(int(s[1]), pos=pos)
    if t == "tile":
        return Tile(s[1], pos=pos)
    if t == "button":
        return Button(pos=pos)
    if t == "chest":
        return Chest(pos=pos)
    if t == "pot":
        return Pot(pos=pos)
    if t == "statue":
        return Statue(s[1], pos=pos)
    if t == "plinth":
        return Plinth(s[1], pos=pos)
    if t == "vine":
        return Vine(int(s[1]), pos=pos)

    if t == "pen":
        return Pen(s[1], pos=pos)
    if t == "bomb":
        return Bomb(pos=pos)
    if t == "key":
        return Key(pos=pos)
    if t == "sack":
        return Sack(pos=pos)
    if t == "gem":
        return Gem(pos=pos)
    if t == "pearl":
        return Pearl(pos=pos)
    if t == "relic":
        return Relic(pos=pos)
    if t == "ink":
        return Ink(s[1], pos=pos)
