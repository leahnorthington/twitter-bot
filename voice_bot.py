# import statements
from urllib.request import urlopen
from bs4 import BeautifulSoup

# save URL of article
current_article = 'https://georgetownvoice.com/2019/01/08/epic-adventure-aquaman-reaches-for-greatness/'
# pull html from article page
html_from_page = urlopen(current_article)
# parse html using BeautifulSoup
parsed_html = BeautifulSoup(html_from_page, 'html.parser')
# pull info in title tags
title = parsed_html.title.string

print(title)
