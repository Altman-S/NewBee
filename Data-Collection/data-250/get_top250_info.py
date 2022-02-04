import requests
import logging
from fake_useragent import UserAgent
from get_top250_tconst import random_ua, scrape_html
import json
import sys


# Read top250_tconst.txt
tconst_list = []
with open('data/top250_tconst.txt', 'r') as f:
    for line in f:
        tconst_list.extend([line.strip('\n')])


a = 'http://www.omdbapi.com/?i=tt3896198&apikey=94feff88'
base_url = 'http://www.omdbapi.com/'
tconst_url = '?i='
apikey_url = 'apikey=94feff88'


def get_info_url(tt):
    return base_url + tconst_url + tt + '&' + apikey_url


def get_info():
    info_list = []
    for i in range(len(tconst_list)):
        movie_info = scrape_html(get_info_url(tconst_list[i]))
        info_list.extend([movie_info])

    return info_list


def output_info():
    info_list = get_info()

    # clear file
    with open('data/top250_info.txt', 'w') as f:
        f.write('')

    file = open('data/top250_info.txt', 'w')
    for i in range(len(info_list)):
        s = info_list[i] + "\n"
        file.write(s)
    file.close()


if __name__ == '__main__':
    output_info()

