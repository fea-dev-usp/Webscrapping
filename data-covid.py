# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:38:22 2020

@author: JOAO VICTOR
"""
import requests as req
from bs4 import BeautifulSoup
import pandas as pd


def get_covid_data(arg=None):
    url = 'https://www.worldometers.info/coronavirus/'
    page = req.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find(name='table')

    table_str = str(table)

    df = pd.read_html(table_str)[0]

    df.set_index('Country,Other', inplace = True)
    return df





