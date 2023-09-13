import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from utils.randomizer import get_random_movie

from async_tkinter_loop import async_mainloop

# main window
root = tk.Tk()
root.geometry("250x500")
root.title("Movies App")
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create a notebook to add tabs
notebook = ttk.Notebook(root, padding=0)
notebook.grid(row=0, column=0, columnspan=1, rowspan=1, sticky="NESW")

# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Random")

tab1.columnconfigure(0, weight=1)
tab1.rowconfigure(0, weight=1)

# dice image
image = Image.open("assets/dice.png")
new_size = (210, 150)
resized_image = image.resize(new_size, Image.ANTIALIAS)
dice_image = ImageTk.PhotoImage(resized_image)

# image label
image_label = ttk.Label(tab1, image=dice_image)
image_label.grid(row=0, column=0, columnspan=1, rowspan=1, sticky="NESW")

# text label
label = ttk.Label(tab1, text="Get random movie!", wraplength=200, justify="center")
label.grid(row=1, column=0, columnspan=1, rowspan=1)

# random movie button
button = ttk.Button(tab1, text="Go", command=lambda: get_random_movie(image_label, label, button))
button.grid(row=2, column=0, columnspan=1, rowspan=1)

# exit button
exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=3, column=0, columnspan=1, rowspan=1, sticky="NESW")

# Create the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Top250")

async_mainloop(root)
