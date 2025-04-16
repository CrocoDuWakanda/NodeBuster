from scripts.utilitaries.saves_manager import load_upgrades, update_stats
from scripts.screen.upgrade_node import UpgradeNode
import pyxel



class UpgradeScreen:
    def __init__(self, app, save_data):
        self.app = app
        self.save_data = save_data
        self.upgrades = load_upgrades()
        self.nodes = []
        self.init_nodes()

    def init_nodes(self):
        spacing = 24
        start_x = 30
        start_y = 30
        for i, (name, data) in enumerate(self.upgrades.items()):
            self.nodes.append(UpgradeNode(name, start_x + i * spacing, start_y, data, self.level_up))

    def level_up(self, name):
        self.upgrades[name]["level"] += 1
        update_stats(self.save_data)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            for node in self.nodes:
                if node.is_hovered(mx, my):
                    node.click()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, "Skill Tree", 7)
        for node in self.nodes:
            node.draw()
