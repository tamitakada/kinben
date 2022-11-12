import tkinter as tk
from PIL import Image, ImageTk
from gui.widgets.button import Button


class SearchResultsView(tk.Frame):

    def __init__(
        self,
        root,
        bg_color,
        search_command
    ):
        super().__init__(
            root,
            bg=bg_color
        )
        self.bg_color = bg_color
        self.result_views = []
        self.search_command = search_command

    def show_results(self, results):
        for r in self.result_views[::-1]: r.destroy()
        self.result_views = []

        self.detail_img = ImageTk.PhotoImage(
            Image.open("gui/images/forward.png")
                .resize((32, 32), Image.Resampling.LANCZOS)
        )
        self.bg_img = ImageTk.PhotoImage(
            Image.open("gui/images/result-frame.png")
                .resize((520, 50), Image.Resampling.LANCZOS)
        )
        
        for result in results:
            frame = tk.Frame(self, bg="#FA7268", height=50, width=520)
            frame.pack_propagate(0)
            frame.pack(pady=5)

            bg_label = tk.Label(frame, image=self.bg_img, borderwidth=0)
            bg_label.place(relx=0.5, rely=0.5, anchor='center')
            
            kanji_label = tk.Label(
                frame,
                text=result["kanji"],
                fg="white",
                bg="#973C6B",
                font=("Zen Maru Gothic", 16)
            )
            kanji_label.pack(padx=10, pady=10, anchor="w")
            
            detail_button = Button(
                frame,
                self.detail_img,
                self.bg_color,
                self.search_command
            )
            detail_button.place(relx=0.95, rely=0.5, anchor="center")
            
            self.result_views.append(frame)
