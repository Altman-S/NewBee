from json.tool import main
from turtle import down
import requests
from pymongo import MongoClient
import pandas

key = "94feff88"


def download_movies():
    movies = []
    for i in range(3000000, 3050000):
        id = f'tt{i:07d}'
        params = {"i": id, "apikey": key}
        respond = requests.get('http://www.omdbapi.com/', params=params)
        if respond.status_code == 200:
            movie = respond.json()
            if movie['Response'] == 'True':
                print(id)
                genres = [genre.strip() for genre in movie['Genre'].split(",")]
                del movie['Response']
                movie['Genre'] = genres
                movies.append(movie)
    return movies


def get_top250_movies():
    top250 = []
    with open('data-top/data/top250_tconst.txt', 'r') as reader:
        for line in reader:
            tconst = line.strip()
            params = {"i": tconst, "apikey": key}
            respond = requests.get('http://www.omdbapi.com/', params=params)
            if respond.status_code == 200:
                movie = respond.json()
                genres = [genre.strip() for genre in movie['Genre'].split(",")]
                del movie['Response']
                movie['Genre'] = genres
                top250.append(movie)
    return top250


def get_db():
    uri = "mongodb+srv://m001-student:789654123@sandbox.xzdvv.mongodb.net/test"
    client = MongoClient(uri)
    db = client.sample_movies
    return db


def insert_movies(db, movies):
    respond = db.movies.insert_many(movies)
    return respond


def insert_top250(db, top250):
    respond = db.top_250_rated.insert_many(top250)
    return respond


if __name__ == "__main__":
    # top250 = get_top250_movies()
    movies = download_movies()
    # print(movies)
    db = get_db()
    # respond = insert_top250(db, top250)
    respond = insert_movies(db, movies)
    print(respond)
