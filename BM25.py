from hashlib import new
import math
from multiprocessing.dummy import Process
from pydoc import doc
import re
from unittest import result
import numpy as np
import logging
from collections import Counter
from createindex import *
import os


class BM25:
    def __init__(self, docs) -> None:
        self.docs = docs  # 已经分词的list
        self.doc_num = len(docs)  # 文档数
        self.vocab = set([word for doc in self.docs for word in doc])
        self.avgdl = sum([len(doc)+0.0 for doc in docs]) / self.doc_num
        self.k1 = 1.5
        self.b = 0.75

    def idf(self, word):
        if word not in self.vocab:
            word_idf = 0
        else:
            qn = {}
            for doc in self.docs:
                if word in doc:
                    if word in qn:
                        qn[word] += 1
                    else:
                        qn[word] = 1
                else:
                    continue
            word_idf = np.log((self.doc_num-qn[word]+0.5)/qn[word]+0.5)
        return word_idf

    def score(self, word):
        score_list = []
        for index, doc in enumerate(self.docs):
            word_count = Counter(doc)
            if word in word_count.keys():
                f = (word_count[word]+0.0)/len((doc))
            else:
                f = 0.0
            r_score = (f*(self.k1+1))/(f+self.k1 *
                                       (1-self.b + self.b*len(doc)/self.avgdl))
            score_list.append(self.idf(word)*r_score)
        return score_list

    def score_all(self, sequence):
        sum_score = []
        for word in sequence:
            sum_score.append(self.score(word))
        sim = np.sum(sum_score, axis=0)
        return sim


def search_title(query):
    query = Preprocess(query)[0]
    query_tokens = query.split()
    docs = []
    docs_dict = {}
    for token in query_tokens:
        ids = Title_token_dict[token]
        for id in ids:
            title = title_dict[id]
            title = Preprocess(title)
            # print(title)
            if title not in docs:
                docs.append(title)
                docs_dict[' '.join(title)] = id
    bm = BM25(docs)
    score = bm.score_all(query_tokens)
    score_index = {}
    for i in range(len(score)):
        score_index[i] = score[i]
    score_index = sorted(score_index.items(),
                         key=lambda x: (x[1], x[0]), reverse=True)
    # new_dict = {v : k for k, v in title_dict.items()}
    results = [' '.join(docs[i[0]]) for i in score_index]
    results = [docs_dict[e] for e in results]
    return results

def search_year(year):
    dict_rank = {}
    try:
        ids = Year_dict[year]
        for i in range(len(ids)):
            dict_rank[ids[i]] = dict_score[ids[i]]
        dict_rank = sorted(dict_rank.items(), key=lambda x: x[1], reverse=True)
        oid_list = [i[0] for i in dict_rank]
        return oid_list
    except KeyError as e:
        return None


def search_genre(genre):
    dict_rank = {}
    try:
        ids = Genre_dict[genre]
        for i in range(len(ids)):
            dict_rank[ids[i]] = dict_score[ids[i]]
        dict_rank = sorted(dict_rank.items(), key=lambda x: x[1], reverse=True)
        oid_list = [i[0] for i in dict_rank]
        return oid_list
    except:
        return None


def search_celebrity(query):
    query = Preprocess(query)[0]
    query_tokens = query.split()
    docs = []
    docs_dict = {}
    for token in query_tokens:
        ids = People_token_dict[token]
        for id in ids:
            people = people_dict[id]
            people = Preprocess(people)
            # print(title)
            if people not in docs:
                docs.append(people)
                docs_dict[' '.join(people)] = id
    bm = BM25(docs)
    score = bm.score_all(query_tokens)
    score_index = {}
    for i in range(len(score)):
        score_index[i] = score[i]
    score_index = sorted(score_index.items(),
                         key=lambda x: (x[1], x[0]), reverse=True)
    # new_dict = {v : k for k, v in title_dict.items()}
    results = [' '.join(docs[i[0]]) for i in score_index]
    results = [docs_dict[e] for e in results]
    return results


with open('title_dict.pkl', 'rb') as f:
    title_dict = pickle.load(f, encoding='bytes')
with open('Title_token_dict.pkl', 'rb') as f:
    Title_token_dict = pickle.load(f, encoding='bytes')
with open('people_dict.pkl', 'rb') as f:
    people_dict = pickle.load(f, encoding='bytes')
with open('People_token_dict.pkl', 'rb') as f:
    People_token_dict = pickle.load(f, encoding='bytes')
with open('Genre_dict.pkl', 'rb') as f:
    Genre_dict = pickle.load(f, encoding='bytes')
with open('Genre_dict.pkl', 'rb') as f:
    Year_dict = pickle.load(f, encoding='bytes')
with open('dict_score.pkl', 'rb') as f:
    dict_score = pickle.load(f, encoding='bytes')
print("All index loaded")

# if __name__ == "__main__":
#     if not os.path.isfile('Title_dict.pkl'):
#         get_index('movies.json')
#     query = 'Harry Potter'
#     print(search_celebrity(query))
