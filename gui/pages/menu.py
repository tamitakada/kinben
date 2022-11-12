import tkinter as tk
import gui.constants as c
from PIL import Image, ImageTk
from gui.widgets.button import TextButton


class MenuPage(tk.Frame):
    def __init__(self, root, db, nav):
        super().__init__(root, bg=c.BG, width=800, height=600)
        self.db = db
        self.nav = nav
        self.setup()
    
    def setup(self):
        self.img = ImageTk.PhotoImage(
            Image.open("gui/images/haikei-blob.png")
                .resize((800, 600), Image.Resampling.LANCZOS)
        )
        self.bg_img = tk.Label(self, image=self.img, borderwidth=0)
        self.bg_img.place(relx=0.5, rely=0.5, anchor='center')
        
        self.logo_img = ImageTk.PhotoImage(
            Image.open("gui/images/kinben-logo.png")
                .resize((200, 160), Image.Resampling.LANCZOS)
        )
        logo = tk.Label(self, image=self.logo_img, borderwidth=0)
        logo.place(relx=0.5, rely=0.1, anchor='n')
        
        button_frame = tk.Frame(self, bg=c.BG)
        button_frame.place(relx=0.5, rely=0.6, anchor='center')
        
        button_infos = [
            ("練習を始める", self.go_to_kanji_test),
            ("データ変更", self.go_to_edit)
        ]
        for info in button_infos:
            b = TextButton(
                button_frame,
                info[0],
                ("Zen Maru Gothic Bold", 20),
                "white",
                c.BG,
                info[1]
            )
            b.pack(side=tk.TOP, anchor="w", pady=15)
        
    def go_to_kanji_test(self):
         self.nav.go_to_route("/kanji")
        
    def go_to_edit(self):
        self.nav.go_to_route("/search")
