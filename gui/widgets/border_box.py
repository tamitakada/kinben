from tkinter import *


class BorderBox(Frame):

    def __init__(
        self,
        root,
        border_width,
        width,
        height,
        border_color="white",
        bg_color="#454545"
    ):
        super().__init__(
            root,
            width=width,
            height=height,
            bg=bg_color
        )
        
        outer_border = Frame(
            self,
            width=width,
            height=height,
            bg=border_color
        )
        outer_border.pack()
        
        inner_border = Frame(
            outer_border,
            width=width-(2*border_width),
            height=height-(2*border_width),
            bg=bg_color
        )
        inner_border.place(relx=0.5, rely=0.5, anchor='center')
