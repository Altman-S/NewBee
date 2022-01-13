from pymongo import MongoClient

db = None

def get_db():
    uri = "mongodb+srv://m001-student:789654123@sandbox.xzdvv.mongodb.net/test"
    client = MongoClient(uri)
    db = client.sample_movies
    return db

db = get_db()

def get_movies():
    query = {}
    cursor = db.movies.find(query)
    return list(cursor)
    