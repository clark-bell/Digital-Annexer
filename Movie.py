import json
import requests


class Movie(object):
    def __init__(self, actors, director, genres, language,
                 plot, poster, production, rated, released,
                 runtime, title, year):
        self.actors = actors
        self.director = director
        self.genres = genres
        self.language = language
        self.plot = plot
        self.poster = poster
        self.production = production
        self.rated = rated
        self.released = released
        self.runtime = runtime
        self.title = title
        self.year = year


def get_movie(title):
    api_key = ""
    url = "http://www.omdbapi.com/"

    payload = {
        "apikey": api_key,
        "t": title
    }

    response = requests.get(url, headers=None, params=payload)

    if response.status_code == 200:
        body = json.loads(response.text)
        return Movie(
            body.get("Actors").split(","),
            body.get("Director"),
            body.get("Genre").split(","),
            body.get("Language"),
            body.get("Plot"),
            body.get("Poster"),
            body.get("Production"),
            body.get("Rated"),
            body.get("Released"),
            body.get("Runtime"),
            body.get("Title"),
            body.get("Year")
        )

    return None

if __name__ == "__main__":
    movie = get_movie("Guardians of the Galaxy Vol. 2")
