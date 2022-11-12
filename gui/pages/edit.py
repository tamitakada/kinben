import tkinter as tk
from gui.widgets.button import TextButton
from PIL import Image, ImageTk
from gui.widgets.button_bar import ButtonBar
import gui.constants as c
from gui.widgets.placeholder_entry import PlaceholderEntry


class EditPage(tk.Frame):
    
    def __init__(self, root, db, nav, data):
        super().__init__(root, bg=c.BG, width=800, height=600)
        self.db = db
        self.nav = nav
        
        self.word = data["word"]
        
        self.setup()

    def setup(self):
        self.img = ImageTk.PhotoImage(
            Image.open("gui/images/haikei-waves-2.png")
                .resize((800, 600), Image.Resampling.LANCZOS)
        )
        self.bg_img = tk.Label(self, image=self.img, borderwidth=0)
        self.bg_img.place(relx=0.5, rely=0.5, anchor='center')
        
        self.button_bar = ButtonBar(
            self,
            [{"image": "gui/images/back.png", "command": self.go_back_to_search}],
            10,
            c.BG
        )
        self.button_bar.place(relx=0.15, rely=0.1, anchor='n')
        
        entry_frame = tk.Frame(self, bg=c.BG)
        entry_frame.place(relx=0.5, rely=0.5, anchor='center')

        kanji_lbl = tk.Label(
            entry_frame,
            text="単語",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic", 18)
        )
        kanji_lbl.pack(anchor="w")

        self.kanji_entry = tk.Entry(
            entry_frame,
            font=("Zen Maru Gothic", 50),
            width=22,
            bg=c.BG,
            borderwidth=0,
            fg="white",
            insertborderwidth=0,
            selectborderwidth=0
        )
        self.kanji_entry.insert(0, self.word["kanji"])
        self.kanji_entry.pack(pady=5)

        yomi_lbl = tk.Label(
            entry_frame,
            text="読み",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic", 18)
        )
        yomi_lbl.pack(side=tk.TOP, anchor="w")

        self.yomi_entry = tk.Entry(
            entry_frame,
            font=("Zen Maru Gothic", 30),
            width=36,
            bg=c.BG,
            borderwidth=0,
            fg="white",
            insertborderwidth=0,
            selectborderwidth=0
        )
        self.yomi_entry.insert(0, self.word["yomi"])
        self.yomi_entry.pack(pady=5)

        example_lbl = tk.Label(
            entry_frame,
            text="例文",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic", 18)
        )
        example_lbl.pack(anchor="w")
        
        self.example_entry = tk.Entry(
            entry_frame,
            font=("Zen Maru Gothic", 16),
            width=72,
            bg=c.BG,
            borderwidth=0,
            fg="white",
            insertborderwidth=0,
            selectborderwidth=0
        )
        self.example_entry.pack(pady=5)

        if "example" in self.word.keys(): 
            self.example_entry.insert(0, self.word["example"])

        save_button = TextButton(
            self,
            "保存",
            ("Zen Maru Gothic", 18),
            "white",
            c.BG,
            self.save_edits
        )
        save_button.place(relx=0.5, rely=0.8, anchor='center')

        self.save_label = tk.Label(
            self,
            bg=c.BG,
            font=("Zen Maru Gothic", 18)
        )
        self.save_label.place(relx=0.5, rely=0.87, anchor='center')

    def save_edits(self):
        result = self.db.edit_word(
            self.word["id"], 
            yomi=self.yomi_entry.get(), 
            kanji=self.kanji_entry.get(), 
            example=self.example_entry.get()
        )
        if result == 1:
            self.save_label.configure(
                text="保存完了",
                fg="green"
            )
        else:
            self.save_label.configure(
                text="保存失敗",
                fg="red"
            )

    def go_back_to_search(self):
        self.nav.go_to_route("/search")
