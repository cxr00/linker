from cxr import SM
from editor import WIDTH, HEIGHT

class Camera(SM):

    def __init__(self, key, name):
        super().__init__(key, name)
        self.toggle_ser_priority(False)
        self._initialize()

    def _initialize(self):
        self["x"], self["y"] = WIDTH // 2, HEIGHT // 2
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
                self["x_speed"] = -10 if self.move_debt[0] > 0 else 10
            if self.move_debt[1] == 0:
                self["y_speed"] = 0
            elif abs(self.move_debt[1]) < 20:
                self["y_speed"] = -1 if self.move_debt[1] > 0 else 1
            else:
                self["y_speed"] = -10 if self.move_debt[1] > 0 else 10
            self["x"] += self.x_speed
            self["y"] += self.y_speed


    def negative(self):
        return -self.x, -self.y

    def x_offset(self):
        return self.x - WIDTH // 2

    def y_offset(self):
        return self.y - HEIGHT // 2