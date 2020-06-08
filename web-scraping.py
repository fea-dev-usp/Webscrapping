# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:45:37 2020

@author: JOAO VICTOR
"""

import requests
from bs4 import BeautifulSoup

# teste1 page = urlopen('https://www.newegg.com/global/br-en/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards')
url = 'https://www.newegg.com/global/br-en/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'
page = requests.get(url)

soup = BeautifulSoup(page, 'lxml')

names = []
costs =[]


for name in soup.find_all('div', class_ = 'item-info'):
    title = name.find('a', class_ = 'item-title').get_text()
    names.append(title)
    price = name.find('li', attrs={'class': 'price-ship'})
    costs.append(price)


print(names)
print(costs)