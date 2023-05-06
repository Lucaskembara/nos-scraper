from bs4 import BeautifulSoup
from utils import load_exclude
import pandas as pd
import requests
import time


def get_articles(DATE_RANGE, SLEEP=1):
    output = []

    for date in DATE_RANGE:
        URL = "https://nos.nl/nieuws/archief/" + date

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        a_href = soup.find_all("a", {"class": "link-block"})
        a_href = [a.get("href") for a in a_href]

        output.append([date, a_href])
        time.sleep(SLEEP)

    return output


def get_text(articles, SLEEP=1):
    output = []

    for date in articles:
        for article in date[1]:
            URL = "https://nos.nl" + article

            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")

            title = soup.find("h1").getText()
            content = [i.getText() for i in soup.find_all("p")]

            output.append([date[0], title, content])
        time.sleep(SLEEP)

    return output


def scrape_loop(DATE_RANGE, EXCLUDE=True):
    articles = get_articles(DATE_RANGE=DATE_RANGE)
    text = get_text(articles=articles)

    if EXCLUDE:
        exclude_list = load_exclude()

        for i, e in enumerate(text):
            text[i][2] = "".join([x for x in e[2] if x not in exclude_list])

    return pd.DataFrame(text, columns=["Date", "Title", "Text"])
