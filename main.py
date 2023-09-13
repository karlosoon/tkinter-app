import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from utils.randomizer import get_random_movie

from async_tkinter_loop import async_mainloop

# main window
root = tk.Tk()
root.geometry("250x380")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# dice image
image = Image.open("assets/dice.png")
new_size = (210, 150)
resized_image = image.resize(new_size, Image.ANTIALIAS)
dice_image = ImageTk.PhotoImage(resized_image)

# image label
image = ttk.Label(root, image=dice_image)
image.grid(row=0, column=0, columnspan=1, rowspan=1)

# text label
label = ttk.Label(root, text="Get random movie!", wraplength=200, justify="center")
label.grid(row=1, column=0, columnspan=1, rowspan=1)

# random movie button
button = ttk.Button(root, text="Go",
                    command=lambda: [get_random_movie(image, label, button)])
button.grid(row=2, column=0, columnspan=1, rowspan=1)

# exit button
exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=3, column=0, columnspan=1, rowspan=1)

async_mainloop(root)
