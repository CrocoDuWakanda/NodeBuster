from scripts.utilitaries.button import Button
from scripts.screen.upgrade_screen import UpgradeScreen
import pyxel



class GameScreen:
    def __init__(self, app, constants, save_data):
        self.app = app
        self.constants = constants
        self.save_data = save_data
        self.current_game_screen = None
        self.set_game_screen("upgrades")


    def set_game_screen(self, new_state):
        self.state = new_state
        if new_state == "upgrades":
            self.current_game_screen = UpgradeScreen(self, self.save_data)


    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        if self.current_game_screen:
            self.current_game_screen.draw()

