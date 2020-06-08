# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:46:47 2020

@author: JOAO VICTOR
"""
from sgs_api import sgs_api
import matplotlib.pyplot as plt


def graph_sgs(tipo = None, codigo = None):

    df = sgs_api(codigo)

    if tipo == 'area' or None:
        plt.fill_between('data', 'valor', data=df)


    elif tipo == 'linha':
        plt.plot('data', 'valor', data=df)

    else:
        print('Tipo de gráfico inválido')

print(graph_sgs('area', '13069'))