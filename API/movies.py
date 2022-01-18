from flask import Blueprint, request, jsonify
from API.db import get_movie_by_id, get_movies
from flask_cors import CORS

movies_api = Blueprint('movies_api', __name__, url_prefix='/api/movies')

"""
In a production environment, you should only allow cross-origin requests from the 
domain where the front-end application is hosted. 
Refer to the Flask-CORS documentation for more info on this
"""
CORS(movies_api)

# get all movies on the home page


@movies_api.route('/', methods=['GET'])
def api_get_movies():
    movies = get_movies()
    response = {
        "movies": movies
    }
    return jsonify(response), 200


# basic search function
@movies_api.route('/search', methods=['GET'])
def api_search_movie():
    filters = {}
    title = request.args.get('title')
    casts = request.args.getlist('cast')
    genres = request.args.getlist('genre')
    if title:
        filters['title'] = title
    if casts:
        filters['casts'] = casts
    if genres:
        filters['genres'] = genres
    return jsonify(filters), 200


# get movie by ID
@movies_api.route('/id/<id>', methods=['GET'])
def api_get_movie_by_id(id):
    movie = get_movie_by_id(id)
    if movie is None:
        return jsonify({
            "error": "Not found"
        }), 400
    elif movie == {}:
        return jsonify({
            "error": "uncaught general exception"
        }), 400
    else:
        return jsonify(
            {
                "movie": movie,
            }
        ), 200
