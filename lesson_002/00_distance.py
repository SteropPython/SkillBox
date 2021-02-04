#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscowToLondon = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
moscowToParis = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
londonToParis = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscowToLondon
distances['Moscow']['Paris'] = moscowToParis

distances['London'] = {}
distances['London']['Moscow'] = moscowToLondon
distances['London']['Paris'] = londonToParis

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscowToParis
distances['Paris']['London'] = londonToParis

pprint(distances)
