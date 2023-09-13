import requests
from PIL import Image, ImageTk

name, year, rating, poster_url, description = '', '', '', '', ''
movie_list = []


def get_top_movies():
    url = "https://api.kinopoisk.dev/v1.3/movie?sortField=rating.imdb&sortType=-1&page=1&limit=250&top250=%21null" \
          "&isSeries=false"
    headers = {
        "X-API-KEY": "SPX4QTH-PNY4E5J-MZR2RHR-1XNTB82"
    }
    response = requests.get(url, headers=headers)

    for doc in response.json()['docs']:
        name = doc["name"]
        year = doc["year"]
        rating = doc["rating"]["kp"]
        poster_url = doc["poster"]["url"]
        description = doc["shortDescription"]
        movie_list.append([name, year, rating, poster_url, description])
