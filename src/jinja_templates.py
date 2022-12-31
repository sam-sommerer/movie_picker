INSERT_MOVIE_TEMPLATE = """
    INSERT INTO movies VALUES (
        {{ imdb_id }}, {{ title }}, {{ year }}, {{ rating }}, {{ release_date }}, {{ runtime }}, {{ plot }},
        {{ imdb_rating }}, {{ rotten_tomato_rating }}
    )
"""

CHECK_MOVIE_EXISTS_TEMPLATE = """
    SELECT * FROM MOVIES WHERE MOVIES.TITLE = {{ title }} AND MOVIES.YEAR = {{ year }}
"""

CHECK_ACTOR_EXISTS_TEMPLATE = """
    SELECT * FROM ACTORS WHERE ACTORS.NAME = {{ name }}
"""

CHECK_DIRECTOR_EXISTS_TEMPLATE = """
    SELECT * FROM DIRECTORS WHERE DIRECTORS.NAME = {{ name }}
"""
