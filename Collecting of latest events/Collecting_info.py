import requests, lxml
from bs4 import BeautifulSoup

req = requests.get("https://smr.kassir.ru/bilety-v-teatr")
soup = BeautifulSoup(req.text, 'lxml')
events = [i.get_text().strip() for i in soup.select('div.caption > div.title > a')]
date = [i.get_text().strip() for i in soup.select('div.caption > div.date')]
places = [i.get_text().strip() for i in soup.select('div.caption > div.place > a')]
cost = [i.get_text().strip() for i in soup.select('div.caption > div.cost')]
print("Ближайшие театральные постановки для Самары:")
for i in zip(events, date, places, cost):
    print(f'Мероприятие: {i[0]}')
    print(f'Дата: {i[1]}')
    print(f'Место: {i[2]}')
    print(f'Стоимость в рублях: {i[3]}')
    print()
# Постараться представить это в виде Pandas-DataFrame
