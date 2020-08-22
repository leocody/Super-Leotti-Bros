import pyxel
from constants import HEIGHT, WIDTH, NORMAL, SPECIAL
from leotti import Leotti
import random
COUNTER = 2


class Coin:
    def __init__(self):
        self.vel = 3
        self.reset()
        self.height = 14
        self.width = 14
        self.counter = COUNTER
        self.type = NORMAL

    def reset(self):
        self.x = WIDTH + 50
        self.y: int = random.randint(0, HEIGHT)
        self.type = random.choice([NORMAL, NORMAL, NORMAL, SPECIAL])

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

    def is_collision(self, leotti: Leotti):

        if self.top() <= leotti.top() <= self.bottom() and self.left() <= leotti.left() <= self.right():
            return True
        if self.top() <= leotti.bottom() <= self.bottom() and self.left() <= leotti.right() <= self.right():
            return True

        return False

    def draw(self):
        if self.type == NORMAL:
            pyxel.blt(self.x, self.y, 0, 32, 0, 15,
                      47, colkey=pyxel.COLOR_BLACK)
        if self.type == SPECIAL:
            pyxel.blt(self.x, self.y, 0, 48, 0, 63,
                      15, colkey=pyxel.COLOR_BLACK)
        # pyxel.rect(self.x, self.y, self.width, self.height, pyxel.COLOR_NAVY)

    def score(self):
        if self.type == NORMAL:
            return 2
        elif self.type == SPECIAL:
            return 4
