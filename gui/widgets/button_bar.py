import tkinter as tk
from PIL import Image, ImageTk

from gui.widgets.button import Button


class ButtonBar(tk.Frame):

    def __init__(
        self,
        root,
        button_info,
        spacing,
        bg_color
    ):
        super().__init__(
            root,
            bg=bg_color
        )
        
        self.spacing = spacing
        self.bg_color = bg_color
        self.buttons = []
        self.set_buttons(button_info)

    def set_buttons(self, button_info):
        for b in self.buttons[::-1]: b.destroy()
    
        for i in range(len(button_info)):
            img = ImageTk.PhotoImage(
                Image.open(button_info[i]["image"])
                    .resize(
                        (30, 30),
                        Image.Resampling.LANCZOS
                    )
            )
        
            b = Button(
                self,
                img,
                self.bg_color,
                button_info[i]["command"]
            )
            b.grid(column=i, row=0, padx=self.spacing)
            
            self.buttons.append(b)
