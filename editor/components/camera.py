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

            self["x"], self["y"] = event.pos


    def negative(self):
        return -self.x, -self.y

    def x_offset(self):
        return self.x - WIDTH // 2

    def y_offset(self):
        return self.y - HEIGHT // 2