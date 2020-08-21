import pyxel
from constants import HEIGHT, WIDTH, UP, DOWN
from leotti import Leotti
from coin import Coin
from combination_wall import ConbinationWall


class App:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Super Leotti Bros.", fps=30)
        self.leotti = Leotti(20, HEIGHT / 2)
        self.init_coin()
        self.score = 0
        self.init_wall()
        self.game_over = False
        pyxel.load("assets/game_assets.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.game_over:
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

            if wall.is_out_screen():
                self.score += 1
                wall.reset()

        for coin in self.coins:
            coin.move()
            if coin.is_collision(self.leotti):
                self.score += 2
                coin.reset()

            if coin.is_out_screen():
                coin.reset()

    def init_wall(self):
        self.walls = [
            ConbinationWall(WIDTH),
            ConbinationWall(WIDTH + 100)
        ]

    def init_coin(self):
        self.coins = [
            Coin()
        ]

    def draw(self):
        pyxel.cls(0)
        self.leotti.draw()
        for coin in self.coins:
            coin.draw()
        for wall in self.walls:
            wall.draw()
        pyxel.text(0, 0, "Score :" + str(self.score), pyxel.COLOR_GREEN)
        if self.game_over:
            pyxel.text(50, HEIGHT / 2, "GAME OVER", pyxel.COLOR_LIGHTBLUE)


App()
