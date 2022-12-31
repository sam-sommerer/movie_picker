import movie_requests
import db_handler

if __name__ == "__main__":
    payload = {"t": "killing them softly"}

    response_json = movie_requests.get_movie_info(payload=payload)
    (
        actors_list,
        directors_list,
        genre_list,
        movie_db_attr,
    ) = movie_requests.extract_db_information(response_json)

    db_handler.register_movie(actors_list, directors_list, genre_list, movie_db_attr)
