from scripts.utilitaries.constants import WIDTH,HEIGHT
from scripts.utilitaries.button import Button
from scripts.utilitaries.saves_manager import load_saves,save_to_file,load_default_save
from scripts.screen.game_screen import GameScreen
from scripts.screen.menu_screen import MenuScreen
import pyxel
import json
import os




class App:
    def __init__(self):
        self.state = None
        self.current_screen = None

        pyxel.init(WIDTH, HEIGHT, title="NodeBuster", display_scale=5)
        pyxel.mouse(True)

        self.set_state("menu")
        pyxel.run(self.update, self.draw)


    def set_state(self, new_state, save_data=None):
        self.state = new_state
        if new_state == "menu":
            self.current_screen = MenuScreen(self, {"width":WIDTH,"height":HEIGHT}, load_saves())

        elif new_state == "game":
            self.current_screen = GameScreen(self, {"width":WIDTH,"height":HEIGHT}, save_data)


    def start_game(self, slot_index):
        saves = load_saves()
        data = saves[slot_index]
        if data is None:
            data = load_default_save()
            save_to_file(slot_index, data)

        self.set_state("game", save_data=data)


    def update(self):
        if self.current_screen:
            self.current_screen.update()
        elif self.state == "save_select":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                mx, my = pyxel.mouse_x, pyxel.mouse_y
                for btn in self.save_buttons:
                    if btn.is_hovered(mx, my):
                        btn.click()

    def draw(self):
        pyxel.cls(0)

        if self.current_screen:
            self.current_screen.draw()

App()
