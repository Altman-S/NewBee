from functions import *


# Prepare for page url (top250 movies)
type_list = ["sort=user_rating,desc"]
page_first = "ref_=adv_prv"
page_next = "ref_=adv_nxt"
base_url = "https://www.imdb.com/search/title/?groups=top_250"
start_url = "start="

# example = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc"


# Get the url of each page (5 pages in all)
def get_top250_page_url(page_num):
    if page_num == 1:
        return base_url + '&' + type_list[0] + '&' + page_first
    elif page_num > 1:
        num = 50 * (page_num - 1) + 1
        return base_url + '&' + type_list[0] + '&' + start_url + str(num) + '&' + page_next
    else:
        return "Wrong Page"


# Get the top 250 movies' tconst
def get_all_top250_tconst():
    all_tconst_list = []

    for i in range(5):
        url = get_top250_page_url(i + 1)
        all_tconst_list.extend(get_tconst(url))

    return all_tconst_list


# Output top 250 tconst to txt file
def output_top250_tconst():
    t_list = get_all_top250_tconst()

    # clear file
    with open('data/top250_tconst.txt', 'w') as f:
        f.write('')

    file = open('data/top250_tconst.txt', 'w')
    for i in range(len(t_list)):
        s = t_list[i] + "\n"
        file.write(s)
    file.close()


if __name__ == '__main__':
    output_top250_tconst()

