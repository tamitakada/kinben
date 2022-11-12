import tkinter as tk
import gui.constants as c

from gui.pages.kanji_test import KanjiTestPage
from gui.pages.results import ResultsPage
from gui.navigator import Navigator
from gui.pages.menu import MenuPage
from gui.pages.search import SearchPage
from database.database import Database
from gui.pages.edit import EditPage

window = tk.Tk()
window.geometry("800x600")
window["background"] = c.BG

db = Database()
nav = Navigator(
    window,
    db,
    {
        "/": MenuPage,
        "/kanji": KanjiTestPage,
        "/results": ResultsPage,
        "/search": SearchPage,
        "/edit": EditPage
    }
)

window.mainloop()
