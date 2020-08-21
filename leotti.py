import pyxel
from pyxel import load
from constants import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, UP, DOWN


class Leotti:
    vel = 2
    direction = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y -= self.vel
        if 0 > self.y:
            self.y = 0

    def move_down(self):
        self.y += self.vel
        if HEIGHT - PLAYER_HEIGHT < self.y:
            self.y = HEIGHT - PLAYER_HEIGHT

    def update(self):
        if self.direction == UP:
            self.move_up()
        if self.direction == DOWN:
            self.move_down()

    def change_direction(self, direction):
        self.direction = direction

    def top(self):
        return self.y + 2

    def bottom(self):
        return self.y + PLAYER_HEIGHT - 5

    def left(self):
        return self.x + 3

    def right(self):
        return self.x + PLAYER_WIDTH - 3

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, pyxel.COLOR_ORANGE)
