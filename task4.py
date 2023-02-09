from time import sleep

import requests
from bs4 import BeautifulSoup

from task3 import get_html


WEBSITE = "https://ifconfig.me/"


def get_ip_address(html: str) -> list:
    """Получает на вход html страницу, возвращает IP-адрес."""
    soup = BeautifulSoup(html, "html.parser")
    ip_address = soup.find("strong", id="ip_address").contents
    return ip_address[0]


def main() -> None:
    """Главная функция, точка входа."""
    try:
        html = get_html(WEBSITE)
    except requests.exceptions.RequestException as error:
        print(error)
        sleep(10)
        main()
    ip_address = get_ip_address(html)
    print(f"ip_address: {ip_address}")


if __name__ == "__main__":
    main()
