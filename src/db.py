import sqlite3

from typing import Any
from jinjasql import JinjaSql
from constants import DB_FILEPATH  # type: ignore
from jinja_templates import (
    INSERT_MOVIE_TEMPLATE,
    CHECK_MOVIE_EXISTS_TEMPLATE,
    CHECK_ACTOR_EXISTS_TEMPLATE,
    CHECK_DIRECTOR_EXISTS_TEMPLATE,
)  # type: ignore


def insert_movie(attr: dict[str, Any]) -> None:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore
    query: str
    bind_params: dict[str, Any]
    query, bind_params = j.prepare_query(INSERT_MOVIE_TEMPLATE, attr)

    cur.execute(query, bind_params)
    con.commit()
    con.close()


def check_if_movie_exists(movie: str, year: str) -> bool:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()
    data = {"movie": movie, "year": year}

    j = JinjaSql(param_style="qmark")  # type: ignore
    query: str
    bind_params: dict[str, Any]
    query, bind_params = j.prepare_query(CHECK_MOVIE_EXISTS_TEMPLATE, data)

    result = cur.execute(query, bind_params)
    con.close()

    return result.fetchone() is not None


def check_if_actor_exists(actor_dict: dict[str, bool]) -> dict[str, bool]:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore

    for actor in actor_dict:
        data = {"name": actor}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(CHECK_ACTOR_EXISTS_TEMPLATE, data)
        result = cur.execute(query, bind_params)

        actor_dict[actor] = result.fetchone() is not None

    con.close()

    return actor_dict


def check_if_director_exists(director_dict: dict[str, bool]) -> dict[str, bool]:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore

    for actor in director_dict:
        data = {"name": actor}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(CHECK_DIRECTOR_EXISTS_TEMPLATE, data)
        result = cur.execute(query, bind_params)

        director_dict[actor] = result.fetchone() is not None

    con.close()

    return director_dict
