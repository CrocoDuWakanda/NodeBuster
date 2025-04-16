from scripts.utilitaries.constants import COLORS
import pyxel




class UpgradeNode:
    def __init__(self, name, x, y, data, click_action=None):
        self.name = name
        self.x = x
        self.y = y
        self.level = data["level"]
        self.max_level = data["max_level"]
        self.increase = data["increase"]
        self.action = click_action

    def is_hovered(self, mx, my):
        return self.x <= mx <= self.x + 16 and self.y <= my <= self.y + 16

    def click(self):
        if self.level < self.max_level:
            self.level += 1
            if self.action:
                self.action(self.name)

    def draw_tooltip(self, offset_x=0, offset_y=0):
        x = self.x + offset_x
        y = self.y + offset_y
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        if self.is_hovered(mx - offset_x, my - offset_y):
            text = f"{self.name} ({self.level}/{self.max_level})"
            width = len(text) * 4 + 4
            pyxel.rect(mx, my - 10, width, 10, 1)
            pyxel.text(mx + 2, my - 8, text, 7)

    def draw(self, offset_x=0, offset_y=0):
        color = COLORS["red"] if self.level < self.max_level else COLORS["yellow"]
        pyxel.rect(self.x+offset_x, self.y+offset_y, 16, 16, color)
        pyxel.text(self.x + 2, self.y + 6, str(self.level), 0)