import requests
from bs4 import BeautifulSoup as soup
import random
import string
response = requests.get("https://www.nytimes.com")
if not response:
    print("An error occurred")
else:
    soup_art = soup(response.text, "html.parser")
    articles = soup_art.findall("h2")
    articles.extend(soup_art.findall("h3"))
    random.shuffle(articles)
    print("The following are the heading in the New york times")

    for element in articles:
        try:
            if len(element.string)>25:
                print("=>" + element.string)
        except TypeError:
            pass