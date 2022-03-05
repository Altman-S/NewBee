import json
from nltk.stem.porter import PorterStemmer
from numpy import *
import numpy as np


def get_index(file_name):
    with open(file_name, encoding='utf-8') as f:
        movie_inf = json.load(f)
    Title_text = ""
    Year = []
    People = ""
    Genre = ""
    #votes = []
    #ratings = []

    for movie in movie_inf:
        movie['Genre'] = movie['Genre'].replace(',', ' ')
        Title_text += (' '+movie['Title'])
        Year.append(movie['Year'])
        People+=(' '+(movie['Director']))
        movie['Actors'] = movie['Actors'].replace(',', ' ')
        people= ""
        people+=(' '+str(movie['Actors']))
        Genre+=(' '+str(movie['Genre']))
        if movie['Writer']!='N/A':
            people+=(' '+movie['Writer'])
        People+=people
        movie['people'] = Preprocess(people)
        movie['Director'] = Preprocess(movie['Director'])#.split(' ')
        movie['Title'] =Preprocess(movie['Title'])#.split(' ')
        #ratings.append(float(movie['imdbRating']))
        #votes.append(float(movie['imdbVotes'].replace(",",'')))
        movie['Genre']= movie['Genre'].split(' ')
    Texts = Title_text+Genre+People
    f = open('text.txt', 'w', encoding='utf-8')
    f.write(Texts)
    f.close()

    Title_text =Preprocess(Title_text)
        #print(len(People))
        #People += (' '+(movie['Director']))
        #Genre += (' '+str(movie['Genre']))
        #movie['Director'] = Preprocess(movie['Director'])  # .split(' ')
        #movie['Title'] = Preprocess(movie['Title'])  # .split(' ')
        # ratings.append(float(movie['imdbRating']))
        # votes.append(float(movie['imdbVotes'].replace(",",'')))
        #movie['Genre'] = movie['Genre'].split(' ')
        #Title_text = Preprocess(Title_text)
        # print(len(People))

    Genre = Genre.split(' ')
    #print(Genre)
    Genre_dict = {}
    People = Preprocess(People)
    People_dict = {}
    Title_dict = {}
    # initialize the dict
    for i in range(len(People)):
        People_dict[People[i]] = []
    for i in range(len(Title_text)):
        Title_dict[Title_text[i]] = []
    Year_dict = {}
    for i in range(len(Year)):
        Year_dict[str(Year[i])] = []
    for i in range(len(Genre)):
        Genre_dict[Genre[i]] = []
    #print(Genre_dict)
    #print(Year)
    
    # print(Genre_dict)
    # print(Year)

    for movie in movie_inf:
        # print(movie)

        for item in movie['Genre']:
            Genre_dict[item].append(movie['_id']['$oid'])
        Year_dict[movie['Year']].append(movie['_id']['$oid'])
        for item in movie['Title']:
            Title_dict[item].append(movie['_id']['$oid'])
        for item in movie['people']:
            
            People_dict[item].append(movie['_id']['$oid'])
    return Title_dict, People_dict, Year_dict, Genre_dict


def get_score(file_name):
    votes = []
    ratings = []
    with open(file_name, encoding='utf-8') as f:
        movie_inf = json.load(f)
    dict_score = {}
    for movie in movie_inf:
        # print(movie.keys())
        x = 0
        if 'imdbRating' in movie.keys():
            if movie['imdbRating'] != 'N/A':
                x = float(movie['imdbRating'])
                ratings.append(x)
            else:
                x = 0.0
        if 'imdbVotes' in movie.keys():
            if movie['imdbVotes'] != 'N/A':
                movie['imdbVotes'] = movie['imdbVotes'].replace(',', '')
                x += float(movie['imdbVotes'])/10000
                votes.append(float(movie['imdbVotes']))
            else:
                x += 0.0

        dict_score[movie['_id']['$oid']] = x
    for i in range(len(votes)):
        if votes[i] != 0:
            votes[i] = np.log(votes[i])
        else:
            continue
    max_index = votes.index(max(votes, key=abs))
    maxvote = votes[max_index]+0
    meanvote = mean(votes)
    min_index = votes.index(min(votes, key=abs))
    minvote = votes[min_index]+0

    for i in range(len(votes)):
        votes[i] = (votes[i]-minvote)/(maxvote-minvote)
    max_idx = ratings.index(max(ratings, key=abs))
    maxrating = ratings[max_idx]+0
    min_idx = ratings.index(min(ratings, key=abs))
    minrating = ratings[min_idx]+0
    for i in range(len(ratings)):
        ratings[i] = (ratings[i]-minrating)/(maxrating-minrating)

    for movie in movie_inf:
        x = 0
        if 'imdbRating' in movie.keys():
            if movie['imdbRating'] != 'N/A':
                x = float(movie['imdbRating'])
                score1 = (x-minrating)/(maxrating-minrating)
            else:
                score1 = 0
        if 'imdbVotes' in movie.keys():
            if movie['imdbVotes'] != 'N/A':
                score2 = np.log(float(movie['imdbVotes']))
                score2 = (score2-minvote)/(maxvote-minvote)
            else:
                score2 = 0
        score = score1 + score2
        dict_score[movie['_id']['$oid']] = score
    return dict_score


# def Retrieval(query, dict_score):
#     dict_rank = {}
#     ids = Year_dict[query]
#     # print(ids)
#     rank_dict = {}
#     for i in range(len(ids)):

#         dict_rank[ids[i]] = dict_score[ids[i]]

#     dict_rank = sorted(dict_rank.items(), key=lambda x: x[1], reverse=True)
#     return dict_rank


def Preprocess(query):
    stemmer_porter = PorterStemmer()
    query = query.lower()
    query = query.split(' ')
    stemmed_query = []
    for word in query:
        stemmed_query.append(stemmer_porter.stem(word))
    return stemmed_query


Title_dict, People_dict, Year_dict, Genre_dict = get_index('movies.json')
dict_score= get_score('movies.json')
#print(dict_score)

#print(People_dict)

title = json.dumps(Title_dict)
people = json.dumps(People_dict)
with open('title.json', 'w') as f:
    f.write(title)
with open('people.json','w') as f:
    f.write(people)

def get_title_list(file_name):
    with open(file_name, encoding='utf-8') as f:
        movie_inf = json.load(f)
    title_list = []
    for movie in movie_inf:
        Title_text = movie['Title']
        Title_text = ' '.join(Preprocess(Title_text))
        title_list.append(Title_text)
    return title_list


def get_title_dict(file_name):
    with open(file_name, encoding='utf-8') as f:
        movie_inf = json.load(f)
    title_dict = dict()
    for movie in movie_inf:
        title_text = Preprocess(movie['Title'])
        title_text = ' '.join(title_text)
        movie_id = movie['_id']['$oid']
        if movie_id not in title_dict.keys():
            title_dict[movie_id] = title_text
    return title_dict

