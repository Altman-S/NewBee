from functions import *
import json

# Prepare for page url (popular movies)
type_list = ["year=2010-01-01,2021-12-31"]
page_pre = "ref_=adv_prv"
page_nxt = "ref_=adv_nxt"
base_url = "https://www.imdb.com/search/title/?title_type=feature"
home_url = "https://www.imdb.com"
start_url = "start="

# example0 = "https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&ref_=adv_prv"
# example1 = "https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&start=9951&ref_=adv_prv"
# example2 = "https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&after=WzM4NDM2LCJ0dDcwNzM1MjIiLDEwMDAxXQ%3D%3D&ref_=adv_nxt"


# Get the url of each page (100 pages in all)
def get_pop_page_url(page_num):
    if page_num == 1:
        return base_url + '&' + type_list[0] + '&' + page_pre
    elif page_num > 1:
        num = 50 * (page_num - 1) + 1
        return base_url + '&' + type_list[0] + '&' + start_url + str(num) + '&' + page_nxt
    else:
        return "Wrong Page"


# Get the url of next page
def get_next_page_url(url):

    return home_url + get_next_html(url)

# print(get_next_page_url('https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&start=9951&ref_=adv_prv'))


# Get the top 100,000 movies' tconst
def get_all_pop_tconst():
    all_tconst_list = []

    for i in range(2000):
        url = get_pop_page_url(i + 1)
        all_tconst_list.extend(get_tconst(url))
        print("Crawl Movie: " + str(50 * (i + 1)))

    return all_tconst_list


# Get the top 100,000 movies' infos
def get_all_pop_info():
    all_info_list = []

    for j in range(200):
        i = j + 200 * 1
        url = get_pop_page_url(i + 1)
        all_info_list.extend(get_info50(url))
        print("page: " + str(i))
        print("Crawl Movie: " + str(50 * (i + 1)))

    return all_info_list


# Get next 10,000 movies' infos
def get_next_10k_info():
    all_info_list = []
    url = "https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&after=Wzc0MTc0OSwidHQxODQ0NzQ5Iiw4OTk1MV0%3D&ref_=adv_nxt"

    for i in range(200):
        url = get_next_page_url(url)
        all_info_list.extend(get_info50(url))
        print(url)
        print("page: " + str(i + 1))
        print("Crawl Movie: " + str(50 * (i + 1)))

        if i == 199:
            print("last url: " + str(url))

    return all_info_list


# Output top 100,000 tconst to txt file
def output_pop_tconst():
    t_list = get_all_pop_tconst()

    # clear file
    with open('data/pop_tconst.txt', 'w') as f:
        f.write('')

    # write tconst to file
    file = open('data/pop_tconst.txt', 'w')
    for i in range(len(t_list)):
        s = t_list[i] + "\n"
        file.write(s)
    file.close()


# Output top 100,000 info to txt file
def output_pop_info():
    info_list = get_next_10k_info()

    # clear file
    with open('data/data100k/info_90k_100k.txt', 'w') as f:
        f.write('')

    # write tconst to file
    file = open('data/data100k/info_90k_100k.txt', 'a')
    for i in range(len(info_list)):
        s = json.dumps(info_list[i]) + "\n"
        file.write(s)
    file.close()


if __name__ == '__main__':
    output_pop_info()