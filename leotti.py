import pyxel


class Leotti:
    vel = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pyxel.rect(self.x, self.y, 30, 30, pyxel.COLOR_DARKBLUE)
