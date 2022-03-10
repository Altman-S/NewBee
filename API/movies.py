from flask import Blueprint, request, jsonify
from API.db import get_movie_by_imdbID, get_movies, get_movies_by_oid
from flask_cors import CORS
from BM25 import *

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
    genre = request.args.get('Genre')
    year = request.args.get('Year')
    if all:
        filters['all'] = all
    if title:
        filters['title'] = title
    if celes:
        filters['celes'] = celes
    if genre:
        filters['genre'] = genre
    if year:
        filters['year'] = year
    print(filters)
    oid_list = get_oid_from_BM25(filters)
    if oid_list:
        print(len(oid_list))
        movies, total_number = get_movies_by_oid(
            oid_list, page, DEFAULT_MOVIES_PER_PAGE)
        response = {
            "movies": movies,
            "total_number": total_number,
            "current_page": page,
            "response": 'success'
        }
    else:
        response = {
            "response": 'fail'
        }
    return jsonify(response), 200


# get movie by ID
@movies_api.route('/id/<id>', methods=['GET'])
def api_get_movie_by_id(id):
    movie = get_movie_by_imdbID(id)
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


def get_oid_from_BM25(filters):
    print("Seaching")
    oid_list = None
    if 'title' in filters:
        oid_list = search_title(filters['title'])
    if 'celes' in filters:
        oid_list = search_celebrity(filters['celes'])
    if 'year' in filters:
        oid_list = search_year(filters['year'])
    if 'genre' in filters:
        oid_list = search_genre(filters['genre'])
    return oid_list
