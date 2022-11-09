from re import L
import tkinter as tk
from gui.widgets.border_box import BorderBox
from gui.widgets.image_box import ImageBox
import gui.widgets.button
from gui.widgets.kanji_view import KanjiView
from PIL import Image, ImageTk
from gui.widgets.button_bar import ButtonBar
import gui.constants as c
from gui.widgets.results_view import ResultsView


class KanjiTestPage(tk.Frame):

    question_count = 0
    correct_count = 0
    current_word = ""
    incorrect_words = []
    
    def __init__(self, root, db, nav):
        super().__init__(root, bg=c.BG, width=800, height=600)
        
        self.question_count = 0
        self.correct_count = 0
        self.current_word = ""
        self.incorrect_words = []
        
        self.db = db
        self.nav = nav
        self.setup()

    def setup(self):
        self.img = ImageTk.PhotoImage(
            Image.open("gui/images/haikei-waves-0.png")
                .resize((800, 600), Image.Resampling.LANCZOS)
        )
        self.bg_img = tk.Label(self, image=self.img, borderwidth=0)
        self.bg_img.place(relx=0.5, rely=0.5, anchor='center')

        self.kanji_view = KanjiView(self)
        self.kanji_view.place(relx=0.15, rely=0.4, anchor='w')

        self.button_bar = ButtonBar(
            self,
            [
                {"image": "gui/images/exit-icon.png", "command": self.go_to_menu},
                {"image": "gui/images/score-icon.png", "command": self.quit_to_results},
                {"image": "gui/images/skip-icon.png", "command": self.skip_question},
                {"image": "gui/images/check-icon.png", "command": self.check_answer}
            ],
            10,
            c.BG
        )
        self.button_bar.place(relx=0.85, rely=0.1, anchor='n')

        self.question_count += 1 
        self.get_new_question()

    def go_to_menu(self):
        self.nav.go_to_route("/")

    def skip_question(self):
        self.get_new_question()

    def quit_to_results(self):
        data = {
            "question_count": self.question_count,
            "correct_count": self.correct_count,
            "incorrect_words": self.incorrect_words
        }
        self.nav.go_to_route_with_data("/results", data)

    def check_answer(self):
        self.ans_img = ImageTk.PhotoImage(
            Image.open("gui/images/haikei-waves-1.png")
                .resize((800, 600), Image.Resampling.LANCZOS)
        )
        self.bg_img.configure(image=self.ans_img)

        self.kanji_view.set_question_count_color("#3D8B9D")
        self.kanji_view.set_question_count("答え")
        self.kanji_view.set_word(self.current_word["kanji"])
        self.kanji_view.set_example("")

        self.button_bar.set_buttons(
            [
                {"image": "gui/images/incorrect-icon.png", "command": self.incorrect_answer},
                {"image": "gui/images/correct-icon.png", "command": self.correct_answer},
            ]
        )

    def reset_ui(self):
        self.bg_img.configure(image=self.img)
        self.button_bar.set_buttons(
            [
                {"image": "gui/images/exit-icon.png", "command": self.go_to_menu},
                {"image": "gui/images/score-icon.png", "command": self.quit_to_results},
                {"image": "gui/images/skip-icon.png", "command": self.skip_question},
                {"image": "gui/images/check-icon.png", "command": self.check_answer}
            ]
        )

    def correct_answer(self):
        self.reset_ui()

        self.correct_count += 1
        self.question_count += 1
        self.get_new_question()

    def incorrect_answer(self):
        self.reset_ui()

        self.incorrect_words.append(self.current_word)
        self.question_count += 1
        self.get_new_question()

    def get_new_question(self):
        new_word = self.db.get_random_word()
        self.current_word = new_word

        self.kanji_view.set_question_count_color("#DD445D")
        self.kanji_view.set_question_count(str(self.question_count))

        self.kanji_view.set_word(self.current_word["yomi"])

        if "example" in self.current_word.keys():
            self.kanji_view.set_example(self.current_word["example"])
        else: self.kanji_view.set_example("")
