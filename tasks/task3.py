from time import sleep

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


WEBSITE = "https://greenatom.ru"


def get_html(website: str) -> str:
    """
    Получает html страницу в формате str,
    в случае недоступности сервера райзит ошибку.
    """
    ua = UserAgent()
    headers = {"User-Agent": ua.chrome}
    page = requests.get(website, headers=headers)
    if page.reason != 'OK':
        raise requests.exceptions.RequestException
    return page.text


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
