from scripts.utilitaries.button import Button
from scripts.screen.upgrade_screen import UpgradeScreen
import pyxel



class GameScreen:
    def __init__(self, app, constants, save_data):
        self.app = app
        self.constants = constants
        self.save_data = save_data
        self.current_game_screen = None


    def set_game_screen(self, new_state):
        self.state = new_state
        if new_state == "upgrades":
            self.current_game_screen = UpgradeScreen(self, self.save_data)


    def update(self):
        pass

    def draw(self):

        pyxel.text(10, 10, "Game Starts...", 11)

