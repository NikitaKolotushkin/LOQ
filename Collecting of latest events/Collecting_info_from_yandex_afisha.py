import requests, lxml

from bs4 import BeautifulSoup


req = requests.get('https://afisha.yandex.ru/perm/cinema?source=menu')
soup = BeautifulSoup(req.text, 'lxml')
names, hrefs = [i.get_text().strip() for i in soup.select('a.Inner-sc-5s87mw-1 > div.Root-sc-5meihc-4 > h2')], \
               ['https://afisha.yandex.ru' + i.attrs['href'] for i in soup.select('a.Inner-sc-5s87mw-1')]
assert soup.select_one('head > title').get_text().strip() != 'Ой!', "Обнаружен машинный запрос. Попытка провалилась"
print(hrefs, names)
films = dict(zip(names, hrefs))
print(f'Выберите фильм из предложенных для дальнейшей информации: {films.keys()}')
while True:
    name = input()
    req = requests.get(films[name])
    soup = BeautifulSoup(req.text, 'lxml')
    assert soup.select_one('head > title').get_text().strip() != 'Ой!', "Обнаружен машинный запрос. Попытка провалилась"
    print(f"Краткое описание: {soup.select_one('div.event-concert-description div.event-concert-description__argument').get_text().strip()}")