from time import sleep

import requests
from bs4 import BeautifulSoup


WEBSITE = "https://greenatom.ru"

HEADER = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'no-cache',
  'dnt': '1',
  'pragma': 'no-cache',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def get_html(website: str) -> str:
    """
    Получает html страницу в формате str,
    в случае недоступности сервера райзит ошибку.
    """
    session = requests.Session()
    session.headers = HEADER
    r = session.get(website)
    if r.reason != 'OK':
        raise requests.exceptions.RequestException
    return r.text


def get_numbers_tags(html: str) -> tuple[int, int]:
    """
    Получает на вход html страницу, подсчитывает
    количество тегов и тегов с атрибутами.
    """
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all()
    count_tags = 0
    count_tags_attrs = 0

    for tag in tags:
        if tag.attrs:
            count_tags_attrs += 1
        count_tags += 1
    return count_tags, count_tags_attrs


def main() -> None:
    """Главная функция, точка входа."""
    try:
        html = get_html(WEBSITE)
    except requests.exceptions.RequestException as error:
        print(error)
        sleep(10)
        main()
    result = get_numbers_tags(html)
    print(
        f"Количество тегов: {result[0]};\n"
        f"Количество тегов с атрибутами: {result[1]}."
    )


if __name__ == "__main__":
    main()
