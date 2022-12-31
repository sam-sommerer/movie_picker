import requests
from typing import Any, Optional

from constants import OMDB_API_KEY  # type: ignore

OMDB_URL = "http://www.omdbapi.com"


def get_movie_info(payload: dict[str, str]) -> dict[str, Any]:
    payload["apikey"] = OMDB_API_KEY
    r: requests.models.Response = requests.get(OMDB_URL, params=payload)
    return r.json()


def extract_db_information(response: dict[str, Any]) -> Any:
    movie_db_attr: dict[str, Any] = dict()

    movie_db_attr["imdb_id"] = response["imdbID"]
    movie_db_attr["title"] = response["Title"]
    movie_db_attr["year"] = int(response["Year"])
    movie_db_attr["rating"] = response["Rated"]
    movie_db_attr["runtime"] = int(response["Runtime"].split()[0])
    movie_db_attr["plot"] = response["Plot"]

    rotten_tomato_rating: Optional[int] = None
    imdb_rating: Optional[float] = None
    for rating in response["Ratings"]:
        if rating.get("Source") is not None:
            if rating.get("Source") == "Rotten Tomatoes":
                rotten_tomato_rating = int(rating.get("Value")[:-1])
            elif rating.get("Source") == "Internet Movie Database":
                imdb_rating = float(rating.get("Value").split("/")[0])
    movie_db_attr["rotten_tomato_rating"] = rotten_tomato_rating
    movie_db_attr["imdb_rating"] = imdb_rating

    actors: str = response["Actors"]
    actors: list[str] = actors.split(", ") if actors is not None else None

    director: str = response["Director"]

    return actors, director, movie_db_attr
