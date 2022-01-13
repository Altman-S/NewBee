from flask import Blueprint, request, jsonify
from API.db import get_movies

movies_api = Blueprint('movies_api',__name__,url_prefix='/movies/api')

@movies_api.route('/',methods=['GET'])
def api_get_movies():
    movies = get_movies()
    response = {
        "movies":movies
    }
    return jsonify(response)