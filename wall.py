from leotti import Leotti
from random import randint
import pyxel
from constants import HEIGHT, WIDTH, PLAYER_HEIGHT, PLAYER_WIDTH
import random


pos = [-40, -40, -20, 30, 50, 40, 70, -90, -30]
COUNTER = 2


class Wall:

    def __init__(self, x: int):
        self.vel = 3
        self.x: int = x
        self.y: int = random.choice(pos)
        self.height = HEIGHT
        self.width = random.randint(10, 30)
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

    def reset(self):
        self.x = WIDTH
        self.y = random.choice(pos)
        self.height = HEIGHT
        self.width = random.randint(10, 20)

    def is_collision(self, leotti: Leotti):

        if self.top() <= leotti.top() <= self.bottom() and self.left() <= leotti.left() <= self.right():
            return True
        if self.top() <= leotti.bottom() <= self.bottom() and self.left() <= leotti.right() <= self.right():
            return True

        return False

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, pyxel.COLOR_ORANGE)
