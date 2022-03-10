import json
<<<<<<< HEAD
from nltk.stem.porter import PorterStemmer
from numpy import *
import numpy as np

=======
# from matplotlib.pyplot import bar_label, title
from nltk.stem.porter import PorterStemmer
from numpy import *
import numpy as np
import pickle
>>>>>>> upstream/master

def get_index(file_name):
    with open(file_name, encoding='utf-8') as f:
        movie_inf = json.load(f)
    Title_text = ""
    Year = []
    People = ""
    Genre = ""
<<<<<<< HEAD
=======
    title_dict = dict()
    people_dict = dict()
>>>>>>> upstream/master
    #votes = []
    #ratings = []

    for movie in movie_inf:
<<<<<<< HEAD
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
=======
         ################################get_title_dict()
        title_text = Preprocess(movie['Title'])
        title_text = ' '.join(title_text)
        movie_id = movie['_id']['$oid']
        if movie_id not in title_dict.keys():
            title_dict[movie_id] = title_text

        ################################# get_people_dict()
        director_text = Preprocess(movie['Director'].replace(',',' '))
        # print(director_text)
        # break
        actor_text = Preprocess(movie['Actors'].replace(',',' '))
        writer_text = Preprocess(movie['Writer'].replace(',',' '))
        # print(actor_text)
        # break
        people_text = ' ' + ' '.join(director_text) + ' ' + ' '.join(actor_text)+ ' ' + ' '.join(writer_text)
        people_text = people_text.replace('n/a',' ')
        # print(people_text)
        # break
        movie_id = movie['_id']['$oid']
        if movie_id not in people_dict.keys():
            people_dict[movie_id] = people_text
        #############################################

        movie['Genre'] = movie['Genre'].replace(',', ' ')
        Title_text += (' '+movie['Title'])
        Year.append(movie['Year'])
        # People+=(' '+(movie['Director'].replace(',',' ')))
        # movie['Actors'] = movie['Actors'].replace(',', ' ')
        # people= ""
        # people+=(' '+str(movie['Actors']))
        Genre+=(' '+str(movie['Genre']))
        # if movie['Writer']!='N/A':
        #     people+=(' '+movie['Writer'].replace(',',' '))
        People+=(' '+people_text)
        movie['people'] = Preprocess(people_text)
        # movie['Director'] = Preprocess(movie['Director'])#.split(' ')
>>>>>>> upstream/master
        movie['Title'] =Preprocess(movie['Title'])#.split(' ')
        #ratings.append(float(movie['imdbRating']))
        #votes.append(float(movie['imdbVotes'].replace(",",'')))
        movie['Genre']= movie['Genre'].split(' ')
<<<<<<< HEAD
    Texts = Title_text+Genre+People
    f = open('text.txt', 'w', encoding='utf-8')
    f.write(Texts)
    f.close()
=======
>>>>>>> upstream/master

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
<<<<<<< HEAD
    People_dict = {}
    Title_dict = {}
    # initialize the dict
    for i in range(len(People)):
        People_dict[People[i]] = []
    for i in range(len(Title_text)):
        Title_dict[Title_text[i]] = []
=======
    People_token_dict = {}
    Title_token_dict = {}
    # initialize the dict
    for i in range(len(People)):
        # print(People[i])
        People_token_dict[People[i]] = []
    for i in range(len(Title_text)):
        Title_token_dict[Title_text[i]] = []
>>>>>>> upstream/master
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
<<<<<<< HEAD

=======
>>>>>>> upstream/master
        for item in movie['Genre']:
            Genre_dict[item].append(movie['_id']['$oid'])
        Year_dict[movie['Year']].append(movie['_id']['$oid'])
        for item in movie['Title']:
<<<<<<< HEAD
            Title_dict[item].append(movie['_id']['$oid'])
        for item in movie['people']:
            
            People_dict[item].append(movie['_id']['$oid'])
    return Title_dict, People_dict, Year_dict, Genre_dict


def get_score(file_name):
    votes = []
    ratings = []
    with open(file_name, encoding='utf-8') as f:
        movie_inf = json.load(f)
=======
            Title_token_dict[item].append(movie['_id']['$oid'])
        for item in movie['people']:
            People_token_dict[item].append(movie['_id']['$oid'])
    
    with open('pkl_data/Title_token_dict.pkl','wb') as f:
        pickle.dump(Title_token_dict,f)
    with open('pkl_data/People_token_dict.pkl','wb') as f:
        pickle.dump(People_token_dict,f)
    with open('pkl_data/Genre_dict.pkl','wb') as f:
        pickle.dump(Genre_dict,f)
    with open('pkl_data/Year_dict.pkl','wb') as f:
        pickle.dump(Year_dict,f)
    with open('pkl_data/title_dict.pkl','wb') as f:
        pickle.dump(title_dict,f)
    with open('pkl_data/people_dict.pkl','wb') as f:
        pickle.dump(people_dict,f)

    ######################################## get_score()
    votes = []
    ratings = []
>>>>>>> upstream/master
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
<<<<<<< HEAD
    return dict_score
=======
    with open('pkl_data/dict_score.pkl','wb') as f:
        pickle.dump(dict_score,f)
    

>>>>>>> upstream/master


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
<<<<<<< HEAD
    
    query = query.lower()
    query = query.replace('-',' ')
=======
    query = query.lower()
>>>>>>> upstream/master
    query = query.split(' ')
    stemmed_query = []
    for word in query:
        stemmed_query.append(stemmer_porter.stem(word))
    return stemmed_query

<<<<<<< HEAD

Title_dict, People_dict, Year_dict, Genre_dict = get_index('movies.json')
dict_score= get_score('movies.json')
#print(dict_score)

#print(People_dict)
import pickle


with open('title.pkl', 'wb') as handle:
    pickle.dump(Title_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('people.pkl', 'wb') as handle:
    pickle.dump(People_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
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

=======
if __name__=='__main__':
    get_index('json_data/movies.json')
    
>>>>>>> upstream/master
