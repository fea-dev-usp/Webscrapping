# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:08:08 2020

@author: JOAO VICTOR
"""

import requests as req
import json

tabela = input('Código da tabela Sidra para extrair:')
periodo = input('Período desejado, utilize last para os últimos períodos')
valor = input('Digite valores desejados, allxp para todos os valores')

codigo =  f'/t/{tabela}/n1/1/v/{valor}/p/{periodo}'


def sidra(codigo):
    sidra_url = f'http://api.sidra.ibge.gov.br/values/{codigo}'
    serie = req.get(sidra_url)
    serie = json.loads(serie.text)
    serie.pop(0)
    data = []
    cache = []
    for i in serie:
        if i.get('D1C') not in cache:
            cache.append(i.get('D1C'))
            data.append({'date' : i.get('D1C')})
        data[len(cache) - 1].update({i.get('D3N') : i.get('V')})

    return data