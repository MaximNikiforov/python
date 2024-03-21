import csv
import requests
from lxml import html

# URL веб-сайта с табличными данными
url = "https://www.espn.com/tennis/rankings"

# Строка агента пользователя для имитации веб-браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.5060.114 Safari/537.36"
}

# Выражение XPath для выбора элементов данных таблицы
xpath = "//table[@class='ResponsiveTable']/tbody/tr"


def get_html(url, headers):
    """Отправка HTTP GET-запроса и получение HTML-содержимого."""

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Ошибка HTTP-запроса: {}".format(response.status_code))

    return response.content.decode()


def parse_html(html_content, xpath):
    """Парсинг HTML-содержимого и извлечение данных таблицы."""

    tree = html.fromstring(html_content)
    data = []

    for element in tree.xpath(xpath):
        try:
            value = element.text_content().strip()
        except AttributeError:
            value = ""
        data.append(value)

    return data


def save_to_csv(data, filename):
    """Сохранение данных в CSV-файл."""

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)
    print("Данные рейтинга теннисистов ESPN успешно сохранены в CSV-файл.")


# main функция

def main():
    # Получение HTML-содержимого
    html_content = get_html(url, headers)
    # Парсинг HTML-содержимого и извлечение данных таблицы
    data = parse_html(html_content, xpath)
    # Сохранение данных в CSV-файл
    save_to_csv(data, "espn_tennis_rankings.csv")


if __name__ == "__main__":
    main()
