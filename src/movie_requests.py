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
    movie_db_attr["year"] = response["Year"]
    movie_db_attr["rating"] = response["Rated"]
    movie_db_attr["runtime"] = response["Runtime"].split()[0]
    movie_db_attr["plot"] = response["Plot"]

    rotten_tomato_rating: Optional[int] = None
    imdb_rating: Optional[float] = None
    for rating in response["Ratings"]:
        if rating.get("Source") is not None:
            if rating.get("Source") == "Rotten Tomatoes":
                rotten_tomato_rating = rating.get("Value")[:-1]
            elif rating.get("Source") == "Internet Movie Database":
                imdb_rating = rating.get("Value").split("/")[0]
    movie_db_attr["rotten_tomato_rating"] = rotten_tomato_rating
    movie_db_attr["imdb_rating"] = imdb_rating

    actors_str: Optional[str] = response["Actors"]
    actors_list: Optional[list[str]] = (
        actors_str.split(", ") if actors_str is not None else None
    )

    directors_str: Optional[str] = response["Director"]
    directors_list: Optional[list[str]] = (
        directors_str.split(", ") if directors_str is not None else None
    )

    genre_str: Optional[str] = response["Genre"]
    genre_list: Optional[list[str]] = (
        genre_str.split(", ") if genre_str is not None else None
    )

    return actors_list, directors_list, genre_list, movie_db_attr
