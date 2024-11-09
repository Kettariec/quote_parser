import requests
from bs4 import BeautifulSoup
import json

# Базовый URL
base_url = 'https://quotes.toscrape.com/page/'

# Список для хранения данных
quotes_list = []

# Сбор данных с нескольких страниц
page = 1
while True:
    response = requests.get(f'{base_url}{page}/')
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    # Проверка на наличие цитат
    if not quotes:
        break

    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

        quotes_list.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    page += 1

# Сохранение данных в JSON файл
with open('quotes_data.json', 'w', encoding='utf-8') as file:
    json.dump(quotes_list, file, ensure_ascii=False, indent=4)

print("Сбор данных завершен, файл quotes_data.json создан.")