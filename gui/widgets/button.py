import tkmacosx
import tkinter as tk


class Button(tkmacosx.Button):

    def __init__(
        self,
        root,
        img,
        bg_color,
        command
    ):
        self.img = img
        super().__init__(
            root,
            image=img,
            bg=bg_color,
            bd=0,
            width=28,
            height=28,
            activebackground=bg_color,
            activeforeground=bg_color,
            disabledforeground=bg_color,
            disabledbackground=bg_color,
            fg=bg_color,
            highlightbackground=bg_color,
            highlightcolor=bg_color,
            overbackground=bg_color,
            overforeground=bg_color,
            overrelief=tk.FLAT,
            focuscolor=bg_color,
            bordercolor=bg_color,
            highlightthickness = 0,
            relief=tk.FLAT,
            command=command
        )
