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


# get info of bug page



# get all the information of each movie in a single page
def get_info50(url):
    page_info50_list = []
    html_text = scrape_html(url)

    movie_block = re.findall('<span class="lister-item-year text-muted unbold">(.*?)</span>', html_text)

    page_year = re.findall('<span class="lister-item-year text-muted unbold">(.*?)</span>', html_text)

    # 0: Title  2: Poster  3: imdbID
    page_info1 = re.findall('> <img alt="(.*?)"\nclass="(.*?)"\nloadlate="(.*?)"\ndata-tconst="(.*?)"\nheight="(.*?)"\nsrc="(.*?)"\nwidth="(.*?)" />', html_text)

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
    # print(page_runtime)
    # print(len(page_runtime))
    if len(page_runtime) != 50:
        for i in range(50-len(page_runtime)):
            page_runtime.extend(["N/A"])

    page_genre = re.findall('<span class="genre">\n(.*?)</span>', html_text)
    for i in range(len(page_genre)):
        page_genre[i] = page_genre[i].strip()
    if len(page_genre) != 50:
        for i in range(50-len(page_genre)):
            page_genre.extend(["N/A"])

    # page_rating = re.findall('<div class="inline-block ratings-imdb-rating" name="ir" data-value="(.*?)">', html_text)
    page_rating1_reg = r'<div class="ratings-bar">(.*?)div class="inline-block ratings-(.*?)-rating"(.*?)>'
    page_rating1_content = re.compile(page_rating1_reg, re.DOTALL)
    page_rating1 = page_rating1_content.findall(html_text)
    page_rating = []
    # print(len(page_rating1))
    for i in range(len(page_rating1)):
        if "data-value" in page_rating1[i][2]:
            a = re.findall(' name="ir" data-value="(.*?)"', page_rating1[i][2])
            page_rating.extend([a[0]])
        else:
            page_rating.extend(["N/A"])
    # print(page_rating)
    # print(len(page_rating))
    if len(page_rating) != 50:
        for i in range(50-len(page_rating)):
            page_rating.extend(["N/A"])

    page_plot_reg = r'<p class="text-muted">\n(.*?)</p>'
    page_plot_content = re.compile(page_plot_reg, re.DOTALL)
    page_plot = page_plot_content.findall(html_text)
    # page_plot = re.findall('<p class="text-muted">\n(.*?)</p>', html_text)
    # print(page_plot[19])
    # print(len(page_plot))
    if len(page_plot) != 50:
        for i in range(50-len(page_plot)):
            page_plot.extend(["N/A"])

    # page_votes_reg = r'<span class="text-muted">Votes:</span>(.*?)<span name="nv" data-value="(.*?)">(.*?)</span>'
    # page_votes_content = re.compile(page_votes_reg, re.DOTALL)
    # page_votes = page_votes_content.findall(html_text)
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
    # print(len(page_votes1))
    # print(page_votes)
    if len(page_votes) != 50:
        for i in range(50-len(page_votes)):
            page_votes.extend(["N/A"])

    # page_director = re.findall('Director(.*?):\n<a href="(.*?)"\n>(.*?)</a>(.*?)', html_text)
    page_director_reg = r'Director(.*?):\n<a href="(.*?)"\n>(.*?)</a>'
    page_director_content = re.compile(page_director_reg, re.DOTALL)
    page_director = page_director_content.findall(html_text)
    # print(page_director)
    if len(page_director) != 50:
        for i in range(50-len(page_director)):
            page_director.extend(["N/A"])

    for i in range(50):
        page_dict = {}

        page_dict['Title'] = page_info1[i][0]
        page_dict['Year'] = page_year[i][-5:-1]
        page_dict['Rated'] = "N/A"
        page_dict['Released'] = "N/A"
        page_dict['Runtime'] = page_runtime[i]
        page_dict['Genre'] = page_genre[i]
        page_dict['Director'] = page_director[i][2]
        page_dict['Writer'] = "N/A"
        page_dict['Actors'] = "N/A"
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
# print(a[1])

# print(html_text)
