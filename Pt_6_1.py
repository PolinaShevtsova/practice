import requests
from bs4 import BeautifulSoup
from loguru import logger

link_on_tracks = input("Вставьте ссылку на популярные треки исполнителя в сервисе Yandex Music: ")

try:
    accession = requests.get(link_on_tracks)
    soup = BeautifulSoup(accession.text, "html.parser")

    name_of_artist = soup.find("h1", class_="page-artist__title typo-h1 typo-h1_big").text
    print(f"Топ 10 песен {name_of_artist} на сервисе Yandex Music: ")
    k = 1
    all_tracks = soup.find_all("a", class_="d-track__title deco-link deco-link_stronger")
    for track in all_tracks[:10]:
        print(f"{k}. {track.text}")
        k += 1
except requests.exceptions.MissingSchema:
    logger.error("Invalid URL! Try again, following the example https://music.yandex.ru/artist/0000000/tracks")

except requests.exceptions.InvalidSchema:
    logger.error(f"No connection adapters were found for {link_on_tracks}. Use the right schema"
                 f" and follow the example https://music.yandex.ru/artist/0000000/tracks")
except requests.exceptions.RequestException as e:
    logger.error(e)
