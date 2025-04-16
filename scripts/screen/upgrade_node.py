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

    def draw(self):
        color = "red" if self.level < self.max_level else "yellow"
        pyxel.rect(self.x, self.y, 16, 16, color)
        pyxel.text(self.x + 2, self.y + 6, str(self.level), 0)