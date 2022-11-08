import tkinter as tk
from gui.widgets.border_box import BorderBox
from gui.widgets.image_box import ImageBox
import gui.widgets.button
from gui.widgets.kanji_view import KanjiView
from PIL import Image, ImageTk
from gui.widgets.button_bar import ButtonBar
import gui.constants as c


class ResultsView(tk.Frame):
    
    def __init__(self, root, correct_count, total_count, incorrect_words):
        super().__init__(root, bg=c.BG)
        
        self.correct_count = correct_count
        self.total_count = total_count
        self.incorrect_words = incorrect_words

        if total_count == 0: self.correct_percent = -1
        else: self.correct_percent = int((float(correct_count) / float(total_count)) * 100)
        
        self.setup()

    def setup(self):
        heading_lbl = self.question_count_lbl = tk.Label(
            self,
            text="結果",
            fg="#DD445D", 
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 40)
        )
        heading_lbl.pack()

        total_count_frame = tk.Frame(self, bg=c.BG)
        total_count_frame.pack(side=tk.TOP, anchor="w")

        total_count_lbl = tk.Label(
            total_count_frame,
            text="スコア",
            fg="white", 
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 14)
        )
        total_count_lbl.pack(side=tk.TOP, anchor="w")

        total_count_data_lbl = tk.Label(
            total_count_frame,
            text=f"{self.correct_count}/{self.total_count}",
            fg="white", 
            bg=c.BG,
            font=("Zen Maru Gothic", 20)
        )
        total_count_data_lbl.pack(side=tk.TOP, anchor="w")

        correct_str = ""
        if self.correct_percent < 0: correct_str = "正解率 | --"
        else: correct_str = f"正解率 | {self.correct_percent}%"
        correct_count_lbl = tk.Label(
            self,
            text=correct_str,
            fg="white", 
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 20)
        )
        correct_count_lbl.pack(anchor="w", pady=10)

        str = ""
        for i in range(len(self.incorrect_words)):
            if i == 0: str = "間違えた漢字 | "
            str += self.incorrect_words[i]["kanji"] + "\n"
            
        incorrect_word_lbl = tk.Label(
            self,
            text=str,
            fg="white", 
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 20)
        )
        incorrect_word_lbl.pack(pady=10)

