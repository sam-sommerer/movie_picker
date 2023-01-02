from rich.console import Console
from rich.table import Table


def print_movie_filter_results(
    results: list[tuple[str, int, float, float]], console: Console
) -> None:
    table = Table(title="Movies :clapper:")

    table.add_column("Year", justify="left", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("IMDB Rating", style="sky_blue3")
    table.add_column(":tomato:", style="indian_red")

    for result in results:
        title, year, imdb_rating, rotten_tomato_rating = result
        table.add_row(str(year), title, str(imdb_rating), str(rotten_tomato_rating))

    console.print(table)
