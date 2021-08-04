import requests
import json
from pprint import pprint


def code_to_url(string):
    res = ''
    '''
    for i in '.,':
        string = string.replace(i, '')
    '''
    for el in string:

        if not el:
            n = "%20"
        elif r'\x' in str(el.encode()):
            n = "%".join([i.upper() for i in str(el.encode())[2:-1].split(r'\x')])
        else:
            n = el
        res += n
    return '%20'.join(res.split())


def geocode(address):
    params = {
        'key': "AIzaSyD_Q0i70lgi6yI1RzkmwD27mcsmTbPbDPc",
        'address': '+'.join(address.split()),
        'language': "RU"
    }

    geo = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json", params=params)  # Вся информация о месте. Возможно, что из нее можно извлечь еще что-то ценное
    #pprint(json.loads(geo.text))
    di = dict(json.loads(geo.text))

    if di['results']:
        with open("int_places2.txt", "a") as f:
            f.write(f"Адрес: {address}\n")
            f.write(f"Место - {di['results'][0]['formatted_address']}\n")
            f.write(f"Координаты: {list(di['results'][0]['geometry']['location'].values())}\n")
            f.write('\n')
        return f"Successfully found"
    return 'Not found'


while True:
    print(geocode("Самара " + input()))
