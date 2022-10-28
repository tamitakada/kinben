from tkinter import *
from PIL import Image, ImageTk


class ImageBox(Label):
    def __init__(
        self,
        root,
        width,
        height,
        image
    ):
        img = ImageTk.PhotoImage(Image.open(image).resize((width, height), Image.Resampling.LANCZOS))
        super().__init__(root, image=img, borderwidth=0)
