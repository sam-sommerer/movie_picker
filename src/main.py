import typer
from rich.console import Console
from typing import Any, Optional

from movie_requests import get_movie_info, extract_db_information
from db_handler import register_movie, get_filtered_movies, delete_movie
from utils import get_formatted_list_from_string
from rich_utils import print_movie_filter_results

app = typer.Typer()
console = Console()


@app.command()
def register(title: str, year: Optional[str] = typer.Argument(None)):
    payload: dict[str, str]
    if year is not None:
        payload = {"t": title, "y": year}
    else:
        payload = {"t": title}

    movie_response: dict[str, Any] = get_movie_info(payload=payload)

    actors_list: Optional[list[str]]
    directors_list: Optional[list[str]]
    genre_list: Optional[list[str]]
    movie_db_attr: dict[str, Any]
    actors_list, directors_list, genre_list, movie_db_attr = extract_db_information(
        movie_response
    )

    if register_movie(
        movie=movie_db_attr,
        actors=actors_list,
        directors=directors_list,
        genres=genre_list,
    ):
        console.print("[green]Registration success![/green] :sparkles: :confetti_ball:")
    else:
        console.print(
            "[bold red]Registration failed![/bold red] :skull: Maybe movie is already registered? :thinking_face:"
        )


@app.command()
def delete(title: str, year: Optional[int] = typer.Argument(None)):
    if delete_movie(title=title, year=year):
        console.print("[green]Movie deleted![/green] :pray:")
    else:
        console.print(
            "[bold red]Deletion failed![/bold red] :flushed: Maybe try specifying the year? :tear-off_calendar:"
        )


@app.command()
def getmovie(
    actors: Optional[str] = typer.Argument(None),
    directors: Optional[str] = typer.Argument(None),
    genres: Optional[str] = typer.Argument(None),
    num: Optional[int] = typer.Argument(1),
    random: bool = typer.Argument(True),
):
    actors_list: list[str] = (
        get_formatted_list_from_string(actors) if actors is not None else None
    )
    directors_list: list[str] = (
        get_formatted_list_from_string(directors) if directors is not None else None
    )
    genres_list: list[str] = (
        get_formatted_list_from_string(genres) if genres is not None else None
    )
    results = get_filtered_movies(
        actors=actors_list,
        directors=directors_list,
        genres=genres_list,
        num=num,
        random=random,
    )
    print_movie_filter_results(results)


if __name__ == "__main__":
    app()
