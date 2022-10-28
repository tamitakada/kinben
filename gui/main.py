import tkinter as tk
from tkmacosx import Button
from widgets.border_box import BorderBox
from widgets.image_box import ImageBox
import widgets.button
from PIL import Image, ImageTk
from widgets.button_bar import ButtonBar

window = tk.Tk()
window.geometry("800x600")

img = ImageTk.PhotoImage(Image.open("images/haikei-waves-0.png").resize((800, 600), Image.Resampling.LANCZOS))
lbl = tk.Label(window, image=img, borderwidth=0)
lbl.place(relx=0.5, rely=0.5, anchor='center')

frame = tk.Frame(window, bg="#001220")
frame.place(relx=0.3, rely=0.4, anchor='center')
question_count = tk.Label(frame, text="05", fg="#DD445D", bg="#001220", font=("Zen Maru Gothic Bold", 30))
question_count.pack(anchor="w")
word_text = tk.Label(frame, text="コウリョ", bg="#001220", font=("Zen Maru Gothic", 50))
word_text.pack(anchor="w")
example_text = tk.Label(frame, text="状況をコウリョする。", bg="#001220", font=("Zen Maru Gothic", 25))
example_text.pack(anchor="w")

def go_to_main_menu():
    print("main menu")
    
def skip_question():
    print("skipp")

def check_answer():
    print("check")
    
button_bar = ButtonBar(
    window,
    [
        {"image": "images/exit-icon.png", "command": go_to_main_menu},
        {"image": "images/skip-icon.png", "command": skip_question},
        {"image": "images/check-icon.png", "command": check_answer}
    ],
    10,
    "#001220"
)
button_bar.place(relx=0.9, rely=0.1, anchor='n')

#new_img = ImageTk.PhotoImage(Image.open("images/exit-icon.png").resize((30, 30), Image.Resampling.LANCZOS))
#button = widgets.button.Button(window, new_img, "#001220", go_to_main_menu)
#button.place(relx=0.9, rely=0.1, anchor='n')
#
#img_0 = ImageTk.PhotoImage(Image.open("images/skip-icon.png").resize((30, 30), Image.Resampling.LANCZOS))
#button_0 = widgets.button.Button(window, img_0, "#001220", skip_question)
#button_0.place(relx=0.84, rely=0.1, anchor='n')
#
#img_1 = ImageTk.PhotoImage(Image.open("images/check-icon.png").resize((30, 30), Image.Resampling.LANCZOS))
#button_1 = widgets.button.Button(window, img_1, "#001220", check_answer)
#button_1.place(relx=0.78, rely=0.1, anchor='n')

window.mainloop()

