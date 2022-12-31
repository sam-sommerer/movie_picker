import sqlite3

from typing import Any
from jinjasql import JinjaSql
from constants import DB_FILEPATH  # type: ignore
from jinja_templates import INSERT_MOVIE_TEMPLATE  # type: ignore


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
