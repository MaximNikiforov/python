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
xpath = "//*[@id='fittPageContainer']/div[3]/div/div[1]/section/div/div/section/div[4]/div[2]/div/div[2]/table/tbody/tr"


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

    for rows in tree.xpath(xpath):
        columns = rows.xpath(".//td/span/text()")
        data.append({
            'rank': columns[0].strip(),
            'trend': '-' + rows.xpath(".//td/div/text()")[0] if rows.xpath(".//td/div[@class='trend tc negative']") else rows.xpath(".//td/div/text()")[0],
            'name': rows.xpath(".//td[3]/div/a/text()")[0],
            'points': columns[1].strip().replace(',', ''),
            'age': columns[2].strip()
        })
    return data


def save_to_csv(data, filename):
    """Сохранение данных в CSV-файл по ячейкам."""
    fields = ['rank', 'trend', 'name', 'points', 'age']

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
    print("Данные успешно сохранены в CSV-файл.")


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
