INSERT_MOVIE_TEMPLATE = """
    INSERT INTO movies VALUES (
        {{ imdb_id }}, {{ title }}, {{ year }}, {{ rating }}, {{ release_date }}, {{ runtime }}, {{ plot }},
        {{ imdb_rating }}, {{ rotten_tomato_rating }}
    )
"""

INSERT_ACTOR_TEMPLATE = """
    INSERT INTO actors VALUES ({{ actor_id }}, {{ name }})
"""

INSERT_DIRECTOR_TEMPLATE = """
    INSERT INTO directors VALUES ({{ director_id }}, {{ name }})
"""

INSERT_GENRE_TEMPLATE = """
    INSERT INTO genres VALUES ({{ genre_id }}, {{ genre_type }})
"""

CHECK_MOVIE_EXISTS_TEMPLATE = """
    SELECT * FROM movies WHERE MOVIES.TITLE = {{ title }} AND MOVIES.YEAR = {{ year }}
"""

CHECK_ACTOR_EXISTS_TEMPLATE = """
    SELECT * FROM actors WHERE ACTORS.NAME = {{ name }}
"""

CHECK_DIRECTOR_EXISTS_TEMPLATE = """
    SELECT * FROM directors WHERE DIRECTORS.NAME = {{ name }}
"""

CHECK_GENRE_EXISTS_TEMPLATE = """
    SELECT * FROM genres WHERE GENRE.genre_type = {{ genre_type }}
"""
