from html.parser import HTMLParser
from urllib.request import urlopen


class Parser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('start tag: ' + tag)
        # if tag == 'a':
        #     print('1')

    def handle_endtag(self, tag):
        print('end tag: ' + tag)


response = urlopen('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc')
# response = urlopen('https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2021-12-31&ref_=adv_prv')
html_bytes = response.read()
html_string = html_bytes.decode('utf-8')

parser = Parser()
parser.feed(html_string)
