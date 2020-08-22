from combination_wall import ConbinationWall
from constants import WIDTH, HEIGHT, UP, DOWN, NORMAL, SPECIAL
from coin import Coin
from wall import Wall
import pyxel
from leotti import Leotti
from typing import List


class MainScreen:
    def __init__(self):
        self.reset()

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.reset()
                self.game_over = False
            return

        if pyxel.btn(pyxel.KEY_DOWN):
            self.leotti.change_direction(DOWN)

        if pyxel.btn(pyxel.KEY_UP):
            self.leotti.change_direction(UP)
        self.leotti.update()

        for wall in self.walls:
            wall.move()
            if wall.is_collision(self.leotti):
                self.game_over = True
                pyxel.stop()
                pyxel.play(3, 4)

            if wall.is_out_screen():
                self.score += 1
                wall.reset()

        for coin in self.coins:
            coin.move()
            if coin.is_collision(self.leotti):
                if coin.type == NORMAL:
                    pyxel.playm(0)
                elif coin.type == SPECIAL:
                    pyxel.play(1, 3)
                self.score += coin.score()
                coin.reset()

            if coin.is_out_screen():
                coin.reset()

    def init_wall(self):
        self.walls: List[Wall] = [
            ConbinationWall(WIDTH),
            ConbinationWall(WIDTH + 100)
        ]

    def init_coin(self):
        self.coins = [
            Coin()
        ]

    def reset(self):
        self.leotti = Leotti(20, HEIGHT / 2)
        self.init_coin()
        self.score = 0
        self.init_wall()
        self.game_over = False

        pyxel.play(3, 2, loop=True)

    def draw(self):
        pyxel.cls(0)
        self.leotti.draw()
        for coin in self.coins:
            coin.draw()
        for wall in self.walls:
            wall.draw()
        pyxel.text(0, 0, "Score :" + str(self.score), pyxel.COLOR_GREEN)
        if self.game_over:
            pyxel.text(50, HEIGHT / 2, "GAME OVER RESET = R",
                       pyxel.COLOR_LIGHTBLUE)
