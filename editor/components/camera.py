from cxr import SM
from editor.utils import screen_size

class Camera(SM):

    def __init__(self, key, name):
        super().__init__(key, name)
        self.toggle_ser_priority(False)
        self._initialize()

    def _initialize(self):
        self["x"], self["y"] = screen_size[0] // 2, screen_size[1] // 2
        self["x_speed"] = self["y_speed"] = 0
        self["move_debt"] = 0, 0
        self["character_offset"] = 0, 0

        @self.controller
        def controller(event):
            self["move_debt"] = self.x - (event.pos[0] + self.character_offset[0]), self.y - (event.pos[1] + self.character_offset[1])
            if self.move_debt[0] == 0:
                self["x_speed"] = 0
            elif abs(self.move_debt[0]) < 20:
                self["x_speed"] = -1 if self.move_debt[0] > 0 else 1
            else:
                self["x_speed"] = -4 if self.move_debt[0] > 0 else 4
            if self.move_debt[1] == 0:
                self["y_speed"] = 0
            elif abs(self.move_debt[1]) < 20:
                self["y_speed"] = -1 if self.move_debt[1] > 0 else 1
            else:
                self["y_speed"] = -4 if self.move_debt[1] > 0 else 4
            self["x"] += self.x_speed
            self["y"] += self.y_speed


    def negative(self):
        return -self.x, -self.y
