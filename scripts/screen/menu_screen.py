from scripts.utilitaries.button import Button
from scripts.utilitaries.saves_manager import delete_save, load_saves
import pyxel



class MenuScreen:
    def __init__(self, app, constants, saves_data):
        self.app = app
        self.saves_data = saves_data

        pyxel.load("ressources.pyxres")

        self.constants = constants
        self.offset = 40
        self.btn_width = 180
        self.btn_height = 30
        self.x_btn = (constants["width"]/2)-self.btn_width/2
        self.y_btn = constants["height"]//5
        self.buttons = [
            Button(self.x_btn, self.y_btn + self.offset*1, self.btn_width, self.btn_height, "heavy_blue", img=(self.x_btn+50,self.y_btn+self.offset*1.15,2,0,0,79,23,0), action=self.to_save_select),
            Button(self.x_btn, self.y_btn + self.offset*2, self.btn_width, self.btn_height, "heavy_blue", img=(self.x_btn+35,self.y_btn+self.offset*2.10,2,80,0,114,23,0), action=self.settings),
            Button(self.x_btn, self.y_btn + self.offset*3, self.btn_width, self.btn_height, "heavy_blue", img=(self.x_btn+60,self.y_btn+self.offset*3.10,2,200,0,55,23,0), action=pyxel.quit)
        ]
        self.save_buttons = []

    def to_save_select(self):
        self.app.set_state("save_select")
        self.save_buttons = []
        for i in range(3):
            data = self.saves_data[i]
            label = "Continue" if data else "New Game"
            self.save_buttons.append(Button(int(self.constants["width"]/2)-self.btn_width/2, 
                                            self.constants["width"]//6 + self.offset*i, 
                                            self.btn_width, self.btn_height,
                                            "heavy_blue",
                                            text=f"{label} - Slot {i+1}", 
                                            action=lambda i=i: self.app.start_game(i)))
            
            self.save_buttons.append(Button(int(self.constants["width"]/2) + self.btn_width//2,
                                            self.constants["height"]//6 + self.offset*i + 30,
                                            20,
                                            self.btn_height,
                                            "pink",
                                            text="X",
                                            action=lambda i=i: self.delete_slot(i)))

    def settings(self):
        print("Settings not implemented.")

    def delete_slot(self, i):
        delete_save(i)
        self.saves_data =  load_saves()
        self.to_save_select()
        
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            if self.app.state == "menu":
                for btn in self.buttons:
                    if btn.is_hovered(mx, my):
                        btn.click()
            elif self.app.state == "save_select":
                for btn in self.save_buttons:
                    if btn.is_hovered(mx, my):
                        btn.click()

    def draw(self):
        pyxel.text(60, 10, "NodeBuster", 7)
        if self.app.state == "menu" :
            for btn in self.buttons:
                btn.draw()
        elif self.app.state == "save_select":
            pyxel.text(50, 10, "Choose a Save", 7)
            for btn in self.save_buttons:
                btn.draw()