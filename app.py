import pyxel
from constants import HEIGHT, WIDTH, UP, DOWN, NORMAL, SPECIAL
from leotti import Leotti
from coin import Coin
from combination_wall import ConbinationWall
from main_screen import MainScreen
from title_screen import TitleScreen


class App:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Super Leotti Bros.", fps=30)
        pyxel.load("assets/game_assets.pyxres")

        self.current_screen = TitleScreen()
        pyxel.run(self.update, self.draw)

    def update(self):
        if isinstance(self.current_screen, TitleScreen):
            if pyxel.btnp(pyxel.KEY_S) or pyxel.btnp(pyxel.GAMEPAD_1_START):
                self.current_screen = MainScreen()

        if isinstance(self.current_screen, MainScreen):
            if self.current_screen.game_over and (pyxel.btnp(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD_1_START)):
                self.current_screen = TitleScreen()

        self.current_screen.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.current_screen.draw()


App()
