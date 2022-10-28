import tkinter as tk
import gui.constants as c
from gui.kanji_test import KanjiTestPage
from gui.navigator import Navigator
from gui.menu import MenuPage
from database.database import Database

window = tk.Tk()
window.geometry("800x600")
window["background"] = c.BG

db = Database()
nav = Navigator(window, db, {"/": KanjiTestPage, "/menu": MenuPage})

window.mainloop()