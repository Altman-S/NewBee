from functions import *

# Prepare for page url (popular movies)
type_list = ["year=2010-01-01,2020-12-31"]
page_pre = "ref_=adv_prv"
page_nxt = "ref_=adv_nxt"
base_url = "https://www.imdb.com/search/title/?title_type=feature"
start_url = "start="

# example = "https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&ref_=adv_prv"


# Get the url of each page (100 pages in all)
def get_pop_page_url(page_num):
    if page_num == 1:
        return base_url + '&' + type_list[0] + '&' + page_pre
    elif page_num > 1:
        num = 50 * (page_num - 1) + 1
        return base_url + '&' + type_list[0] + '&' + start_url + str(num) + '&' + page_nxt
    else:
        return "Wrong Page"


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

    for i in range(200):
        url = get_pop_page_url(i + 1)
        all_info_list.extend(get_info50(url))
        print("Crawl Movie: " + str(50 * (i + 1)))

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
    info_list = get_all_pop_info()

    # clear file
    with open('data/pop_info.txt', 'w') as f:
        f.write('')

    # write tconst to file
    file = open('data/pop_info.txt', 'a')
    for i in range(len(info_list)):
        s = str(info_list[i]) + "\n"
        file.write(s)
    file.close()


if __name__ == '__main__':
    output_pop_info()