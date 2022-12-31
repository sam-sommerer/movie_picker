import sqlite3
import shortuuid

from typing import Any
from jinjasql import JinjaSql
from constants import DB_FILEPATH  # type: ignore
from jinja_templates import (
    INSERT_MOVIE_TEMPLATE,
    INSERT_ACTOR_TEMPLATE,
    INSERT_DIRECTOR_TEMPLATE,
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


def insert_actor(actors_dict: dict[str, bool]) -> None:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore
    for actor in actors_dict:
        if not actors_dict[actor]:
            continue

        data = {"actor_id": shortuuid.uuid(), "name": actor}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(INSERT_ACTOR_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

    con.close()


def insert_director(directors_dict: dict[str, bool]) -> None:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore
    for director in directors_dict:
        if not directors_dict[director]:
            continue

        data = {"director_id": shortuuid.uuid(), "name": director}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(INSERT_DIRECTOR_TEMPLATE, data)

        cur.execute(query, bind_params)
        con.commit()

    con.close()


def check_if_movie_exists(title: str, year: str) -> bool:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()
    data = {"movie": title, "year": year}

    j = JinjaSql(param_style="qmark")  # type: ignore
    query: str
    bind_params: dict[str, Any]
    query, bind_params = j.prepare_query(CHECK_MOVIE_EXISTS_TEMPLATE, data)

    result = cur.execute(query, bind_params)
    con.close()

    return result.fetchone() is not None


def check_if_actor_exists(actors_dict: dict[str, bool]) -> dict[str, bool]:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore

    for actor in actors_dict:
        data = {"name": actor}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(CHECK_ACTOR_EXISTS_TEMPLATE, data)
        result = cur.execute(query, bind_params)

        actors_dict[actor] = result.fetchone() is not None

    con.close()

    return actors_dict


def check_if_director_exists(directors_dict: dict[str, bool]) -> dict[str, bool]:
    con: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
    cur: sqlite3.Cursor = con.cursor()

    j = JinjaSql(param_style="qmark")  # type: ignore

    for actor in directors_dict:
        data = {"name": actor}
        query: str
        bind_params: dict[str, Any]
        query, bind_params = j.prepare_query(CHECK_DIRECTOR_EXISTS_TEMPLATE, data)
        result = cur.execute(query, bind_params)

        directors_dict[actor] = result.fetchone() is not None

    con.close()

    return directors_dict