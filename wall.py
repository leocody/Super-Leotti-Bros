from leotti import Leotti
import pyxel
from constants import HEIGHT, WIDTH
COUNTER = 2


class Wall:

    def __init__(self, x: int, y: int):
        self.vel = 3
        self.x: int = x
        self.y: int = y
        self.height = HEIGHT
        self.width = 25
        self.counter = COUNTER

    def move(self):
        self.counter -= 1
        self.counter %= COUNTER
        if self.counter == 0:
            self.x -= self.vel

    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.height

    def right(self):
        return self.x + self.width

    def left(self):
        return self.x

    def is_out_screen(self):
        if self.right() < 0:
            return True
        else:
            return False

    def reset(self, y):
        self.x = WIDTH
        self.y = y

    def is_collision(self, leotti: Leotti):

        if self.top() <= leotti.top() <= self.bottom() and self.left() <= leotti.left() <= self.right():
            return True
        if self.top() <= leotti.bottom() <= self.bottom() and self.left() <= leotti.right() <= self.right():
            return True

        return False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, 24, 143, colkey=pyxel.COLOR_BLACK)
