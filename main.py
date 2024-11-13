import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/page/'
quotes_list = []
page = 1

while True:
    response = requests.get(f'{url}{page}/')
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

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

with open('quotes.json', 'w', encoding='utf-8') as file:
    json.dump(quotes_list, file, ensure_ascii=False, indent=4)

print("Сбор данных завершен, цитаты собраны в quotes.json.")
