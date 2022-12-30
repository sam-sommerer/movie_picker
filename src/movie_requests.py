import requests

from constants import OMDB_API_KEY  # type: ignore

OMDB_URL = "http://www.omdbapi.com"


def get_movie_info(payload: dict[str, str]) -> dict[str, str]:
    payload["apikey"] = OMDB_API_KEY
    r: requests.models.Response = requests.get(OMDB_URL, params=payload)
    return r.json()
