# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех
# категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
# Затем сохранить эту информацию в JSON-файле.


import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/110.0.0.0 Safari/537.36'}

print(__name__)


def join_func():
    # URL веб-сайта
    url = 'http://books.toscrape.com/'

    release_links = []
    url_joined = []

    while True:
        print(url)
        response = requests.get(url, headers=headers)

        # Парсинг HTML-содержимого веб-страницы с помощью Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Вывод ссылок на книги
        for link in soup.find_all('li', ('class', "col-xs-6 col-sm-4 col-md-3 col-lg-3")):
            a_tag = link.find('a')
            if a_tag:
                release_links.append(a_tag.get('href'))

        # Ссылка кнопки next
        find_next = soup.find('li', ('class', "next"))
        if find_next:
            b_next = find_next.find('a').get('href')
            if 'catalogue' in b_next:
                new_url = urllib.parse.urljoin('http://books.toscrape.com/', b_next)
            else:
                new_url = urllib.parse.urljoin('http://books.toscrape.com/catalogue/', b_next)
        else:
            break
        url = new_url

    # Объединение ссылок с базовым URL-адресом для создания списка URL-адресов
    for link in release_links:
        if 'catalogue' in link:
            url_joined.append(urllib.parse.urljoin('http://books.toscrape.com/', link))
        else:
            url_joined.append(urllib.parse.urljoin('http://books.toscrape.com/catalogue/', link))
    return url_joined


def book_info(url_joined):
    data = []
    for url in url_joined:
        print(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.find('div', ('class', "col-sm-6 product_main"))
        price = soup.find('p', ('class', "price_color"))
        instock = soup.find('p', ('class', "instock availability"))
        description = soup.find('div', ('class', "sub-header"))

        data.append(
            {
                "name": name.find('h1').text.strip(),
                "price": float(price.text.strip().replace('£', '')),
                "instock": int(re.findall(r'\d+', instock.text.strip())[0]),
                "description": description.find_next('p').text.strip()
            }
        )

    return data


def save_data_to_json(data, filename='books.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    url_joined = join_func()
    data = book_info(url_joined)
    save_data_to_json(data)


if __name__ == '__main__':
    main()
