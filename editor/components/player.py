from cxr import SM

from editor.utils import draw_fps
from linker.sprites import character
from editor.components import Camera
from editor import TICK, WIDTH, HEIGHT
import pygame

controls = (
    pygame.K_UP, pygame.K_w,
    pygame.K_DOWN, pygame.K_s,
    pygame.K_LEFT, pygame.K_a,
    pygame.K_RIGHT, pygame.K_d
)
move_speed = 25


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
                mov = [0, 0]
                if self.pressed[pygame.K_UP] or self.pressed[pygame.K_w]:
                    mov[1] -= move_speed
                if self.pressed[pygame.K_DOWN] or self.pressed[pygame.K_s]:
                    mov[1] += move_speed
                if self.pressed[pygame.K_LEFT] or self.pressed[pygame.K_a]:
                    mov[0] -= move_speed
                if self.pressed[pygame.K_RIGHT] or self.pressed[pygame.K_d]:
                    mov[0] += move_speed
                if any(mov):
                    if mov[0] > 0:
                        self.character.turn_right()
                    elif mov[0] < 0:
                        self.character.turn_left()
                    self.character.pos = self["pos"] = self.character.pos[0]+mov[0], self.character.pos[1]+mov[1]
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
        pos = WIDTH//2 + (self.character.pos[0]-self.camera.x), HEIGHT//2 + (self.character.pos[1]-self.camera.y)
        self.character.draw(surface, pos)

    def shift_palette(self):
        self.character.shift_palette()

    def attach_camera(self, camera: Camera):
        self["camera"] = camera

def test_player():
    from cxr import SMR
    from editor import WIDTH, HEIGHT

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
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