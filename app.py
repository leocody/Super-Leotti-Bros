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

        self.main_screen = MainScreen()
        self.title_screen = TitleScreen()
        self.current_screen = self.main_screen
        # self.current_screen = self.title_screen
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.main_screen.update()

    def draw(self):
        self.main_screen.draw()


App()
