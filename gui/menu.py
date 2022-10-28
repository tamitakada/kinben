import tkinter as tk
import gui.constants as c


class MenuPage(tk.Frame):
    def __init__(self, root, db, nav):
        super().__init__(root, bg=c.BG, width=800, height=600)
        self.db = db
        self.nav = nav
        # self.setup()