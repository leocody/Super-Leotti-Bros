import pyxel
from constants import HEIGHT, WIDTH
from leotti import Leotti


class App:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Super Leotti Bros.")
        self.leotti = Leotti(HEIGHT / 2, WIDTH / 2)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):

        self.leotti.draw()


App()
