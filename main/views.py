import re

import requests

from django.http import JsonResponse
from bs4 import BeautifulSoup

from .models import Medicine

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/108.0.0.0 Safari/537.36'
}


def econom():
    # url = f'https://aptekaeconom.com/catalog/lekarstva-i-bady/lechenie-gemorroya/?SHOWALL_1=1'
    url = f'https://aptekaeconom.com/catalog/lekarstva-i-bady/lechenie-gemorroya/'
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    titles = soup.find_all(class_='catalog_item')

    for title in titles:
        params = dict()

        item = title.find(class_="item-title")
        params['name'] = item.a.span.text
        params['link'] = item.a.get('href')

        price = title.find(class_="price_value")
        if price is not None:
            params['price'] = price

        # medicine = Medicine.objects.filter(name=title.get_text()).first()
        # if medicine is None:
        #     Medicine.objects.create(name=re.sub("^\s+|\n|\r|\s+$", '', title.get_text()),
        #                             link=f"https://aptekaeconom.com{title.a['href']}")


def index(request):
    econom()
    return JsonResponse({'foo': 'bar'})


def get_medicines(request):
    response = JsonResponse([{'title': medicine.name, 'link': medicine.link} for medicine in Medicine.objects.all()],
                            safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response
