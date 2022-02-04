from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.local import LocalProxy

db = None


def get_db():
    uri = "mongodb+srv://m001-student:789654123@sandbox.xzdvv.mongodb.net/test"
    client = MongoClient(uri)
    db = client.sample_movies
    return db


db = LocalProxy(get_db)


def get_movies(filters, page, movies_per_page):
    query = {}
    cursor = db.movies.find(query)
    movies = cursor.skip(page*movies_per_page).limit(movies_per_page)
    total_number = db.movies.count()
    return list(movies),total_number


def get_movie_by_id(id):
    try:
        query = {"_id": ObjectId(id)}
        movie = db.movies.find_one(query)
        return movie
    except Exception as e:
        return {}
