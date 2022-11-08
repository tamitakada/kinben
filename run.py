import tkinter as tk
import gui.constants as c

from gui.pages.kanji_test import KanjiTestPage
from gui.pages.results import ResultsPage
from gui.navigator import Navigator
from gui.pages.menu import MenuPage
from database.database import Database

window = tk.Tk()
window.geometry("800x600")
window["background"] = c.BG

db = Database()
nav = Navigator(
    window,
    db,
    {
        "/": KanjiTestPage,
        "/menu": MenuPage,
        "/results": ResultsPage
    }
)

window.mainloop()
