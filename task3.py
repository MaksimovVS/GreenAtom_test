import requests
from bs4 import BeautifulSoup

WEBSITE = "https://greenatom.ru/"

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
    session = requests.Session()
    session.headers = HEADER
    r = session.get(website)
    return r.text


def get_numbers_tags(html: str) -> tuple[int, int]:
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all()
    count1 = 0
    count2 = 0

    for tag in tags:
        if tag.attrs:
            count2 += 1
        count1 += 1
    return count1, count2


def main() -> None:
    html = get_html(WEBSITE)
    result = get_numbers_tags(html)
    print(
        f"Количество тегов: {result[0]};\n"
        f"Количество тегов с атрибутами: {result[1]}."
    )


if __name__ == "__main__":
    main()
















# import requests
# from bs4 import BeautifulSoup as Bs
# from fake_useragent import UserAgent
#
#
# def get_html(url: str) -> object:
#     ua = UserAgent()
#     headers = {'User-Agent': ua.chrome}
#
#     try:
#         page = requests.get(url, headers=headers)
#         page.raise_for_status()
#     except requests.exceptions.RequestException as error:
#         return error
#
#     html = Bs(page.text, 'html.parser')
#     return html.find('html')
#
#
# def tags_quantity(tag: object, count: int, attrs: bool = False) -> int:
#     if tag.name:
#         if attrs and tag.attrs:
#             count += 1
#         elif not attrs:
#             count += 1
#
#         for child in tag.children:
#             count = tags_quantity(child, count, attrs)
#
#     return count
#
#
# if __name__ == '__main__':
#     url = 'https://greenatom.ru/'
#     html = get_html(url)
#
#     print('All tags quantity:', tags_quantity(html, 0))
#     print(
#         'Quantity of tags with attributes:',
#         tags_quantity(html, 0, attrs=True)
#     )