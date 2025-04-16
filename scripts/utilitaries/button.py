from scripts.utilitaries.constants import COLORS
import pyxel



class Button:
    def __init__(self, x, y, w, h, color, text=None, img=None, action=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = COLORS[color]
        self.text = text
        self.img = img
        self.action = action



    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)
        if self.text:
            pyxel.text(self.x + 2, self.y + 2, self.text, 7)
        elif self.img:
            pyxel.blt(*self.img)

    def is_hovered(self, mx, my):
        return self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h

    def click(self):
        if self.action:
            self.action()