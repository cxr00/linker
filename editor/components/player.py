from cxr import SM
from linker.sprites import character
from editor.components import Camera
from editor.utils import TICK, PLAYER_MOVE, screen_size
import pygame

controls = (
    pygame.K_UP, pygame.K_w,
    pygame.K_DOWN, pygame.K_s,
    pygame.K_LEFT, pygame.K_a,
    pygame.K_RIGHT, pygame.K_d
)
move_speed = 30


class Player(SM):
    def __init__(self, key, name, palette="pico-8", pos=None):
        super().__init__(key, name)
        self.toggle_ser_priority(False)
        self._initialize(palette, pos)

    def _initialize(self, palette, pos):
        self["pos"] = pos
        self["character"] = character.Player(palette=palette, pos=pos)
        self["camera"] = None
        self["move_speed"] = [0, 0]

        @self.controller
        def controller(event):
            if self.camera is None:
                raise ValueError(f"No camera is attached to player {self.name}({self.key})")
            self["pressed"] = pygame.key.get_pressed()
            if any([self.pressed[k] for k in controls]) and self.current_state() != "walk":
                self.change_state("walk")
                self.character.change_state("walk")
            if event.type == TICK:
                self.camera(event)
                self.character.update()

        @self.add_state("idle")
        def idle(event):
            self["move_speed"] = [0, 0]

        @self.add_state("walk")
        def walk(event):
            if not any([self.pressed[k] for k in controls]):
                self.change_state("idle")
                self.character.change_state("idle")
            else:
                mov_ud, mov_lr = False, False
                if self.pressed[pygame.K_UP] or self.pressed[pygame.K_w]:
                    self["move_speed"][1] = self.move_speed[1] - 5 if abs(self.move_speed[1]) < move_speed else -move_speed
                    mov_ud = True
                if self.pressed[pygame.K_DOWN] or self.pressed[pygame.K_s]:
                    self["move_speed"][1] = self.move_speed[1] + 5 if self.move_speed[1] < move_speed else move_speed
                    mov_ud = True
                if not mov_ud:
                    if abs(self.move_speed[1]) < 5:
                        self.move_speed[1] = 0
                    elif self.move_speed[1] != 0:
                        to_add = (5 if self.move_speed[1] < 0 else -5)
                        self["move_speed"][1] = self.move_speed[1] + to_add
                if self.pressed[pygame.K_LEFT] or self.pressed[pygame.K_a]:
                    self["move_speed"][0] = self.move_speed[0] - 5 if abs(self.move_speed[0]) < move_speed else -move_speed
                    mov_lr = True
                if self.pressed[pygame.K_RIGHT] or self.pressed[pygame.K_d]:
                    self["move_speed"][0] = self.move_speed[0] + 5 if self.move_speed[0] < move_speed else move_speed
                    mov_lr = True
                if not mov_lr:
                    if abs(self.move_speed[0]) < 5:
                        self.move_speed[0] = 0
                    elif self.move_speed[0] != 0:
                        self["move_speed"][0] = self.move_speed[0] + (5 if self.move_speed[0] < 0 else -5)

                if any(self.move_speed):
                    if self.move_speed[0] > 0:
                        self.character.turn_right()
                    elif self.move_speed[0] < 0:
                        self.character.turn_left()
                    self.character.pos = self["pos"] = self.camera.x+self.move_speed[0], self.camera.y+self.move_speed[1]
                else:
                    self.change_state("idle")
                    self.character.change_state("idle")

        @self.add_state("fade")
        def fade(event):
            pass

        @self.add_state("fall")
        def fall(event):
            pass

    def draw(self, surface):
        pos = screen_size[0]//2 + (self.character.pos[0]-self.camera.x), screen_size[1]//2 + (self.character.pos[1]-self.camera.y)
        self.character.draw(surface, pos)

    def shift_palette(self):
        self.character.shift_palette()

    def attach_camera(self, camera: Camera):
        self["camera"] = camera

def test_player():
    from cxr import SMR
    from editor.utils import screen_size

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size)
    FPS = 60

    SMR.initialize("test")
    player = SM.generate("test", Player, palette="nes", pos=(100, 100))
    camera = SM.generate("test", Camera)
    camera.attach_player(player)

    run = True
    while run:
        clock.tick(FPS)
        pygame.event.post(pygame.event.Event(TICK))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == TICK:
                player(event)
                camera(event)

        # Draw
        screen.fill((0, 0, 0))
        player.draw(screen)
        draw_fps(screen, clock)
        pygame.display.update()


if __name__ == "__main__":
    test_player()