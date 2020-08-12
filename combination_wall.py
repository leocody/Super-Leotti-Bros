from random import choice
from wall import Wall
import random

MAP = [
    {"upper": -50, "lower": 108},  # local
    {"upper": -50, "lower": 138},  # wide
    {"upper": -30, "lower": 140},  # local
    {"upper": -128, "lower": 30},  # top
    {"upper": -30, "lower": 128},  # bottom
    {"upper": -79, "lower": 79},  # center
    {"upper": -90, "lower": 68},  # local
    {"upper": -115, "lower": 43},  # local
    {"upper": -40, "lower": 118},  # local
]


class ConbinationWall:
    def __init__(self, x):
        self.x = x
        self.reset()

    def draw(self):
        self.upper.draw()
        self.lower.draw()

    def reset(self):
        choice = random.choice(MAP)
        self.upper = Wall(self.x, choice["upper"])
        self.lower = Wall(self.x, choice["lower"])

    def is_collision(self, leotti):
        if self.upper.is_collision(leotti):
            return True
        if self.lower.is_collision(leotti):
            return True
        return False

    def move(self):
        self.upper.move()
        self.lower.move()

    def is_out_screen(self):
        if self.upper.right() < 0:
            return True
        if self.lower.right() < 0:
            return True
        return False