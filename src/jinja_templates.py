INSERT_MOVIE_TEMPLATE = """
    INSERT INTO movies VALUES (
        {{ imdb_id }}, {{ title }}, {{ year }}
        {% if rating %}
        , {{ rating }}
        {% endif %}
        {% if release_date %}
        , {{ release_date }}
        {% endif %}
        {% if runtime %}
        , {{ runtime }}
        {% endif %}
        {% if plot %}
        , {{ plot }}
        {% endif %}
        {% if imdb_rating %}
        , {{ imdb_rating }}
        {% endif %}
        {% if rotten_tomato_rating %}
        , {{ rotten_tomato_rating }}
        {% endif %}
    )
"""
