from rich.table import Table

from main import console


def print_movie_filter_results(results: list[tuple[str, str, str, str]]) -> None:
    table = Table(title="Movies :clapper:")

    table.add_column("Year", justify="left", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("IMDB Rating", style="sky_blue3")
    table.add_column(":tomato:")

    for result in results:
        title, year, imdb_rating, rotten_tomato_rating = result
        table.add_row(year, title, imdb_rating, rotten_tomato_rating)

    console.print(table)
