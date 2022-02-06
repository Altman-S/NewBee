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