import tkinter as tk


def show_movie_description(text):
    notification_window = tk.Toplevel()
    notification_window.geometry("200x100")
    notification_window.title("Notification")

    label = tk.Label(notification_window, text=text)
    label.pack(expand=True)

    button = tk.Button(notification_window, text="Close", command=notification_window.destroy)
    button.pack()
