import pyxel
from constants import HEIGHT, WIDTH, PLAYER_HEIGHT, PLAYER_WIDTH
import random


class Wall:
    vel = random.randint(1, 2)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 30
        self.counter = self.vel

    def move(self):
        self.counter -= 1
        self.counter %= 10
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

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, pyxel.COLOR_ORANGE)
