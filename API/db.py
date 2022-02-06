from pymongo import MongoClient, DESCENDING, ASCENDING
from bson.objectid import ObjectId
from werkzeug.local import LocalProxy

db = None


def get_db():
    uri = "mongodb+srv://m001-student:789654123@sandbox.xzdvv.mongodb.net/test"
    client = MongoClient(uri)
    db = client.sample_movies
    return db


db = LocalProxy(get_db)


def build_query_sort_project(filters):
    query = {}
    sort = [("imdbRating", DESCENDING), ("_id", ASCENDING)]
    project = None
    # print(filters)
    if filters:
        if "title" in filters:
            query = {"$text": {"$search": filters["title"]}}
            meta_score = {"$meta": "textScore"}
            sort = [("score", meta_score)]
            project = {"score": meta_score}
        elif "cast" in filters:
            query = {"Cast": {"$in": filters["cast"]}}
        elif "genre" in filters:
            query = {"Genre": {"$in": filters['genre']}}

    return query, sort, project


def get_movies(filters, page, movies_per_page):
    query, sort, project = build_query_sort_project(filters)
    print(query, sort, project)
    if project:
        cursor = db.movies.find(query, project).sort(sort)
    else:
        cursor = db.movies.find(query).sort(sort)
    total_num_movies = 0
    if page == 1:
        total_num_movies = db.movies.count_documents(query)
    movies = cursor.skip(page*movies_per_page).limit(movies_per_page)
    print(f"total number: {total_num_movies}")
    return list(movies), total_num_movies


def get_movie_by_id(id):
    try:
        query = {"imdbID": id}
        movie = db.movies.find_one(query)
        return movie
    except Exception as e:
        return {}
