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
    SELECT actor_id FROM actors WHERE ACTORS.NAME = {{ name }}
"""

CHECK_DIRECTOR_EXISTS_TEMPLATE = """
    SELECT director_id FROM directors WHERE DIRECTORS.NAME = {{ name }}
"""

CHECK_GENRE_EXISTS_TEMPLATE = """
    SELECT genre_id FROM genres WHERE GENRES.genre_type = {{ genre_type }}
"""

FILTER_TEMPLATE = """
    SELECT movies.title, movies.year FROM movies
    INNER JOIN actors USING(imdb_id)
    INNER JOIN directors USING(imdb_id)
    INNER JOIN genres USING(imdb_id)
    {% if actors %}
    WHERE actors.name in {{ actors }}
    {% endif %}
    {% if directors %}
    WHERE directors.name in {{ directors }}
    {% endif %}
    {% if genres %}
    WHERE genre_type in {{ genres }}
    {% endif %}
    GROUP BY movies.imdb_id
    {% if random %}
    ORDER BY RANDOM()
    {% endif %}
    {% if num %}
    LIMIT {{ num }}
    {% endif %}
"""
