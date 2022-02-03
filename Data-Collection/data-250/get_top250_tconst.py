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


# Prepare for page url
type_list = ["user_rating,desc"]
page_first = "ref_=adv_prv"
page_next = "ref_=adv_nxt"
base_url = "https://www.imdb.com/search/title/?groups=top_250"
sort_url = "sort="
start_url = "start="


# Get the url of each page (5 pages in all)
def get_page_url(page_num):
    if page_num == 1:
        return base_url + '&' + sort_url + type_list[0] + '&' + page_first
    elif page_num > 1:
        num = 50 * (page_num - 1) + 1
        return base_url + '&' + sort_url + type_list[0] + '&' + start_url + str(num) + '&' + page_next
    else:
        return "Wrong Page"


# Get the top 250 movies' tconst
def get_all_tconst():
    all_tconst_list = []

    for i in range(5):
        url = get_page_url(i + 1)
        all_tconst_list.extend(get_tconst(url))

    return all_tconst_list


# Output top 250 tconst to txt file
def output_tconst():
    t_list = get_all_tconst()

    # clear file
    with open('data/top250_tconst.txt', 'w') as f:
        f.write('')

    file = open('data/top250_tconst.txt', 'w')
    for i in range(len(t_list)):
        s = t_list[i] + "\n"
        file.write(s)
    file.close()


if __name__ == '__main__':
    output_tconst()

