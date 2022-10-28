import tkinter as tk
import gui.constants as c


class KanjiView(tk.Frame):
    def __init__(self, root):
        super().__init__(root, bg=c.BG)

        self.question_count_lbl = tk.Label(
            self,
            fg="#DD445D", 
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 30)
        )
        self.question_count_lbl.pack(anchor="w")

        self.word_lbl = tk.Label(
            self,
            bg=c.BG, 
            font=("Zen Maru Gothic", 50)
        )
        self.word_lbl.pack(anchor="w")
        
        self.example_lbl = tk.Label(
            self,
            bg=c.BG, 
            font=("Zen Maru Gothic", 25)
        )
        self.example_lbl.pack(anchor="w")

    def set_question_count_color(self, color):
        self.question_count_lbl.configure(fg=color)

    def set_question_count(self, text):
        self.question_count_lbl.configure(text=text)

    def set_word(self, text):
        self.word_lbl.configure(text=text)
    
    def set_example(self, text):
        self.example_lbl.configure(text=text)