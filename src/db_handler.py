from typing import Any, Optional

import db


def register_movie(
    movie: dict[str, Any],
    actors: Optional[list[str]] = None,
    directors: Optional[list[str]] = None,
    genres: Optional[list[str]] = None,
) -> bool:
    # check if movie is already in db
    movie_exists: bool = db.check_if_movie_exists(
        title=movie["title"], year=movie["year"]
    )

    if not movie_exists:
        db.insert_movie(movie)
    else:
        return False

    imdb_id: str = movie["imdb_id"]

    if actors is not None:
        # check if actor(s) already in db
        actors_dict: dict[str, Optional[str]] = {actor: None for actor in actors}
        actors_dict = db.check_if_actor_exists(actors_dict)

        db.insert_actor(actors_dict, imdb_id=imdb_id)

    if directors is not None:
        # check if director(s) already in db
        directors_dict: dict[str, Optional[str]] = {
            director: None for director in directors
        }
        directors_dict = db.check_if_director_exists(directors_dict)

        db.insert_director(directors_dict, imdb_id=imdb_id)

    if genres is not None:
        # check if genre(s) already in db
        genres_dict: dict[str, Optional[str]] = {genre: None for genre in genres}
        genres_dict = db.check_if_genre_exists(genres_dict)

        db.insert_genre(genres_dict, imdb_id=imdb_id)

    return True


def get_filtered_movies(
    actors: Optional[list[str]] = None,
    directors: Optional[list[str]] = None,
    genres: Optional[list[str]] = None,
    num: Optional[int] = None,
    random: bool = True,
) -> Optional[list[tuple[str, int, float, float]]]:
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


def delete_movie(title: str, year: Optional[int] = None) -> bool:
    args = locals()
    data: dict[str, str | int] = dict()

    for arg in args:
        if args[arg] is not None:
            data[arg] = args[arg]

    return db.delete_movie(data)
