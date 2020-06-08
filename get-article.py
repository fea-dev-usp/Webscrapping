# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:45:37 2020

@author: JOAO VICTOR
"""

import requests
from bs4 import BeautifulSoup

link = input('Url da notícia:')

def get_article(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    p = soup.find_all('p')
    paragrafos = []
    paragrafos.append(soup.title.text.strip())

    for texto in p:
        texto = texto.text.strip()
        paragrafos.append(texto)

    return paragrafos

print(get_article(link))