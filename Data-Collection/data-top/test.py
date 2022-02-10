from html.parser import HTMLParser
from urllib.request import urlopen
import re

class Parser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('start tag: ' + tag)
        # if tag == 'a':
        #     print('1')

    def handle_endtag(self, tag):
        print('end tag: ' + tag)


# response = urlopen('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc')
response = urlopen('https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&ref_=adv_prv')
html_bytes = response.read()
html_string = html_bytes.decode('utf-8')

print(html_string)
# parser = Parser()
# parser.feed(html_string)

page = """
<span class="lister-item-year text-muted unbold">(2017)</span>

> <img alt="King Richard"
class="loadlate"
loadlate="https://m.media-amazon.com/images/M/MV5BYTcyNmY4ZGEtYmE4Zi00ZDViLTlmYzMtMmQ4ZTM4OWNmZjQxXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX67_CR0,0,67,98_AL_.jpg"
data-tconst="tt9620288"
height="98"
src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png"
width="67" />

            <span class="certificate">12A</span>
                 <span class="ghost">|</span> 
                <span class="runtime">133 min</span>
                 <span class="ghost">|</span> 
            <span class="genre">
Action, Adventure, Sci-Fi            </span>

<div class="inline-block ratings-imdb-rating" name="ir" data-value="7.4">
<div class="inline-block ratings-user-rating">

<div class="inline-block ratings-imdb-rating" name="ir" data-value="7.4">

<p class="text-muted">
Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.</p>

<p class="text-muted">
<a href="/name/nm8877502">Mohamedou Ould Slahi</a> fights for freedom after being detained and imprisoned without charge by the U.S. Government for years.</p>

                <span class="text-muted">Votes:</span>
                <span name="nv" data-value="609830">609,830</span>

    Director:
<a href="/name/nm1218281/"
>Jon Watts</a>
                 <span class="ghost">|</span> 
    Stars:
<a href="/name/nm4043618/"
>Tom Holland</a>, 
<a href="/name/nm0000474/"
>Michael Keaton</a>, 
<a href="/name/nm0000375/"
>Robert Downey Jr.</a>, 
<a href="/name/nm0000673/"
>Marisa Tomei</a>
    </p>
    
    Directors:
<a href="/name/nm1158544/"
>Jared Bush</a>, 
<a href="/name/nm0397174/"
>Byron Howard</a>, 
<a href="/name/nm4146781/"
>Charise Castro Smith</a>
                 <span class="ghost">|</span> 
                 
    <p class="text-muted ">
            
            <span class="genre">
Action, Adventure, Drama            </span>

    <p class="text-muted ">
            <span class="certificate">15</span>
                 <span class="ghost">|</span> 
                <span class="runtime">97 min</span>
                 <span class="ghost">|</span> 
            <span class="genre">


# vote 
Director:
<a href="/name/nm0000437/?ref_=adv_li_dr_0"
>Woody Harrelson</a>
                 <span class="ghost">|</span> 
    Stars:
<a href="/name/nm0705356/?ref_=adv_li_st_0"
>Daniel Radcliffe</a>, 
<a href="/name/nm0005562/?ref_=adv_li_st_1"
>Owen Wilson</a>, 
<a href="/name/nm0000437/?ref_=adv_li_st_2"
>Woody Harrelson</a>, 
<a href="/name/nm0095104/?ref_=adv_li_st_3"
>Bono</a>
    </p>
        <p class="sort-num_votes-visible">
                <span class="text-muted">Votes:</span>
                <span name="nv" data-value="3991">3,991</span>
            
        </p>
        </div>
    </div>

Director:
<a href="/name/nm3268802/?ref_=adv_li_dr_0"
>Alan Brown</a>
    </p>
        </div>
    </div>


    <div class="ratings-bar">
    <div class="inline-block ratings-imdb-rating" name="ir" data-value="6.2">
    
    <div class="ratings-bar">
            <div class="inline-block ratings-user-rating">

"""

page_year = re.findall('<span class="lister-item-year text-muted unbold">(.*?)</span>', page)

# 0: Title  2: Poster  3: imdbID
page_info1 = re.findall('> <img alt="(.*?)"\nclass="(.*?)"\nloadlate="(.*?)"\ndata-tconst="(.*?)"\nheight="(.*?)"\nsrc="(.*?)"\nwidth="(.*?)" />', page)

# page_runtime = re.findall('<span class="runtime">(.*?)</span>', page)
page_runtime_reg = r'<p class="text-muted ">(.*?)<span class="genre">'
page_runtime_content = re.compile(page_runtime_reg, re.DOTALL)
page_runtime = page_runtime_content.findall(page)
for i in range(len(page_runtime)):
    if "runtime" in page_runtime[i]:
        a = re.findall('<span class="runtime">(.*?)</span>', page_runtime[i])
        page_runtime[i] = a[0]
    else:
        page_runtime[i] = "N/A"

page_genre = re.findall('<span class="genre">\n(.*?)</span>', page)
for i in range(len(page_genre)):
    page_genre[i] = page_genre[i].strip()

# page_rating = re.findall('<div class="inline-block ratings-imdb-rating" name="ir" data-value="(.*?)">', page)
page_rating1_reg = r'<div class="ratings-bar">(.*?)<div class="inline-block ratings-(.*?)-rating"(.*?)>'
page_rating1_content = re.compile(page_rating1_reg, re.DOTALL)
page_rating1 = page_rating1_content.findall(page)
page_rating = []
print(len(page_rating1))
for i in range(len(page_rating1)):
    if "data-value" in page_rating1[i][2]:
        a = re.findall(' name="ir" data-value="(.*?)"', page_rating1[i][2])
        page_rating.extend([a[0]])
    else:
        page_rating.extend(["N/A"])

page_plot_reg = r'<p class="text-muted">\n(.*?)</p>'
page_plot_content = re.compile(page_plot_reg, re.DOTALL)
page_plot = page_plot_content.findall(page)

# page_votes_reg = r'<span class="text-muted">Votes:</span>(.*?)<span name="nv" data-value="(.*?)">(.*?)</span>'
# page_votes_content = re.compile(page_votes_reg, re.DOTALL)
# page_votes = page_votes_content.findall(page)
page_votes1_reg = r'Director(.*?):(.*?)</p>(.*?)</div>'
page_votes1_content = re.compile(page_votes1_reg, re.DOTALL)
page_votes1 = page_votes1_content.findall(page)
page_votes = []
for i in range(len(page_votes1)):
    if "Votes:" in page_votes1[i][2]:
        page_votes2_reg = r'<span class="text-muted">Votes:</span>(.*?)<span name="nv" data-value="(.*?)">(.*?)</span>'
        page_votes2_content = re.compile(page_votes2_reg, re.DOTALL)
        page_votes2 = page_votes2_content.findall(page_votes1[i][2])
        # print(page_votes2)
        page_votes.extend([page_votes2[i][2]])
    else:
        page_votes.extend(["N/A"])

page_director_reg = r'Director(.*?):\n<a href="(.*?)"\n>(.*?)</a>'
page_director_content = re.compile(page_director_reg, re.DOTALL)
page_director = page_director_content.findall(page)

aa = {}
aa["a"] = 'b'
aa["b"] = 'c'
print(page_year[0][-5:-1])

print(page_rating)

# for i in range(len(page_votes1)):
#     print(page_votes1[i])
#     print(len(page_votes1[i]))



# data format
"""
{"Title":"Jai Bhim", page_info1[i][0]
"Year":"2021", page_year[i][1:-1]
"Rated":"TV-MA",
"Released":"02 Nov 2021",
"Runtime":"164 min", page_runtime[i]
"Genre":"Crime, Drama", page_genre[i]
"Director":"T.J. Gnanavel", page_director[i][1]
"Writer":"T.J. Gnanavel",
"Actors":"Suriya, Lijo Mol Jose, Manikandan",
"Plot":"When a tribal man is arrested for a case of alleged theft, his wife turns to a human-rights lawyer to help bring justice.", page_plot[i]
"Language":"Tamil, Hindi",
"Country":"India",
"Awards":"3 wins",
"Poster":"https://m.media-amazon.com/images/M/MV5BY2Y5ZWMwZDgtZDQxYy00Mjk0LThhY2YtMmU1MTRmMjVhMjRiXkEyXkFqcGdeQXVyMTI1NDEyNTM5._V1_SX300.jpg", page_info1[i][2]
"Ratings":[{"Source":"Internet Movie Database","Value":"9.3/10"},{"Source":"Rotten Tomatoes","Value":"100%"}],
"Metascore":"N/A",
"imdbRating":"9.3", page_rating[i]
"imdbVotes":"172,126", page_votes[i][2]
"imdbID":"tt15097216", page_info1[i][3]
"Type":"movie",
"DVD":"N/A",
"BoxOffice":"N/A",
"Production":"N/A",
"Website":"N/A",
"Response":"True"}
"""
