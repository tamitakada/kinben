import tkinter as tk

class PlaceholderEntry(tk.Entry):
    def __init__(self, root, placeholder):
        super().__init__(root)

        self.showing_placeholder = True
        self.placeholder = placeholder

        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        self.insert_placeholder()

    def insert_placeholder(self):
        self.insert(0, self.placeholder)

    def focus_in(self, *args):
        if self.showing_placeholder: self.delete('0', 'end')

    def focus_out(self, *args):
        if not self.get():
            self.showing_placeholder = True
            self.insert_placeholder()
        else: self.showing_placeholder = False