from scripts.utilitaries.saves_manager import load_upgrades, update_stats
from scripts.screen.upgrade_node import UpgradeNode
import pyxel


class UpgradeScreen:
    def __init__(self, app, save_data):
        self.app = app
        self.save_data = save_data
        self.upgrades = load_upgrades()
        self.nodes = []
        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False
        self.last_mouse = (0, 0)
        self.init_nodes()

        self.canvas_width = 500
        self.canvas_height = 300

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
        mx, my = pyxel.mouse_x, pyxel.mouse_y

        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            self.dragging = True
            self.last_mouse = (mx, my)
        if not pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            self.dragging = False
        # Mise à jour de l’offset caméra
        if self.dragging:
            dx = mx - self.last_mouse[0]
            dy = my - self.last_mouse[1]
            self.offset_x -= dx
            self.offset_y -= dy
            self.last_mouse = (mx, my)
            # (Optionnel) Limiter le déplacement à l’intérieur du canvas
            self.offset_x = max(0, min(self.offset_x, self.canvas_width - pyxel.width))
            self.offset_y = max(0, min(self.offset_y, self.canvas_height - pyxel.height))

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            for node in self.nodes:
                if node.is_hovered(mx - self.offset_x, my - self.offset_y):
                    print("node clicked")
                    node.click()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, "Skill Tree", 7)
        for node in self.nodes:
            node.draw(self.offset_x, self.offset_y)
        for node in self.nodes:
            node.draw_tooltip(self.offset_x, self.offset_y)
