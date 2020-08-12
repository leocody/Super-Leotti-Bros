import pyxel
from pyxel import text
from constants import HEIGHT, WIDTH
from leotti import Leotti
from wall import Wall


class App:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Super Leotti Bros.", fps=60)
        self.leotti = Leotti(50, HEIGHT / 2)
        self.wall = Wall(128, HEIGHT / 2)
        self.game_over = False
        pyxel.load("assets/game_assets.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_over:
            return

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.leotti.move_down()

        if pyxel.btnp(pyxel.KEY_UP):
            self.leotti.move_up()

        if self.is_collision():
            self.game_over = True
        self.wall.move()

    def is_collision(self):

        if self.wall.top() <= self.leotti.top() <= self.wall.bottom() and self.wall.left() <= self.leotti.left() <= self.wall.right():
            return True
        if self.wall.top() <= self.leotti.bottom() <= self.wall.bottom() and self.wall.left() <= self.leotti.right() <= self.wall.right():
            return True

        return False

    def draw(self):
        pyxel.cls(0)
        self.leotti.draw()
        self.wall.draw()
        if self.game_over:
            pyxel.text(50, HEIGHT / 2, "GAME OVER", pyxel.COLOR_ORANGE)


App()
