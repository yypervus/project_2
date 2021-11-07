import requests
from bs4 import BeautifulSoup
from datetime import datetime

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

resp = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(resp.text, 'html.parser')


articles = soup.find_all('article')

for article in articles:
    title_element = article.find('a', class_='post__title_link')
    title_text = title_element.text.strip()

    hubs = [hub.text.strip().lower() for hub in article.find_all('a', class_='hub-link')]
    preview = article.find('div', class_='post__text-html').text.strip().lower()

    href = title_element.attrs.get('href')
    res = requests.get(href)
    soup_ = BeautifulSoup(res.text, 'html.parser')

    body_element = soup_.find('div', class_='post__text')
    body = body_element.text.strip().lower()

    for desired in KEYWORDS:
        if desired in title_text.lower() or desired in hubs or desired in preview or desired in body:
            data_element = soup_.find('span', class_='post__time')
            data_text = data_element.attrs.get('data-time_published')
            date_old = datetime.strptime(data_text, "%Y-%m-%dT%H:%MZ")
            data = datetime.strftime(date_old, "%d-%m-%Y")
            print(data, title_text, href)