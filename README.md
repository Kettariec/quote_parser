# Техническое задание на позицию: Junior Python разработчик 
## Задание: 
Сбор данных с сайта https://quotes.toscrape.com/ 
## Результаты:
1. JSON файл с собранными данными
2. MD файл с анализом задачи, включающий:
<br> a. Что было сделано 
<br> b. Откуда были получены данные
<br> c. Как осуществлялся сбор
<br> d. Почему был выбран тот или иной метод/инструмент, а не другой
3. Ссылка на репозиторий с кодом на GitHub


# Отчет по сбору данных с сайта quotes.toscrape.com

## 1. Что было сделано
Собраны цитаты, имена авторов и теги с сайта https://quotes.toscrape.com/ и сохранены в JSON файл.

## 2. Откуда были получены данные
Данные получены со страниц сайта, указанного в задании.

## 3. Как осуществлялся сбор
Для получения данных использовались библиотека `requests`, для отправки HTTP-запросов и парсинга `BeautifulSoup`. Цикл проходит по страницам сайта до тех пор, пока не закончится контент.

## 4. Почему был выбран данный метод
- **requests**: простой и эффективный способ для отправки запросов на сайт и получения ответа.
- **BeautifulSoup**: удобный инструмент для извлечения данных из HTML и XML документов благодаря его легкому синтаксису и поддержке различных парсеров.



<br>

kettariec@gmail.com

https://github.com/Kettariec/quote_parser