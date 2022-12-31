INSERT_MOVIE_TEMPLATE = """
    INSERT INTO movies VALUES (
        {{ imdb_id }}, {{ title }}, {{ year }}, {{ rating }}, {{ runtime }}, {{ plot }}, {{ imdb_rating }},
        {{ rotten_tomato_rating }}
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

INSERT_MOVIE_ACTOR_TEMPLATE = """
    INSERT INTO movie_actors VALUES ({{ imdb_id }}, {{ actor_id }})
"""

INSERT_MOVIE_DIRECTOR_TEMPLATE = """
    INSERT INTO movie_directors VALUES ({{ imdb_id }}, {{ director_id }})
"""

INSERT_MOVIE_GENRE_TEMPLATE = """
    INSERT INTO movie_genres VALUES ({{ imdb_id }}, {{ genre_id }})
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
    SELECT * FROM genres WHERE GENRES.genre_type = {{ genre_type }}
"""
