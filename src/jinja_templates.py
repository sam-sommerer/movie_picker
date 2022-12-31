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

CHECK_MOVIE_EXISTS_TEMPLATE = """
    SELECT * FROM movies WHERE MOVIES.TITLE = {{ title }} AND MOVIES.YEAR = {{ year }}
"""

CHECK_ACTOR_EXISTS_TEMPLATE = """
    SELECT * FROM actors WHERE ACTORS.NAME = {{ name }}
"""

CHECK_DIRECTOR_EXISTS_TEMPLATE = """
    SELECT * FROM directors WHERE DIRECTORS.NAME = {{ name }}
"""
