import os

import customtkinter as ctk
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.dirname(current_dir)


def append_movie_to_frame(scrollable_frame, movie_list):
    for i in range(250):
        scrollable_frame.add_item(
            f'{i + 1}. ' + f'{movie_list[i][2]} ' + f'{movie_list[i][0]}' + f' ({movie_list[i][1]})',
            image=ctk.CTkImage(
                Image.open(os.path.join(root_folder, "test_images", "chat_light.png"))))
