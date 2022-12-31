import sqlite3
import shortuuid  # type: ignore

from typing import Any, Optional
from jinjasql import JinjaSql  # type: ignore
from constants import DB_FILEPATH  # type: ignore
from jinja_templates import (
    INSERT_MOVIE_TEMPLATE,
    INSERT_ACTOR_TEMPLATE,
    INSERT_DIRECTOR_TEMPLATE,
    INSERT_GENRE_TEMPLATE,
    INSERT_MOVIE_ACTOR_TEMPLATE,
    INSERT_MOVIE_DIRECTOR_TEMPLATE,
    INSERT_MOVIE_GENRE_TEMPLATE,
    CHECK_MOVIE_EXISTS_TEMPLATE,
    CHECK_ACTOR_EXISTS_TEMPLATE,
    CHECK_DIRECTOR_EXISTS_TEMPLATE,
    CHECK_GENRE_EXISTS_TEMPLATE,
)  # type: ignore


def insert_movie(attr: dict[str, str]) -> None:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore
    query: str
    bind_params: dict[str, Any]
    query, bind_params = j.prepare_query(INSERT_MOVIE_TEMPLATE, attr)

    cur.execute(query, bind_params)
    con.commit()
    con.close()


def insert_actor(actors_dict: dict[str, Optional[str]], imdb_id: str) -> None:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore
    for actor in actors_dict:
        actor_exists: bool = actors_dict[actor] is not None

        actor_id: str = shortuuid.uuid() if not actor_exists else actors_dict[actor]

        data: dict[str, str] = {"imdb_id": imdb_id, "actor_id": actor_id}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(INSERT_MOVIE_ACTOR_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

        if actor_exists:
            continue

        data = {"actor_id": actor_id, "name": actor}
        query, bind_params = j.prepare_query(INSERT_ACTOR_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

    con.close()


def insert_director(directors_dict: dict[str, Optional[str]], imdb_id: str) -> None:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore
    for director in directors_dict:
        director_exists: bool = directors_dict[director] is not None

        director_id: str = (
            shortuuid.uuid() if not director_exists else directors_dict[director]
        )

        data: dict[str, str] = {"imdb_id": imdb_id, "director_id": director_id}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(INSERT_MOVIE_DIRECTOR_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

        if director_exists:
            continue

        data = {"director_id": director_id, "name": director}
        query, bind_params = j.prepare_query(INSERT_DIRECTOR_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

    con.close()


def insert_genre(genres_dict: dict[str, Optional[str]], imdb_id: str) -> None:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore
    for genre in genres_dict:
        genre_exists: bool = genres_dict[genre] is not None

        genre_id: str = shortuuid.uuid() if not genre_exists else genres_dict[genre]

        data: dict[str, str] = {"imdb_id": imdb_id, "genre_id": genre_id}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(INSERT_MOVIE_GENRE_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

        if genre_exists:
            continue

        data = {"genre_id": genre_id, "genre_type": genre}
        query, bind_params = j.prepare_query(INSERT_GENRE_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

    con.close()


def check_if_movie_exists(title: str, year: str) -> bool:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()
    data: dict[str, str] = {"title": title, "year": year}

    j = JinjaSql(param_style="qmark")  # type: ignore
    query: str
    bind_params: dict[str, Any]
    query, bind_params = j.prepare_query(CHECK_MOVIE_EXISTS_TEMPLATE, data)

    result = cur.execute(query, bind_params)
    exists = result.fetchone() is not None
    con.close()

    return exists


def check_if_actor_exists(
    actors_dict: dict[str, Optional[str]]
) -> dict[str, Optional[str]]:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore

    for actor in actors_dict:
        data: dict[str, str] = {"name": actor}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(CHECK_ACTOR_EXISTS_TEMPLATE, data)
        result = cur.execute(query, bind_params)

        # actors_dict[actor] = result.fetchone() is not None
        actor_id: str = result.fetchone()

        if actor_id is not None:
            actors_dict[actor] = actor_id[0]

    con.close()

    return actors_dict


def check_if_director_exists(
    directors_dict: dict[str, Optional[str]]
) -> dict[str, Optional[str]]:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore

    for director in directors_dict:
        data: dict[str, str] = {"name": director}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(CHECK_DIRECTOR_EXISTS_TEMPLATE, data)
        result = cur.execute(query, bind_params)

        # directors_dict[actor] = result.fetchone() is not None
        director_id: str = result.fetchone()

        if director_id is not None:
            directors_dict[director] = director_id[0]

    con.close()

    return directors_dict


def check_if_genre_exists(
    genres_dict: dict[str, Optional[str]]
) -> dict[str, Optional[str]]:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore

    for genre in genres_dict:
        data: dict[str, str] = {"genre_type": genre}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(CHECK_GENRE_EXISTS_TEMPLATE, data)
        result = cur.execute(query, bind_params)

        # genres_dict[genre] = result.fetchone() is not None
        genre_id: str = result.fetchone()

        if genre_id is not None:
            genres_dict[genre] = genre_id[0]

    con.close()

    return genres_dict
