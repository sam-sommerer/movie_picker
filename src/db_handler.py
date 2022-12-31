from typing import Any, Optional

import db


def register_movie(
    actors: list[str], directors: list[str], genres: list[str], movie: dict[str, Any]
) -> None:
    # check if movie is already in db
    movie_exists: bool = db.check_if_movie_exists(
        title=movie["title"], year=movie["year"]
    )

    if not movie_exists:
        db.insert_movie(movie)
    else:
        return

    imdb_id: str = movie["imdb_id"]

    # check if actor(s) already in db
    actors_dict: dict[str, Optional[str]] = {actor: None for actor in actors}
    actors_dict = db.check_if_actor_exists(actors_dict)

    db.insert_actor(actors_dict, imdb_id=imdb_id)

    # check if director(s) already in db
    directors_dict: dict[str, Optional[str]] = {
        director: None for director in directors
    }
    directors_dict = db.check_if_director_exists(directors_dict)

    db.insert_director(directors_dict, imdb_id=imdb_id)

    # check if genre(s) already in db
    genres_dict: dict[str, Optional[str]] = {genre: None for genre in genres}
    genres_dict = db.check_if_genre_exists(genres_dict)

    db.insert_genre(genres_dict, imdb_id=imdb_id)


def get_filtered_movies(
    actors: Optional[list[str]] = None,
    directors: Optional[list[str]] = None,
    genres: Optional[list[str]] = None,
    num: Optional[int] = None,
    random: bool = False,
) -> Optional[list[tuple[str, str, str, str]] | tuple[str, str, str, str]]:
    data: dict[str, list[str] | int | bool] = dict()

    # use locals()/vars() instead?
    if actors is not None:
        data["actors"] = actors
    if directors is not None:
        data["directors"] = directors
    if genres is not None:
        data["genres"] = genres
    if num is not None:
        data["num"] = num
    if random:
        data["random"] = random

    return db.select_from_filter(data)
