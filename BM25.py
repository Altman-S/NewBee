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


class BM25:
    def __init__(self,docs) -> None:
        self.docs = docs #已经分词的list
        self.doc_num = len(docs) #文档数
        self.vocab = set([word for doc in self.docs for word in doc])
        self.avgdl = sum([len(doc)+0.0 for doc in docs]) / self.doc_num
        self.k1 = 1.5
        self.b = 0.75

    def idf(self,word):
        if word not in self.vocab:
            word_idf = 0
        else:
            qn = {}
            for doc in self.docs:
                if word in doc:
                    if word in qn:
                        qn[word]+=1
                    else:
                        qn[word]=1
                else:
                    continue
            word_idf=np.log((self.doc_num-qn[word]+0.5)/qn[word]+0.5)
        return word_idf
    
    def score(self,word):
        score_list = []
        for index,doc in enumerate(self.docs):
            word_count = Counter(doc)
            if word in word_count.keys():
                f = (word_count[word]+0.0)/len((doc))
            else:
                f = 0.0
            r_score = (f*(self.k1+1))/(f+self.k1*(1-self.b + self.b*len(doc)/self.avgdl))
            score_list.append(self.idf(word)*r_score)
        return score_list
    
    def score_all(self,sequence):
        sum_score = []
        for word in sequence:
            sum_score.append(self.score(word))
        sim = np.sum(sum_score,axis=0)
        return sim



if __name__ == "__main__":
    title_list = get_title_list('movies.json')
    title_dict = get_title_dict('movies.json')
    # print(title_dict)
    Title_dict, People_dict, Year_dict, Genre_dict = get_index('movies.json')
    # print(Title_dict)
    query = Preprocess('Harry')[0]
    query_tokens = query.split()
    # print(query_tokens)
    docs = []
    docs_dict = {}
    for token in query_tokens:
        ids = Title_dict[token]
        for id in ids:
            title = title_dict[id]
            title = Preprocess(title)
            # print(title)
            if title not in docs:
                docs.append(title)
                docs_dict[' '.join(title)]=id
            # print(doc_list)
    # print(docs)
    print(len(docs))
    bm = BM25(docs)
    score = bm.score_all(query_tokens)
    score_index = {}
    for i in range(len(score)):
        score_index[i]=score[i]
    score_index = sorted(score_index.items(),key = lambda x:(x[1],x[0]),reverse=True)
    print(score_index[:10])
    new_dict = {v : k for k, v in title_dict.items()}
    # for i in title_dict.values():
    #     if i == 'harri potter and the deathli hallows: part 1':
    #         print(11111111111111)
    # print(docs)
    # print(title_dict)
    results = [' '.join(docs[i[0]]) for i in score_index]
    results = [docs_dict[e] for e in results]    
    # for i in title_dict.values():
    #     print(i)
    # print(results)

    print(results[:10])

