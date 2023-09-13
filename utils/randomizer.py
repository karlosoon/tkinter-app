import httpx
import requests
from PIL import Image, ImageTk

from async_tkinter_loop import async_handler


@async_handler
async def get_random_movie(img, lbl, btn):
    btn.config(state="disabled")
    btn.config(text="Loading...")
    async with httpx.AsyncClient() as client:
        url = "https://api.kinopoisk.dev/v1.3/movie/random"
        headers = {
            "X-API-KEY": "SPX4QTH-PNY4E5J-MZR2RHR-1XNTB82"
        }
        response = await client.get(url, headers=headers)
        poster_url = str(response.json()["poster"]['url'])
        image_data = Image.open(requests.get(poster_url, stream=True).raw)

        image_data = image_data.resize((200, 300), Image.ANTIALIAS)

        # Convert the PIL Image to a PhotoImage for tkinter
        global tk_image  # Keep a global reference to tk_image
        tk_image = ImageTk.PhotoImage(image_data)
        img.config(image=tk_image)

        lbl.config(
            text=f'{round(response.json()["rating"]["kp"], 2)} '
                 + f'{response.json()["name"]}' + f' ({response.json()["year"]})')

    btn.config(state="normal")
    btn.config(text="Go")
