# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:29:31 2020
@author: JOAO VICTOR
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.anp.gov.br/dados-estatisticos'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

teste = []
teste2 =[]

for i in soup.find_all('ul', class_ = 'interna-faq'):
   for x in i.find_all('a', href=True):
       teste.append(x['href'])
       teste2.append(x['href'].split('/')[-1].split('.')[0])


def get_file_anp(link):
    url2 = 'http://www.anp.gov.br{}'.format(link)
    file = requests.get(url2)
    cln_link = link.split('/')[-1].split('\\')[-1]

    if cln_link.split('.')[1] == 'pdf':
        cln_link = cln_link.split('.')[-2]
        with open('{}.pdf'.format(cln_link), 'wb') as code:
            code.write(file.content)

    elif cln_link.split('.')[1] == 'xls' or 'xlsx':
        cln_link = cln_link.split('.')[-2]
        with open('{}.xls'.format(cln_link), 'wb') as code:
            code.write(file.content)

    elif cln_link.split('.')[1] == 'zip':
        cln_link = cln_link.split('.')[-2]
        with open('{}.zip'.format(cln_link), 'wb') as code:
            code.write(file.content)