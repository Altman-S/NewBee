from json.tool import main
from turtle import down
import requests
from pymongo import MongoClient


def download_movies():
    movies = []
    key="94feff88"
    for i in range(1,11):
        id = f'tt{i:07d}'
        params = {"i":id,"apikey":key}
        respond = requests.get('http://www.omdbapi.com/',params=params)
        if respond.status_code==200:
            movie = respond.json()
            del movie['Response']
            movies.append(movie)
    return movies

def get_db():
    uri = "mongodb+srv://m001-student:789654123@sandbox.xzdvv.mongodb.net/test"
    client = MongoClient(uri)
    db = client.sample_movies
    return db

def insert_movies(db,movies):
    respond = db.movies.insert_many(movies)
    return respond

if __name__ == "__main__":
    db = get_db()
    movies = download_movies()
    response = insert_movies(db,movies)
    print(response)
