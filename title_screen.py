import pyxel
import constants as C


class TitleScreen:
    def __init__(self):
        pyxel.playm(1, loop=True)

    def __del__(self):
        pyxel.stop()

    def update(self):
        return

    def draw(self):
        pyxel.blt(C.WIDTH / 2 - 15, 32, 1, 0, 0, 31, 17)
        pyxel.text(50, 60, "Press S key to start", pyxel.COLOR_LIGHTBLUE)
