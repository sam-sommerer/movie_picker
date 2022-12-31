from typing import Any

import db


def register_movie(
    actors: list[str], directors: list[str], genres: list[str], movie: dict[str, Any]
) -> None:
    # check if movie is already in db
    movie_exists: bool = db.check_if_movie_exists(
        title=movie["title"], year=movie["year"]
    )

    if movie_exists:
        db.insert_movie(movie)
    else:
        return

    # check if actor(s) already in db
    actors_dict: dict[str, bool] = {actor: False for actor in actors}
    actors_dict = db.check_if_actor_exists(actors_dict)

    db.insert_actor(actors_dict)

    # check if director(s) already in db
    directors_dict: dict[str, bool] = {director: False for director in directors}
    directors_dict = db.check_if_director_exists(directors_dict)

    db.insert_director(directors_dict)

    # check if genre(s) already in db
    genres_dict: dict[str, bool] = {genre: False for genre in genres}
    genres_dict = db.check_if_genre_exists(genres_dict)

    db.insert_genre(genres_dict)
