import pyxel



class Button:
    def __init__(self, x, y, w, h, color, text=None, img=None, action=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        colors = {"black" : 0,
                  "dark_blue" : 1,
                  "heavy_blue" : 5,
                  "blue" : 12,
                  "light_blue" : 6,
                  "blue_green" : 3,
                  "light_blue_green" : 11,
                  "purple" : 2,
                  "red" : 8,
                  "pink" : 14,
                  "brown" : 4,
                  "gray" : 13,
                  "orange" : 9,
                  "beige" : 15,
                  "white" : 7,
                  "yellow" : 10}
        self.color = colors[color]
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