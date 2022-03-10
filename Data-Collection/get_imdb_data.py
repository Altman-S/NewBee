from genericpath import isfile
import json
from turtle import down
import requests
from pymongo import MongoClient
import pandas
import os

key = "94feff88"


def download_movies():
    movies = []
    with open('data-top/data/pop_tconst.txt', 'r') as reader:
        for line in reader:
            tconst = line.strip()
            params = {"i": tconst, "apikey": key}
            print(params)
            # respond = requests.get('http://www.omdbapi.com/', params=params)
            # if respond.status_code == 200:
            #     movie = respond.json()
            #     if movie['Response'] == 'True':
            #         genres = [genre.strip() for genre in movie['Genre'].split(",")]
            #         del movie['Response']
            #         movie['Genre'] = genres
            #         movies.append(movie)
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


def get_movie():
    movies = []
    path = 'data-top/data/data100k/'
    for f in os.listdir(path):
        if isfile(os.path.join(path,f)) and f!='page_url.txt':
            with open(os.path.join(path,f),'r',encoding='utf-8') as reader:
                for line in reader:
                    movie = json.loads(line)
                    movies.append(movie)
    return movies

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
    movies = get_movie()
    print(len(movies))
    print(movies[0])
    db = get_db()
    respond = insert_movies(db, movies[50000:])
    print(respond)
    
