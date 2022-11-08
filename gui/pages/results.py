import tkinter as tk
from gui.widgets.button import Button
from PIL import Image, ImageTk
from gui.widgets.button_bar import ButtonBar
import gui.constants as c


class ResultsPage(tk.Frame):

    question_count = 0
    correct_count = 0
    incorrect_words = []
    current_incorrect_index = 0
    
    def __init__(self, root, db, nav, data):
        super().__init__(root, bg=c.BG, width=800, height=600)
        self.db = db
        self.nav = nav
        
        self.question_count = data["question_count"]
        self.correct_count = data["correct_count"]
        self.incorrect_words = data["incorrect_words"]
        
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
            [
                {"image": "gui/images/exit-icon.png", "command": self.go_to_menu}
            ],
            10,
            c.BG
        )
        self.button_bar.place(relx=0.85, rely=0.1, anchor='n')
        
        heading_lbl = self.question_count_lbl = tk.Label(
            self,
            text="結果",
            fg="#FCAF3C",
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 40)
        )
        heading_lbl.place(relx=0.5, rely=0.2, anchor='n')

        total_count_lbl = tk.Label(
            self,
            text="スコア",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 20)
        )
        total_count_lbl.place(relx=0.35, rely=0.4, anchor='n')

        total_count_data_lbl = tk.Label(
            self,
            text=f"{self.correct_count}/{self.question_count - 1}",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic", 20)
        )
        total_count_data_lbl.place(relx=0.65, rely=0.4, anchor='n')
        
        percentage_lbl = tk.Label(
            self,
            text="正解率",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 20)
        )
        percentage_lbl.place(relx=0.35, rely=0.5, anchor='n')
        
        percentage_data_lbl = tk.Label(
            self,
            text=f"{self.get_correct_percent()}%",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic", 20)
        )
        percentage_data_lbl.place(relx=0.65, rely=0.5, anchor='n')
        
        if len(self.incorrect_words) > 0:
            incorrect_lbl = tk.Label(
                self,
                text="間違えた漢字",
                fg="white",
                bg=c.BG,
                font=("Zen Maru Gothic Bold", 20)
            )
            incorrect_lbl.place(relx=0.386, rely=0.6, anchor='n')
            
            incorrect_data_frame = tk.Frame(self, bg=c.BG)
            incorrect_data_frame.place(relx=0.65, rely=0.6, anchor='n')
            
            if len(self.incorrect_words) > 1:
                self.incorrect_back_img = ImageTk.PhotoImage(
                    Image.open("gui/images/back.png")
                        .resize(
                            (20, 20),
                            Image.Resampling.LANCZOS
                        )
                )
                incorrect_data_back = Button(
                    incorrect_data_frame,
                    self.incorrect_back_img,
                    c.BG,
                    self.display_prev_incorrect_word
                )
                incorrect_data_back.grid(row=0, column=0)
                
                self.incorrect_data_lbl = tk.Label(
                    incorrect_data_frame,
                    text=self.incorrect_words[self.current_incorrect_index]["kanji"],
                    fg="white",
                    bg=c.BG,
                    font=("Zen Maru Gothic", 20)
                )
                self.incorrect_data_lbl.grid(row=0, column=1)
                
                self.incorrect_next_img = ImageTk.PhotoImage(
                    Image.open("gui/images/forward.png")
                        .resize(
                            (20, 20),
                            Image.Resampling.LANCZOS
                        )
                )
                incorrect_data_next = Button(
                    incorrect_data_frame,
                    self.incorrect_next_img,
                    c.BG,
                    self.display_next_incorrect_word
                )
                incorrect_data_next.grid(row=0, column=2)
        
    def get_correct_percent(self):
        if self.question_count - 1 == 0: return 0
        else: return int((float(self.correct_count) / float(self.question_count - 1)) * 100)
        
    def display_prev_incorrect_word(self):
        if self.current_incorrect_index == 0:
            self.current_incorrect_index = len(self.incorrect_words) - 1
        else:
            self.current_incorrect_index -= 1
        self.incorrect_data_lbl.configure(
            text=self.incorrect_words[self.current_incorrect_index]["kanji"]
        )
        
    def display_next_incorrect_word(self):
        if self.current_incorrect_index < len(self.incorrect_words) - 1:
            self.current_incorrect_index += 1
        else:
            self.current_incorrect_index = 0
        self.incorrect_data_lbl.configure(
            text=self.incorrect_words[self.current_incorrect_index]["kanji"]
        )

    def go_to_menu(self):
        self.nav.go_to_route("/menu")
