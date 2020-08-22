import pyxel


class TitleScreen:
    def __init__(self):
        pass

    def update(self):
        return

    def draw(self):
        pyxel.text(50, 50, "SUPER LEOTTI BROS.", pyxel.COLOR_LIGHTBLUE)
        pyxel.text(40, 40, "Press S key to start", pyxel.COLOR_LIGHTBLUE)
