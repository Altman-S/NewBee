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


def get_movies():
    query = {}
    cursor = db.movies.find(query)
    return list(cursor)


def get_movie_by_id(id):
    try:
        query = {"_id": ObjectId(id)}
        movie = db.movies.find_one(query)
        return movie
    except Exception as e:
        return {}
