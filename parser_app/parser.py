import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "http://www.manascinema.com"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}


# START PARSING
@csrf_exempt
def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# GET DATA
@csrf_exempt
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="short_movie_info")
    manas_film = []

    for item in items:
        manas_film.append(
            {
                "title_name": item.find("div", class_="m_title").get_text(),
                "title_url": URL + item.find("a").get("href"),
                "image": URL
                + item.find("div", class_="m_thumb").find("img").get("src"),
            }
        )

    return manas_film


# endparse
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_films = []
        for page in range(0, 1):
            html = get_html(f"http://www.manascinema.com/movies", params=page)
            all_films.extend(get_data(html.text))
            return all_films
        # print(all_films)
    else:
        raise Exception("Ошибка парсинга")


# parser()
