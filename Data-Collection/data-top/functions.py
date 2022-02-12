import re
import requests
import logging
from fake_useragent import UserAgent

# Basic configuration of the log output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Generate request headers randomly
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')


def random_ua():
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "keep-alive",
        "User-Agent": ua.random
    }
    return headers


# Scrape html page
def scrape_html(url):
    resp = requests.get(url, headers=random_ua())
    # print(resp.status_code, type(resp.status_code))
    if resp.status_code == 200:
        return resp.text
        # return resp.content

    else:
        logging.info('Page request failed')


# Get the tconst of each movie, so we can get the whole information
def get_tconst(url):
    page_tconst_list = []
    html_text = scrape_html(url)
    tconst_info = re.findall('<div class="(.*?)" data-tconst="(.*?)" data-caller="(.*?)">', html_text)

    for cls, tconst, caller in tconst_info:
        page_tconst_list.extend([tconst])

    return page_tconst_list


# get all the information of each movie in a single page
def get_info50(url):
    page_info50_list = []
    html_text = scrape_html(url)

    # movie_block = re.findall('<span class="lister-item-year text-muted unbold">(.*?)</span>', html_text)

    # get the Year of movies
    page_year = re.findall('<span class="lister-item-year text-muted unbold">(.*?)</span>', html_text)

    # get Title, Poster and imdbID of movies   0: Title  2: Poster  3: imdbID
    page_info1 = re.findall('> <img alt="(.*?)"\nclass="(.*?)"\nloadlate="(.*?)"\ndata-tconst="(.*?)"\nheight="(.*?)"\nsrc="(.*?)"\nwidth="(.*?)" />', html_text)

    # get Runtime of movies
    # page_runtime = re.findall('<span class="runtime">(.*?)</span>', html_text)
    page_runtime_reg = r'<p class="text-muted ">(.*?)<span class="genre">'
    page_runtime_content = re.compile(page_runtime_reg, re.DOTALL)
    page_runtime = page_runtime_content.findall(html_text)
    for i in range(len(page_runtime)):
        if "runtime" in page_runtime[i]:
            a = re.findall('<span class="runtime">(.*?)</span>', page_runtime[i])
            page_runtime[i] = a[0]
        else:
            page_runtime[i] = ''
    if len(page_runtime) != 50:
        for i in range(50-len(page_runtime)):
            page_runtime.extend(["N/A"])

    # get Genre of movies
    page_genre = re.findall('<span class="genre">\n(.*?)</span>', html_text)
    for i in range(len(page_genre)):
        page_genre[i] = page_genre[i].strip()
    if len(page_genre) != 50:
        for i in range(50-len(page_genre)):
            page_genre.extend(["N/A"])

    # get imdbRating of movies
    # page_rating = re.findall('<div class="inline-block ratings-imdb-rating" name="ir" data-value="(.*?)">', html_text)
    page_rating1_reg = r'<div class="ratings-bar">(.*?)div class="inline-block ratings-(.*?)-rating"(.*?)>'
    page_rating1_content = re.compile(page_rating1_reg, re.DOTALL)
    page_rating1 = page_rating1_content.findall(html_text)
    page_rating = []
    for i in range(len(page_rating1)):
        if "data-value" in page_rating1[i][2]:
            a = re.findall(' name="ir" data-value="(.*?)"', page_rating1[i][2])
            page_rating.extend([a[0]])
        else:
            page_rating.extend(["N/A"])
    if len(page_rating) != 50:
        for i in range(50-len(page_rating)):
            page_rating.extend(["N/A"])

    # get Plot of movies
    page_plot_reg = r'<p class="text-muted">\n(.*?)</p>'
    page_plot_content = re.compile(page_plot_reg, re.DOTALL)
    page_plot = page_plot_content.findall(html_text)
    # page_plot = re.findall('<p class="text-muted">\n(.*?)</p>', html_text)
    if len(page_plot) != 50:
        for i in range(50-len(page_plot)):
            page_plot.extend(["N/A"])

    # get imdbVotes of movies
    page_votes1_reg = r'Director(.*?):(.*?)</p>(.*?)</div>'
    page_votes1_content = re.compile(page_votes1_reg, re.DOTALL)
    page_votes1 = page_votes1_content.findall(html_text)
    page_votes = []
    page_votes2_reg = r'<span class="text-muted">Votes:</span>(.*?)<span name="nv" data-value="(.*?)">(.*?)</span>'
    page_votes2_content = re.compile(page_votes2_reg, re.DOTALL)
    for i in range(len(page_votes1)):
        if "Votes:" in page_votes1[i][2]:
            page_votes2 = page_votes2_content.findall(page_votes1[i][2])
            # print(page_votes2)
            page_votes.extend([page_votes2[0][2]])
        else:
            page_votes.extend(["N/A"])
    if len(page_votes) != 50:
        for i in range(50-len(page_votes)):
            page_votes.extend(["N/A"])

    # page_director = re.findall('Director(.*?):\n<a href="(.*?)"\n>(.*?)</a>(.*?)', html_text)
    # page_director_reg = r'Director(.*?):\n<a href="(.*?)"\n>(.*?)</a>'
    # page_director_content = re.compile(page_director_reg, re.DOTALL)
    # page_director = page_director_content.findall(html_text)
    # if len(page_director) != 50:
    #     for i in range(50-len(page_director)):
    #         page_director.extend(["N/A"])

    # get Director of movies
    page_director1_reg = r'    Director(.*?):\n(.*?)<span class="ghost">|</span>    '
    page_director1_content = re.compile(page_director1_reg, re.DOTALL)
    page_director1 = page_director1_content.findall(html_text)
    directors_str = []
    for i in range(len(page_director1)):
        directors_str.extend([page_director1[i][1]])
    page_director2 = []
    for i in range(len(directors_str)):
        director = re.findall('>(.*?)<', directors_str[i])
        director_str = ""
        for j in range(len(director)):
            if j != len(director) - 1:
                director_str += str(director[j]) + ", "
            else:
                director_str += str(director[j])
        page_director2.extend([director_str])
    page_director = []
    for i in range(len(page_director2)):
        if page_director2[i] != '':
            page_director.extend([page_director2[i]])
    if len(page_director) != 50:
        for i in range(50-len(page_director)):
            page_director.extend(["N/A"])

    # get Actors of movies
    page_actor1_reg = r'    Star(.*?):\n(.*?)</p>'
    page_actor1_content = re.compile(page_actor1_reg, re.DOTALL)
    page_actor1 = page_actor1_content.findall(html_text)
    actors_str = []
    for i in range(len(page_actor1)):
        actors_str.extend([page_actor1[i][1]])
    page_actor = []
    for i in range(len(actors_str)):
        actor = re.findall('>(.*?)<', actors_str[i])
        actor_str = ""
        for j in range(len(actor)):
            if j != len(actor) - 1:
                actor_str += str(actor[j]) + ", "
            else:
                actor_str += str(actor[j])
        page_actor.extend([actor_str])
    if len(page_actor) != 50:
        for i in range(50-len(page_actor)):
            page_actor.extend(["N/A"])

    for i in range(50):
        page_dict = {}

        page_dict['Title'] = page_info1[i][0]
        page_dict['Year'] = page_year[i][-5:-1]
        page_dict['Rated'] = "N/A"
        page_dict['Released'] = "N/A"
        page_dict['Runtime'] = page_runtime[i]
        page_dict['Genre'] = page_genre[i]
        page_dict['Director'] = page_director[i]
        page_dict['Writer'] = "N/A"
        page_dict['Actors'] = page_actor[i]
        page_dict['Plot'] = page_plot[i]
        page_dict['Language'] = "N/A"
        page_dict['Country'] = "N/A"
        page_dict['Awards'] = "N/A"
        page_dict['Poster'] = page_info1[i][2]
        page_dict['Ratings'] = "N/A"
        page_dict['Metascore'] = "N/A"
        page_dict['imdbRating'] = page_rating[i]
        page_dict['imdbVotes'] = page_votes[i]
        page_dict['imdbID'] = page_info1[i][3]
        page_dict['Type'] = "movie"
        page_dict['DVD'] = "N/A"
        page_dict['BoxOffice'] = "N/A"
        page_dict['Production'] = "N/A"
        page_dict['Website'] = "N/A"
        page_dict['Response'] = "True"

        page_info50_list.extend([page_dict])

    return page_info50_list


# url = 'https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2020-12-31&start=6101&ref_=adv_nxt'
# html_text = scrape_html(url)
# a = get_info50(url)
# print(a)

# print(html_text)
