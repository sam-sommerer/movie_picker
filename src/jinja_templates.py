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

DELETE_TEMPLATE = """
    DELETE FROM movies WHERE title = {{ title }} AND year = {{ year }}
"""

FILTER_TEMPLATE = """
    SELECT movies.title, movies.year, movies.imdb_rating, movies.rotten_tomato_rating FROM movies
    {% if actors %}
        INNER JOIN movie_actors USING(imdb_id)
        INNER JOIN actors USING(actor_id)
    {% endif %}
    {% if directors %}
        INNER JOIN movie_directors USING(imdb_id)
        INNER JOIN directors USING(director_id)
    {% endif %}
    {% if genres %}
        INNER JOIN movie_genres USING(imdb_id)
        INNER JOIN genres USING(genre_id)
    {% endif %}
    {% if actors %}
        WHERE actors.name in {{ actors | inclause }}
    {% endif %}
    {% if directors %}
        {% if actors %}
            AND
        {% else %}
            WHERE
        {% endif %}
        directors.name in {{ directors | inclause }}
    {% endif %}
    {% if genres %}
        {% if actors or directors %}
            AND
        {% else %}
            WHERE
        {% endif %}
        genre_type in {{ genres | inclause }}
    {% endif %}
        GROUP BY movies.imdb_id
    {% if random %}
        ORDER BY RANDOM()
    {% endif %}
    {% if num %}
        LIMIT {{ num }}
    {% endif %}
"""
