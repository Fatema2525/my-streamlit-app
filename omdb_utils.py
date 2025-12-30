# omdb_utils.py
import requests

def get_movie_details(title, api_key):

    url = f"http://omdbapi.com/?t={title}&apikey={api_key}"
    res = requests.get(url).json()
    if res.get("Response") == "True":
        plot = res.get("Plot", "Plot not available")
        poster = res.get("Poster","N/A")
        return plot, poster

    return "Plot not available", "N/A"