from random import randint
import pyxel
from pyxel import text
from constants import HEIGHT, WIDTH
from leotti import Leotti
from wall import Wall
from combination_wall import ConbinationWall


class App:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Super Leotti Bros.", fps=30)
        self.leotti = Leotti(20, HEIGHT / 2)
        self.score = 0
        self.init_wall()
        self.game_over = False
        pyxel.load("assets/game_assets.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_over:
            return

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_DOWN):
            self.leotti.move_down()

        if pyxel.btn(pyxel.KEY_UP):
            self.leotti.move_up()

        for wall in self.walls:
            wall.move()
            if wall.is_collision(self.leotti):
                self.game_over = True

            if wall.is_out_screen():
                self.score += 1
                wall.reset()

    def init_wall(self):
        self.walls = [
            ConbinationWall(WIDTH),
            ConbinationWall(WIDTH + 70),
            ConbinationWall(WIDTH + 130)
        ]

    def draw(self):
        pyxel.cls(0)
        self.leotti.draw()
        for wall in self.walls:
            wall.draw()
        pyxel.text(0, 0, "Score :" + str(self.score), pyxel.COLOR_GREEN)
        if self.game_over:
            pyxel.text(50, HEIGHT / 2, "GAME OVER", pyxel.COLOR_ORANGE)


App()
