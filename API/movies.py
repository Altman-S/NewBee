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
DEFAULT_MOVIES_PER_PAGE = 20


@movies_api.route('/', methods=['GET'])
def api_get_movies():
    page = int(request.args.get('page', 1))
    print(page)
    movies, total_number = get_movies(
        None, page=page, movies_per_page=DEFAULT_MOVIES_PER_PAGE)
    response = {
        "movies": movies,
        'total_number': total_number,
        'current_page': page
    }
    return jsonify(response), 200


# basic search function
@movies_api.route('/search', methods=['GET'])
def api_search_movie():
    filters = {}
    page = int(request.args.get('page', 1))
    all = request.args.get('All')
    title = request.args.get('Title')
    celes = request.args.get('Celebrity')
    genre = request.args.getlist('Genre')
    if title:
        filters['title'] = title
    if celes:
        filters['celes'] = celes
    if genre:
        filters['genre'] = genre
    movies, total_number = get_movies(
        filters, page=page, movies_per_page=DEFAULT_MOVIES_PER_PAGE)
    response = {
        "movies": movies,
        'total_number': total_number,
        'current_page': page
    }
    return jsonify(response), 200


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
