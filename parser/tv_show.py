import requests
from bs4 import BeautifulSoup

URL = "https://animekisa.tv/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="episode-box test")
    anime = []

    for item in items:
        anime.append(
            {
                "title": URL + item.find('a', class_="an").get("href"),
                # "image": URL + item.find('div', class_="image-box").find("img").get("src")
            }
        )
    return anime[0].values()


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 5):
            html = get_html(f"https://animekisa.tv/latest/{page}")
            anime.extend(get_data(html.text))
        return anime
    else:
        raise Exception("Error in parser function")
