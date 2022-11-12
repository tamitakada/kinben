import tkinter as tk
from gui.widgets.button import Button
from PIL import Image, ImageTk
from gui.widgets.button_bar import ButtonBar
import gui.constants as c
from gui.widgets.search_results_view import SearchResultsView


class SearchPage(tk.Frame):
    
    def __init__(self, root, db, nav):
        super().__init__(root, bg=c.BG, width=800, height=600)

        self.db = db
        self.nav = nav
        
        self.results = []
        self.current_page = 0
        self.page_count = 0
        
        self.setup()

    def setup(self):
        self.img = ImageTk.PhotoImage(
            Image.open("gui/images/haikei-waves-3.png")
                .resize((800, 600), Image.Resampling.LANCZOS)
        )
        self.bg_img = tk.Label(self, image=self.img, borderwidth=0)
        self.bg_img.place(relx=0.5, rely=0.5, anchor='center')
        
        heading_lbl = tk.Label(
            self,
            text="漢字・単語検索",
            fg="#DD445D",
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 40)
        )
        heading_lbl.place(relx=0.5, rely=0.15, anchor='n')
        
        search_frame = tk.Frame(self, bg=c.BG, borderwidth=0)
        search_frame.place(relx=0.5, rely=0.3, anchor='n')
        
        self.search_img = ImageTk.PhotoImage(
            Image.open("gui/images/search-icon.png")
                .resize((30, 30), Image.Resampling.LANCZOS)
        )
        search_button = Button(
            search_frame,
            self.search_img,
            c.BG,
            self.search_for_word
        )
        search_button.grid(column=0,row=0)
        
        self.search_entry = tk.Entry(
            search_frame,
            font=("Zen Maru Gothic", 16),
            width=60,
            bg=c.BG,
            borderwidth=0,
            fg="white",
            insertborderwidth=0,
            selectborderwidth=0
        )
        self.search_entry.grid(column=1,row=0, padx=10)
        
        self.results_view = SearchResultsView(self, c.BG, self.go_to_edit)
        self.results_view.place(relx=0.5, rely=0.38, anchor='n')
        
        self.back_img = ImageTk.PhotoImage(
            Image.open("gui/images/back.png")
                .resize((30, 30), Image.Resampling.LANCZOS)
        )
        self.back_button = Button(
            self,
            self.back_img,
            c.BG,
            self.go_to_prev_page
        )
        
        self.next_img = ImageTk.PhotoImage(
            Image.open("gui/images/forward.png")
                .resize((30, 30), Image.Resampling.LANCZOS)
        )
        self.next_button = Button(
            self,
            self.next_img,
            c.BG,
            self.go_to_next_page
        )

        self.none_frame = tk.Frame(self, bg=c.BG)

        none_lbl = tk.Label(
            self.none_frame,
            text=f"ヽ(◉ロ◉)ﾉ",
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic Bold", 36)
        )
        none_lbl.pack()

        self.none_sub = tk.Label(
            self.none_frame,
            fg="white",
            bg=c.BG,
            font=("Zen Maru Gothic", 20)
        )
        self.none_sub.pack(pady=10)
        
        self.button_bar = ButtonBar(
            self,
            [{"image": "gui/images/exit-icon.png", "command": self.go_to_menu}],
            10,
            c.BG
        )
        self.button_bar.place(relx=0.85, rely=0.1, anchor='n')
        
    def go_to_menu(self):
        self.nav.go_to_route("/")
        
    def search_for_word(self):
        query = self.search_entry.get()
        self.results = self.db.search_for_word(query)
        
        self.current_page = 0
        self.page_count = int(len(self.results) / 5) + 1

        if len(self.results) == 0:
            self.none_sub.configure(text=f"「{query}」\nに該当する項目は見つかりませんでした")
            self.none_frame.place(relx=0.5, rely=0.6, anchor='center')
            self.back_button.place_forget()
            self.next_button.place_forget()
        elif self.page_count > 2:
            self.back_button.place(relx=0.175, rely=0.9)
            self.next_button.place(relx=0.79, rely=0.9)
            self.none_frame.place_forget()
        else:
            self.back_button.place_forget()
            self.next_button.place_forget()
            self.none_frame.place_forget()
        
        self.results_view.show_results(self.results[0:5])
        
    def go_to_prev_page(self):
        if self.current_page == 0:
            self.current_page = self.page_count - 1
        else: self.current_page -= 1
        self.results_view.show_results(
            self.results[
                (5 * self.current_page):(5 * self.current_page + 5)
            ]
        )
        
    def go_to_next_page(self):
        if self.current_page == self.page_count - 1:
            self.current_page = 0
        else: self.current_page += 1
        self.results_view.show_results(
            self.results[
                (5 * self.current_page):(5 * self.current_page + 5)
            ]
        )
    
    def go_to_edit(self, word):
        self.nav.go_to_route_with_data(
            "/edit",
            {"word": word}
        )
